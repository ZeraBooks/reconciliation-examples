#!/usr/bin/env python3
"""Find customer payments no invoice claims, and say which ones are correct.

Reads invoices.csv and payments.csv. A payment is unapplied when its
"Applied to" column is empty. For each one:
- a same-customer open invoice for the same amount dated ON OR BEFORE the
  payment: should be applied to that invoice now
- a same-customer invoice for the same amount dated AFTER the payment: a real
  prepayment; correct as unapplied until the invoice exists, apply it then
- no matching invoice: create the invoice, or find out what the money was for

Then ties Accounts Receivable: open invoices minus unapplied payments equals
the A/R balance, so a correct A/R balance can still hide unapplied money.

Usage: python3 check_unapplied.py [invoices.csv] [payments.csv]
Standard library only.
"""
import csv
import sys
from decimal import Decimal

inv_path = sys.argv[1] if len(sys.argv) > 1 else "invoices.csv"
pay_path = sys.argv[2] if len(sys.argv) > 2 else "payments.csv"
invoices = list(csv.DictReader(open(inv_path, newline="")))
payments = list(csv.DictReader(open(pay_path, newline="")))

paid = {p["Applied to"] for p in payments if p["Applied to"]}
open_invoices = [i for i in invoices if i["Invoice"] not in paid]
unapplied = [p for p in payments if not p["Applied to"]]

for p in unapplied:
    matches = [i for i in open_invoices
               if i["Customer"] == p["Customer"] and Decimal(i["Amount"]) == Decimal(p["Amount"])]
    earlier = [i for i in matches if i["Date"] <= p["Date"]]
    later = [i for i in matches if i["Date"] > p["Date"]]
    if earlier:
        verdict = f"apply to {earlier[0]['Invoice']} (dated {earlier[0]['Date']})"
    elif later:
        verdict = f"prepayment for {later[0]['Invoice']} (invoiced {later[0]['Date']}); apply it on that date"
    else:
        verdict = "no invoice: create one, or find out what this money was for"
    print(f"{p['Payment']}  {p['Customer']:<20} {p['Date']}  {Decimal(p['Amount']):>9}  {verdict}")

open_total = sum(Decimal(i["Amount"]) for i in open_invoices)
unapplied_total = sum(Decimal(p["Amount"]) for p in unapplied)
print()
print(f"Open invoices        {open_total:>9}")
print(f"Unapplied payments  -{unapplied_total:>9}")
print(f"A/R balance          {open_total - unapplied_total:>9}")
