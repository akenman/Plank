# 实战经验与最佳实践

> 加载条件：需要参考实战经验时，或首次使用前

## 常见陷阱

### 陷阱 1：Phase 1 依赖遗漏

**现象**：Phase 2 填充时发现需要调用另一个模块的接口，但蓝图未标注。

**根因**：Phase 1 只考虑了"主数据流"的依赖，忽略了"辅助查询"依赖。

**预防**：
```
依赖标注时对各模块问两个问题：
1. 核心逻辑依赖哪些模块？（主数据流）
2. 输出需要引用哪些模块的数据翻译 ID 为名称？（辅助查询）
```

### 陷阱 2：层号直觉误判

**现象**：直觉认为两个模块"差不多"同层，但实际不同。如 reports 依赖 transactions(3层) 和 budgets(4层)，按公式 reports=5 而非 4。

**预防**：列出每个模块的所有直接依赖及其层号，再计算 max+1。

### 陷阱 3：Windows 编码崩溃

**现象**：包含 ¥ 等半角符号的输出在 Windows PowerShell 5 上报错。

**预防**：使用 ￥（全角）替代 ¥（半角），或使用 ASCII 文本。

### 陷阱 4：接口级与依赖级异常混淆

**现象**：发现"缺少依赖"时执行了级联回退，导致已完成的下游模块被重置。

**判断方法**：问"这个变更是否改变了本模块对外暴露的接口签名？"

## 最佳实践

### 依赖标注使用 import 路径格式

```
好：依赖: - from storage import loadData, saveData
差：依赖: storage
```

import 路径让 Phase 2 填充时无需回看依赖模块源码。

### CHECKPOINT.md 轻量追踪

模块完成时只更新 CHECKPOINT.md，同层全部完成后再批量更新 BLUEPRINT.md。

### Phase 1 完成后再选择模式

预估接口数通常不准确。Phase 1 画完蓝图后才能看到确切数字，再决定简化/完整模式。

### 运行时验证渐进策略

先测最底层的 FLOW → 再测跨层 FLOW → 最后测最复杂的 FLOW。

## 创新模式

### 蓝图快照（Blueprint Snapshot）

每层完成后保存快照到 `.arch/snapshots/`：
- 上下文压力大时只加载当前层快照
- 回滚时快速恢复到某一层状态

### 接口契约测试自动生成

从 BEHAVIOR 声明的 pre/post/error 自动生成 pytest：
- 每个 pre/error → 一个异常测试
- 每个 post → 一个断言测试

### 依赖图可视化

在 SUMMARY.md 中用 ASCII 或 Mermaid 生成依赖图，一眼看出循环依赖。

```mermaid
graph TD
    storage --> categories
    categories --> transactions
    transactions --> budgets
    transactions --> reports
    transactions --> budgets
    budgets --> reports
    categories --> reports