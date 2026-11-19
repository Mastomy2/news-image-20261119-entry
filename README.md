# The World in One Day — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Mastomy2/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Mastomy2/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for the make.fun bounty [news-image-20261119](https://make.fun/bounty/news-image-20261119):
sum up the world's news of Thursday 19 November 2026 in one image.

## The image

`image.png` (1024×1024) packs the day's six defining world stories into
one poster — two columns of three cards, each with a headline, a one-line
summary, and its source:

1. **GTA VI launches worldwide** — Grand Theft Auto VI launches globally
   today, scoring 99 on Metacritic as players return to Vice City
   (AP News / The Guardian)
2. **Voyager 1 reaches one light-day** — NASA's Voyager 1 reaches one
   light-day from Earth, a milestone confirmed at a press conference today
   (NASA)
3. **EU proposes €45bn Ukraine loan** — The European Commission proposes a
   €45 billion loan to Ukraine, to be repaid once Russia pays reparations
   (Financial Times)
4. **Jeffries set to be first Black House Speaker** — Democrats nominate
   Hakeem Jeffries as Speaker of the US House; he would be the first Black
   Speaker (BBC / NDTV)
5. **ICJ rules on Myanmar genocide case** — The International Court of
   Justice delivers its ruling in The Gambia v. Myanmar over the treatment
   of the Rohingya (BBC)
6. **Israeli tanks push into central Gaza** — Israeli tanks cross the
   'yellow line' into Hamas-held central Gaza after evacuation orders, a
   rare ground operation (BBC / The Guardian)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`image.png` to `/output/entry.png`. It first checks the file is a real PNG,
then verifies the output SHA-256 and size match the source, so every run
writes byte-identical output.

```bash
python3 main.py   # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
