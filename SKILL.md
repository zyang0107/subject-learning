---
name: subject-learning
description: 按学科核心问题与解决主线整理课程或教材，覆盖范围框架、主线讲义、习题册与错题测验。当用户提供课件、讲稿、大纲、习题或教材，要求划定重点框架、编写主线学习讲义或进行测验复习时使用。
---

# 入口

每次调用先检查输出主题目录下是否已有 `_notes/plan.md`：

**继续已有任务**：读 `_notes/plan.md` 的 front matter，按顺序匹配第一条成立的动作：

| 状态 | 动作 |
| --- | --- |
| 用户要求出习题册 / 刷题 / 测验 / 复习错题 | 进入「测验与复习」（若尚未整理素材，先按新任务走阶段一） |
| `map: pending` | 若 `_notes/plan.md` 三节齐全，直接做阶段一确认；否则从头跑阶段一 |
| `mode: map` 且 `map: approved` 且 `status: in_progress` | 按 `references/map.md` 输出框架文档 `<主题目录名>.md`，通过 `audit.py` 后置 `status: complete` |
| `mode: map` 且 `map: approved` 且 `status: complete` | 告知框架已完成，询问是否升级写成学习讲义；确认后改为 `mode: guide`、`status: in_progress` 并补齐 `sections` 进入阶段二 |
| 有板块为 `stale` | 先回改该板块 |
| 有板块为 `review` | 发给用户做样章确认 |
| 有板块为 `pending` | 写第一个 `pending` 板块 |
| 全部 `done` 且 `status` 非 `complete` | 进入阶段三通篇检查与完成 |

**开始新任务**：一次向用户问清尚未提供的 4 项信息：
1. 素材目录或文件路径；
2. 输出目录；
3. `mission`（学习目标：为什么学、学完想解决什么问题）；
4. `mode`（`map` 只出框架：导览图与重点清单 / `guide` 学习讲义：默认项，在框架基础上写成主线学习文档）。

无论选 `map` 还是 `guide`，都必须先走完**阶段一**定好框架；`map` 在框架确认后输出结束，`guide` 沿用同一框架继续走阶段二。

# 工作流

## 阶段一 · 定框架与标重点（`map` 与 `guide` 共用）

读取 `references/map.md`（`guide` 模式写样例时一并读取 `references/style.md`），完成以下动作：
1. 整理素材与考核要求，提炼核心问题、解决主线、研究边界与前置知识，划出问题模块并按「枢纽 / 重点 / 常规 / 带过」分级，写入 `_notes/plan.md`（`map: pending`、`status: in_progress`）。
2. 将范围与重点清单（`guide` 模式附 1 个常规要点样例）一次发给用户确认；获批后置 `map: approved` 并写入最终分级与写作偏好。
3. 若为 `mode: map`，按 `map.md` 写出 `<主题目录名>.md`，运行 `audit.py` 通过后置 `status: complete` 结束。

**完成标准**：`_notes/plan.md` 固定三节齐全，前置知识、考核排除项、模块结构与四档重点均已获用户确认（`mode: map` 还需通过 `audit.py`）。

## 阶段二 · 按问题模块写讲义（`guide` 模式）

读取 `references/guide.md` 与 `references/style.md`，每次只写一个板块：
1. 开写前核对正文目录与上节结尾（保留用户手工修改，半截板块整块重写），精读本板块原始素材，核对前置概念均已讲过，重读 `_notes/plan.md`「写作偏好」。
2. 按 `guide.md` 写法与 `style.md` 风格写完本板块，满足单板块完成标准后置 `done`。
3. **样章确认**：首个正式问题模块写完置 `review`，交用户审 4 件事（开场是否切中真实问题、要点衔接是否顺畅、深浅与例子是否合适、收尾是否自然）；将反馈记入「写作偏好」，确认后置 `done`。
4. **结构调整**：模块内拆合先改 `_notes/plan.md` 再改正文；增删模块或调整依赖关系时停下来向用户说明冲突，并将受影响的已完成模块置 `stale`。

**完成标准**：本板块满足 `guide.md` 全部写法要求，与 `_notes/plan.md` 标题、术语和前置依赖完全一致。

## 阶段三 · 通篇检查与完成（`guide` 模式）

全部 `sections` 置 `done` 后执行：
1. 通篇核对：枢纽概念首次讲透、后续点名衔接；竞争方案前提与取舍清晰；要点无跨节重复展开；首尾固定节与正文及 `terms` 一致。
2. 运行校验：`python3 "<skill-dir>/scripts/audit.py" "<主题目录>"`（`<skill-dir>` 为本 `SKILL.md` 所在目录的绝对路径）。

**完成标准**：通篇核对与 `audit.py` 全部通过 → `status` 置 `complete`。

## 测验与复习

读取 `references/practice.md`，执行：
1. 若目录下尚无 `<主题目录名>-习题册.md`，先按 `practice.md` 的覆盖配额与三类题型标准生成完整习题册（含全部答案与得分要点）。
2. 对话测验时先读 `_notes/quiz.md`（无则新建），确认范围与模式（`顺序刷` / `打乱刷` / `只看错题`），每次出 1 题并更新指针；用户作答后对照习题册答案判分，将结果与错因记入 `_notes/quiz.md`，错题同步记入 `<主题目录名>-错题本.md`。
3. 一轮结束后依据 `_notes/quiz.md` 做测后回顾，对薄弱模块按原标准补充难度略低的专项题，直接并入习题册对应模块。

# 输出格式

```text
<主题目录>/
├── <主题目录名>.md          # 唯一正文（map 为框架版；guide 为主线学习讲义）
├── <主题目录名>-习题册.md    # 按需生成：分模块题库、参考答案与得分要点（含专项补题）
├── <主题目录名>-错题本.md    # 按需生成：面向读者复盘的错题、主线纠偏与复习状态
└── _notes/
    ├── plan.md              # 规划与进度：YAML front matter + 固定三节 H2（模板见 references/map.md）
    └── quiz.md              # 按需生成：做题指针、分模块对错统计与用户错因（不放答案）
```

`_notes/plan.md` 标准 YAML front matter（`guide` 模式的 `sections` 固定为 `全书导览` + 各问题模块 + `全书速查与自测`，与正文 H2 同名同序；`map` 模式可省略 `sections`；`terms` 可选，供 `audit.py` 拦截术语漂移）：

```yaml
---
topic: <主题名>
source: <素材目录或文件路径>
mission: <学习目标>
mode: guide # map | guide
map: pending # pending | approved
status: in_progress # in_progress | complete
sections:
  - title: 全书导览
    status: pending # pending | review | done | stale
  - title: <问题模块标题>
    status: pending
  - title: 全书速查与自测
    status: pending
terms:
  - zh: <规范中文译名>
    en: <英文原词>
    avoid: [<需拦截的误译或别称>]
---
```
