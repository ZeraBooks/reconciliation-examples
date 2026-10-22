# Sales tax tie-out

A sales tax tie-out proves two things each month: the sales tax payable balance
rolls forward correctly (opening payable plus tax collected minus tax remitted
equals closing payable), and the tax collected is close to taxable sales times
the rate. The first is arithmetic and must tie to the cent. The second is a
reasonableness test, and a gap points to invoices to review.

This is step 10 of the [month-end close checklist](https://www.zerabooks.com/month-end-close-checklist).

## Files

| File | What it is |
|---|---|
| `sales-tax.csv` | A fictional business, three months (April to June 2026), one flat 7.25% rate. Columns: taxable sales, rate, opening payable, collected, remitted, closing payable per ledger. |
| `check_sales_tax.py` | Python 3, standard library only. Checks the roll-forward and each opening against the prior closing, then compares collected with sales times rate. |

Run it: `python3 check_sales_tax.py sales-tax.csv`

## Reading the sample

All figures are fictional.

April opens with 2,610.40 payable, collects 2,987.00 and remits the 2,610.40
owed from March, so it closes at 2,987.00. May and June repeat the pattern:
each month's remittance pays the previous month's balance. The roll-forward
ties in all three months.

June is the one to look at. Taxable sales of 44,120.00 at 7.25% should produce
3,198.70, but the ledger collected 3,194.20, which is 4.50 less. The ledger
and the payable agree with each other, so the roll-forward still ties; the gap
means one or more invoices were taxed at the wrong amount or marked non-taxable
(4.50 is 62.07 of sales at 7.25%). Fix those invoices before filing, not the
payable.

## What the script does not do

It assumes one rate and one filing period per row. A business that sells in
several jurisdictions needs one row per jurisdiction per month, each with its
own rate, and the rate in the file must be the rate that applied to the sales.

## FAQ

### Why does sales tax payable need to roll forward to the cent?

The payable is a liability owed to the tax authority, and the return reports
tax collected for the period. If opening plus collected minus remitted does not
equal the balance in the ledger, a collection or payment was posted twice, to
the wrong account or not at all.

### What if tax collected differs from sales times the rate?

Look at invoices, not the payable. Common causes are items marked non-taxable
by mistake, tax rounded per line instead of per invoice, discounts applied
after tax, and sales in another jurisdiction at another rate.
