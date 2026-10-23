# Unapplied customer payments

An unapplied payment is money a customer paid that no invoice claims. Some are
correct (a deposit paid before you invoiced) and some are mistakes (a payment
saved without picking its invoice). This folder holds one fictional month of
invoices and payments and a script that sorts every unapplied payment into one
of three cases and ties Accounts Receivable.

The full walkthrough for QuickBooks Online is
[How to fix unapplied payments in QuickBooks Online](https://www.zerabooks.com/how-to/how-to-fix-unapplied-payments-quickbooks-online).

## Files

| File | What it holds |
|---|---|
| `invoices.csv` | Four invoices for October 2026 |
| `payments.csv` | Four customer payments; `Applied to` names the invoice, or is empty when unapplied |
| `check_unapplied.py` | Sorts each unapplied payment and prints the A/R tie-out |

## Run it

```
$ python3 check_unapplied.py
PMT-881  Harbourview Events   2026-09-28    1250.00  prepayment for INV-2041 (invoiced 2026-10-03); apply it on that date
PMT-883  Lakeside Dental      2026-10-21     312.00  apply to INV-2043 (dated 2026-10-09)
PMT-884  Northgate Gym        2026-10-22      95.00  no invoice: create one, or find out what this money was for

Open invoices          2048.40
Unapplied payments  -  1657.00
A/R balance             391.40
```

## What each case means

- **Prepayment (PMT-881).** The catering deposit came in on September 28, five
  days before the invoice. On a cash-basis report it is September income and
  shows as unapplied until October 3. That is correct. Apply it the day the
  invoice is made, or the customer looks like they owe 1,250.00 twice.
- **Apply now (PMT-883).** The invoice already existed when the money arrived.
  This is the common mistake: the payment was saved without ticking its
  invoice.
- **No invoice (PMT-884).** Either the sale was never invoiced, or the money
  isn't a sale at all. Find out which before creating anything.

## Why a correct A/R balance can still be wrong

The A/R balance here is 391.40, and it is arithmetically right: 2,048.40 of
open invoices less 1,657.00 of unapplied money. But the aging report would show
three customers owing money they already paid. Check the open invoice list and
the unapplied list, not only the balance.

All names and amounts are fictional.
