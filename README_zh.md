# subject-learning

[English](README.md) | 简体中文

很多教材和讲义按章节平铺知识点，学到一半容易只记住零散定义，不知道整门课到底在解决什么问题。

`subject-learning` 先理清这门学科要解决的核心问题和推导主线，搭出按问题组织的模块骨架，再把概念、方法和高频考点填进对应的位置。文档写完后，还能直接做一题一判的主动回忆测验，帮你查出理解卡在哪里。

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

**用法**：调用 `/subject-learning`（或 `$subject-learning`），提供素材路径（支持 PDF、PPTX、DOCX、EPUB 或文本，原文件保持只读）、输出目录、学习目标（`mission`）和输出形式（`map` 只出框架：直接输出导览图与重点清单；`guide` 学习讲义：默认项，先完成框架，再按模块写出主线学习文档）。输出目录下已有 `notes/plan.md` 时，会自动从断点续写或进入测验。

## 怎么工作

1. **定框架与重点（[`map.md`](references/map.md)，两种模式均必经）**：梳理可用素材、前置知识与考核排除项，提炼出核心问题、解决主线和问题模块。按**枢纽**（全书仅 2–4 个、支撑后续多个模块的核心概念）、**重点**（本模块核心结论、高频考点或关键争议）、**常规**与**带过**四个层级划分，并在 `guide` 模式下按 [`style.md`](references/style.md) 默认文风写好一个真实样例交给你确认；若选 `map`（只出框架），确认后直接输出面向阅读的框架文档即结束。
2. **按模块写讲义（[`guide.md`](references/guide.md) 与 [`style.md`](references/style.md)，`guide` 模式）**：沿用第一阶段确认好的框架，写完首个核心模块先停下来做样章确认，校准深度和写法；获批后默认按序逐块保存进度并一次性写完其余章节。按内容性质（概念机制 / 观点现象 / 分歧批判）自然展开，抽象概念配可反向验证的最短路径例子，统一复用固定色板的 Mermaid 结构图；只有遇到阻断理解的缺口时，才联网核查权威资料。
3. **校验与完成（[`audit.py`](scripts/audit.py)）**：通篇检查核心概念的前后衔接、竞争方案对照与全书速查自测，最后运行 `audit.py`，确保标题结构与 `notes/plan.md` 完全对齐，且正文没有遗留占位符或术语混用（`terms.avoid`）。
4. **测验与复习（[`practice.md`](references/practice.md)）**：进入测验时默认先询问练习整本还是局部指定模块，再按统一标准在同目录下生成对应范围的 `<主题目录名>-习题册.md`（全部题目、参考答案与得分要点均放入其中，按「选择题 → 判断题 → 问答题」集中编排）。对话测验提供「顺序刷 / 打乱刷 / 只看错题」三种模式，用 `notes/quiz.md` 作为做题指针与对错/错因记录，对照习题册答案严格判分，错题记入 `<主题目录名>-错题本.md`；一轮结束后自动做薄弱点回顾，针对错得多的模块将难度略低的专项题追加到原模块末尾（不改动旧题号）。

## 产出结构

```text
<主题目录>/
├── <主题目录名>.md          # 唯一正文（map 模式只出框架；guide 模式为主线学习讲义）
├── <主题目录名>-习题册.md    # 按需生成：分模块练习题库、答案与得分要点（含专项补题）
├── <主题目录名>-错题本.md    # 按需生成：错题记录、理解卡点与复习进度
└── notes/
    ├── plan.md              # 学习计划与进度：状态、考核要求、分模块重点、写作偏好与缺口
    └── quiz.md              # 按需生成：做题指针、分模块对错统计与用户错因记录
```
