# Monday Morning Punchlines

My entry for the [Monday Morning Punchlines](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc) bounty on [make.fun](https://make.fun) — one joke about Monday mornings, at most 200 characters.

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/arsalive-dot/monday-morning-punchlines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/arsalive-dot/monday-morning-punchlines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

## The joke

> I set my alarm for Monday. It went off. I negotiated. We settled on Tuesday.

## How it runs

`main.py` (Python 3, standard library only) writes the joke to `/output/entry.txt` deterministically — via a temp file plus `os.replace`, mode 644.

```sh
python3 main.py
```
