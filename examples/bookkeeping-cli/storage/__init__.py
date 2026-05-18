import json
import os


def loadData(filepath):
    if not filepath:
        raise ValueError("filepath 不能为空")
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except PermissionError:
        raise IOError(f"文件权限不足: {filepath}")
    except json.JSONDecodeError:
        return {}


def saveData(filepath, data):
    if not filepath:
        raise ValueError("filepath 不能为空")
    if not isinstance(data, dict):
        raise TypeError("data 必须为 dict 类型")
    dir_path = os.path.dirname(filepath)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except PermissionError:
        raise IOError(f"文件权限不足: {filepath}")