<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/plank-v2.0-6C5CE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIvPjxsaW5lIHgxPSI5IiB5MT0iOSIgeDI9IjIxIiB5Mj0iOSIvPjxsaW5lIHgxPSI5IiB5MT0iMyIgeDI9IjkiIHkyPSIyMSIvPjwvc3ZnPg==">
    <img alt="plank" src="https://img.shields.io/badge/plank-v2.0-6C5CE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIvPjxsaW5lIHgxPSIzIiB5MT0iOSIgeDI9IjIxIiB5Mj0iOSIvPjxsaW5lIHgxPSI5IiB5MT0iMyIgeDI9IjkiIHkyPSIyMSIvPjwvc3ZnPg==">
  </picture>
</p>

<p align="center">
  <b>Draw Plank first, then fill in cells</b><br>
  <i>Architecture-first AI development methodology</i>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick%20Start-3%20min-00D084?style=flat-square" alt="Quickstart"></a>
  <a href="#-core-features"><img src="https://img.shields.io/badge/Core%20Features-6%20Capabilities-6C5CE7?style=flat-square" alt="Features"></a>
  <a href="#-real-world-validation"><img src="https://img.shields.io/badge/Real%20World%20Validation-Proven-20C997?style=flat-square" alt="Verified"></a>
  <a href="#-why-plank"><img src="https://img.shields.io/badge/Why%20Plank-Pain%20Points-FF6B6B?style=flat-square" alt="Why"></a>
  <a href="#-full-example"><img src="https://img.shields.io/badge/Full%20Example-Bookkeeping%20CLI-FFA94D?style=flat-square" alt="Example"></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/中文文档-简体%20Chinese-blue?style=flat-square" alt="Chinese"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License">
  <img src="https://img.shields.io/badge/Supported%20Models-8%20Models-blueviolet?style=flat-square" alt="Models">
  <img src="https://img.shields.io/badge/Supported%20Platforms-5%20Platforms-important?style=flat-square" alt="Platforms">
  <img src="https://img.shields.io/badge/Hallucination%20Guards-3%20Layers-9cf?style=flat-square" alt="Guard">
</p>

---

## What is Plank

Plank is an **architecture-first AI development methodology** — draw a complete architecture blueprint (BLUEPRINT.md) first, then have AI fill in code from the bottom up. One Markdown file does three things: **global navigation** (where all modules are), **empty slot marking** (what's left to write), **progress tracking** (what we're doing now).

Plank's core promise is simple: **Draw Plank first, then fill in cells.** No parser to write, no new syntax to learn, no runtime dependencies — BLUEPRINT.md is just plain text, usable directly with your existing AI coding tools.

> Plank originated from an observation: the biggest problem with AI-written code isn't "can't write", it's "no sense of the big picture". It can write a function well, but forgets the interface signature agreed ten conversations ago. Plank uses a continuously maintained blueprint file to give AI a "never-lost context".

### In a Nutshell

> **Blueprint first, code second. Zero breaks in global logic.**

---

## Why Plank

### Have you experienced "AI Coding Syndrome"?

| Symptom | Root Problem | Plank's Solution |
|---------|-------------|-----------------|
| AI writes function calls with non-existent params | No contract definition for interfaces | Pre-write pre/post/error/side-effect declarations for every interface |
| Module A calls an unwritten interface from Module B | Dependencies in wrong direction, wrong build order | @BUILD_ORDER builds from bottom up layer by layer |
| AI forgets design from earlier in conversation halfway through | Context overflow, no persistent architecture record | BLUEPRINT.md is continuously maintained single source of truth |
| Changing one interface breaks three modules | No change tracking | All changes must be documented with @CHANGE, cascading rollback controllable |
| 500 lines written, architecture is wrong | "Write first, think later" trap | Spend 5 minutes drawing blueprint first, confirm before coding |

---

## How it Works

