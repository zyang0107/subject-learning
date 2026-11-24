# subject-learning

English | [简体中文](README_zh.md)

Textbooks and lecture slides usually introduce concepts one chapter at a time, making it easy to memorize isolated definitions without seeing how the pieces fit together.

`subject-learning` works in the opposite direction. It starts by identifying the core problem a discipline solves and the reasoning chain behind it, organizes the material into problem-based modules, and fills in concepts, methods, and exam-heavy topics in order of importance. Afterward, you can quiz yourself one question at a time with pre-locked grading criteria.

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

**Usage**: Run `/subject-learning` (or `$subject-learning`) with your source path (PDF, PPTX, DOCX, EPUB, or text, kept read-only), output directory, `mission`, and `depth` (`blueprint_only` for a standalone readable study blueprint, `outline`, or `full`). When `_notes/plan.md` already exists in the output directory, the skill resumes from the last checkpoint or enters quiz mode.

## How It Works

1. **Map the backbone and priorities ([`blueprint.md`](references/blueprint.md))**: Audits usable materials, prerequisites, and exam exclusions, extracts the core problem and solution chain, and groups topics into problem modules. Concepts that later modules rely on or that appear often in exercises are flagged as priorities, along with one sample section for your approval before full writing begins (or outputs a clean readable blueprint directly in `blueprint_only` mode).
2. **Draft module by module ([`drafting.md`](references/drafting.md))**: Writes one module at a time, with a review gate after the first core module to lock in tone and depth. Each major concept explains what gap it fills, how it works, and where it breaks down, backed by worked examples for method/calculation topics, concrete examples that pass a reverse check, and targeted web verification only when source gaps block the argument.
3. **Check structure and terms ([`audit.py`](scripts/audit.py))**: Reviews cross-module consistency and the closing quick-reference self-check, then runs `audit.py` to verify a single H1, exact heading parity with `_notes/plan.md`, no placeholders, and optional terminology consistency (`terms.avoid`).
4. **Quiz and trace mistakes ([`practice.md`](references/practice.md))**: Presents one question at a time across three difficulty tiers (recall, course exercises, and edge-case transfer) while saving the answer key in `_notes/quiz-key.md` before grading. Memory slips are corrected directly, conceptual misses are traced back to the module's core problem, and mistakes are tracked in `<topic-dir-name>-错题本.md` across three states (`待复测` → `复测通过1次` → `已掌握`).

## Output Layout

```text
<topic-dir>/
├── <topic-dir-name>.md          # Single deliverable (positioning, prerequisites, exam scope & map + modules + exam cheat-sheet & self-check)
├── <topic-dir-name>-错题本.md    # On demand: learner-facing error log, backbone breakpoints, and 3-state review status
└── _notes/
    ├── plan.md                  # Single-source working ledger: state, scope, per-module priority map, style notes, and gaps
    └── quiz-key.md              # On demand: pre-locked answer key and scoring rubric for the active question
```
