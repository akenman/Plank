# Platform Adaptation

> Load condition: Non-DeepSeek TUI environment, or when tool calls fail and you need to check the table

## Tool Mapping

This skill uses behavior descriptions instead of specific tool names, cross-platform通用的。AI selects corresponding tools based on current environment:

| Behavior | DeepSeek TUI | Claude Code | Trae CN | Cursor | Codex CLI |
|------|-------------|-------------|---------|--------|-----------|
| List directory | list_dir | LS / Bash ls | list_dir | list_dir | Bash ls |
| Search code | grep_files | Grep | grep_files | search | Grep |
| Read file | read_file | Read | read_file | read_file | Read |
| Write/edit file | write_file / edit_file | Write / Edit | write_file / edit_file | edit_file | Write |
| Run command | exec_shell | Bash | exec_shell | terminal | Bash |
| Track progress | checklist_write | TodoWrite | checklist_write | —（skip） | —（skip） |
| Plan steps | update_plan | — | update_plan | — | — |
| Spawn subtask | agent_spawn | agent_spawn | Task | —（serial） | —（serial） | —（serial） |
| Compact context | /compact | /compact | —（release code） | /compact | —（release code） |

When tools unavailable, fallback strategies:
- Progress/plan tools unavailable → use code comments or file records instead
- Subtasks unavailable → serial fill, implement same-layer modules sequentially
- Context compaction unavailable → release implementation code immediately after each module [done]

## Encoding Adaptation

Different OS terminals have different encoding, directly affecting feasibility of "output encoding" declaration in @CROSSCUT.

### Encoding Matrix

| Platform | Default Terminal Encoding | UTF-8 Special Chars | Common Issues |
|------|------------|----------------|---------|
| macOS / Linux | UTF-8 | ✓ Full support | None |
| Windows (PowerShell 5) | GBK | ✗ Some chars can't encode | Currency symbol errors |
| Windows (PowerShell 7+) | UTF-8 | ✓ Needs config | Need `$OutputEncoding = [Text.Encoding]::UTF8` |
| Windows (CMD) | Code page dependent | △ Unstable | `chcp 65001` for temp switch |

### Encoding Adaptation Strategy

When declaring output encoding in @CROSSCUT, handle per this strategy:

```
1. Prefer ASCII-safe characters
   Currency: use "￥" (full-width, U+FFE5) instead of "¥" (half-width, U+00A5)
   Or use plain text like "CNY", "RMB"

2. If must use UTF-8 special chars
   Python: add encoding adaptation in entry file
     if sys.platform == "win32":
         os.system("chcp 65001 >nul 2>&1")
   Node.js: no extra handling (default UTF-8)

3. During runtime verification
   Windows may show garbled first run → run again
   Verification standard: output has no traceback, allow encoding warning on first run
```

### @CROSSCUT Encoding Declaration Template

```
@CROSSCUT
  Output encoding: UTF-8 (Windows needs chcp 65001 adaptation)
  Encoding adaptation: Entry file adds platform detection, auto-switch code page
  Safe characters: Prefer ASCII-compatible chars
```
