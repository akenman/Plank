<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/plank-v2.0-6C5CE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIvPjxsaW5lIHgxPSI5IiB5MT0iOSIgeDI9IjIxIiB5Mj0iOSIvPjxsaW5lIHgxPSI5IiB5MT0iMyIgeDI9IjkiIHkyPSIyMSIvPjwvc3ZnPg==">
    <img alt="plank" src="https://img.shields.io/badge/plank-v2.0-6C5CE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIvPjxsaW5lIHgxPSIzIiB5MT0iOSIgeDI9IjIxIiB5Mj0iOSIvPjxsaW5lIHgxPSI5IiB5MT0iMyIgeDI9IjkiIHkyPSIyMSIvPjwvc3ZnPg==">
  </picture>
</p>

<p align="center">
  <b>画好 Plank，再逐格填充</b><br>
  <i>Architecture-first AI development methodology</i>
</p>>

<p align="center">
  <a href="#-快速体验"><img src="https://img.shields.io/badge/快速体验-3分钟-00D084?style=flat-square" alt="Quickstart"></a>
  <a href="#-核心特性"><img src="https://img.shields.io/badge/核心特性-6大能力-6C5CE7?style=flat-square" alt="Features"></a>
  <a href="#-实战验证"><img src="https://img.shields.io/badge/实战验证-真实项目-20C997?style=flat-square" alt="Verified"></a>
  <a href="#-为什么需要-plank"><img src="https://img.shields.io/badge/为什么需要-痛点分析-FF6B6B?style=flat-square" alt="Why"></a>
  <a href="#-完整示例"><img src="https://img.shields.io/badge/完整示例-6模块记账工具-FFA94D?style=flat-square" alt="Example"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License">
  <img src="https://img.shields.io/badge/适用模型-8种-blueviolet?style=flat-square" alt="Models">
  <img src="https://img.shields.io/badge/适用平台-5个-important?style=flat-square" alt="Platforms">
  <img src="https://img.shields.io/badge/幻觉防护-3层-9cf?style=flat-square" alt="Guard">
</p>

---

## Plank 是什么

Plank 是一套**架构优先的 AI 编程方法论**——先绘制完整的架构蓝图（BLUEPRINT.md），再让 AI 从底层向上逐格填充代码。它用一份 Markdown 文件同时做到三件事：**全局导航**（所有模块在哪）、**空位标记**（还剩什么没写）、**进度追踪**（当前在做什么）。

Plank 的核心主张很简单：**先画好 Plank，再逐格填充。** 不写解析器、不学新语法、不引入运行时依赖——BLUEPRINT.md 就是纯文本，你现有的 AI 编程工具直接使用。

> Plank 最初来源于一个观察：AI 写代码最大的问题不是"不会写"，而是"没有全局感"。它能写好一个函数，但会忘记十个对话前确定的接口签名。Plank 用一份持续维护的蓝图文件，给 AI 提供一个"永不丢失的上下文"。

### 一句话概括

> **先蓝图，后代码。全局逻辑零断裂。**

---

## 为什么需要 Plank

### 你是否有过这些「AI 编程综合征」？

| 症状 | 深层问题 | Plank 的方案 |
|------|---------|-------------|
| AI 写的函数调用不存在的参数 | 接口没有契约定义 | 每个接口先写 pre/post/error/side-effect 四段声明 |
| 模块 A 调了模块 B 还没写的接口 | 依赖方向反了，或构建顺序不对 | @BUILD_ORDER 从底层向上逐层构建 |
| 对话到一半 AI 忘了前面 10 轮的设计 | 上下文溢出，无持久化架构记录 | BLUEPRINT.md 是持续维护的架构真相源 |
| 改了一个接口，三个模块跟着崩 | 无变更追踪 | 所有变更必须记录 @CHANGE，级联回退可控 |
| 写了 500 行发现架构不对 | "先写再说"的陷阱 | 先花 5 分钟画蓝图，确认后再写代码 |

---

## 它是如何工作的

```
传统方式：      "帮我写个记账工具" → AI 直接写代码 → 改 5 轮 → 架构崩坏

Plank 方式：    "用 plank 帮我写个记账工具"
               ↓
           Phase 1 ── AI 画出 BLUEPRINT.md（模块 / 接口 / 依赖 / 数据流）
               ↓
           你确认蓝图（约 1 分钟）
               ↓
           Phase 2 ── AI 从底层向上逐格填充代码
               ↓
           Phase 3 ── AI 自动运行验证所有功能路径
               ↓
           产出可运行的项目 + 30 行架构摘要
```

