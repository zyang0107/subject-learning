# subject-learning

English | [简体中文](README_zh.md)

**Every discipline exists because a specific class of problems demanded it.** Most textbooks and lecture notes pile concepts bottom-up, chapter by chapter—leaving learners with isolated definitions and no map.

`subject-learning` flips that order: it first pins down **why the subject exists** and the **solution backbone** behind it, then fills in concepts, methods, and exam-weighted details **top-down** only where they carry weight in that backbone—paired with an anti-sycophancy quiz loop that traces mistakes back to the backbone.

## Quickstart

```bash
# Install globally and wire to Claude Code & Codex
npx skills add zyang0107/subject-learning -a claude-code codex -g -y

# Or auto-detect all installed Agent Skills clients (Cursor, Gemini CLI, etc.)
npx skills add zyang0107/subject-learning -g -y
```

Manual clone targets:
- **Claude Code**: `git clone https://github.com/zyang0107/subject-learning ~/.claude/skills/subject-learning`
- **Codex**: `git clone https://github.com/zyang0107/subject-learning ~/.codex/skills/subject-learning`
- **Generic clients**: `git clone https://github.com/zyang0107/subject-learning .agents/skills/subject-learning`

**Usage**: Run `/subject-learning` (or `$subject-learning`) with your source path (PDF, PPTX, DOCX, EPUB, or text — kept read-only), output directory, `mission`, and `depth` (`blueprint_only`, `outline`, or `full`). If `_notes/syllabus.md` already exists, it resumes from the current checkpoint or switches to quiz mode.

## How It Works

1. **Start from Why the Subject Exists ([`blueprint.md`](references/blueprint.md))**: Audit sources and exam exclusions, distill *Core Problem → Solution Backbone → Problem Modules*, rank foundational hubs and high-weight exam topics, and get user sign-off on a real sample before drafting.
2. **Fill Top-Down ([`drafting.md`](references/drafting.md))**: Draft one module at a time (calibrated by a sample-chapter gate after Module 1). Every concept explains what gap on the backbone it solves, how it works, and where it breaks; abstractions require concrete examples verified by a reverse test.
3. **Verify Structure ([`audit.py`](scripts/audit.py))**: Audit book-wide hub back-references and competing-approach tradeoffs, then run `audit.py` to enforce a single H1, exact H2 parity with `syllabus.md`, zero placeholders, and zero term drift (`terms.avoid`).
4. **Quiz & Trace Breakpoints ([`practice.md`](references/practice.md))**: Ask 1 question per turn (L1 recall / L2 course exercises / L3 boundary transfer) with the rubric pre-locked in `_notes/quiz-key.md`; triage misses between memory slips and backbone comprehension breakpoints in `_notes/mistakes.md` on a `+2 → +5 → +10` schedule.

## Output Layout

```text
<topic-dir>/
├── <topic-dir-name>.md  # Single deliverable book (backbone Mermaid map, scope, modules, review, glossary)
└── _notes/
    ├── structure.md     # Core problem & scope, module backbone, priority index, file inventory
    ├── syllabus.md      # Progress state, ordered sections, and terminology guardrails (terms.avoid)
    ├── mistakes.md      # On demand: error log, backbone breakpoints, and spaced-repetition queue
    └── quiz-key.md      # On demand: pre-locked answer key and scoring points per active question
```
