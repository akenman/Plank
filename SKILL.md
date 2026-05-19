---
name: plank
description: Draw complete architecture blueprint (BLUEPRINT.md) first, then fill code from bottom up. One Markdown file, no parser, no new syntax, no runtime dependencies — BLUEPRINT.md is just plain text, directly usable with your existing AI coding tools. Usage scenarios: (1) Any medium+ complexity coding tasks, especially multi-module project repair or refactor. (2) When user says "design first then code", "bad architecture", "code is scattered", "logic has gaps". (3) Proactively suggest when task complexity clearly needs global design.
metadata:
  short-description: Blueprint first, code second. AI coding with zero global logic breaks.
---

# Plank — Architecture-First Development

Draw complete blueprint (BLUEPRINT.md) first, then fill from bottom up. Blueprint is three roles in one: global navigation, empty slot marker, progress tracking. One file replaces all scattered design docs.

## Quick Start (First Time, 3 Minutes)

```
1. Think of a small task (like "command-line todo app", "simple bookkeeping tool")
2. Say: "use plank L1 to design interface"
   → AI outputs pre/post/error/side-effect behavior declarations per interface
3. Say: "continue, L3 full process"
   → AI draws blueprint → fills module by module → validates runtime → generates SUMMARY.md
4. Look at .arch/SUMMARY.md, understand full architecture in 30 lines

Takes 3-5 minutes, produces fully working project.
```

## Layered Loading

This skill loads in layers based on trigger conditions to avoid irrelevant content consuming context.

### L1 Core (Always Loaded, ~300 lines)
These sections are always available:
- Core concepts / quick start / startup instructions
- 7 constraints / 3 hallucination guards / context pressure awareness
- Phase 1/2/3 full workflow + blueprint revision protocol
- Incremental development / iteration mode / reverse blueprint

### L2 Conditional Loading (Auto-expands when conditions met)

| Trigger Condition | Loaded Content |
|-----------------|---------------|
| Not DeepSeek TUI or tool calls fail | [Platform Adaptation](references/platform-adaptation.md) — 5 platform tool mapping + encoding adaptation + fallback |
| Model not in 8 known list | [Model Adaptation](references/model-adaptation.md) — 8 model lookup + 4-question self-classification |
| First session triggering skill | [Capability Probing](references/model-adaptation.md) — lazy probe validation for parameters |

### L3 On-Demand Reference (Expands when explicitly requested)

| Trigger Condition | Loaded Section (all in [Advanced Features](references/advanced-features.md)) |
|-----------------|-------------------|
| Need to verify implementation after interface done | Behavior-Code line-by-line comparison |
| Module marked [done] | Auto-Checkpoint write rules |
| Choosing design alternative | Design Decision Log format |
| ≥ 2 [empty] modules on same layer | Parallel filling strategy |
| Multi-person collaboration scenario | Multi-session collaboration protocol (LOCKS.md + merging) |
| User asks "when to exit skill" | Exit conditions |
| Modifying blueprint needs change type distinction | @CHANGE vs @DECISION boundaries |
| Downstream modules can't connect due to upstream changes | Rollback protocol |
| Module [done] needs tests | Test strategy + acceptance checklist |
| Need to reference practical experience | [Practical Experience](references/practical-patterns.md) — common pitfalls & best practices |


## Constraint System (7 Hard Rules, No Bypass)

| # | Constraint | One-Liner | Violation Consequence |
|---|-----------|-----------|---------------------|
| 1 | User Confirmation Gate | Blueprint unconfirmed = no Phase 2 | Architecture diverges from user expectation |
| 2 | One Slot at a Time | Only one [in progress] at once | Context splits, interfaces inconsistent |
| 3 | Dependencies First | Upper layers wait until lower [done] | Written but dependencies still empty |
| 4 | Changes Documented | Blueprint changes must have @CHANGE | Implicit changes cause interface mismatch |
| 5 | Module Boundaries | No direct access to other modules' internals | Modules tightly coupled |
| 6 | Interfaces Have Consumers | Every interface must appear in @FLOW | Defined but unused interfaces |
| 7 | Read Once | Dependency source code read only once | Context filled with implementation details |

Violation handling: Stop → Rollback → Correct → Document @CHANGE → Resume. Same constraint all passed; same constraint violated 3x in a row → pause and report to user.

## Hallucination Guard (3 Layers)

Common AI code hallucination: no errors but data is wrong.

**Layer 1 — Behavior Declarations**: Every interface expanded to four sections:

```
InterfaceName(params) → return
  pre:  Conditions that must hold before calling
  post: Conditions guaranteed to hold after returning
  error: What inputs throw what errors
  side-effect: What state is changed
```

