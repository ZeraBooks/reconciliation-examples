# Provider switch tie-out

To switch bookkeeping providers, pick a cutover date at a month end the old
provider fully closed, enter the old books' balance for every balance sheet
account on that date as the new opening balances, and prove each bank, card
and loan balance against the printed statement for that date.

A difference is only acceptable when a specific item, such as a check written
but not yet cashed, explains it. ZeraBooks' page on switching from Bench, a
[Bench alternative](https://www.zerabooks.com/alternatives/bench), lists the
reports to download from the old provider before you leave.

## Files

| File | What it is |
|---|---|
| `tie-out.csv` | A fictional business switching providers at December 31, 2025. One row per balance sheet account, with the old books' balance, the new opening balance, the difference and how it was proven. Liabilities and equity are negative, so the column sums to zero like a trial balance. |

## Picking the cutover date

- Use the last month the old provider closed and reconciled, not the last
  month they touched. A month with uncategorized lines is not closed.
- A year end is easiest, because your accountant already signed off on it and
  the tax return was built from it.
- If you leave mid-year, the cutover is still a month end. Months after it are
  entered fresh in the new books from the statements.

## Tying old to new

1. Download the old provider's balance sheet (or trial balance) as of the
   cutover date.
2. Fill in the Old books balance column from it.
3. Enter the same figures as opening balances in the new books and fill in the
   New opening balance column. Difference should be 0.00 on every row.
4. For each bank, card and loan row, compare the figure with the statement
   printed for the cutover date and write what you found in Explanation.

## Reading the sample

All figures are fictional.

Business checking is 31,406.12 in the books but 32,186.12 on the statement. The
780.00 gap is check 2291, written December 30 and cashed January 5. That is
expected: the check is entered as uncleared in the new books and the opening
balance stays at 31,406.12. When it clears in January, the January statement
ties.

Every other row agrees with its source document. The last row, owner equity
and retained earnings, is the balancing figure; it agrees with the old balance
sheet, so the opening trial balance sums to zero.

A difference with no uncleared item behind it means the old provider's last
month needs another look before anything is built on it.

## FAQ

### Do I have to re-enter old transactions when I switch bookkeepers?

No. The new books start from the old provider's last balance sheet or trial
balance, so old transactions do not need to be entered again one by one.
Uncleared checks at the cutover are listed and carried forward.

### What should I download from my old bookkeeper before switching?

The latest balance sheet or trial balance, as of the last month they finished,
comes first because the new books start from it. Download bank statements from
each bank directly, and ask for back any receipts, loan papers and payroll
reports you sent them.

### What happened to Bench bookkeeping?

Bench stopped on December 27, 2024, and Employer.com announced it was acquiring
the company on December 30, 2024. Bench now operates under that ownership.
