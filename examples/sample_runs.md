# sample runs

A handful of `bean-mode` outputs for different mood-and-hour pairs, so
you can see what the tool offers before installing it.

> Generated with `--seed 42` for reproducibility.

---

## Early morning, sleepy

```bash
$ python bean_mode.py --mood sleepy --hour 6 --seed 42
```

```
🫘  bean-mode  ·  mood=sleepy  ·  hour=06:00

  • method      : Moka pot
  • bean        : espresso blend, 70/30 arabica/robusta
  • grind       : fine
  • water       : 100 °C  /  120 ml
  • brew time   : 3 minutes
  • soundtrack  : Italian neorealism soundtrack
  • note        : The morning ritual that no espresso machine can replace.
```

## Late evening, studying

```bash
$ python bean_mode.py --mood studying --hour 22 --seed 7
```

```
🫘  bean-mode  ·  mood=studying  ·  hour=22:00

  • method      : AeroPress (inverted)
  • bean        : medium-roast Colombian Supremo
  • grind       : medium
  • water       : 85 °C  /  220 ml
  • brew time   : 2 minutes
  • soundtrack  : Bonobo — Migration
  • note        : Body without bitterness. Forgiving if your hand shakes.
```

## Friday afternoon, celebrating

```bash
$ python bean_mode.py --mood celebrating --hour 17 --seed 1
```

```
🫘  bean-mode  ·  mood=celebrating  ·  hour=17:00

  • method      : Affogato (dessert)
  • bean        : espresso shot + vanilla ice cream
  • grind       : very fine
  • water       : 93 °C  /  36 ml
  • brew time   : 1 minutes
  • soundtrack  : Eros Ramazzotti — Più bella cosa
  • note        : Reward, not breakfast.
```

## Anxious, mid-morning

```bash
$ python bean_mode.py --mood anxious --hour 10 --seed 11
```

```
🫘  bean-mode  ·  mood=anxious  ·  hour=10:00

  • method      : Chemex
  • bean        : washed Guatemalan Antigua
  • grind       : medium-coarse
  • water       : 93 °C  /  600 ml
  • brew time   : 4.5 minutes
  • soundtrack  : Hiatus Kaiyote — Choose Your Weapon
  • note        : Bright, clean, makes good conversation.
```

> The picker explicitly avoids espresso, Turkish coffee, and other
> high-jolt drinks when the mood is `anxious`. See `_filter()` in
> `bean_mode.py`.
