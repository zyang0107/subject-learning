# subject-learning

[English](README.md) | 简体中文

很多教材和讲义按章节平铺知识点，学到一半容易只记住零散定义，不知道整门课到底在解决什么问题。

`subject-learning` 先厘清这门学科要解决的核心问题和推导主线，搭出按问题组织的模块骨架，再把概念、方法和高频考点填进对应的位置。文档写完后，还能直接做一题一判的主动回忆测验，帮你查出理解断在哪里。

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

**用法**：调用 `/subject-learning`（或 `$subject-learning`），提供素材路径（支持 PDF、PPTX、DOCX、EPUB 或文本，原文件保持只读）、输出目录、学习目标（`mission`）和深度（`blueprint_only` 只出范围蓝图、`outline` 精简骨架、`full` 替代原书的完整版本）。输出目录下已有 `_notes/syllabus.md` 时，会自动从断点续写或进入测验。

## 怎么工作

1. **先立主线，再定重点（[`blueprint.md`](references/blueprint.md)）**：盘点素材并梳理考核范围与排除项，提炼出核心问题、解决主线和问题模块。后续反复用到的基础概念以及习题常考内容会优先标为重点，同时写好一个真实样例交给你确认，拍板后再动笔。
2. **逐模块撰写（[`drafting.md`](references/drafting.md)）**：每次只写一个模块，写完首个核心模块先停下来过样章，校准深度和写法。每个要点一次讲清它解决什么问题、怎么运作以及适用边界，先跑通主干再补充例外，并给抽象概念配上可验证的具体例子；只有遇到阻断理解的缺口时，才联网核查权威资料。
3. **校验与交付（[`audit.py`](scripts/audit.py)）**：通篇检查基础概念的回指与不同流派的取舍对比，最后运行 `audit.py`，确保标题结构与 `syllabus.md` 完全对齐，且正文没有遗留占位符或术语混用（`terms.avoid`）。
4. **测验与诊断（[`practice.md`](references/practice.md)）**：每次只出一道题，覆盖基础回忆、课程原题应用和边界迁移三种难度，并在发题前把参考答案和得分点先写入 `_notes/quiz-key.md`，避免批改时顺从放水。答错后区分记忆遗漏和理解偏差，理解偏差会退回学科主线指出卡点，并按 `+2 -> +5 -> +10` 的间隔安排复测。

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
