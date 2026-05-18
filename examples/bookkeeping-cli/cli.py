import argparse
import os
import sys

if sys.platform == "win32":
    os.system("chcp 65001 >nul 2>&1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from categories import addCategory, listCategories
from transactions import addTransaction, listTransactions, deleteTransaction
from budgets import setBudget, checkBudget
from reports import monthlyReport, budgetOverview


def formatCurrency(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("amount 必须为数字")
    return f"￥{amount:,.2f}"


def formatTable(headers, rows):
    if not headers:
        raise ValueError("headers 不能为空")
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    lines = []
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    separator_line = "-+-".join("-" * w for w in col_widths)
    lines.append(separator_line)
    for row in rows:
        row_line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        lines.append(row_line)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(prog="bookkeeping", description="命令行记账工具")
    subparsers = parser.add_subparsers(dest="command")

    p_add_cat = subparsers.add_parser("add-cat", help="添加分类")
    p_add_cat.add_argument("name", help="分类名称")
    p_add_cat.add_argument("type", choices=["income", "expense"], help="分类类型")

    p_list_cat = subparsers.add_parser("list-cats", help="列出分类")
    p_list_cat.add_argument("--type", choices=["income", "expense"], dest="type_", help="按类型筛选")

    p_add_tx = subparsers.add_parser("add-tx", help="添加交易")
    p_add_tx.add_argument("amount", type=float, help="金额")
    p_add_tx.add_argument("category_id", type=int, help="分类 ID")
    p_add_tx.add_argument("date", help="日期 (YYYY-MM-DD)")
    p_add_tx.add_argument("--note", default="", help="备注")
    p_add_tx.add_argument("type", choices=["income", "expense"], help="交易类型")

    p_list_tx = subparsers.add_parser("list-tx", help="列出交易")
    p_list_tx.add_argument("--category-id", type=int, dest="category_id")
    p_list_tx.add_argument("--type", choices=["income", "expense"], dest="type_")
    p_list_tx.add_argument("--start-date", dest="start_date")
    p_list_tx.add_argument("--end-date", dest="end_date")

    p_del_tx = subparsers.add_parser("del-tx", help="删除交易")
    p_del_tx.add_argument("tx_id", type=int, help="交易 ID")

    p_set_budget = subparsers.add_parser("set-budget", help="设置预算")
    p_set_budget.add_argument("category_id", type=int, help="分类 ID")
    p_set_budget.add_argument("month", help="月份 (YYYY-MM)")
    p_set_budget.add_argument("limit_amount", type=float, help="预算金额")

    p_check_budget = subparsers.add_parser("check-budget", help="查看预算")
    p_check_budget.add_argument("category_id", type=int, help="分类 ID")
    p_check_budget.add_argument("month", help="月份 (YYYY-MM)")

    p_report = subparsers.add_parser("report", help="月度报表")
    p_report.add_argument("month", help="月份 (YYYY-MM)")

    p_budget_overview = subparsers.add_parser("budget-overview", help="预算概览")
    p_budget_overview.add_argument("month", help="月份 (YYYY-MM)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "add-cat":
            cat = addCategory(args.name, args.type)
            print(f"已添加分类: #{cat['id']} {cat['name']} ({cat['type']})")

        elif args.command == "list-cats":
            cats = listCategories(type_=args.type_)
            if not cats:
                print("暂无分类")
                return
            headers = ["ID", "名称", "类型"]
            rows = [[c["id"], c["name"], c["type"]] for c in cats]
            print(formatTable(headers, rows))

        elif args.command == "add-tx":
            tx = addTransaction(args.amount, args.category_id, args.date, args.note, args.type)
            print(f"已添加交易: #{tx['id']} {formatCurrency(tx['amount'])} ({tx['type']})")

        elif args.command == "list-tx":
            filters = {}
            if args.category_id:
                filters["category_id"] = args.category_id
            if args.type_:
                filters["type"] = args.type_
            if args.start_date:
                filters["start_date"] = args.start_date
            if args.end_date:
                filters["end_date"] = args.end_date
            txs = listTransactions(filters if filters else None)
            if not txs:
                print("暂无交易记录")
                return
            headers = ["ID", "金额", "分类ID", "日期", "备注", "类型"]
            rows = [[t["id"], formatCurrency(t["amount"]), t["category_id"], t["date"], t["note"], t["type"]] for t in txs]
            print(formatTable(headers, rows))

        elif args.command == "del-tx":
            ok = deleteTransaction(args.tx_id)
            if ok:
                print(f"已删除交易 #{args.tx_id}")
            else:
                print(f"交易 #{args.tx_id} 不存在")

        elif args.command == "set-budget":
            b = setBudget(args.category_id, args.month, args.limit_amount)
            print(f"已设置预算: {b['month']} 预算 {formatCurrency(b['limit_amount'])}")

        elif args.command == "check-budget":
            status = checkBudget(args.category_id, args.month)
            print(f"预算状态: 已花费 {formatCurrency(status['spent'])} / 预算 {formatCurrency(status['limit'])}")
            print(f"剩余: {formatCurrency(status['remaining'])} ({status['percentage']}%)")

        elif args.command == "report":
            r = monthlyReport(args.month)
            print(f"=== {args.month} 月度报表 ===")
            print(f"总收入: {formatCurrency(r['total_income'])}")
            print(f"总支出: {formatCurrency(r['total_expense'])}")
            print(f"净额: {formatCurrency(r['net'])}")
            if r["by_category"]:
                print("\n按分类:")
                headers = ["分类", "金额"]
                rows = [[name, formatCurrency(amt)] for name, amt in r["by_category"].items()]
                print(formatTable(headers, rows))

        elif args.command == "budget-overview":
            overview = budgetOverview(args.month)
            if not overview:
                print(f"{args.month} 暂无预算")
                return
            headers = ["分类", "已花费", "预算", "剩余", "百分比"]
            rows = [[o["category"], formatCurrency(o["spent"]), formatCurrency(o["limit"]), formatCurrency(o["remaining"]), f"{o['percentage']}%"] for o in overview]
            print(formatTable(headers, rows))

    except (ValueError, TypeError) as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"IO 错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()