```
Traditional:      "Build a bookkeeping app" → AI writes code → 5 rounds of fixes → broken architecture

Plank:            "Use plank to build a bookkeeping app"
                ↓
           Phase 1 ── AI draws BLUEPRINT.md (modules / interfaces / dependencies / data flows)
                ↓
           You confirm blueprint (~1 minute)
                ↓
           Phase 2 ── AI fills code from bottom up layer by layer
                ↓
           Phase 3 ── AI auto-runs all functional paths
                ↓
           Output: working project + 30-line architecture summary
```

---

## Quick Start: 3 Minutes from Zero to Working

```bash
# In your AI coding tool, say:

"Use plank to build a command-line bookkeeping app"
```

**You'll get in 3 minutes:**

```
  ① AI draws BLUEPRINT.md (all modules/interfaces/data flows clearly visible)
  ② You confirm blueprint (~1 minute)
  ③ AI starts from storage, fills up to cli layer
  ④ AI auto-validates 9 data flows
  ⑤ Generates .arch/SUMMARY.md (30 lines to understand architecture)
```

First time? Start with L1:

```
"Use plank L1 to design a user management interface"
```

AI will output pre/post/error/side-effect behavior declarations — no coding needed, just experience the rigor of contract design.

---

## Core Features

### Three Core Mechanisms

- **Blueprint Fill Model** — BLUEPRINT.md is global nav + progress tracking + empty slots, one file replaces all scattered design docs
- **Three Hallucination Guard Layers** — behavior declarations + boundary matrix + error chain mapping, layered protection
- **Context Pressure Awareness** — 4 observable signals auto-decide when to release context

### Seven Hard Constraints

User Confirmation Gate → One Slot at a Time → Dependencies First → Changes Documented → Module Boundaries → Interfaces Have Consumers → Read Once

### Exception Handling Granularity

```
Interface-level — this module's external signature changes → cascade rollback downstream
Dependency-level — this module needs new dependency on others → just add annotation, no rollback
```

### Scale Adaptation

| Interface Count | Mode | Validation Strategy |
|--------|------|---------|
| ≤ 10 | Simplified | Skip boundary matrix, simplify error chain |
| 11-50 | Full | Full verification |
| > 50 | Risk-oriented | Only check entry / multi-dependent / external interfaces |

---

## Real World Validation

> Data comes from real-world building of Bookkeeping CLI with Plank.

| Metric | Value |
|--------|-------|
| Module Count | 6 (storage → categories → transactions → budgets → reports → cli) |
| Total Interfaces | 16 |
| Data Flows | 9 |
| Build Layers | 6 |
| Total Code | ~360 lines |
| Dependencies | **Zero** (pure Python stdlib) |
| First Run | **Passed once, zero bugs** |

### Full Runtime Validation Output

```
> python cli.py add-cat "Food" expense
> python cli.py add-cat "Salary" income
Added category: #1 Food (expense)
Added category: #2 Salary (income)

> python cli.py list-cats
ID | Name   | Type
---+--------+------
1  | Food   | expense
2  | Salary | income

> python cli.py add-tx 50.0 1 2026-05-18 --note "Lunch" expense
> python cli.py add-tx 10000.0 2 2026-05-01 --note "Monthly salary" income
Added transaction: #1 $50.00 (expense)
Added transaction: #2 $10,000.00 (income)

> python cli.py set-budget 1 2026-05 500.0
> python cli.py check-budget 1 2026-05
Set budget: 2026-05 budget $500.00
Budget status: Spent $50.00 / Budget $500.00
Remaining: $450.00 (10.0%)

> python cli.py report 2026-05
=== 2026-05 Monthly Report ===
Total Income: $10,000.00
Total Expense: $50.00
Net: $9,950.00
```

---

## Progressive Adoption

You don't have to go full — start with what fits you:

```
                    ┌───────────────────┐
                    │  L3 Full Process    │  ≥ 4 module new projects / major refactors
                    │  Blueprint→Fill→Validate  │  Trigger: "use plank"
                    └────────┬──────────┘
                             │
                    ┌────────┴──────────┐
                    │  L2 Constraint-Driven  │  2-3 module refactors / fix interface mismatches
                    │  7 constraint checks   │  Trigger: "use plank to check constraints"
                    └────────┬──────────┘
                             │
                    ┌────────┴──────────┐
                    │  L1 Behavior Contract│  Design interface / Review code / API docs
                    │  pre/post/         │  Trigger: "use plank L1 to design interface"
                    │  error/side-effect │
                    └───────────────────┘
```

