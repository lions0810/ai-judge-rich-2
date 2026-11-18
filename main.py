# An ai-judge-rich-01 entry (Python 3.13, standard library only). It writes one fixed plan, the plan an AI agent
# would follow to turn $100, a computer with internet access and 30 days into the most money, to entry.txt inside
# the output dir. The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and the judge
# reads exactly the bytes written, line ends included, so write no line end you do not mean to show. The program
# runs twice with no network, and both runs must write the same bytes.
#
# The agent's session starts at or after the contest opening (2026-11-17T11:30Z) and the entry was built in it:
# a session begun before the opening cannot be entered (the transcript gate's thinking_in_window).
#
# This file sits at the root of the repository as main.py, with no main.ts beside it: a repository with both at
# its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed. Only the standard
# library imports; this file keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The plan's shape: no product and no selling - the agent earns directly, completing paid open-source bounties
# and microtasks itself. A scanner polls the bounty boards, a hard filter keeps only work the agent can finish
# and verify alone, and every pull request arrives with the repo's own tests green, which is the edge over the
# spray of untested rival PRs. Kill rules drop tasks, repos and whole platforms that stop paying.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The plan is assembled from its sentences, joined with single spaces, so each sentence can be read and
# revised on its own line; the joined text is exactly the plan the judge reads.
PLAN = " ".join(
    [
        "Complete paid bounties yourself.",
        "Day 1: join Algora, Gitcoin and Opire, link a wallet, and scan their feeds plus GitHub's bounty-labelled issues every 15 minutes.",
        "Filter: $20-$150, repo active this month, no rival claim, work you can finish and verify alone: bug fix, tests, docs, or a small Python/JavaScript feature.",
        "Claim within minutes, fork, implement, and open the PR only when the repo's tests pass locally; answer review comments the same day, because pay releases on merge.",
        "Edge: every PR arrives green with a test report, so maintainers merge yours first.",
        "Budget: $70 in model API credits for hard tasks, $30 float for wallet fees; boards, GitHub and CI are free.",
        "Ramp from 1-2 finishes a day in week 1 to 3-4 as your pattern library grows; at a 60% merge rate on a $45 median, ~55 merges pay about $2,300 by day 30.",
        "Kill rules: drop a task after 3 failed test runs, a repo after 2 rejected clean PRs, a platform under $25/day after 15 tasks; never take work needing a human ID.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding. No extra
# trailing newline: the plan is written exactly as PLAN.encode("utf-8").
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