**Layer 2 — Boundary Matrix**: Every module checked dimension by dimension:

```
Empty Input | Non-existent Reference | Boundary Value | Repetition | Type Out-of-Bounds | Dependency Failure
```

Each is either ✓ (covered) or — (not applicable); no empty ❌ allowed.

**"Not applicable" criteria**:
- Empty Input —: interface has no parameters (like `listAll()`)
- Non-existent Reference —: interface receives no ID/reference params
- Boundary Value —: param is enum with finite values (exhausted in pre)
- Repetition —: operation is idempotent (repeat calls same result, like read operations)
- Type Out-of-Bounds —: param type is bool or fixed enum, no overflow possible
- Dependency Failure —: module has no external dependencies (Layer 1 module)

**Layer 3 — Error Chain Mapping**: Cross-module error propagation explicitly listed:

```
@ERROR_CHAIN
  Source: A.getX() → null
  Propagation: B.doSomething() → checks return value, throws
  Termination: B handles internally
```

Any guard incomplete → no Phase 3.


## Context Pressure Awareness (Observable Signals Only)

Thresholds adapted per model (see [Model Adaptation](references/model-adaptation.md) table). AI can't directly read "context usage %", so uses 4 observable signals:

| Signal | Trigger Condition | Judgment |
|--------|----------------|---------|
| Old Content Reflow | Tool output repeats file content processed in last 3 turns (same section reappears) | 🟠 |
| Reasoning Steps Increased | Tool calls per fill cycle > baseline×1.5 (baseline = interface count × 1.5, min 4, max 8) | 🟡 |
| Frequent Blueprint Reads | BLUEPRINT.md read > 2x during same fill | 🔴 |
| Error Pattern Repeats | Same kind of interface mismatch occurs consecutively | 🟠 |

Decision logic: 🟢 no signals → continue; 🟡 1 yellow → release completed module code; 🟠 1 orange → release code + reduce load scope; 🔴 red → pause filling, write CHECKPOINT, report to user.


## Startup Instructions

On receiving "use plank" or trigger scenario:

```
Step 0: Decide
  ├── New project → Phase 1
  ├── Existing project → Reverse Blueprint → Phase 2
  └── Simple task (<3 files, single module) → don't trigger this skill

Step 0.3: Choose adoption granularity (progressive)
  Don't have to go full L3. Choose based on need:
  
  L1 Behavior Contract    — Good for: design interface, review code, write API docs
    Output: pre/post/error/side-effect declarations per interface
    NO BLUEPRINT.md, NO Phase 2/3
    Trigger: "use plank L1" / "use plank to design interface"
  
  L2 Constraint-Driven  — Good for: refactor existing code, fix interface mismatches
    Output: L1 + 7 constraint checks + BEHAVIOR comparison (critical interfaces)
    Optional: minimal blueprint (only @MODULE + @FLOW, no @DATA/@BUILD_ORDER)
    Trigger: "use plank to check constraints" / "are this module's interfaces okay?"
  
  L3 Full Process       — Good for: new projects, major refactors
    Output: full BLUEPRINT.md + Phase 1→2→3
    Trigger: "use plank" / "design first then code"
  
  If no granularity specified, auto-select:
    Single module/interface design → L1
    2-3 module refactor → L2
    ≥ 4 module new project → L3
  
Step 0.5: Directory structure
  One directory per module, entry file exports only blueprint-defined interfaces
  
Step 0.6: Choose mode (delay until after Phase 1 complete)
  Mode depends on interface count, which is only known after Phase 1.
  Phase 0 just marks "pending". After Phase 1→2 pre-check passes:
    ├── Total interfaces ≤ 10 → Simplified mode: skip boundary matrix, @ERROR_CHAIN only 1-2 most critical paths,
    │                             @DECISION only record non-obvious choices; Phase 3 only verify ①⑤⑥
    └── Total interfaces > 10 → Full mode: boundary matrix + full @ERROR_CHAIN + full @DECISION
```


## Phase 1: Draw Blueprint

7-step decomposition framework:

```
① Entity extraction → @DATA
② Behavior identification → @FLOW
③ Module partitioning → @MODULE
④ Dependency annotation → write clearly with import path:
   
   Dependencies:
     - from storage import loadData, saveData
     - from categories import getCategoryById
   
   (NOT just "depends on B" — must have import path so Phase 2 fills without looking back)

⑤ Build ordering → @BUILD_ORDER (rule: each module layer = max(all direct dependencies layers) + 1;
   no-dependency modules = Layer 1. Ex: A depends B depends C → C=1, B=2, A=3)
   
   Layer validation: check from Layer 1 upward, each module layer = max(dependencies layers) + 1.
   If inconsistent → recalculate. Especially note cross-multi-layer modules (like reports depends L3 and L4 → reports=5, not 4)

⑥ Coverage check → every feature has @FLOW→@MODULE path complete
⑦ User confirmation → show blueprint, wait for approval
```

