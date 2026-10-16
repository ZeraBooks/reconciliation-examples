# Proof of cash

A proof of cash, or four-column bank reconciliation, ties a bank account's
beginning balance, receipts, disbursements and ending balance for a period to
the books. A standard bank reconciliation ties only the ending balance, so it
can miss a receipt and a payment of the same size that were both left out.
The full explanation, with each reconciling item walked through, is ZeraBooks'
guide, [Proof of cash](https://www.zerabooks.com/proof-of-cash).

## Files

| File | What it is |
|---|---|
| `proof-of-cash-template.csv` | A fictional March 2026 operating account: bank row, books row and eight reconciling items. The last column is a row check that reads 0.00 on every line. Replace the amounts with your own. |
| `check_proof.py` | Checks any file in this layout: every row reads across, and bank plus items equals books in every column. Python 3, standard library only. |

## Where each item goes

| Item | Beginning | Receipts | Disbursements | Ending |
|---|---|---|---|---|
| Deposit in transit, prior period end | + | - | | |
| Deposit in transit, current period end | | + | | + |
| Outstanding checks, prior period end | - | | - | |
| Outstanding checks, current period end | | | + | - |
| Returned (NSF) check or bank fee not in books | | | - | + |
| Interest credited not in books | | - | | - |

## Reading a difference

| Columns that don't tie | Likely cause |
|---|---|
| Receipts and ending, same amount | The bank received money the books didn't record |
| Disbursements and ending, same amount | The bank paid money the books didn't record |
| Receipts and disbursements, same amount, ending agrees | Offsetting unrecorded receipt and payment |
| One row only (row check not 0.00) | That row was entered in the wrong column or with the wrong sign |

All figures are fictional.
