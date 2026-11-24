---
name: subject-learning
description: 围绕学科核心问题与解决主线，梳理课程/教材的范围、考核口径与基础枢纽重点，产出可替代原书的中文学习文档，并支持配套测验巩固。用户提供课件、讲稿、大纲、习题或教材，要求整理重点范围、编写系统学习文档或进行学后测验时使用。
---

# 入口

每次调用先检查用户指定的主题目录下是否已有 `_notes/plan.md` 且 `skill: subject-learning`：

**接手**：读 `_notes/plan.md` 的 front matter，按优先级从上到下匹配动作：

| 状态 | 动作 |
| --- | --- |
| 用户要求测验 / 刷题 / 复测错题 | 直接进入「按需分支 · 测验与巩固」（若连素材都未盘点，先按新建走阶段一） |
| `blueprint: pending` | 若 `_notes/plan.md` 三节齐全，从阶段一第 4 步报用户开始；否则从第 1 步开始 |
| `depth: blueprint_only` 且 `blueprint: approved` | 蓝图已交付；问用户是否升级写书。确认升级后更新 `depth`（`outline`/`full`）、置 `book: in_progress` 并补齐 `sections` 进入阶段二（无样例时以首个问题模块的样章门定手感） |
| 有板块为 `stale` | 先回改该板块 |
| 有板块为 `review` | 把该板块交给用户过样章门 |
| 有板块为 `pending` | 写第一个 `pending` 板块 |
| 全部 `done` 且 `book` 非 `complete` | 进入阶段三终审交付 |

**新建**：一次向用户问清尚未提供的 4 项信息：
1. 素材目录或文件路径；
2. 输出主题目录（落点路径）；
3. `mission`（学习目标：为什么学、学完想解决什么问题）；
4. `depth`（`blueprint_only` 只出范围与重点蓝图 / `outline` 精简骨架版 / `full` 替代原书详尽版）。

# 工作流

## 阶段一 · 定主线与标重点（蓝图）

本阶段仅读取 `references/blueprint.md`。

1. **盘素材与抓口径**：扫清可用素材与不可读/缺漏文件（保持原文件只读，无需登记行政杂项）；提取大纲、考核、评分标准、练习与反馈中的难度要求及明确不考项。
2. **定主线与标重点**：提炼核心问题、解决主线、研究边界与前置知识，顺主线划分问题模块（原课程顺序契合主线时直接沿用，零散或倒置时按问题逻辑重排），标出各模块的**基础枢纽**与**考核高频**重点及原题位置。
3. **落盘账本**：创建输出目录，写入 `_notes/plan.md`（`blueprint: pending`，记录 `source`、前置知识、口径、分模块重点定位及 `sections`）。本阶段只记决策与来源定位，正文细节留待阶段二精读原文直接成文。
4. **报用户拍板**：一次报齐四样——① 核心问题、解决主线、考核口径与明确不考项；② 前置知识；③ 问题模块与重点清单（附基础枢纽/考核权重依据，默认分「重点 / 常规 / 带过」请用户调整）；④ 按所选 `depth` 真写出来的 1 个常规要点样例（`blueprint_only` 模式免写样例）。
5. **批准蓝图**：用户确认后将 `blueprint` 置 `approved`，回填最终分档并把样例写入 `_notes/plan.md`「写作偏好」。若 `depth: blueprint_only`，直接将面向读者的蓝图写入 `<主题目录名>.md`（含 `## 学科定位与全书地图` 与 `## 重点与学习范围`），置 `book: blueprint_only` 并跑 `audit.py` 交付结束。

**完成标准**：`_notes/plan.md` 三节齐全；前置知识、考核排除项与重点分档已获用户确认。

## 阶段二 · 按问题模块成文

本阶段仅读取 `references/drafting.md`。

