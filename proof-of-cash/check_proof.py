"""Check a four-column proof of cash CSV.

Every row must read across (beginning + receipts - disbursements = ending),
and the per-bank line plus every reconciling item must land on the per-books
line in each column. Usage: python check_proof.py proof-of-cash-template.csv
"""
import csv
import sys
from decimal import Decimal

COLS = ["Beginning balance", "Receipts", "Disbursements", "Ending balance"]


def amount(cell: str) -> Decimal:
    return Decimal(cell) if cell and cell.strip() else Decimal("0")


def check(path: str) -> bool:
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["Line"] != "Source"]

    ok = True
    for r in rows:
        b, rc, d, e = (amount(r[c]) for c in COLS)
        diff = b + rc - d - e
        if diff != 0:
            ok = False
            print(f"Row does not read across: {r['Line']} (off by {diff})")

    bank = next(r for r in rows if r["Line"] == "Balance per bank")
    books = next(r for r in rows if r["Line"] == "Balance per books")
    items = [r for r in rows if r not in (bank, books)]
    for c in COLS:
        adjusted = amount(bank[c]) + sum((amount(r[c]) for r in items), Decimal("0"))
        diff = adjusted - amount(books[c])
        if diff != 0:
            ok = False
            print(f"{c}: adjusted bank {adjusted} vs books {amount(books[c])} (off by {diff})")
    print("Ties on every row and column." if ok else "Does not tie.")
    return ok


if __name__ == "__main__":
    sys.exit(0 if check(sys.argv[1]) else 1)
