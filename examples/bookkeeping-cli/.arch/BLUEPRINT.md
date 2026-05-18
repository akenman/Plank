# BLUEPRINT.md — bookkeeping-cli

## @PROGRESS

- [x] Phase 1: 蓝图设计
- [x] Phase 2: 代码填充
- [x] Phase 3: 验证完成
- 进度: 6/6 模块已完成

## @MODULE

### storage (L1)
- 职责: 数据持久化（JSON 文件读写）
- 接口:
  - `loadData(filepath) -> dict`
  - `saveData(filepath, data) -> None`
- 依赖: 无
- 状态: [done]

### categories (L2)
- 职责: 收支分类管理
- 接口:
  - `addCategory(name, type_) -> Category`
  - `listCategories(type_=None) -> list[Category]`
  - `getCategoryById(cat_id) -> Category | None`
- 依赖:
  - `from storage import loadData, saveData`
- 状态: [done]

### transactions (L3)
- 职责: 交易记录管理
- 接口:
  - `addTransaction(amount, category_id, date, note, type_) -> Transaction`
  - `listTransactions(filters=None) -> list[Transaction]`
  - `deleteTransaction(tx_id) -> bool`
  - `getTransactionsByCategory(cat_id) -> list[Transaction]`
- 依赖:
  - `from storage import loadData, saveData`
  - `from categories import getCategoryById`
- 状态: [done]

### budgets (L4)
- 职责: 预算设置与检查
- 接口:
  - `setBudget(category_id, month, limit_amount) -> Budget`
  - `checkBudget(category_id, month) -> BudgetStatus`
- 依赖:
  - `from storage import loadData, saveData`
  - `from categories import getCategoryById`
  - `from transactions import getTransactionsByCategory`
- 状态: [done]

### reports (L5)
- 职责: 报表生成
- 接口:
  - `monthlyReport(month) -> MonthlyReport`
  - `budgetOverview(month) -> list[BudgetOverviewItem]`
- 依赖:
  - `from transactions import listTransactions`
  - `from budgets import checkBudget`
  - `from categories import getCategoryById, listCategories`
- 状态: [done]

### cli (L6)
- 职责: 命令行界面
- 接口:
  - `main()` — 入口函数
- 依赖:
  - `from categories import addCategory, listCategories`
  - `from transactions import addTransaction, listTransactions, deleteTransaction`
  - `from budgets import setBudget, checkBudget`
  - `from reports import monthlyReport, budgetOverview`
- 状态: [done]

## @DATA

### Category
```yaml
id: int          # 唯一标识，自增
name: string     # 分类名称
type: string    # "income" | "expense"
```

### Transaction
```yaml
id: int
amount: float    # 金额
category_id: int # 关联分类 ID
date: string    # YYYY-MM-DD
note: string    # 备注
type: string    # "income" | "expense"
```

### Budget
```yaml
id: int
category_id: int
month: string   # YYYY-MM
limit_amount: float
```

### BudgetStatus
```yaml
spent: float
limit: float
remaining: float
percentage: float
```

## @FLOW

### F1: 添加分类
```
用户 → cli → addCategory() → categories → storage
```

### F2: 列出分类
```
用户 → cli → listCategories() → categories → storage
```

### F3: 添加交易
```
用户 → cli → addTransaction() → transactions → getCategoryById() → categories
                           ↓
                        storage
```

### F4: 列出交易
```
用户 → cli → listTransactions() → transactions → storage
```

### F5: 删除交易
```
用户 → cli → deleteTransaction() → transactions → storage
```

### F6: 设置预算
```
用户 → cli → setBudget() → budgets → getCategoryById() → categories
                        ↓
                     storage
```

### F7: 检查预算
```
用户 → cli → checkBudget() → budgets → getCategoryById() → categories
                          ↓
                       getTransactionsByCategory() → transactions → storage
```

### F8: 月度报表
```
用户 → cli → monthlyReport() → reports → listTransactions() → transactions → storage
                            ↓
                         getCategoryById() → categories → storage
```

### F9: 预算概览
```
用户 → cli → budgetOverview() → reports → listCategories() → categories → storage
                            ↓
                         checkBudget() → budgets → getCategoryById() → categories
                                      ↓
                                   getTransactionsByCategory() → transactions → storage
```

## @BUILD_ORDER

1. storage (L1)
2. categories (L2)
3. transactions (L3)
4. budgets (L4)
5. reports (L5)
6. cli (L6)

## @CROSSCUT

- 输出编码: UTF-8
- 编码适配: Windows PowerShell 5 使用全角货币符号 ￥
- 平台检测: `sys.platform == "win32"` 时执行 `chcp 65001`
- 数据文件: 默认 `data.json`，可通过 `BOOKKEEPING_DATA` 环境变量配置

## @ERROR_CHAIN

### EC1: 分类不存在
```
源头: transactions.addTransaction(category_id=不存在的ID)
传播: categories.getCategoryById() 返回 None
终点: ValueError("分类 ID {id} 不存在")
```

### EC2: 预算未设置
```
源头: budgets.checkBudget() 查询不存在的预算
传播: 遍历 budgets 列表未找到匹配项
终点: ValueError("分类 {id} 在 {month} 没有设置预算")
```

## @CHANGE

- @CHANGE_001: 初始蓝图设计 (2026-05-18)
- @CHANGE_002: 补充 transactions 依赖 categories (2026-05-18)
- @CHANGE_003: 补充 budgets 依赖 transactions (2026-05-18)
- @CHANGE_004: 补充 reports 依赖 budgets/categories/transactions (2026-05-18)
