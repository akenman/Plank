import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from storage import loadData, saveData

_DATA_FILE = os.environ.get("BOOKKEEPING_DATA", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data.json"))
_VALID_TYPES = {"income", "expense"}


def _load():
    return loadData(_DATA_FILE)


def _save(data):
    saveData(_DATA_FILE, data)


def addCategory(name, type_):
    if not name or not name.strip():
        raise ValueError("分类名称不能为空")
    if type_ not in _VALID_TYPES:
        raise ValueError(f"分类类型必须为 {', '.join(_VALID_TYPES)}")
    data = _load()
    categories = data.get("categories", [])
    for cat in categories:
        if cat["name"] == name.strip() and cat["type"] == type_:
            raise ValueError(f"分类 '{name}' 已存在")
    next_id = max((c["id"] for c in categories), default=0) + 1
    new_cat = {"id": next_id, "name": name.strip(), "type": type_}
    categories.append(new_cat)
    data["categories"] = categories
    _save(data)
    return new_cat


def listCategories(type_=None):
    data = _load()
    categories = data.get("categories", [])
    if type_ is not None:
        if type_ not in _VALID_TYPES:
            raise ValueError(f"分类类型必须为 {', '.join(_VALID_TYPES)}")
        categories = [c for c in categories if c["type"] == type_]
    return categories


def getCategoryById(cat_id):
    if not isinstance(cat_id, int) or cat_id <= 0:
        raise ValueError("cat_id 必须为正整数")
    data = _load()
    categories = data.get("categories", [])
    for cat in categories:
        if cat["id"] == cat_id:
            return cat
    return None