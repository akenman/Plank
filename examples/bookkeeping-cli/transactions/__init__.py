import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage import loadData, saveData
from categories import getCategoryById

_DATA_FILE = os.environ.get("BOOKKEEPING_DATA", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data.json"))
_VALID_TYPES = {"income", "expense"}
_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _load():
    return loadData(_DATA_FILE)


def _save(data):
    saveData(_DATA_FILE, data)


def addTransaction(amount, category_id, date, note, type_):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("金额必须大于 0")
    cat = getCategoryById(category_id)
    if cat is None:
        raise ValueError(f"分类 ID {category_id} 不存在")
    if not _DATE_PATTERN.match(date):
        raise ValueError("日期格式必须为 YYYY-MM-DD")
    if type_ not in _VALID_TYPES:
        raise ValueError(f"交易类型必须为 {', '.join(_VALID_TYPES)}")
    data = _load()
    transactions = data.get("transactions", [])
    next_id = max((t["id"] for t in transactions), default=0) + 1
    new_tx = {
        "id": next_id,
        "amount": float(amount),
        "category_id": category_id,
        "date": date,
        "note": note or "",
        "type": type_,
    }
    transactions.append(new_tx)
    data["transactions"] = transactions
    _save(data)
    return new_tx


def listTransactions(filters=None):
    data = _load()
    transactions = data.get("transactions", [])
    if filters is None:
        return transactions
    result = transactions
    if "category_id" in filters:
        result = [t for t in result if t["category_id"] == filters["category_id"]]
    if "type" in filters:
        result = [t for t in result if t["type"] == filters["type"]]
    if "start_date" in filters:
        result = [t for t in result if t["date"] >= filters["start_date"]]
    if "end_date" in filters:
        result = [t for t in result if t["date"] <= filters["end_date"]]
    return result


def deleteTransaction(tx_id):
    if not isinstance(tx_id, int) or tx_id <= 0:
        raise ValueError("tx_id 必须为正整数")
    data = _load()
    transactions = data.get("transactions", [])
    for i, t in enumerate(transactions):
        if t["id"] == tx_id:
            transactions.pop(i)
            data["transactions"] = transactions
            _save(data)
            return True
    return False


def getTransactionsByCategory(cat_id):
    if not isinstance(cat_id, int) or cat_id <= 0:
        raise ValueError("cat_id 必须为正整数")
    data = _load()
    transactions = data.get("transactions", [])
    return [t for t in transactions if t["category_id"] == cat_id]