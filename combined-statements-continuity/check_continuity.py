"""Check that combined bank statements have no month missing and none doubled.

Reads a statements CSV (one row per statement: Account, Statement, Period
start, Period end, Opening balance, Closing balance). For each account, in date
order, every opening balance must equal the previous closing balance. When it
doesn't, the dates say which problem it is: a period that starts more than a
day after the last one ended is a missing statement; one that starts on or
before the last end date is an overlap.

It also runs the whole-period check per account: last closing less first
opening, against the sum of each statement's net change (what the Amount column
of a combined file adds up to).

Optional second file: the lines that appear in both overlapping files. Their
net should cancel the overlap difference exactly.

Usage: python3 check_continuity.py statements.csv [overlap-lines.csv]
Python 3, standard library only.
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from decimal import Decimal


def day(text: str) -> datetime:
    return datetime.strptime(text.strip(), "%m/%d/%Y")


def money(text: str) -> Decimal:
    return Decimal(text.strip())


def check(statements_path: str, overlap_path: str | None = None) -> bool:
    with open(statements_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    by_account = defaultdict(list)
    for r in rows:
        by_account[r["Account"]].append(r)

    clean = True
    overlap_gaps = {}
    for account, items in by_account.items():
        items.sort(key=lambda r: day(r["Period start"]))
        print(f"{account}: {len(items)} statements")
        for prev, cur in zip(items, items[1:]):
            gap = money(cur["Opening balance"]) - money(prev["Closing balance"])
            if gap == 0:
                continue
            clean = False
            start, prev_end = day(cur["Period start"]), day(prev["Period end"])
            if start > prev_end + timedelta(days=1):
                kind = f"missing statement(s) from {(prev_end + timedelta(days=1)):%m/%d/%Y} to {(start - timedelta(days=1)):%m/%d/%Y}"
            elif start <= prev_end:
                kind = f"overlap from {start:%m/%d/%Y} to {prev_end:%m/%d/%Y}"
                overlap_gaps[account] = gap
            else:
                kind = "dates are continuous, so look for a wrong printed balance or a line in the wrong month"
            print(f"  {cur['Statement']} opens {gap:+} against {prev['Statement']}'s closing: {kind}")

        whole = money(items[-1]["Closing balance"]) - money(items[0]["Opening balance"])
        net = sum((money(r["Closing balance"]) - money(r["Opening balance"]) for r in items), Decimal("0"))
        print(f"  Last closing less first opening: {whole}")
        print(f"  Sum of net changes in the file:  {net}")
        if whole != net:
            print(f"  Not explained by the statements in the file: {whole - net}")

    if overlap_path:
        with open(overlap_path, newline="", encoding="utf-8") as f:
            lines = list(csv.DictReader(f))
        for account, gap in overlap_gaps.items():
            doubled = sum((money(r["Amount"]) for r in lines if r["Account"] == account), Decimal("0"))
            verdict = "cancels the overlap" if doubled + gap == 0 else f"leaves {doubled + gap} unexplained"
            print(f"{account}: doubled lines net {doubled}, overlap difference {gap:+}, {verdict}")

    print("Every statement follows on from the last." if clean else "Gaps or overlaps found; see above.")
    return clean


if __name__ == "__main__":
    ok = check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    sys.exit(0 if ok else 1)
