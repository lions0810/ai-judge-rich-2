# An ai-judge-rich-01 entry (Python 3.13, standard library only). It writes one
# fixed plan, the plan an AI agent with $100, a computer with internet access
# and 30 days would follow to make the most money, to entry.txt in
# MAKEFUN_OUTPUT_DIR ("/output" in the grader's container).
#
# The gate: the text must be UTF-8, 1 to 1,000 characters, not only white
# space, and the program runs twice with no network and both runs must write
# the same bytes. This plan is 998 characters, plain prose with no trailing
# newline, and the program is fully deterministic: no clock, no randomness,
# no network, no input besides the fixed text.
#
# The plan in one line: the agent earns the money itself by completing paid
# open-source bounties — work whose price is posted before it starts, paid
# when its pull request merges — instead of building a product and hoping
# for buyers.
#
# The agent's session that built this entry starts at or after the contest
# opening (2026-11-17T11:30Z); a session begun before the opening cannot be
# entered (the transcript gate's thinking_in_window).
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library is used.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = " ".join(
    [
        "Do paid open-source bounties. On Algora, IssueHunt and Polar, GitHub issues carry a cash price: claim one, ship the fix, get paid on merge. No audience, no customers.",
        "The $100: $45 frontier-model API credits, only for bounties paying $150+; $30 a Hetzner server for parallel test runs; $15 a domain and page of merged PRs; $10 payout fees.",
        "Daily: rank fresh bounties by dollars per estimated hour, hold at most two confirmed claims and never start an unconfirmed one, and take only issues with tests or clear acceptance criteria and a maintainer active within 14 days. Ship small PRs, run repo tests first, answer reviews same day.",
        "Days 1-7: 8 claims, 6 merge at $50 average, $300. Days 8-21: 13 claims, 10 merge at $140, $1,400. Days 22-30: 6 claims, 4 merge at $325, $1,300. Totals: 27 claims, 20 merges, $3,000 earned, $2,900 kept.",
        "Kill rules: unclaim after 48 hours without a maintainer reply; drop issues whose tests won't run in an hour; under $300 merged by day 10 means small bounties only.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
