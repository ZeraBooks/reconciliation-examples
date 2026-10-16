# Divorce disclosure timeline

A column layout for turning several accounts' bank and card statements into one
transaction timeline for family law review, with a fictional month as an
example. The full guide, including how to prove the statements are complete,
is ZeraBooks' [Bank statements for divorce](https://www.zerabooks.com/bank-statements-for-divorce).

This is a spreadsheet layout, not legal advice. The attorney decides the period
and what is produced or filed; courts generally want the statements themselves.

## Files

| File | What it is |
|---|---|
| `january-2025.csv` | Eight fictional rows across a joint checking account, a savings account in one name and a card, after review columns were added. |

## Columns

| Column | Source | Purpose |
|---|---|---|
| Date | Statement | One timeline across all accounts |
| Account | Converter, when statements are combined | Which account the line moved through |
| Account holder | Reviewer, one value per account | Joint money vs money in one name |
| Description | Statement | Payee, transfer target, check number |
| Amount | Statement, money out negative | Every filter totals itself |
| Category | Reviewer | Monthly figures for an expense declaration |
| Flag | Reviewer | The short list of lines to explain |
| Pair | Reviewer | Same ID on a transfer out and its matching transfer in |

## Before the timeline is used

1. Each statement's opening balance plus its rows equals its printed closing
   balance.
2. Each statement's opening balance equals the previous statement's closing
   balance for the same account. A break means a missing statement.
3. Every transfer out has a Pair. One without a Pair, in any disclosed account,
   points to an account or statement not yet produced.
