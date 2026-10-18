# Bank reconciliation, step by step

A bank reconciliation adjusts the bank statement's closing balance for items
the bank hasn't processed yet (deposits in transit, outstanding checks) and
adjusts the ledger balance for items only the bank knew about (fees, interest,
errors), then confirms both adjusted balances are equal.

This folder holds one fictional month, Alder & Finch Bakery's checking account
for May 2026, with every common reconciling item. The full walk-through, with
the adjusting entries and how to find a difference, is ZeraBooks' guide,
[How to do a bank reconciliation](https://www.zerabooks.com/how-to-do-a-bank-reconciliation).

## Files

| File | What it is |
|---|---|
| `bank-reconciliation.csv` | Bank side and books side, one row per item. Both sides add up to 18,396.75. |
| `check_reconciliation.py` | Adds each side and reports the difference, with a hint when it is divisible by 9. Python 3, standard library only. |

## The month

| Bank side | Amount | Books side | Amount |
|---|---|---|---|
| Statement closing balance | 19,312.40 | Ledger balance | 18,402.55 |
| Deposit in transit | 2,150.00 | Bank fee not in books | -35.00 |
| Outstanding check 1043 | -1,240.00 | Interest not in books | 2.20 |
| Outstanding check 1045 | -1,825.65 | Check 1039 recorded as 452.00, cleared as 425.00 | 27.00 |
| **Adjusted bank balance** | **18,396.75** | **Adjusted book balance** | **18,396.75** |

Delete the last Books row and run the script: the difference is 27.00, and
27 is divisible by 9, which is the sign of a transposed amount.

Only the books-side items become journal entries. The bank-side items clear on
next month's statement.

All figures are fictional.
