"""Check a bank reconciliation CSV in this folder's layout.

Adds every Bank row and every Books row and reports whether the adjusted
balances agree. If they don't, says whether the difference is divisible by 9
(a likely transposition). Usage: python check_reconciliation.py bank-reconciliation.csv
"""
import csv
import sys
from decimal import Decimal


def check(path: str) -> bool:
    totals = {"Bank": Decimal("0"), "Books": Decimal("0")}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            totals[row["Side"]] += Decimal(row["Amount"])
    diff = totals["Bank"] - totals["Books"]
    print(f"Adjusted bank balance:  {totals['Bank']:,.2f}")
    print(f"Adjusted book balance:  {totals['Books']:,.2f}")
    if diff == 0:
        print("Reconciled: the two adjusted balances agree.")
        return True
    hint = " Divisible by 9: look for two digits swapped." if diff % 9 == 0 else ""
    print(f"Difference: {diff:,.2f}.{hint}")
    return False


if __name__ == "__main__":
    sys.exit(0 if check(sys.argv[1] if len(sys.argv) > 1 else "bank-reconciliation.csv") else 1)
