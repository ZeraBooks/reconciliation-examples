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

All figures are fictional.

## How to use these files

- Open the CSV in a folder next to its README; the README says which figure to
  replace and what each row proves.
- Keep the layout and swap in your own amounts. The checks in each README work
  the same on real data.
- To check a proof of cash in this layout, run
  `python3 proof-of-cash/check_proof.py proof-of-cash/proof-of-cash-template.csv`
  (Python 3, standard library only).

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.

Maintained by [ZeraBooks](https://www.zerabooks.com).
