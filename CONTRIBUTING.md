# Contributing to Plank

感谢你考虑为 Plank 贡献！

## 我能贡献什么

- **修复文档错误**：拼写错误、链接失效、示例代码问题
- **增加平台适配**：新的 AI 编程平台
- **改进 skill 流程**：优化 Phase 1/2/3 中的任一步骤
- **实战示例**：用 Plank 构建的实际项目
- **翻译**：将文档翻译为其他语言

## 贡献流程

```
1. 选择或创建 Issue
2. Fork 并创建分支: git checkout -b feat/my-feature
3. 实现变更
4. 用实际项目验证（至少 3 模块）
5. 提交 Pull Request
```

### 提交 PR

标题格式：`<type>: <简短描述>`

类型：`feat` / `fix` / `docs` / `refactor` / `chore`

PR 描述包含：
1. 变更内容概述
2. 验证方式
3. 关联 Issue 链接

### 验证要求

所有贡献需用实际项目验证：
1. 至少 3 模块的项目
2. Phase 1→2→3 完整走通
3. Phase 3 运行时验证全部通过

## 代码风格

- Markdown：ATX 标题（##），GFM 表格
- 代码块：标注语言
- 链接：相对路径引用仓库内文件
- 中文：全角标点，英文术语保留半角

## 项目结构

```
plank/
├── SKILL.md                  # L1 核心
├── references/               # L2/L3 引用
├── examples/                 # 实战示例
└── .github/                  # GitHub 配置
```