---

## 快速体验：3 分钟从零到运行

```bash
# 在你的 AI 编程工具中输入：

"用 plank 帮我做一个命令行记账工具"
```

**你将在 3 分钟内得到：**

```
 ① AI 画 BLUEPRINT.md（所有模块/接口/数据流清晰可见）
 ② 你确认蓝图（约 1 分钟）
 ③ AI 从 storage 开始，逐层填充到 cli 层
 ④ AI 自动运行 9 条数据流验证
 ⑤ 生成 .arch/SUMMARY.md（30 行看懂架构）
```

首次使用，建议先从 L1 开始熟悉：

```
"用 plank L1 设计一个用户管理接口"
```

AI 会输出该接口的 pre/post/error/side-effect 行为声明——不需要写代码，先感受下契约设计的严谨性。

---

## 核心特性

### 三大核心机制

- **蓝图填充模型** — BLUEPRINT.md 是全局导航 + 进度追踪 + 空位标记，一份文件代替所有散落的设计文档
- **三层幻觉防护** — 行为声明 + 边界矩阵 + 错误链映射，环环相扣
- **上下文压力感知** — 4 个可观察信号自动判断何时释放上下文

### 7 条硬约束

用户确认门 → 一次一格 → 依赖先填 → 变更有痕 → 模块边界 → 接口有消费者 → 一次读取

### 异常处理细分

```
接口级异常 ── 本模块对外接口签名变了 → 级联回退下游模块
依赖级异常 ── 本模块需要新增对其他模块的依赖 → 只补充标注，不回退
```

### 规模自适应

| 接口数 | 模式 | 验证策略 |
|--------|------|---------|
| ≤ 10 | 简化 | 跳过边界矩阵，精简错误链 |
| 11-50 | 完整 | 全量检查 |
| > 50 | 风险导向 | 只检查入口/被多模块依赖/外部依赖接口 |

---

## 实战验证

> 以下数据来自用 Plank 从零构建 Bookkeeping CLI 的真实过程。

| 指标 | 数据 |
|------|------|
| 模块数 | 6（storage → categories → transactions → budgets → reports → cli） |
| 接口总数 | 16 |
| 数据流 | 9 条 |
| 构建层数 | 6 层 |
| 总代码量 | ~360 行 |
| 第三方依赖 | **零**（纯 Python 标准库） |
| 首次运行 | **一次性通过，零 bug** |

### 完整的运行时验证输出

```
> python cli.py add-cat "餐饮" expense
> python cli.py add-cat "工资" income
已添加分类: #1 餐饮 (expense)
已添加分类: #2 工资 (income)

> python cli.py list-cats
ID | 名称 | 类型
---+------+----
1  | 餐饮 | expense
2  | 工资 | income

> python cli.py add-tx 50.0 1 2026-05-18 --note "午餐" expense
> python cli.py add-tx 10000.0 2 2026-05-01 --note "月薪" income
已添加交易: #1 ￥50.00 (expense)
已添加交易: #2 ￥10,000.00 (income)

> python cli.py set-budget 1 2026-05 500.0
> python cli.py check-budget 1 2026-05
已设置预算: 2026-05 预算 ￥500.00
预算状态: 已花费 ￥50.00 / 预算 ￥500.00
剩余: ￥450.00 (10.0%)

> python cli.py report 2026-05
=== 2026-05 月度报表 ===
总收入: ￥10,000.00
总支出: ￥50.00
净额: ￥9,950.00
```

---

## 渐进式采用

不一定要走完整流程，从最适合你的粒度开始：

```
                    ┌───────────────────┐
                    │  L3 完整流程       │  ≥ 4 模块新项目 / 大型重构
                    │  蓝图→填充→验证    │  触发: "用 plank"
                    └────────┬──────────┘
                             │
                    ┌────────┴──────────┐
                    │  L2 约束驱动       │  2-3 模块重构 / 修复接口不一致
                    │  7 条约束检查      │  触发: "用 plank 检查约束"
                    └────────┬──────────┘
                             │
                    ┌────────┴──────────┐
                    │  L1 行为契约       │  设计接口 / Review 代码 / 写 API 文档
                    │  pre/post/        │  触发: "用 plank L1 设计接口"
                    │  error/side-effect │
                    └───────────────────┘
```

---

## 完整示例：6 模块记账工具

