# One month of a general ledger

A general ledger holds every account and every transaction posted to it as
equal debits and credits. Its account balances make the trial balance, and the
trial balance makes the financial statements.

This folder follows one fictional month, Fernwood Studio's March 2026, from
journal entries to a trial balance. The explanation, with the profit and loss
that comes out of it, is ZeraBooks' guide,
[What is a general ledger?](https://www.zerabooks.com/what-is-a-general-ledger)

## Files

| File | What it is |
|---|---|
| `journal.csv` | Six entries, two lines each: Entry, Date, Description, Account, Debit, Credit. |
| `check_trial_balance.py` | Checks each entry balances, totals each account and prints the trial balance. Python 3, standard library only. |

## The trial balance it produces

| Account | Debit | Credit |
|---|---|---|
| Cash | 12,200.00 | |
| Accounts receivable | 2,500.00 | |
| Equipment | 2,400.00 | |
| Credit card payable | | 2,520.00 |
| Owner's equity | | 10,000.00 |
| Design revenue | | 6,500.00 |
| Rent expense | 1,800.00 | |
| Software expense | 120.00 | |
| **Totals** | **19,020.00** | **19,020.00** |

Net income for the month is 6,500.00 - 1,800.00 - 120.00 = 4,580.00.

All figures are fictional.
