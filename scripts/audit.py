#!/usr/bin/env python3
"""Validate a subject-learning directory (map or single-file guide)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|待补|占位", re.I)
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE_RE = re.compile(r"^(?:`{3,}|~{3,})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")

REQUIRED_NOTES = ("plan.md",)
OPTIONAL_NOTES = ("quiz.md", "quiz-key.md")
PLAN_H2_GROUPS = (
    ("学习定位与要求", "核心口径与前置"),
    ("模块主线与重点", "模块主线与重点定位"),
    ("写作偏好与素材缺口",),
)
MAP_H2_GROUPS = (
    ("全书导览", "学科定位与全书地图"),
    ("重点与学习范围",),
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def strip_yaml_comment(raw: str) -> str:
    """Strip an unquoted YAML inline comment and surrounding quotes."""
    in_single = False
    in_double = False
    for idx, ch in enumerate(raw):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            if idx == 0 or raw[idx - 1].isspace():
                raw = raw[:idx]
                break
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    return value


def read_front_matter(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path}")
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"{path.name} has no YAML front matter")
    return match.group(1)


def scalar(block: str, key: str) -> str | None:
    match = re.search(rf"^{key}:\s*(.+?)\s*$", block, re.M)
    if not match:
        return None
    value = strip_yaml_comment(match.group(1))
    return value or None


def sections(block: str) -> list[dict[str, str]]:
    section = re.search(r"^sections:\n(.*?)(?=^\S|\Z)", block, re.M | re.S)
    if not section:
        return []
    items: list[dict[str, str]] = []
    for raw in re.split(r"^\s*-\s+", section.group(1), flags=re.M)[1:]:
        entry: dict[str, str] = {}
        for line in raw.splitlines():
            pair = re.match(r"\s*(\w+):\s*(.+?)\s*$", line)
            if pair:
                entry[pair.group(1)] = strip_yaml_comment(pair.group(2))
        items.append(entry)
    return items


def avoided_terms(block: str) -> list[tuple[str, str]]:
    section = re.search(r"^terms:\n(.*?)(?=^\S|\Z)", block, re.M | re.S)
    if not section:
        return []
    pairs: list[tuple[str, str]] = []
    for raw in re.split(r"^\s*-\s+", section.group(1), flags=re.M)[1:]:
        zh = re.search(r"zh:\s*(.+?)\s*$", raw, re.M)
        avoid = re.search(r"avoid:\s*\[(.*?)]", raw, re.S)
        if not (zh and avoid):
            continue
        canonical = strip_yaml_comment(zh.group(1))
        for variant in avoid.group(1).split(","):
            variant = variant.strip().strip("\"'")
            if variant:
                pairs.append((canonical, variant))
    return pairs


def check_markdown(path: Path, errors: list[str]) -> list[str]:
    """Check one body file; return its H2 titles in document order."""
    text = path.read_text(encoding="utf-8")
    body = FRONT_MATTER_RE.sub("", text)
    in_fence = False
    h1_count = 0
    previous = 0
    h2_titles: list[str] = []
    for number, line in enumerate(body.splitlines(), 1):
        stripped = line.lstrip()
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            h1_count += level == 1
            if level == 2:
                h2_titles.append(heading.group(2))
            if previous and level > previous + 1:
                errors.append(f"{path.name}:{number} heading jump")
            previous = level
        if PLACEHOLDER_RE.search(line):
            errors.append(f"{path.name}:{number} placeholder text")
    if h1_count != 1:
        errors.append(f"{path.name} must contain exactly one H1")
    if in_fence:
        errors.append(f"{path.name} unclosed fenced code block")
    if text and not text.endswith("\n"):
        errors.append(f"{path.name} missing final newline")
    return h2_titles


def resolve_notes_dir(book: Path) -> Path:
    """Prefer notes/ and fall back to legacy _notes/ when present."""
    notes = book / "notes"
    if notes.is_dir():
        return notes
    legacy = book / "_notes"
    if legacy.is_dir():
        return legacy
    return notes


def check_notes(notes: Path, errors: list[str]) -> None:
    """notes/ holds plan.md (plus optional quiz.md) and plan.md has its 3 H2s."""
    if not notes.is_dir():
        fail(f"missing directory: {notes}")
    found = {p.name for p in notes.iterdir() if p.is_file() and not p.name.startswith(".")}
    allowed = set(REQUIRED_NOTES) | set(OPTIONAL_NOTES)
    for extra in sorted(found - allowed):
        errors.append(f"{notes.name}/{extra}: unexpected file in {notes.name}/")
    for missing in sorted(set(REQUIRED_NOTES) - found):
        errors.append(f"missing file: {notes.name}/{missing}")

    plan = notes / "plan.md"
    if plan.is_file():
        body = FRONT_MATTER_RE.sub("", plan.read_text(encoding="utf-8"))
        present = set(re.findall(r"^##\s+(.*?)\s*$", body, re.M))
        for names in PLAN_H2_GROUPS:
            if not any(name in present for name in names):
                errors.append(f"plan.md has no `## {names[0]}`")


def check_outline(titles: list[str], headings: list[str], errors: list[str]) -> None:
    """plan sections and body H2 headings must be the same list, same order."""
    for title in titles:
        if title not in headings:
            errors.append(f"plan section {title!r} has no matching H2 in the body")
    for heading in headings:
        if heading not in titles:
            errors.append(f"body H2 {heading!r} is not listed in plan sections")
    if titles != headings and sorted(titles) == sorted(headings):
        errors.append("plan section order does not match body H2 order")


def resolve_body(book: Path, block: str) -> Path:
    body = book / (book.name + ".md")
    if not body.is_file():
        topic = scalar(block, "topic")
        if topic:
            fallback = book / (topic + ".md")
            if fallback.is_file():
                return fallback
    return body


def validate(book: Path) -> int:
    errors: list[str] = []
    notes = resolve_notes_dir(book)
    block = read_front_matter(notes / "plan.md")

    map_state = scalar(block, "map") or scalar(block, "blueprint")
    if map_state != "approved":
        errors.append("map is not approved")

    doc_state = scalar(block, "status") or scalar(block, "book")
    if doc_state not in ("in_progress", "complete", "map", "blueprint_only"):
        errors.append(f"status has no legal value: {doc_state!r}")

    check_notes(notes, errors)

    body = resolve_body(book, block)
    headings: list[str] = []
    if body.is_file():
        headings = check_markdown(body, errors)
    else:
        errors.append(f"missing file: {body.name}")

    is_map_only = (
        scalar(block, "mode") == "map"
        or scalar(block, "depth") == "blueprint_only"
        or doc_state in ("map", "blueprint_only")
    )
    if is_map_only:
        for names in MAP_H2_GROUPS:
            if not any(name in headings for name in names):
                errors.append(f"map deliverable missing `## {names[0]}`")
        if errors:
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print(f"OK: map validated ({body.name})")
        return 0

    entries = sections(block)
    if not entries:
        errors.append("plan lists no sections")
    for number, entry in enumerate(entries, 1):
        label = entry.get("title") or f"#{number}"
        if not entry.get("title"):
            errors.append(f"section {label}: missing title field")
        if entry.get("status") != "done":
            errors.append(f"section {label}: status {entry.get('status')!r}")

    titles = [entry["title"] for entry in entries if entry.get("title")]
    if titles and headings:
        check_outline(titles, headings, errors)

    variants = avoided_terms(block)
    if variants and body.is_file():
        prose = body.read_text(encoding="utf-8")
        for canonical, variant in variants:
            if variant in prose:
                errors.append(f"term drift: {variant!r} should be {canonical!r}")

    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    char_count = len(body.read_text(encoding="utf-8"))
    print(f"OK: {len(entries)} sections, {char_count} characters")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("book", type=Path)
    return validate(parser.parse_args().book.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