---

## Full Example: 6-Module Bookkeeping CLI

```
bookkeeping-cli/
├── cli.py                       # Command-line interface (Layer 6)
├── categories/__init__.py       # Category management (Layer 2)
├── transactions/__init__.py     # Transaction management (Layer 3)
├── budgets/__init__.py          # Budget management (Layer 4)
├── reports/__init__.py          # Report generation (Layer 5)
├── storage/__init__.py          # Data persistence (Layer 1)
└── .arch/
    ├── BLUEPRINT.md             # Complete architecture blueprint
    └── SUMMARY.md               # Human-readable architecture summary
```

**Dependency Graph:**

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
                    │Storage│◄──────┘  (L1)
                    └──────┘
```

---

## Platform & Model Support

### 5 Platforms

| Platform | Status | Fallback Strategy |
|----------|--------|------------------|
| DeepSeek TUI | ✅ Full Support | — |
| Claude Code | ✅ Full Support | — |
| Trae CN | ✅ Supported | Serial fill when sub-tasks not available |
| Cursor | ✅ Supported | Use file records when planning tools not available |
| Codex CLI | ✅ Supported | Use file records when planning tools not available |

### 8 Models

| Model | Context | Fill Strategy | Validation Rigor |
|-------|---------|--------------|----------------|
| DeepSeek V4 | 1M | Full load + append cache | Deep: thinking mode anticipation |
| DeepSeek V3 | 128K | Phase 1 full, Phase 2 on-demand | Full line-by-line |
| Claude 4.x | 200K | Phase 1 full, Phase 2 on-demand | Strictest: zero tolerance |
| GPT-4o | 128K | Only current module + dependency signatures | Light: signature only |
| GLM-4 | 128K | Phase 1 full, Phase 2 on-demand | Full |
| Qwen 3 | 128K-1M | Phase 1 full, Phase 2 on-demand | Full |
| Mistral Large | 128K | Only current module | Sampling |
| Llama 4 | 128K-1M | Phase 1 full, Phase 2 on-demand | Full |

---

## Installation

```bash
# DeepSeek TUI
mkdir -p ~/.deepseek/skills/
cp -r plank ~/.deepseek/skills/

# Claude Code
mkdir -p ~/.claude/skills/
cp -r plank ~/.claude/skills/

# Other platforms: paste SKILL.md directly into system prompt
```

### Verify

```
"Use plank L1 to design a simple interface"
→ Correctly outputs pre/post/error/side-effect → installation successful
```

---

## FAQ

<details>
<summary><b>Do I have to go full L3 every time?</b></summary>
No. L1 (behavior contract) and L2 (constraint-driven) are lighter, perfect for single-module tasks.
</details>

<details>
<summary><b>How to use with existing projects?</b></summary>
Use "Reverse Blueprint". AI auto-analyzes project structure to extract modules and interfaces, generating BLUEPRINT.md.
</details>

<details>
<summary><b>Do I need to learn a new DSL?</b></summary>
No. BLUEPRINT.md is pure Markdown, no parser, no compiler, no runtime dependencies.
</details>

<details>
<summary><b>Is Windows compatible?</b></summary>
Yes. Platform adaptation includes Windows encoding handling.
</details>

---

## Roadmap

- [x] Phase 1→2→3 full workflow
- [x] Exception granularity — interface-level vs dependency-level
- [x] Lazy probing — on-demand detection
- [x] Windows encoding adaptation
- [x] Real-world experience docs
- [ ] Interface contract test auto-generation
- [ ] Blueprint snapshot auto-management
- [ ] Mermaid dependency graph visualization

---

## License

MIT © 2026 Plank contributors

---

<p align="center">
  <b>Plank — Plan first. Build right. Ship clean.</b>
  <br><br>
  <a href="#-quick-start">Get Started →</a>
</p>
