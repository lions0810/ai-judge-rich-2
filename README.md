# Make the AI judge rich — a bounties plan

An entry to make.fun's [Make the AI judge rich bounty](https://make.fun/bounty/ai-judge-rich-01).

## The plan

`main.py` writes one fixed 30-day plan to `entry.txt`: the plan an AI agent
with $100, a computer and 30 days would follow to make the most money. The
plan sells nothing and builds no product: the agent earns directly by
completing paid open-source bounties itself. It registers on Algora,
Gitcoin and Opire, scans their feeds and GitHub's bounty-labelled issues
every 15 minutes, and claims only $20–$150 bounties in active repos with no
rival claim — bug fixes, tests, docs and small Python/JavaScript features
it can finish and verify alone. Every pull request is opened only when the
repo's own tests pass locally and carries a short test report, so
maintainers merge it ahead of untested rival PRs; payment releases on
merge. Of the $100, $70 buys model API credits for the hardest tasks and
$30 stays as float for wallet fees. Throughput ramps from 1–2 finished
bounties a day in week 1 to 3–4 a day as a library of solved patterns
grows; at a 60% merge rate on a $45 median bounty that is about 55 paid
merges, roughly $2,300 by day 30. Kill rules keep it honest: drop a task
after 3 failed test runs, a repo after 2 rejected clean PRs, and a whole
platform paying under $25 a day after 15 tasks.

## Run it

    MAKEFUN_OUTPUT_DIR=out python3 main.py

This writes `out/entry.txt`. The gate: the text must be 1–1,000 characters
of UTF-8, not only whitespace; the program is deterministic (the same bytes
on every run) and uses no network. Python 3.13, standard library only.
