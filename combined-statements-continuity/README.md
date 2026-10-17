# Combined statements continuity check

When several bank statements are combined into one spreadsheet, each
statement's opening balance must equal the previous statement's closing
balance. A difference means a statement is missing or two files overlap, and
the period dates tell you which. A second check needs no table: the combined
Amount column must add up to the last closing balance less the first opening
balance.

Each statement can be proven on its own and the combined file can still be
wrong, because nothing in a single statement knows about the next one. ZeraBooks'
guide to [combining bank statements into one Excel file](https://www.zerabooks.com/combine-bank-statements)
walks through the download and both checks. The wider guide is the
[bank statement converter](https://www.zerabooks.com/bank-statement-converter).

## Files

| File | What it is |
|---|---|
| `statements.csv` | One row per statement in a fictional combined file: account, statement, period dates, printed opening and closing balance. Operating 3318 has 2025 with June never added. Payroll 5120 has a March 2026 statement plus a date-range export that overlaps it. |
| `overlap-lines.csv` | The three Payroll 5120 lines that sit in both the March statement and the export. |
| `check_continuity.py` | Runs both checks on any file in this layout and names each gap as missing or overlapping. Python 3, standard library only. |

Run it from this folder:

```
python3 check_continuity.py statements.csv overlap-lines.csv
```

On the sample it exits with 1 and prints:

```
Operating 3318: 11 statements
  July 2025 opens +2263.46 against May 2025's closing: missing statement(s) from 06/01/2025 to 06/30/2025
  Last closing less first opening: 11309.54
  Sum of net changes in the file:  9046.08
  Not explained by the statements in the file: 2263.46
Payroll 5120: 2 statements
  Export 03/25 to 04/08 opens +375.40 against March 2026's closing: overlap from 03/25/2026 to 03/31/2026
  Last closing less first opening: 2198.40
  Sum of net changes in the file:  1823.00
  Not explained by the statements in the file: 375.40
Payroll 5120: doubled lines net -375.40, overlap difference +375.40, cancels the overlap
Gaps or overlaps found; see above.
```

## Reading the sample

All figures are fictional.

**The missing month.** May closes at 28,276.91 and July opens at 30,540.37.
July starts more than a day after May ended, so a statement is missing, and
the 2,263.46 difference is June's net change. The whole-year check finds the
same number: 35,620.09 less 24,310.55 is 11,309.54, the statements in the file
net to 9,046.08, and 11,309.54 less 9,046.08 is 2,263.46. Add a June row
(opening 28,276.91, closing 30,540.37) and both checks pass.

**The overlap.** The March statement closes at 12,840.00 on 03/31. The export
starts on 03/25 and opens at 13,215.40, the balance on 03/24. Its start date is
before March's end date, so this is an overlap, not a gap. The three lines in
both files net to -375.40, which is exactly the opposite of the +375.40
difference:

| Line in both files | Amount |
|---|---|
| 03/26 ACH payroll | -412.60 |
| 03/28 Customer deposit | 1,200.00 |
| 03/30 Card payment | -1,162.80 |
| Net | -375.40 |

13,215.40 - 412.60 + 1,200.00 - 1,162.80 = 12,840.00. Delete those three rows
from one of the files, or leave the export out, before using any totals.

## Do it in a spreadsheet

With the statements sorted by account and period start, Opening balance in E
and Closing balance in F, put this in G3 and fill down:

| Cell | Formula | What it shows |
|---|---|---|
| G3 | `=IF(A3=A2,ROUND(E3-F2,2),"")` | 0 when a statement follows on; the size of the gap or overlap otherwise |

A non-zero cell is either a missing statement or an overlap. Compare the
period start in C with the previous period end in D to tell which.

## FAQ

### Can the difference be negative?

Yes. The sign is the next opening less the previous closing, so it follows
whatever the missing month or the doubled lines did to the balance. A month
that lost money leaves a negative gap; an overlap of deposits leaves a negative
difference too. Read the dates, not the sign.

### Does this work with several accounts in one combined file?

Yes, as long as each row says which account it is. The checks run per account,
because each account has its own run of balances. Operating 3318 and Payroll 5120
in the same sheet only line up after you filter on the account.

### What if the dates are continuous and the balances still don't follow on?

Then nothing is missing or doubled, and the cause is inside a statement: a
printed balance read wrong, or a line that the bank dated into the next
period. The script says so instead of guessing.