Phase 1→2 pre-check (execute one by one):
  ① @MODULE: every module has name, responsibility, interfaces, dependencies, status → all ✓ to pass
  ② Build order: ordered by increasing layer, no intra-layer dependencies → verify no reverse dependencies
  ③ Dependency completeness: every @MODULE's "dependencies" points to modules existing in @MODULE list
  ④ @FLOW: every module name in @FLOW has corresponding interfaces in @MODULE
  ⑤ @DATA: every data entity referenced in @FLOW defined in @DATA
  ⑥ No circular dependencies: traversing from any module along dependencies never loops back (DFS verify)
  ⑦ No name conflicts: interface names unique across blueprint
  ⑧ Layer recursive validation: every module layer = max(dependency layers) + 1; recalculate if inconsistent

**BLUEPRINT.md Structure**:

```
@PROGRESS (progress bar)
@MODULE (module map: responsibility, interfaces, dependencies, status [empty|done])
@FLOW (data flows: steps and involved modules)
@DATA (data structures: field names and types)
@BUILD_ORDER (build sequence)
@CROSSCUT (cross-cutting: error handling, logging, config, platform adaptation, output encoding, etc.)
@EXTERNAL (external dependencies: DB, 3rd-party API, MQ, filesystem, etc. interface contracts)
@ERROR_CHAIN (error chain mapping)
@CHANGE (change log)
```

@EXTERNAL format example:
```
@EXTERNAL PostgreSQL
  Type: Relational database
  Connection: DATABASE_URL env var
  Contract:
    - All persistence through this DB, no ORM (direct SQL)
    - Table structure 1:1 with @DATA
    - Connection pool: min=2, max=10
  Failure mode: Connection fail → retry 3x → throw DatabaseError

@EXTERNAL Stripe API
  Type: 3rd-party payment
  Auth: STRIPE_SECRET_KEY
  Contract:
    - createPayment(amount, currency) → PaymentIntent
    - Only payments module may call
  Failure mode: API timeout → retry 1x → return pending status
```

@EXTERNAL rules:
  - One entry per external dependency
  - Must declare "which modules may use" (default all modules → unsafe)
  - Failure mode mandatory (external dependencies = most unpredictable failure points)


## Phase 2: Fill Slot by Slot

For each [empty] module:

```
1. Locate → confirm all dependencies [done]
2. Load → current module interfaces + dependency signatures + @CROSSCUT
   (NO reading dependency source code. NO reading unrelated @FLOW)
3. Implement → write to blueprint signature, implement pre/post/error/side-effect.
   Blueprint is single source of truth for behavior, code shouldn't repeat blueprint content.
   @see reference style (choose per project norms):
     - Loose norms: write `@see BLUEPRINT.md @MODULE <name>` at module entry top
     - Strict norms: NO blueprint references in code, implicit association via interface signatures
   (Avoid desync, pick one style and keep consistent)

3.5 Verification strategy (adapt to interface count):
   ≤ 15 interfaces → full comparison (every interface line-by-line 4-section check)
   16-50 interfaces → hybrid comparison (cross-module interfaces full, module-internal interfaces sample 2/module)
   > 50 interfaces → risk-oriented (only compare entry / multi-dependent / external interfaces; trust rest)

4. Progress update → lightweight tracking strategy:
   a. On module done, only write to CHECKPOINT.md (NO update BLUEPRINT.md)
   b. When same layer ALL [done], batch update BLUEPRINT.md @PROGRESS and @MODULE status
   c. This way N modules = only ⌈N/layer_width⌉ blueprint edits, not N

5. Confirm → check updated blueprint doesn't break dependencies
6. Release → use "context pressure awareness" signals, 🟠 or 🔴 release completed code (keep only signatures)
```

6 Fill Exceptions (granularized to interface-level vs dependency-level):

| Exception | Type | Handling |
|-----------|------|---------|
| Module too big, needs split | Structural | Split two, reorder, record @CHANGE |
| Missing own interface discovered | Interface-level | Add interface; this module reset to [in progress]; ALL direct downstream modules also reset [in progress] (cascade rollback) |
| Missing dependency discovered | Dependency-level | Add dependency annotation (with import path); NO module reset; check if @BUILD_ORDER needs adjustment; record @CHANGE |
| Extra interface discovered | Interface-level | Check @FLOW, confirm delete, record @CHANGE |
| Dependency doesn't exist | Structural | Remove dependency, maybe delete zero-reference module |
| Interface mismatch | Interface-level | Confirm who wrong, fix corresponding module |
| Blueprint design problem | Structural | Pause Phase 2, enter Blueprint Revision Protocol, go back Phase 1 repartition |

