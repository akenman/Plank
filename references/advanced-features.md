# Advanced Features

> Load condition: triggers when explicitly needed, each section independent

## Behavior-Code Line-by-Line Comparison
> Triggers when need to verify after implementing interface

Each implemented module's code should compare line-by-line with blueprint BEHAVIOR declaration:

| Declaration Item | What blueprint says | What's in code |
|--------|-------------|------------|
| pre | if not filepath: raise ValueError | same precondition check |
| post | returns Category object with id | return {"id": ...} |
| error | ValueError, TypeError, IOError | corresponding exceptions |
| side-effect | _data appends one record | data["x"].append(item) |

Comparison method:
1. For each interface, find pre check in code → confirm exists ✓
2. Find return → matches post ✓
3. Find raise → covers all errors ✓
4. Find data modification → matches side-effect ✓

## Auto-Checkpoint
> Triggers after module marked [done]

Write to CHECKPOINT.md after each [done]:
```
@CHECKPOINT
  Time: Phase 2 / categories complete
  Status: 2/6 modules done
  Progress: storage [done], categories [done]
  Last change: @CHANGE_001
  Next step: transactions
```

Format: CHECKPOINT is pure Markdown, no @ prefix conflicts.

## Design Decision Log
> Triggers when choosing design alternative

When recording design decisions, add @DECISION in BLUEPRINT.md:

```
@DECISION
  Title: Choose JSON over SQLite for storage solution
  Rationale: This is a single-user CLI tool, small data volume, JSON needs no extra dependencies
  Abandoned alternative: SQLite (needs sqlite3 library)
  Impact: No complex query capability, but not needed for this project
```

Rules:
- Each @DECISION has title and rationale
- Record abandoned alternatives for important decisions
- Don't record for every choice, only "non-obvious" ones

## Parallel Fill Strategy
> Triggers when ≥ 2 same-layer modules [empty]

Modules on same layer with no dependencies can be filled in parallel:

```
Condition: Module A and B are same layer with no mutual dependencies
Method: Task (subtask) parallel implementation
Output: code for both modules + their Behavior comparisons
Risk: Interface naming style inconsistency → unified check after fill complete
```

Serial when conditions not met.

## Multi-Session Collaboration Protocol
> Triggers on multi-person collaboration scenario

Multi-session collaboration flow:

```
Global LOCKS.md maintains lock status:
  @LOCK storage     session_1
  @LOCK categories  session_2
  @LOCK transactions free

Only one session can hold a module lock at a time.
Cross-session dependencies: when accessing [done] module, read only, don't write.
Merge flow: after all sessions complete, global task merges BLUEPRINT.md.
```

## Exit Conditions
> Triggers when user asks "when to exit skill"

```
Completion conditions (any one met to exit):
1. Phase 3 verification passed, all [done]
2. User says "stop", "don't continue", "that's enough"
3. Phase 1 user unsatisfied with blueprint, project abandoned
4. Paused after 3 consecutive constraint violations

After exit, keep .arch/ directory, can resume anytime.
```

## @CHANGE vs @DECISION Boundaries
> Triggers when modifying blueprint needs change type distinction

```
@CHANGE: records "what modifications were made", for development process
@DECISION: records "why this design was chosen", for architecture understanding

Scenarios for changing blueprint → @CHANGE
Scenarios for choosing design alternative → @DECISION

When boundary is unclear:
- Does this entry affect other modules' interface signatures? → @CHANGE
- Does this entry record abandoned alternatives? → @DECISION
```

## Rollback Protocol
> Triggers when downstream modules can't connect due to upstream changes

```
Trigger condition: Phase 2 fill discovers dependency module's interface signature changed
                  causing downstream module can't connect

Steps:
1. Pause downstream module
2. Check @CHANGE for recent changes
3. If upstream interface change is reasonable → update downstream interface calls
4. If upstream interface change is unreasonable → rollback upstream changes
5. Record @CHANGE describing rollback
```

## Test Strategy
> Triggers when generating tests after module [done]

Auto-generate tests from BEHAVIOR declarations:

```python
# Corresponding to blueprint addCategory pre/post/error
def test_addCategory_pre_name_empty():
    with pytest.raises(ValueError):
        addCategory("", "income")

def test_addCategory_post_id_positive():
    cat = addCategory("test", "income")
    assert cat["id"] > 0
```

Each pre/error → one exception test
Each post → one assertion test
Each side-effect → data state verification

## Acceptance Checklist
> Triggers after Phase 3 complete

```
□ Every @MODULE status is [done]
□ Every @FLOW executed at least once and produced output
□ All error chains EC1/EC2/EC3 checked
□ No pending entries in @CHANGE
□ SUMMARY.md generated
□ User confirms "looks good"
```
