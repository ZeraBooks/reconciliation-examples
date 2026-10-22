# Reconciliation examples

A reconciliation proves the books against an outside record, usually a bank
statement: the opening balance plus every transaction has to equal the printed
closing balance, and any difference has to be explained by a specific item,
such as a check not yet cashed. Each folder here works through one kind of
reconciliation with a small fictional data file that adds up exactly.

| Folder | What it shows | Guide |
|---|---|---|
| [`proof-of-cash/`](proof-of-cash/) | A four-column proof of cash template and a script that checks it | [Proof of cash, the four-column bank reconciliation](https://www.zerabooks.com/proof-of-cash) |
| [`scanned-statement-misreads/`](scanned-statement-misreads/) | How one misread amount on a scanned statement shows up as a gap against the printed closing balance | [Converting a scanned bank statement to Excel](https://www.zerabooks.com/scanned-bank-statement-to-excel) |
| [`divorce-disclosure-timeline/`](divorce-disclosure-timeline/) | One month of statements laid out for a financial disclosure, tied to opening and closing balances | [Organizing bank statements for a divorce](https://www.zerabooks.com/bank-statements-for-divorce) |
| [`cleanup-statement-grid/`](cleanup-statement-grid/) | A grid of accounts by month showing which statements are in, tied or off, worked oldest month first | [How a bookkeeping cleanup works](https://www.zerabooks.com/bookkeeping-cleanup) |
| [`provider-switch-tie-out/`](provider-switch-tie-out/) | Old books' balances at a cutover date tied to the new opening balances, with one uncleared check explained | [Moving your books after Bench](https://www.zerabooks.com/alternatives/bench) |
| [`bookkeeping-workload-estimate/`](bookkeeping-workload-estimate/) | Monthly bookkeeping hours estimated from statement line counts plus fixed jobs | [How much a bookkeeper costs](https://www.zerabooks.com/how-much-does-a-bookkeeper-cost) |
| [`combined-statements-continuity/`](combined-statements-continuity/) | A year of statements combined into one file, with a missing month and an overlapping export found from the balances and dates | [Combining bank statements into one Excel file](https://www.zerabooks.com/combine-bank-statements) |
| [`bank-reconciliation-steps/`](bank-reconciliation-steps/) | One month with a deposit in transit, two outstanding checks, a fee, interest and a transposed amount, both sides tying to 18,396.75 | [How to do a bank reconciliation](https://www.zerabooks.com/how-to-do-a-bank-reconciliation) |
| [`general-ledger-month/`](general-ledger-month/) | Six journal entries turned into a trial balance that balances at 19,020.00 | [What is a general ledger?](https://www.zerabooks.com/what-is-a-general-ledger) |
| [`sales-tax-tie-out/`](sales-tax-tie-out/) | Three months of sales tax payable rolled forward to the cent, with sales times rate catching a 4.50 shortfall in June | [Month-end close checklist](https://www.zerabooks.com/month-end-close-checklist) |

All figures are fictional.

## How to use these files

- Open the CSV in a folder next to its README; the README says which figure to
  replace and what each row proves.
- Keep the layout and swap in your own amounts. The checks in each README work
  the same on real data.
- To check a proof of cash in this layout, run
  `python3 proof-of-cash/check_proof.py proof-of-cash/proof-of-cash-template.csv`
  (Python 3, standard library only).
- To check a bank reconciliation, run
  `python3 bank-reconciliation-steps/check_reconciliation.py bank-reconciliation-steps/bank-reconciliation.csv`.
- To build a trial balance from journal entries, run
  `python3 general-ledger-month/check_trial_balance.py general-ledger-month/journal.csv`.
- To roll forward sales tax payable and compare it with sales times rate, run
  `python3 sales-tax-tie-out/check_sales_tax.py sales-tax-tie-out/sales-tax.csv`.
- To check combined statements for a missing month or an overlap, run
  `python3 combined-statements-continuity/check_continuity.py combined-statements-continuity/statements.csv combined-statements-continuity/overlap-lines.csv`.

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.

Maintained by [ZeraBooks](https://www.zerabooks.com).
