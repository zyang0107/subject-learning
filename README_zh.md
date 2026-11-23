# subject-learning

[English](README.md) | 简体中文

**一门学科之所以存在，是因为现实中有一类问题非它不可。** 多数教材和讲义按章节自下而上堆砌概念，读者学到一半只见零散定义，不见全貌。

`subject-learning` 反过来——**先搞清楚这门学科为什么存在、到底要解决什么核心问题**，顺着解决主线搭出问题模块骨架，再**自上而下**把概念、方法与考点填进骨架对应的位置。最后配一套先锁判分标准的主动回忆测验，帮你定位到底卡在主线的哪一环。

## 快速上手

```bash
# 全局安装并自动挂载至 Claude Code 与 Codex
npx skills add zyang0107/subject-learning -a claude-code codex -g -y

# 或自动探测本机所有支持的客户端（Cursor、Gemini CLI 等）
npx skills add zyang0107/subject-learning -g -y
```

手动安装可直接克隆至对应目录：
- **Claude Code**：`git clone https://github.com/zyang0107/subject-learning ~/.claude/skills/subject-learning`
- **Codex**：`git clone https://github.com/zyang0107/subject-learning ~/.codex/skills/subject-learning`
- **通用客户端**：`git clone https://github.com/zyang0107/subject-learning .agents/skills/subject-learning`

**用法**：调用 `/subject-learning`（或 `$subject-learning`），提供素材路径（PDF/PPTX/DOCX/EPUB/文本，保持只读）、输出目录、学习目标（`mission`）与深度（`blueprint_only` 只出范围蓝图 / `outline` 精简骨架 / `full` 替代原书详尽版）。目标目录已有 `_notes/syllabus.md` 时自动断点续写或进入测验。

## 怎么工作

1. **先立主线，再定范围（[`blueprint.md`](references/blueprint.md)）**：盘点素材与考核排除项，提炼「核心问题 → 解决主线 → 问题模块」，标出跨模块复用的**基础枢纽**与**考核高频**，附 1 个真实样例报你拍板后才动笔。
2. **自上而下填肉（[`drafting.md`](references/drafting.md)）**：每次只写一个模块（首章过样章门校准手感）。每个概念必须讲清它在主线上解决什么问题、怎么运作、边界在哪；先跑主干再叠例外，抽象概念配可反向检验的具体例子，不缺则不外部乱搜。
3. **脚本硬检交付（[`audit.py`](scripts/audit.py)）**：全书核对基础枢纽回指与竞争方案取舍，最后跑脚本校验单 H1、章节目录与 `syllabus.md` 逐字一致、无占位符、无术语漂移（`terms.avoid`）。
4. **测验与主线诊断（[`practice.md`](references/practice.md)）**：每次 1 题（L1 基础 / L2 原题应用 / L3 边界迁移），发题前先把答案与得分点锁入 `_notes/quiz-key.md` 防放水；答错按「记混」与「卡在主线哪一环」分流，以 `+2 → +5 → +10` 间隔复测。

## 产出结构

```text
<主题目录>/
├── <主题目录名>.md      # 唯一正文（含核心主线图、学科定位、问题模块、总复习、术语表）
└── _notes/
    ├── structure.md     # 核心问题与口径、模块划分、重点清单与素材定位、材料清单
    ├── syllabus.md      # 进度状态、章节清单与术语表（terms.avoid）
    ├── mistakes.md      # 按需生成：错题本、主线认知断点与复测间隔
    └── quiz-key.md      # 按需生成：发题前预锁的标准答案与得分点
```
