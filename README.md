# subject-learning

English | [简体中文](README_zh.md)

`subject-learning` is an Agent Skill for turning fragmented course materials or dense textbooks into a cohesive, problem-driven Chinese learning guide. Instead of writing chapter-by-chapter summaries, it extracts the discipline's **core problem**, **solution backbone**, and **exam scope**, highlights **foundational hubs** and **high-weight topics**, builds a self-contained study document, and backs it up with active-recall quizzing and spaced-repetition error tracking.

## Quickstart

```bash
# Recommended: install globally and wire to Claude Code & Codex
npx skills add zyang0107/subject-learning -a claude-code codex -g -y

# Or auto-detect all installed Agent Skills clients (Cursor, Gemini CLI, etc.)
npx skills add zyang0107/subject-learning -g -y
```

Prefer manual setup? Clone directly into the target skills directory:
- **Claude Code**: `git clone https://github.com/zyang0107/subject-learning ~/.claude/skills/subject-learning`
- **Codex**: `git clone https://github.com/zyang0107/subject-learning ~/.codex/skills/subject-learning`
- **Any Agent Skills client**: `git clone https://github.com/zyang0107/subject-learning .agents/skills/subject-learning`

**Usage**: Invoke `/subject-learning` (or `$subject-learning`) with four inputs: (1) source materials path (PDF, PPTX, DOCX, EPUB, or text — kept strictly read-only), (2) output topic directory, (3) learning `mission`, and (4) `depth` (`blueprint_only` for scope and priority map, `outline` for a concise backbone, or `full` for a comprehensive textbook replacement). If `_notes/syllabus.md` already exists in the target directory, the skill automatically resumes from the current checkpoint or jumps into practice mode.

## Workflow & Mechanics

The workflow is split into three sequential phases plus an on-demand practice branch, progressively disclosing each guide from `references/`:

| Phase | Reference | What It Does |
| :--- | :--- | :--- |
| **Phase 1 · Blueprint** | [`references/blueprint.md`](references/blueprint.md) | Audits all input files; extracts exam scope, rubrics, and explicit exclusions; distills the core problem, solution backbone, and subject boundary; organizes problem-driven modules, ranks priorities (`重点 / 常规 / 带过`) around foundational hubs and exam frequency, and presents 1 real sample for sign-off. |
| **Phase 2 · Modular Drafting** | [`references/drafting.md`](references/drafting.md) | Drafts one module at a time, gated by a sample-chapter review after Module 1; explains every key concept along three axes (why it is needed, what/how it works, limits & boundaries); grounds abstractions with concrete examples verified by a reverse test; restricts external lookups to blocking conceptual gaps; enforces a 6-point per-module check. |
| **Phase 3 · Final Audit** | [`SKILL.md`](SKILL.md) / [`scripts/audit.py`](scripts/audit.py) | Verifies book-wide hub back-references, competing-approach comparisons, non-duplication, and term consistency; runs `audit.py` to enforce a single H1, exact H2 title/order parity with `syllabus.md`, zero placeholders, and zero terminology drift (`terms.avoid`). |
| **On-Demand · Quiz & Retention** | [`references/practice.md`](references/practice.md) | Poses 1 question per turn across L1 (foundations), L2 (application, prioritizing real course exercises), and L3 (boundary & transfer); pre-locks the grading rubric in `_notes/quiz-key.md` before showing the question to prevent sycophancy; separates memory slips from backbone comprehension breakpoints in `_notes/mistakes.md` with spaced repetition (`+2 → +5 → +10 → mastered`). |

## Output Layout

Inside the user-specified `<topic-dir>`, the skill maintains a single-file book paired with structured state notes:

```text
<topic-dir>/
├── <topic-dir-name>.md  # Single deliverable document (Mermaid backbone map, scope, modules, review, glossary, etc.; optional in blueprint_only)
└── _notes/
    ├── structure.md     # 4 fixed H2 sections: core problem & scope, module backbone, priority index & sources, file inventory & gaps
    ├── syllabus.md      # YAML front matter (state, sections, terms.avoid) + book conventions & writing preferences
    ├── mistakes.md      # Created on demand: error log, backbone breakpoints, and spaced-repetition schedule
    └── quiz-key.md      # Created on demand: pre-locked answer key and rubric for the active question
```

## Repository Contents

- [`SKILL.md`](SKILL.md): Entry point, state-machine router, and three-phase orchestration
- [`references/blueprint.md`](references/blueprint.md): Phase 1 blueprint extraction rules and `structure.md` template
- [`references/drafting.md`](references/drafting.md): Phase 2 book skeleton, modular drafting discipline, and 6-point check
- [`references/practice.md`](references/practice.md): Quiz tiers, anti-sycophancy grading protocol, root-cause triage, and spaced repetition
- [`scripts/audit.py`](scripts/audit.py): Automated validator for structure, section parity, placeholders, and term drift
- [`agents/openai.yaml`](agents/openai.yaml): Codex UI metadata and default prompt configuration
