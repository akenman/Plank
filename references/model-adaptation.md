# Model Adaptation

> Load condition: Model not in 8 known list, or first session trigger needs capability probe

## Model Parameters Table

| Parameter | DeepSeek V4 | DeepSeek V3 | Claude 4.x | GPT-4o | GLM-4 | Qwen 3 | Mistral Large | Llama 4 |
|------|-----------|-----------|-----------|--------|-------|--------|--------------|---------|
| Context window | 1M | 128K | 200K | 128K | 128K | 128K-1M | 128K | 128K-1M |
| Release threshold | ~70% | ~50% | ~50% | ~40% | ~50% | ~50% | ~45% | ~50% |
| Phase 1 reasoning | Deep | Standard | Standard | Fast | Standard | Standard | Fast | Standard |
| Phase 2 verification | Full line-by-line | Full | Sampling | Light | Full | Full | Sampling | Full |
| Blueprint load | Full | Phase 1 full | Phase 1 full | Current module | Phase 1 full | Phase 1 full | Current module | Phase 1 full |
| Cache optimization | Append | Standard | Standard | Standard | Standard | Standard | Standard | Standard |
| Parallel fill | ≤ 3 | ≤ 2 | ≤ 2 | ≤ 2 | ≤ 2 | Serial | ≤ 2 | ≤ 2 |
| Constraint execution | Strict 7 rules | Strict 7 rules | Strictest | Strict 7 rules | Strict 7 rules | Strict 7 rules | Relaxed 6 rules | Strict 7 rules |

### DeepSeek Special Optimization

```
Phase 1 reasoning enhancement: enable thinking mode, think before drawing blueprint
"Which module partitioning minimizes dependencies?"

Phase 2 prefix cache utilization: append BLUEPRINT.md changes instead of replace
Append interface signature updates, cache hit rate can increase from ~60% to ~90%

Phase 3 deep verification: use thinking to anticipate before runtime verification
For each @FLOW, where is it most likely to fail, prioritize testing high-risk paths
```

## New Model Auto-Adaptation

Models not in the table self-classify via 4 questions:

```
1. How large is context window?
   ≥ 500K → full blueprint, release threshold 65%
   200K → Phase 1 full, Phase 2 on-demand
   128K → only current module + dependencies

2. Does it support thinking?
   Yes → deep reasoning + anticipate high-risk paths
   No → standard reasoning

3. Code generation quality?
   High → sampling comparison
   Medium → full line-by-line
   Needs verification → full + complete runtime verification

4. Does it support subtask parallelism?
   Yes → same layer ≤ 3 parallel
   No → serial
```

## Lazy Probes

The original design "run 5-second self-test immediately on skill activation" has problems:
1. BLUEPRINT.md may not exist on first trigger
2. Thinking token detection uncontrollable on most platforms
3. 5-second self-test adds unnecessary delay

Improved to lazy probes — detect only when needed:

```
Probe 1 — Context load verification (triggers after Phase 1 complete)
  Action: load BLUEPRINT.md, record token consumption
  Exception: load fails → downgrade to on-demand load strategy

Probe 2 — Blueprint modification verification (triggers on first BLUEPRINT.md modification)
  Action: normal blueprint modification
  Exception: append fails → fallback to replace mode

Probe 3 — Parallel capability verification (triggers on first same layer ≥ 2 [empty])
  Action: try parallel subtask launch
  Exception: creation fails → mark as serial

Probe 4 — Thinking mode detection (triggers during Phase 1 reasoning)
  Action: observe first reasoning output
  Exception: thinking truncated → mark as no thinking
```

Probe results recorded in CHECKPOINT.md:
```
@PROBE 2026-05-18 DeepSeek V4
  Context: full load ✅
  Cache: append mode ✅
  Parallel: support ≤ 3 ✅
  thinking: support ✅
```

## Context Pressure Quantization

| Model | Baseline calls | 🟡 Threshold | 🟠 Threshold | 🔴 Threshold |
|------|----------|--------|--------|--------|
| DeepSeek V4 | 8-12 | >18 | reflow signal | read blueprint >2x |
| DeepSeek V3 | 6-8 | >12 | reflow signal | read blueprint >2x |
| Claude 4.x | 6-8 | >12 | reflow signal | read blueprint >2x |
| GPT-4o | 4-6 | >9 | reflow signal | read blueprint >2x |

Universal formula: 🟡 = max(interface count × 1.5, baseline × 1.5)
