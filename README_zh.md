# subject-learning

[English](README.md) | 简体中文

`subject-learning` 是一套面向课程材料与专业教材的 Agent Skill——它不做机械的“按章流水账摘要”，而是先抽取出这门学科**到底要解决什么核心问题**、沿着**解决主线**重排知识模块，再按课程考核口径标出**基础枢纽**与**高频重点**，最终产出一份可独立替代原书的中文学习文档，并配套主动回忆测验与错题间隔复习。

## 快速上手

```bash
# 推荐：全局安装并自动挂载至 Claude Code 与 Codex
npx skills add zyang0107/subject-learning -a claude-code codex -g -y

# 或对本机所有支持的 Agent Skills 客户端自动探测并挂载（Cursor、Gemini CLI 等）
npx skills add zyang0107/subject-learning -g -y
```

需要手动装配？直接克隆至对应目录：
- **Claude Code**：`git clone https://github.com/zyang0107/subject-learning ~/.claude/skills/subject-learning`
- **Codex**：`git clone https://github.com/zyang0107/subject-learning ~/.codex/skills/subject-learning`
- **通用 Agent Skills 客户端**：`git clone https://github.com/zyang0107/subject-learning .agents/skills/subject-learning`

**使用方式**：调用 `/subject-learning`（或 `$subject-learning`）并提供四项信息即可启动：① 原始素材路径（支持 PDF、PPTX、DOCX、EPUB 及文本，保持只读）；② 输出主题目录；③ 学习目标（`mission`）；④ 成书深度（`blueprint_only` 只出范围与重点蓝图 / `outline` 精简骨架版 / `full` 替代原书详尽版）。若目标目录下已存在 `_notes/syllabus.md`，Skill 会按进度自动接手断点继续推进，或直接切入测验分支。

## 工作流与核心机制

整套流程分为三个顺序阶段和一个按需分支，每阶段按需加载对应的 `references/` 规范文件：

| 阶段 | 参考规范 | 核心工作内容 |
| :--- | :--- | :--- |
| **阶段一 · 定主线与标重点** | [`references/blueprint.md`](references/blueprint.md) | 盘点全部素材与缺漏；提取大纲/真题/评分标准中的考核口径与明确排除项；提炼学科核心问题、解决主线与研究边界；按问题逻辑划分模块并标出**基础枢纽**与**考核高频**重点，附带 1 个真实样例报用户拍板。 |
| **阶段二 · 按问题模块成文** | [`references/drafting.md`](references/drafting.md) | 每次只写一个模块；首个正式模块交付后走**样章门**校准手感；每个重点/常规要点一次讲全“为什么需要、是什么与怎么运作、局限与边界”；抽象概念配具体案例并通过反向检验；遇阻断主线的缺口仅作断点式权威检索；写完通过 6 条板块级硬检。 |
| **阶段三 · 终审交付** | [`SKILL.md`](SKILL.md) / [`scripts/audit.py`](scripts/audit.py) | 全书核对基础枢纽回指、竞争方案取舍、避免重复展开与术语统一；运行 `audit.py` 校验唯一 H1、章节目录与 `syllabus.md` 逐字对齐、无占位符及术语漂移（`terms.avoid`）。 |
| **按需分支 · 测验与巩固** | [`references/practice.md`](references/practice.md) | 每次只出 1 题（覆盖 L1 基础巩固 / L2 原题应用 / L3 边界与迁移）；发题前先将答案与必含得分点锁入 `_notes/quiz-key.md` 防止顺从判对；按“记忆性错误”与“主线理解断点”分流诊断，并以 `+2 → +5 → +10 → 已掌握` 间隔穿插复测错题。 |

## 产出目录结构

运行时会在用户指定的 `<主题目录>` 下生成如下单文件成书与进度追踪结构：

```text
<主题目录>/
├── <主题目录名>.md      # 唯一正文（含全书地图 Mermaid、学科定位、各问题模块、总复习、术语表等；blueprint_only 模式可不生成）
└── _notes/
    ├── structure.md     # 固定四节：核心问题与课程口径、问题主线与模块划分、重点清单与素材定位、材料清单与缺口
    ├── syllabus.md      # YAML front matter（进度状态、sections 与 terms.avoid）+ 全书约定与写作偏好
    ├── mistakes.md      # 按需生成：错题与认知断点记录及间隔复测进度
    └── quiz-key.md      # 按需生成：当前题目的预设答案与判分细则
```

## 仓库文件

- [`SKILL.md`](SKILL.md)：主入口、状态机路由与三阶段工作流总控
- [`references/blueprint.md`](references/blueprint.md)：阶段一蓝图提炼规范与 `structure.md` 模板
- [`references/drafting.md`](references/drafting.md)：阶段二全书骨架、模块化写作与 6 条板块硬检
- [`references/practice.md`](references/practice.md)：测验分级、防顺从判分、错因分流与间隔复习规则
- [`scripts/audit.py`](scripts/audit.py)：交付前结构、状态、H2 顺序与术语漂移自动校验脚本
- [`agents/openai.yaml`](agents/openai.yaml)：Codex 展示信息与默认触发提示配置
