"""Check a sales tax payable roll-forward and compare tax collected with sales times rate.

Two tests per month:
1. Roll-forward: opening payable + collected - remitted must equal the closing
   payable per ledger, and each opening must equal the previous closing.
2. Expected tax: taxable sales times the rate, rounded to the cent, should equal
   the tax collected. A difference is not an error in the arithmetic, it is a
   list of invoices to look at, so it is reported separately.

Usage: python3 check_sales_tax.py sales-tax.csv
"""
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def check(path: str) -> bool:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    ok = True
    previous_close = None
    for r in rows:
        opening = Decimal(r["Opening payable"])
        collected = Decimal(r["Collected per ledger"])
        remitted = Decimal(r["Remitted"] or "0")
        closing = Decimal(r["Closing payable per ledger"])

        if previous_close is not None and opening != previous_close:
            ok = False
            print(f"{r['Month']}: opening {opening} does not match last month's closing {previous_close}")
        rolled = opening + collected - remitted
        if rolled != closing:
            ok = False
            print(f"{r['Month']}: roll-forward gives {rolled} but ledger shows {closing}")

        expected = (Decimal(r["Taxable sales"]) * Decimal(r["Rate"])).quantize(CENT, ROUND_HALF_UP)
        gap = collected - expected
        if gap != 0:
            print(f"{r['Month']}: collected {collected} vs sales x rate {expected} (difference {gap}); review invoices")
        previous_close = closing

    print("Roll-forward ties every month." if ok else "Roll-forward does not tie.")
    return ok


if __name__ == "__main__":
    sys.exit(0 if check(sys.argv[1]) else 1)
