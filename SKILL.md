---
name: subject-learning
description: 围绕学科核心问题与解决主线，梳理课程/教材的范围、考核口径与基础枢纽重点，产出可替代原书的中文学习文档，并支持配套测验巩固。用户提供课件、讲稿、大纲、习题或教材，要求整理重点范围、编写系统学习文档或进行学后测验时使用。
---

# 入口

每次调用先检查用户指定的主题目录下是否已有 `_notes/syllabus.md` 且 `skill: subject-learning`：

**接手**：读 `syllabus.md` 的 front matter，按优先级从上到下匹配动作：

| 状态 | 动作 |
| --- | --- |
| 用户要求测验 / 刷题 / 复测错题 | 直接进入「按需分支 · 测验与巩固」（若连素材都未盘点，先按新建走阶段一） |
| `blueprint: pending` | 若 `structure.md` 四节齐全，从阶段一第 4 步报用户开始；否则从第 1 步开始 |
| `depth: blueprint_only` 且 `blueprint: approved` | 蓝图已交付；问用户是否升级写书。确认升级后更新 `depth`（`outline`/`full`）、置 `book: in_progress` 并补齐 `sections` 进入阶段二（无样例时以首个问题板块的样章门定手感） |
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

1. **盘素材与抓口径**：盘点全部文件、识别材料角色与缺漏重复（保持原文件只读）；提取大纲、考核、评分标准、练习与反馈中的难度要求及明确不考项。
2. **定主线与标重点**：提炼核心问题与解决主线，顺主线划分问题模块（原课程顺序契合主线时直接沿用，零散或倒置时按问题逻辑重排），列出各模块的核心概念/方法清单，标出**基础枢纽**与**考核/高频权重**作为推荐重点。
3. **落盘笔记**：创建输出目录，写入 `_notes/structure.md` 和 `_notes/syllabus.md`（`blueprint: pending`，记录 `source` 素材路径，并按下方固定首尾节 + 各问题模块初始化 `sections`）。本阶段只填蓝图决策字段，正文细节留待阶段二精读原文直接成文。
4. **报用户拍板**：一次报齐四样——① 核心问题与解决主线（含课程考核口径与排除项）；② 前置知识；③ 问题模块与重点清单（附基础枢纽/考核权重依据，默认分「重点 / 常规 / 带过」请用户调整）；④ 按所选 `depth` 真写出来的 1 个常规要点样例（`blueprint_only` 模式免写样例）。
5. **批准蓝图**：用户确认后将 `blueprint` 置 `approved`，回填最终分档，把样例记入 `syllabus.md`「写作偏好」。若 `depth: blueprint_only`，将 `book` 置 `blueprint_only` 并交付结束。

**完成标准**：`_notes/structure.md` 四节齐全、全部可用素材均已登记在材料清单中；前置知识与重点分档已获用户确认。

## 阶段二 · 按问题模块成文

本阶段仅读取 `references/drafting.md`。

每次只写一个板块。开写前完成 4 件事：
1. 核对正文 H2 目录与上一板块结尾，保留用户跨会话的手工修改；正文里留有半截的板块整块重写。
2. 按 `syllabus.md` 的 `source` 路径与 `_notes/structure.md` 的来源定位，精读本板块常规/重点要点的原始素材并直接用于成文；遇阻断后文的解释断点，按 `drafting.md` 定向查证并将新增来源/缺口补记回 `structure.md`。
3. 核对本板块依赖的前置概念均已由前置知识或更早板块交付；若缺失，先调整结构再动笔。
4. 重读一遍 `syllabus.md`「写作偏好」中的样例与样章反馈。

问题模块通过 `drafting.md`「板块级硬检」全部 6 条后置 `done`；固定首尾 6 节按 `drafting.md` 骨架表各自完成标准核对后置 `done`。

**样章门**：第一个正式问题板块写完置 `review`，交给用户审 4 件事：开场是否切中真实问题、要点之间衔接是否顺畅、深度与例子是否合适、收尾是否自然引向下一板块。将反馈写入「写作偏好」，用户点头后置 `done`。

**结构调整**：板块内拆合可先改笔记再动正文；增删板块或调整板块依赖时，停下来向用户报冲突，并将受影响的已完成板块置 `stale`。

## 阶段三 · 终审交付

全部 `sections` 均为 `done` 后执行：
1. **全书级核对**：基础枢纽在首次出现时讲透并在后续板块显式回指；竞争方案讲清各自前提与取舍；同一要点不在两处重复展开；「全书地图」「学科定位」与末四节完整对齐正文与 `terms`；术语与记号全书统一。
2. **脚本校验**：运行 `python3 "<skill-dir>/scripts/audit.py" "<主题目录>"`（`<skill-dir>` 为本 `SKILL.md` 所在目录的绝对路径）。

**完成标准**：全书级核对与 `audit.py` 全部通过 → `book` 置 `complete`。

## 按需分支 · 测验与巩固

任意模块完成后，或全书读完、需要针对某模块/错题本检验掌握程度时触发。本分支仅读取 `references/practice.md`。

1. 确定测验范围（刚学完的模块 / 指定重点 / 全书综合 / 错题重测）；每次只出 1 题，总轮数按板块难度与重点密度弹性调整，并按间隔穿插往期到期错题。
2. 出题前先将本轮参考答案与可核验得分点落盘至 `_notes/quiz-key.md`，对话中只呈现题目与来源标注（原题 / AI 自拟），等待用户作答。
3. 用户作答后，先重读 `_notes/quiz-key.md` 逐点严格判分；再按错因分流（记忆性错误直接纠偏记录；理解性错误退回学科核心问题与解决主线定位认知断点），将错题记入 `_notes/mistakes.md`。

# 输出格式

```text
<主题目录>/
├── <主题目录名>.md      # 唯一正文，与目录同名，含全部板块（blueprint_only 模式可不生成）
└── _notes/
    ├── structure.md     # 固定四节 H2，格式见 references/blueprint.md
    ├── syllabus.md      # YAML front matter + 固定两节 H2（全书约定、写作偏好）
    ├── mistakes.md      # 可选：测验错题本与认知断点记录（测验分支生成）
    └── quiz-key.md      # 可选：当前测验题的预设判分要点（防顺从判对）
```

`syllabus.md` 标准 YAML front matter（`sections` 固定含前 2 节 + 各问题模块 + 末 4 节，与正文 H2 同名同序；`terms.avoid` 供 `audit.py` 检查术语漂移）：

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
  - title: 全书地图
    status: pending # pending | review | done | stale
  - title: 学科定位
    status: pending
  - title: <问题模块标题>
    status: pending
  - title: 总复习
    status: pending
  - title: 术语表
    status: pending
  - title: 想深入的话去读什么
    status: pending
  - title: 本书故意没讲什么
    status: pending
terms:
  - zh: <规范中文译名>
    en: <英文原词>
    avoid: [<需拦截的误译或别称>]
---
```