```
bookkeeping-cli/
├── cli.py                       # 命令行界面（第 6 层）
├── categories/__init__.py       # 分类管理（第 2 层）
├── transactions/__init__.py     # 交易管理（第 3 层）
├── budgets/__init__.py          # 预算管理（第 4 层）
├── reports/__init__.py          # 报表生成（第 5 层）
├── storage/__init__.py          # 数据持久化（第 1 层）
└── .arch/
    ├── BLUEPRINT.md             # 完整架构蓝图
    └── SUMMARY.md               # 人类可读架构摘要
```

**依赖图：**

```
                      ┌──────┐
                      │ CLI  │  (L6)
                      └──┬───┘
               ┌─────────┼──────────┐
               │         │          │
            ┌──┴──┐  ┌──┴──┐   ┌───┴───┐
            │Rpts │  │Budgt│   │ Cat   │  (L5/L4/L2)
            └──┬──┘  └──┬──┘   └───┬───┘
               │        │          │
            ┌──┴──┐  ┌──┴──┐      │
            │ Tx  │──┘     │       │  (L3)
            └──┬──┘        │       │
               └───────┬───┘       │
                       │           │
                    ┌──┴───┐       │
                    │Storage│◄──────┘  L1)
                    └──────┘
```

---

## 平台 & 模型支持

### 5 个平台

| 平台 | 状态 | 回退策略 |
|------|------|---------|
| DeepSeek TUI | ✅ 完全支持 | — |
| Claude Code | ✅ 完全支持 | — |
| Trae CN | ✅ 支持 | 子任务不可用时串行填充 |
| Cursor | ✅ 支持 | 计划工具不可用时用文件记录 |
| Codex CLI | ✅ 支持 | 计划工具不可用时用文件记录 |

### 8 个模型

| 模型 | 上下文 | 填充策略 | 验证强度 |
|------|--------|---------|---------|
| DeepSeek V4 | 1M | 全量加载 + 追加缓存 | 深度：思考模式预判 |
| DeepSeek V3 | 128K | Phase 1 全量，Phase 2 按需 | 全量逐行 |
| Claude 4.x | 200K | Phase 1 全量，Phase 2 按需 | 最严格：零容忍 |
| GPT-4o | 128K | 仅当前模块+依赖签名 | 轻量：仅检查签名 |
| GLM-4 | 128K | Phase 1 全量，Phase 2 按需 | 全量 |
| Qwen 3 | 128K-1M | Phase 1 全量，Phase 2 按需 | 全量 |
| Mistral Large | 128K | 仅当前模块 | 抽样 |
| Llama 4 | 128K-1M | Phase 1 全量，Phase 2 按需 | 全量 |

---

## 安装

```bash
# DeepSeek TUI
mkdir -p ~/.deepseek/skills/
cp -r plank ~/.deepseek/skills/

# Claude Code
mkdir -p ~/.claude/skills/
cp -r plank ~/.claude/skills/

# 其他平台直接粘贴 SKILL.md 内容到系统提示中
```

### 验证

```
"用 plank L1 设计一个简单的接口"
→ 能正确输出 pre/post/error/side-effect → 安装成功
```

---

## 常见问题

<details>
<summary><b>每次都要走完整 L3 吗？</b></summary>
不需要。L1（行为契约）和 L2（约束驱动）更轻量，适合单模块任务。
</details>

<details>
<summary><b>已有项目怎么用？</b></summary>
使用「逆向蓝图」功能。AI 自动分析项目结构后提取模块和接口，生成 BLUEPRINT.md。
</details>

<details>
<summary><b>需要学习新 DSL 吗？</b></summary>
不需要。BLUEPRINT.md 是纯 Markdown，没有解析器、没有编译器、没有运行时依赖。
</details>

<details>
<summary><b>Windows 兼容吗？</b></summary>
兼容。平台适配中包含 Windows 的编码适配方案。
</details>

---

## 路线图

- [x] Phase 1→2→3 完整工作流
- [x] 异常细分 — 接口级 vs 依赖级
- [x] 惰性探针 — 按需检测
- [x] Windows 编码适配
- [x] 实战经验文档
- [ ] 接口契约测试自动生成
- [ ] 蓝图快照自动管理
- [ ] Mermaid 依赖图可视化

---

## License

MIT © 2026 Plank contributors

---

<p align="center">
  <b>Plank — Plan first. Build right. Ship clean.</b>
  <br><br>
  <a href="#-快速体验">开始使用 →</a>
</p>