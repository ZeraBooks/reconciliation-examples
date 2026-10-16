# Cleanup statement grid

A bookkeeping cleanup goes account by account, oldest month first: a month only
counts as done when it ties to its printed statement, and the next month starts
from that proven closing balance. A statement grid (accounts down, months
across) shows at a glance which statements are in, which are proven and where
the work is stuck.

The full order of a cleanup, from gathering statements to the handover, is in
ZeraBooks' guide to
[bookkeeping cleanup](https://www.zerabooks.com/bookkeeping-cleanup).

## Files

| File | What it is |
|---|---|
| `statement-grid.csv` | A fictional business with 3 accounts and 8 months (January to August 2026), part way through a cleanup. Copy it, replace the accounts and months with yours, and update a cell each time a month moves on. |

## What goes in each cell

| Cell | Meaning |
|---|---|
| Missing | No statement yet. Ask the bank before anything else; a month without its statement can't be proven. |
| Received | The statement is in, but the month hasn't been worked or doesn't tie yet. |
| Off by 48.20 | The month was worked and the books differ from the printed closing balance by this amount. |
| Tied | Opening balance agrees with last month's closing, and the books agree with the printed closing balance. |

## Reading the sample

All figures are fictional.

- **Checking 4410** is proven through March. April is off by 48.20, which is
  the size of one line, so look for a single missing or doubled item before
  anything else. May to August wait for April.
- **Savings 7702** is proven through May. June's statement is missing, so July
  and August can't be tied even though they are in: their opening balance
  depends on June.
- **Business Visa 9015** is off by 1,200.00 in February. A round amount on a
  card often means a payment from checking recorded twice. March onward waits.

## Why oldest month first

Each month's opening balance is the previous month's closing balance. If you
tie August first, an error in April carries into every month after it, and
August only looks right because the error has been absorbed somewhere else.
Working forward, each Tied cell is a fixed point: once a row reads Tied up to a
month, nothing before it needs to be opened again.

A row should never show Tied after a cell that isn't Tied. If it does, that
later month was tied to a balance that hasn't been proven.

## FAQ

### Do I need every bank statement for a bookkeeping cleanup?

Yes, for every account and every month in the cleanup, because a month can only
be proven against its own statement. Most banks let you download past statements
as PDFs from online banking.

### What is the difference between cleanup and catch-up bookkeeping?

A cleanup corrects books that exist. Catch-up bookkeeping records months that
were never entered, and most businesses that are behind need some of each.

### Will a cleanup change numbers my accountant already filed?

It should not. A cleanup normally starts after the last period your accountant
signed off and leaves that period alone; a mistake found inside a filed year is
a question for your accountant.
