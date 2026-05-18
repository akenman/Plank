# 平台适配

> 加载条件：非 DeepSeek TUI 环境，或工具调用失败需要查表时

## 工具映射

本 skill 使用行为描述而非具体工具名，跨平台通用。AI 执行时根据当前环境选择对应工具：

| 行为 | DeepSeek TUI | Claude Code | Trae CN | Cursor | Codex CLI |
|------|-------------|-------------|---------|--------|-----------|
| 列出目录 | list_dir | LS / Bash ls | list_dir | list_dir | Bash ls |
| 搜索代码 | grep_files | Grep | grep_files | search | Grep |
| 读取文件 | read_file | Read | read_file | read_file | Read |
| 写入/编辑文件 | write_file / edit_file | Write / Edit | write_file / edit_file | edit_file | Write |
| 运行命令 | exec_shell | Bash | exec_shell | terminal | Bash |
| 跟踪进度 | checklist_write | TodoWrite | checklist_write | —（跳过） | —（跳过） |
| 规划步骤 | update_plan | — | update_plan | — | — |
| 启动子任务 | agent_spawn | agent_spawn | Task | —（转串行） | —（转串行） | —（转串行） |
| 压缩上下文 | /compact | /compact | —（释放模块代码） | /compact | —（释放模块代码） |

工具不可用时回退策略：
- 进度/计划工具不可用 → 用代码注释或文件记录替代
- 子任务不可用 → 串行填充，同层模块依次实现
- 压缩上下文不可用 → 每个模块 [done] 后立即释放实现代码

## 编码适配

不同操作系统的终端编码不同，直接影响 @CROSSCUT 中"输出编码"声明的可行性。

### 编码矩阵

| 平台 | 默认终端编码 | UTF-8 特殊字符 | 常见问题 |
|------|------------|----------------|---------|
| macOS / Linux | UTF-8 | ✓ 完整支持 | 无 |
| Windows (PowerShell 5) | GBK | ✗ 部分字符无法编码 | 货币符号报错 |
| Windows (PowerShell 7+) | UTF-8 | ✓ 需配置 | 需 `$OutputEncoding = [Text.Encoding]::UTF8` |
| Windows (CMD) | 代码页依赖 | △ 不稳定 | `chcp 65001` 可临时切换 |

### 编码适配策略

在 @CROSSCUT 中声明输出编码时，按以下策略处理：

```
1. 优先使用 ASCII 安全字符
   货币符号：用 "￥"（全角，U+FFE5）替代 "¥"（半角，U+00A5）
   或使用纯文本如 "CNY"、"RMB"
   
2. 若必须使用 UTF-8 特殊字符
   Python: 在入口文件添加编码适配代码
     if sys.platform == "win32":
         os.system("chcp 65001 >nul 2>&1")
   Node.js: 无需额外处理（默认 UTF-8）
   
3. 运行时验证时注意
   Windows 下首次运行可能输出乱码 → 重新运行一次
   验证标准：输出不含 traceback，允许首次运行的编码警告
```

### @CROSSCUT 编码声明模板

```
@CROSSCUT
  输出编码: UTF-8（Windows 需 chcp 65001 适配）
  编码适配: 入口文件添加平台检测，自动切换代码页
  安全字符: 优先使用 ASCII 兼容字符
```