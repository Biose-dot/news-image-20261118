# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Biose-dot/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Biose-dot/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**THE WORLD IN A DAY** — one poster that sums up the world news of **Wednesday, 18 November 2026**. The program copies `entry.png` (1024×1024) to the output; the poster itself is drawn from source by `build_image.py` (Python + PIL, no network, no assets).

## The day's stories on the poster

Top story, plus six more, and a ticker — every item was reported on 18 November 2026 and cross-checked in at least two independent news roundups of that day:

1. **Shenzhen summit** — Xi Jinping hosted Vladimir Putin in Shenzhen as Donald Trump arrived for the APEC gathering, setting up the three leaders' first three-way summit (Ukraine, trade, Iran on the agenda).
2. **Ukraine** — Ukrainian drones and missiles hit the Kerch (Crimean) Bridge for a second straight day; a road arch fell into the strait and cars were diverted to ferries.
3. **The Gulf** — Iran fired on US sites in Kuwait and Bahrain after US jets struck a missile site on Qeshm Island; air defences reported interceptions and no major damage.
4. **United States** — Democrat Mary Peltola defeated Republican senator Dan Sullivan in Alaska, sealing a 56–44 Democratic Senate majority, the party's largest since 2009.
5. **DR Congo** — the Ebola outbreak centred on Bunia and Beni passed 11,000 cases, with children under five dying at the highest rates.
6. **United States health** — the US lost its measles elimination status after 26 years, with more than 5,400 cases and 10 deaths recorded in 2026.
7. **Business** — Nvidia posted a record $115.8B quarter as revenue more than doubled on AI data-centre demand, guiding to roughly $130B next quarter.
8. **Ticker** — COP31 climate talks open in Antalya, Türkiye · Russia & Ukraine agree their largest prisoner swap · Voyager 1 reaches one light-day from Earth · Gold slides 2% to $3,770 an ounce.

### Sources (18 Nov 2026 news roundups)

- Open Chronicle — Global News Brief, November 18, 2026: https://openchronicle.org/2026/11/18/global-news-brief-key-developments-around-the-world-november-18-2026/
- Horizon — World news and markets for 18 November 2026: https://www.horizonapp.link/en/2026/11/18
- US Brief — World Briefing, Nov 18, 2026: https://us-brief.com/brief/world
- Morning Brief World — November 18, 2026: https://morningbriefworldenglish.substack.com/p/morning-brief-world-november-18-2026
- AI Chat World News 18/11/2026: https://human-synthesis.ghost.io/2026/11/18/ai-chat-world-news-18-11-2026/
- Underlying wires cited by those roundups: Reuters, Associated Press, AFP, BBC, Alaska Public Media.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

That writes `out/entry.png`. To redraw the poster from source first: `python3 build_image.py` (needs Python 3 + Pillow and the Noto fonts), then run the command above.

---

<sub>Entered on [make.fun](https://make.fun/?ref=z5jb9v24&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