每次只写一个板块。开写前完成 4 件事：
1. 核对正文 H2 目录与上一板块结尾，保留用户跨会话的手工修改；正文里留有半截的板块整块重写。
2. 按 `_notes/plan.md` 的 `source` 与来源定位，精读本板块常规/重点要点的原始素材并直接用于成文；遇阻断后文的解释断点，按 `drafting.md` 定向查证并将新增来源/缺口补记回 `_notes/plan.md`。
3. 核对本板块依赖的前置概念均已由前置知识或更早板块交付；若缺失，先调整结构再动笔。
4. 重读一遍 `_notes/plan.md`「写作偏好」中的样例与样章反馈。

问题模块通过 `drafting.md`「板块级硬检」全部 6 条后置 `done`；首尾固定 2 节（`学科定位与全书地图`、`考前速查与自检`）按 `drafting.md` 交付标准核对后置 `done`。

**样章门**：第一个正式问题模块写完置 `review`，交给用户审 4 件事：开场是否切中真实问题、要点之间衔接是否顺畅、深度与例子是否合适、收尾是否自然引向下一板块。将反馈写入「写作偏好」，用户点头后置 `done`。

**结构调整**：模块内拆合可先改 `_notes/plan.md` 再动正文；增删模块或调整模块依赖时，停下来向用户报冲突，并将受影响的已完成模块置 `stale`。

## 阶段三 · 终审交付

全部 `sections` 均为 `done` 后执行：
1. **全书级核对**：基础枢纽在首次出现时讲透并在后续模块显式回指；竞争方案讲清各自前提与取舍；同一要点不在两处重复展开；`学科定位与全书地图`、`考前速查与自检` 与正文及术语保持一致。
2. **脚本校验**：运行 `python3 "<skill-dir>/scripts/audit.py" "<主题目录>"`（`<skill-dir>` 为本 `SKILL.md` 所在目录的绝对路径）。

**完成标准**：全书级核对与 `audit.py` 全部通过 → `book` 置 `complete`。

## 按需分支 · 测验与巩固

任意模块完成后，或全书读完、需要针对某模块/错题本检验掌握程度时触发。本分支仅读取 `references/practice.md`。

1. 确定测验范围（刚学完的模块 / 指定重点 / 全书综合 / 错题重测）；每次只出 1 题，总轮数按模块难度与重点密度弹性调整，每过几轮穿插 1 道最久未复测的错题。
2. 出题前先将本轮参考答案与可核验得分点落盘至 `_notes/quiz-key.md`，对话中只呈现题目与来源标注（原题 / AI 自拟），等待用户作答。
3. 用户作答后，先重读 `_notes/quiz-key.md` 逐点严格判分；再按错因分流（记忆性错误直接纠偏；理解性错误退回 `_notes/plan.md` 的核心问题与解决主线定位认知断点），将错题记入 `<主题目录名>-错题本.md`。

# 输出格式

```text
<主题目录>/
├── <主题目录名>.md          # 唯一正文（blueprint_only 模式为蓝图版；outline/full 为完整学习文档）
├── <主题目录名>-错题本.md    # 按需生成：错题、主线认知断点与三态复测进度（面向学习者复盘）
└── _notes/
    ├── plan.md              # 单源工作账本：YAML front matter + 固定三节 H2（见 references/blueprint.md）
    └── quiz-key.md          # 按需生成：当前测验题的预设判分要点（防顺从判对）
```

`_notes/plan.md` 标准 YAML front matter（`sections` 固定为 `学科定位与全书地图` + 各问题模块 + `考前速查与自检`，与正文 H2 同名同序；`terms` 可选，供 `audit.py` 检查易混术语漂移）：

```yaml
---
skill: subject-learning
topic: <主题名>
source: <素材目录或文件路径>
mission: <学习目标>
depth: full # blueprint_only | outline | full
blueprint: pending # pending | approved
book: in_progress # in_progress | complete | blueprint_only
sections:
  - title: 学科定位与全书地图
    status: pending # pending | review | done | stale
  - title: <问题模块标题>
    status: pending
  - title: 考前速查与自检
    status: pending
terms:
  - zh: <规范中文译名>
    en: <英文原词>
    avoid: [<需拦截的误译或别称>]
---
```
