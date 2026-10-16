# Scanned statement misreads

A scanned bank statement has no text layer, so every amount is read from an
image. A small set of misreads causes most errors, and each leaves a difference
of a predictable size between the rows and the printed closing balance. This
folder holds a worked example and a lookup table for those differences.

The full explanation is in ZeraBooks' guide,
[Scanned bank statement to Excel](https://www.zerabooks.com/scanned-bank-statement-to-excel).

## Files

| File | What it is |
|---|---|
| `march-2026-scan.csv` | A fictional two-page March 2026 checking statement. Check 1043 was first read as 1,385.00; the scan says 1,335.00. The first read misses the printed closing balance by 50.00; the corrected read ties. |

All figures are fictional and add up exactly.

## The check

    gap = opening balance + sum(rows) - printed closing balance

A gap of 0.00 means the rows rebuild the statement. Anything else is a misread,
a skipped line or a line read twice.

## Reading the gap

| Misread | Example | Gap it leaves |
|---|---|---|
| 8 read for 3, or 3 for 8 | 1,335.00 read as 1,385.00 | 5, 50 or 500, by the digit's place |
| 7 read for 1, or 1 for 7 | 417.20 read as 477.20 | 6, 60 or 600 |
| 6 and 5 | 2,506.00 read as 2,505.00 | 1, 10 or 100 |
| 0 and 8 | 1,204.00 read as 1,284.00 | 8, 80 or 800 |
| Decimal point lost | 45.00 read as 4500 | 99 times the true amount |
| Minus sign or parentheses lost | (250.00) read as 250.00 | Twice the amount |
| A faint line skipped | A 15.00 fee at the foot of a page | Exactly that line's amount |

When two causes fit the same gap (500 can be a 3/8 swap in the hundreds place
or a lost sign on a 250.00 line), check which amounts on the statement could
produce each. Usually only one can.

## Limits

- A statement that prints no balances can't be checked this way.
- Two errors that cancel each other pass the closing-balance check. A printed
  running balance, compared line by line, catches them.
- Run the check per account on multi-account statements.

## FAQ

### Do I need OCR software before converting a scanned bank statement?

No. ZeraBooks reads the page image itself, so the scan can be uploaded as it is.
Running your own OCR first does no harm, but it does not replace the balance
check.

### How accurate is converting a scanned bank statement to Excel?

It depends on the scan, so a percentage tells you little. What counts is whether
the rows tie to the opening and closing balances printed on the statement to the
cent.

### Can I convert a photo of a bank statement?

Put the photos into one PDF first; most phones and scanners can save straight to
PDF. Pages photographed flat, in good light and without a shadow read best.