**Interface-level vs Dependency-level distinction**:
- Interface-level: this module's own external signature changes → affects downstream → cascade rollback needed
- Dependency-level: this module discovers new need to depend on others → no downstream impact → only add annotation
- Decision method: ask "does this change this module's externally exposed signature?" → yes=interface-level, no=dependency-level


## Phase 3: Connect & Verify

```
① Flow verification: every @FLOW's modules & interfaces exist and status [done]
② Dependency check: interface signatures match (A output shape = B input shape) + call path matches blueprint
③ Boundary check: boundary matrix all ✓ or —
④ Error chain check: every error chain source→propagation→termination complete
⑤ Empty slot check: no [empty] left
⑥ Change review: every @CHANGE confirmed integrated
  
  Simplified mode only verifies ①⑤⑥:
    ① Flow verification + ⑤ Empty slot check + ⑥ Change review
    (Skip ②③④ — no boundary matrix or full error chains in simplified)

⑦ Runtime verification (CANNOT SKIP):
  For every @FLOW, run corresponding command/call AT LEAST ONCE, verify:
    - No ImportError / ModuleNotFoundError / path errors
    - No uncaught runtime exceptions (allow expected business exceptions like ValueError)
  Tool: use run command tool to actually execute project (like python main.py)

  Verification grading (by output type):
    Structured (API return, JSON, exit code):
      → Verify field names/types match @DATA, exit code = 0
    Semi-structured (tables, lists, dashboards):
      → Verify row/column counts, key value reasonable ranges, no "Error" substring
    Unstructured (formatted text, ANSI colors, logs):
      → Verify output non-empty, no traceback, no "Traceback" keyword
  
  Pass standard: ALL @FLOW produce output, no exceptions per corresponding grade.

⑧ Generate architecture summary (human-readable):
  After verification passes, auto-extract from BLUEPRINT.md to .arch/SUMMARY.md:
    - One-line overview ("N modules / M interfaces / K data flows <project type>")
    - Module dependency graph (Mermaid or ASCII tree)
    - 3-5 most important @FLOW (sorted by module count, take most complex)
    - All @DECISION titles + one-line rationale
    - All @EXTERNAL names + failure modes
  Goal: new dev reads SUMMARY.md (~30 lines) and understands full architecture.
```


### Blueprint Revision Protocol

Triggers when Phase 2 discovers blueprint design problem (not just single missing interface):

Trigger conditions (any met):
  - Same module 3 consecutive interface dependencies don't work in implementation
  - @BUILD_ORDER ordered, module's transitive dependencies ≥ 2 layers deeper than expected
  - User feedback "modules partitioned wrong", "dependencies backwards"
  - Discovered @EXTERNAL actual access doesn't match declared "available modules"

Revision steps:
  1. Pause Phase 2, record current progress to CHECKPOINT.md (status: [restructuring])
  2. Record @RESTRUCTURE entry in BLUEPRINT.md
  3. Re-execute Phase 1 ④-⑦ (from module partitioning to user confirmation)
  4. Cascade adjust: update @MODULE, @BUILD_ORDER, @FLOW all affected entries
  5. Reset status: all affected modules → [empty], downstream dependent modules → [empty]
  6. User confirms new blueprint → resume Phase 2 from lowest [empty]


## Incremental Development / Iteration Mode

Adding features or fixing bugs to existing projects:

```
1. Read BLUEPRINT.md (reuse existing blueprint directly)
2. Mark affected modules [in progress]
3. Mark new modules [empty]
4. Update @BUILD_ORDER and @FLOW
5. Execute Phase 2 fill on modified and new modules
6. Execute Phase 3 verification (only verify affected and related @FLOW)
```

For existing projects WITHOUT blueprint, execute Reverse Blueprint:

```
Step 1: List project files → recursively list all source, exclude test/config/generated
Step 2: Identify module by module → judge module boundaries by directory structure
Step 3: Extract interface signatures → read entry files' exports, only collect signatures and type definitions
Step 4: Infer dependencies → from import/require/use statements, only collect cross-module references
Step 5: Generate @DATA → extract cross-module shared data structures from type definitions
Step 6: Generate @FLOW → trace core call chains from entry files
Step 7: Mark [done] and @UNCLEAR → mark uncertain modules @UNCLEAR
Step 8: Organize to BLUEPRINT.md → same blueprint format as new projects
```
