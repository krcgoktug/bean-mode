<!-- ╔══════════════════════════════════════════════════════════════╗ -->
<!-- ║                         BEAN-MODE                            ║ -->
<!-- ╚══════════════════════════════════════════════════════════════╝ -->

<a href="https://github.com/krcgoktug/bean-mode">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=160&color=gradient&customColorList=12,20,24,28&text=bean-mode&fontColor=ffffff&fontSize=58&fontAlignY=38&desc=A%20coffee%20oracle%20that%20reads%20your%20mood%20and%20the%20clock&descSize=15&descAlignY=62&animation=fadeIn" alt="banner" />
</a>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=900&color=64FFDA&center=true&vCenter=true&width=620&height=40&lines=Tell+it+how+you+feel+%26+what+time+it+is.;It+tells+you+what+to+brew.;What+temperature.+What+grind.+What+song." alt="typing" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/zero-dependencies-64FFDA?style=for-the-badge" />
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" />
</p>

---

## 🫘 What

A tiny terminal CLI. You say how you feel — `sleepy`, `wired`, `studying`,
`celebrating`, `anxious`, `homesick` — and what time it is. It picks one
of ten brewing methods from a curated table, suggests the bean, water
temperature, grind, brew time, **and a track to play while you wait.**

No dependencies. No telemetry. Just water, beans, and good judgment.

## ☕ Run it

```bash
git clone https://github.com/krcgoktug/bean-mode.git
cd bean-mode
python bean_mode.py
```

It will ask how you feel and then pour the answer onto your terminal.

## 🎛 Flags

```bash
python bean_mode.py --mood focused --hour 9        # skip the prompt
python bean_mode.py --mood sleepy --hour 6 --json  # machine-readable
python bean_mode.py --mood wired --seed 42         # reproducible suggestion
```

| flag       | description                              |
|------------|------------------------------------------|
| `--mood`   | one of `sleepy / wired / focused / tired / creative / anxious / celebrating / homesick / studying` |
| `--hour`   | hour of day `0–23` (defaults to system hour) |
| `--json`   | print machine-readable JSON              |
| `--seed`   | seed the picker for reproducible runs    |

## 🍵 Example

```
$ python bean_mode.py --mood studying --hour 22 --seed 7

        (
         )      .--.
        (      |o_o |
         )     |:_/ |
              //   \ \
             (|     | )
            /'\_   _/`\
            \___)=(___/

  🫘  bean-mode  ·  mood=studying  ·  hour=22:00

  • method      : AeroPress (inverted)
  • bean        : medium-roast Colombian Supremo
  • grind       : medium
  • water       : 85 °C  /  220 ml
  • brew time   : 2 minutes
  • soundtrack  : Bonobo — Migration
  • note        : Body without bitterness. Forgiving if your hand shakes.
```

## 🌗 The rules behind the picker

- **Late night?** No espresso. You'll regret it.
- **Sleepy?** No cold brew. Sleep won't lift itself.
- **Anxious?** No Turkish coffee, no espresso. Steady cups only.
- **Wired in the afternoon?** Definitely no more espresso.
- **Celebrating?** Affogato is always on the table.

These rules live in `bean_mode.py` and are easy to extend. PRs welcome.

## 🛠 Extend it

Open `bean_mode.py`. The recipes are a list of dataclasses near the top.
Add your favourite brew, push, send a PR. The rules under
`_filter()` decide who gets invited to the party.

## 🤝 Contributing

This is a small repo and contributions are welcome. Open an issue
describing the brew you want added, or send a PR. Soundtrack
recommendations especially appreciated.

## 📜 License

MIT. Brew responsibly.

---

<p align="center">
  <i>"Three sips and your day is decided." — Turkish coffee proverb</i>
</p>

<a href="https://github.com/krcgoktug/bean-mode">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=80&color=gradient&customColorList=12,20,24,28&section=footer&animation=fadeIn" alt="footer" />
</a>
