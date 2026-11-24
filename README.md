# subject-learning

English | [简体中文](README_zh.md)

Textbooks and lecture slides usually introduce concepts one chapter at a time, making it easy to memorize isolated definitions without seeing how the pieces fit together.

`subject-learning` works in the opposite direction. It starts by identifying the core problem a discipline solves and the reasoning chain behind it, organizes the material into problem-based modules, and fills in concepts, methods, and exam-heavy topics in order of importance. Afterward, you can quiz yourself one question at a time with pre-written grading criteria.

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

**Usage**: Run `/subject-learning` (or `$subject-learning`) with your source path (PDF, PPTX, DOCX, EPUB, or text, kept read-only), output directory, `mission`, and `mode` (`map` for a standalone overview and priority list, or `guide`—the default—which builds the same map first and then expands it into a clear study guide). When `notes/plan.md` already exists in the output directory, the skill resumes from the last checkpoint or enters quiz mode.

## How It Works

1. **Build the map & priorities ([`map.md`](references/map.md), required for both modes)**: Reviews usable materials, prerequisites, and exam exclusions, extracts the core problem and solution chain, and groups topics into problem modules. Topics are sorted into four flat tiers—**hubs** (the 2–4 foundational ideas that support later modules), **key points** (core arguments, exam-heavy items, or key debates), **standard**, and **minor**—plus one sample section styled per [`style.md`](references/style.md) in `guide` mode. In `map` mode, once approved, it writes the standalone overview document and stops.
2. **Write the study guide ([`guide.md`](references/guide.md) & [`style.md`](references/style.md), `guide` mode)**: Expands the approved map, pausing after the first core module for a sample check to calibrate tone and depth, then continues writing and saving each remaining module in sequence through completion. Each point follows a lightweight guide by content type (concept/mechanism, claim/phenomenon, or debate/tradeoff) woven into natural prose with fixed-palette Mermaid diagrams, backed by concrete examples that pass a reverse check and targeted web verification only when source gaps block the argument.
3. **Check structure and terms ([`audit.py`](scripts/audit.py))**: Reviews cross-module consistency and the closing quick-reference self-check, then runs `audit.py` to verify a single H1, exact heading parity with `notes/plan.md`, no placeholders, and optional terminology consistency (`terms.avoid`).
4. **Practice workbook & quiz review ([`practice.md`](references/practice.md))**: First confirms whether you want the full book or specific chapters, then compiles a standalone `<topic-dir-name>-习题册.md` for that scope containing all questions, answer keys, and scoring criteria across two difficulty levels (**basic** and **advanced**) and three grouped formats (**multiple choice** as the main bulk, **justified true/false** as support, and **open-ended** as optional supplement). Interactive quizzes offer three modes (**sequential**, **shuffled**, and **mistakes only**) using `notes/quiz.md` purely as a progress pointer and error-reason log, grading directly against the workbook and tracking mistakes in `<topic-dir-name>-错题本.md`. After a round, it reviews strong vs. weak modules and appends targeted, slightly easier follow-up items at the end of each weak module without renumbering existing questions.

## Output Layout

```text
<topic-dir>/
├── <topic-dir-name>.md          # Single deliverable (map mode: overview & priorities; guide mode: backbone study guide)
├── <topic-dir-name>-习题册.md    # On demand: module-based workbook with full answer keys (plus targeted follow-up items)
├── <topic-dir-name>-错题本.md    # On demand: error log, conceptual gaps, and review status
└── notes/
    ├── plan.md                  # Study plan & progress: state, scope, per-module priorities, style notes, and gaps
    └── quiz.md                  # On demand: question pointer, per-module tallies, and learner error reasons (no answers)
```
