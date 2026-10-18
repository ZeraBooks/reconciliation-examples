"""Build a trial balance from a journal CSV and check it balances.

Checks that every entry's debits equal its credits, totals each account,
and prints the trial balance. Usage: python check_trial_balance.py journal.csv
"""
import csv
import sys
from collections import defaultdict
from decimal import Decimal


def amount(cell: str) -> Decimal:
    return Decimal(cell) if cell and cell.strip() else Decimal("0")


def check(path: str) -> bool:
    entries = defaultdict(Decimal)
    accounts = defaultdict(Decimal)
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            net = amount(r["Debit"]) - amount(r["Credit"])
            entries[r["Entry"]] += net
            accounts[r["Account"]] += net
    ok = True
    for entry, net in entries.items():
        if net != 0:
            ok = False
            print(f"Entry {entry} does not balance (off by {net})")
    dr = sum(v for v in accounts.values() if v > 0)
    cr = -sum(v for v in accounts.values() if v < 0)
    for name, v in accounts.items():
        print(f"{name:<24}{v:>12,.2f}" if v > 0 else f"{name:<24}{'':>12}{-v:>12,.2f}")
    print(f"{'Totals':<24}{dr:>12,.2f}{cr:>12,.2f}")
    return ok and dr == cr


if __name__ == "__main__":
    sys.exit(0 if check(sys.argv[1] if len(sys.argv) > 1 else "journal.csv") else 1)
