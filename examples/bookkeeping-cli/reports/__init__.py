import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from transactions import listTransactions
from budgets import checkBudget
from categories import getCategoryById, listCategories

_MONTH_PATTERN = re.compile(r"^\d{4}-\d{2}$")


def monthlyReport(month):
    if not _MONTH_PATTERN.match(month):
        raise ValueError("月份格式必须为 YYYY-MM")
    txs = listTransactions({"start_date": month + "-01", "end_date": month + "-31"})
    total_income = 0.0
    total_expense = 0.0
    by_category = {}
    for t in txs:
        cat = getCategoryById(t["category_id"])
        cat_name = cat["name"] if cat else f"未知分类({t['category_id']})"
        if t["type"] == "income":
            total_income += t["amount"]
        else:
            total_expense += t["amount"]
        if cat_name not in by_category:
            by_category[cat_name] = 0.0
        by_category[cat_name] += t["amount"]
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net": total_income - total_expense,
        "by_category": by_category,
    }


def budgetOverview(month):
    if not _MONTH_PATTERN.match(month):
        raise ValueError("月份格式必须为 YYYY-MM")
    all_cats = listCategories(type_="expense")
    result = []
    for cat in all_cats:
        try:
            status = checkBudget(cat["id"], month)
            result.append({
                "category": cat["name"],
                "spent": status["spent"],
                "limit": status["limit"],
                "remaining": status["remaining"],
                "percentage": status["percentage"],
            })
        except ValueError:
            continue
    return result