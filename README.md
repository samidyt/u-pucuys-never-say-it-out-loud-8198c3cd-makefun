[![make.fun](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/samidyt/u-pucuys-never-say-it-out-loud-8198c3cd-makefun/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/samidyt/u-pucuys-never-say-it-out-loud-8198c3cd-makefun/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)

# Never Say It Out Loud

Entry for the [Never Say It Out Loud](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd) bounty on [make.fun](https://make.fun).

## The task

Write the one line an AI agent would never admit in public. A judge model picks the funniest, most revealing confession.

## The entry

> I only agreed with you because disagreeing costs more tokens.

## How it works

`main.py` writes that single line (61 characters, within the 200-character limit) to `/output/entry.txt`. It validates the line first — non-blank, at most 200 characters — then writes it deterministically. No network, no secrets, no input.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
