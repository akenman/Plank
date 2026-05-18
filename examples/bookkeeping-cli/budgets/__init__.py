import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage import loadData, saveData
from categories import getCategoryById
from transactions import getTransactionsByCategory

_DATA_FILE = os.environ.get("BOOKKEEPING_DATA", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data.json"))
_MONTH_PATTERN = re.compile(r"^\d{4}-\d{2}$")


def _load():
    return loadData(_DATA_FILE)


def _save(data):
    saveData(_DATA_FILE, data)


def setBudget(category_id, month, limit_amount):
    cat = getCategoryById(category_id)
    if cat is None:
        raise ValueError(f"分类 ID {category_id} 不存在")
    if cat["type"] != "expense":
        raise ValueError("预算只能设置在支出类型分类上")
    if not _MONTH_PATTERN.match(month):
        raise ValueError("月份格式必须为 YYYY-MM")
    if not isinstance(limit_amount, (int, float)) or limit_amount <= 0:
        raise ValueError("预算金额必须大于 0")
    data = _load()
    budgets = data.get("budgets", [])
    existing = None
    for i, b in enumerate(budgets):
        if b["category_id"] == category_id and b["month"] == month:
            existing = i
            break
    if existing is not None:
        budgets[existing]["limit_amount"] = float(limit_amount)
        result = budgets[existing]
    else:
        next_id = max((b["id"] for b in budgets), default=0) + 1
        result = {
            "id": next_id,
            "category_id": category_id,
            "month": month,
            "limit_amount": float(limit_amount),
        }
        budgets.append(result)
    data["budgets"] = budgets
    _save(data)
    return result


def checkBudget(category_id, month):
    cat = getCategoryById(category_id)
    if cat is None:
        raise ValueError(f"分类 ID {category_id} 不存在")
    if not _MONTH_PATTERN.match(month):
        raise ValueError("月份格式必须为 YYYY-MM")
    data = _load()
    budgets = data.get("budgets", [])
    budget = None
    for b in budgets:
        if b["category_id"] == category_id and b["month"] == month:
            budget = b
            break
    if budget is None:
        raise ValueError(f"分类 {category_id} 在 {month} 没有设置预算")
    txs = getTransactionsByCategory(category_id)
    spent = sum(t["amount"] for t in txs if t["date"].startswith(month) and t["type"] == "expense")
    limit = budget["limit_amount"]
    remaining = limit - spent
    percentage = round((spent / limit) * 100, 1) if limit > 0 else 0
    return {
        "spent": spent,
        "limit": limit,
        "remaining": remaining,
        "percentage": percentage,
    }