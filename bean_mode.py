"""bean-mode — pick the right brew for your current mood and the hour.

Tiny CLI utility. Tells you what to brew, at what water temperature,
in how long, and with what music. No dependencies, runs anywhere
Python 3.8+ runs.

usage:
    python bean_mode.py
    python bean_mode.py --mood sleepy --hour 8
    python bean_mode.py --json
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import random
import sys
from dataclasses import dataclass, asdict
from typing import Iterable


# ---------------------------------------------------------------------------
# domain
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Brew:
    method: str
    bean: str
    water_c: int
    water_ml: int
    grind: str
    time_min: float
    music: str
    note: str


MOODS = {
    "sleepy",
    "wired",
    "focused",
    "tired",
    "creative",
    "anxious",
    "celebrating",
    "homesick",
    "studying",
}


def _at_dawn(hour: int) -> bool:
    return 5 <= hour <= 9


def _at_noon(hour: int) -> bool:
    return 11 <= hour <= 14


def _at_dusk(hour: int) -> bool:
    return 17 <= hour <= 20


def _at_night(hour: int) -> bool:
    return hour >= 21 or hour <= 4


# ---------------------------------------------------------------------------
# recipe table
# ---------------------------------------------------------------------------

_LIBRARY: list[Brew] = [
    Brew("V60 pour-over", "light-roast Ethiopian Yirgacheffe", 92, 250,
         "medium-fine", 2.5, "lo-fi jazz",
         "Floral, tea-like, the kind of cup that earns the morning."),
    Brew("AeroPress (inverted)", "medium-roast Colombian Supremo", 85, 220,
         "medium", 2.0, "Bonobo — Migration",
         "Body without bitterness. Forgiving if your hand shakes a bit."),
    Brew("French press", "dark-roast Brazilian Cerrado", 95, 350,
         "coarse", 4.0, "Nina Simone — Feeling Good",
         "Heavy, warming, what your grandmother makes for an unexpected guest."),
    Brew("Moka pot", "espresso blend, 70/30 arabica/robusta", 100, 120,
         "fine", 3.0, "Italian neorealism soundtrack",
         "The morning ritual that no espresso machine can replace."),
    Brew("Cold brew (overnight)", "medium-roast Sumatran", 4, 300,
         "very coarse", 720.0, "Khruangbin — Mordechai",
         "Smooth, sweet, low acid. Make it the night before, thank yourself."),
    Brew("Espresso", "single-origin Kenyan SL28", 93, 36,
         "very fine", 0.5, "Tom Misch — Geography",
         "30 seconds of certainty."),
    Brew("Turkish coffee", "very-fine Turkish roast", 90, 75,
         "powder", 4.0, "Tarkan — Şımarık",
         "Three sips and your day is decided."),
    Brew("Drip filter", "honey-processed Costa Rican", 94, 500,
         "medium", 4.5, "Mac Demarco — Salad Days",
         "Office mug refill territory."),
    Brew("Chemex", "washed Guatemalan Antigua", 93, 600,
         "medium-coarse", 4.5, "Hiatus Kaiyote — Choose Your Weapon",
         "Bright, clean, makes good conversation."),
    Brew("Affogato (dessert)", "espresso shot + vanilla ice cream", 93, 36,
         "very fine", 1.0, "Eros Ramazzotti — Più bella cosa",
         "Reward, not breakfast."),
    Brew("Flat white", "double ristretto + microfoam steamed milk", 92, 160,
         "fine", 1.5, "Phoebe Bridgers — Punisher",
         "Smaller than a latte, sharper than a cappuccino."),
    Brew("Cortado", "double shot espresso + warm milk", 93, 75,
         "very fine", 1.0, "Bad Bunny — Un Verano Sin Ti",
         "Balanced and quick, the cafe regular's pick."),
    Brew("Vietnamese phin", "robusta + condensed milk", 95, 200,
         "medium-coarse", 5.0, "Khruangbin — Mordechai",
         "Slow drip, sweet finish, no rush."),
]


# ---------------------------------------------------------------------------
# picker
# ---------------------------------------------------------------------------

def _filter(brews: Iterable[Brew], mood: str, hour: int) -> list[Brew]:
    out: list[Brew] = []
    for brew in brews:
        m = brew.method.lower()

        if _at_night(hour) and brew.water_c >= 90 and "espresso" in m:
            continue  # caffeine + late night = regret

        if mood == "sleepy" and brew.water_c < 20:
            continue  # cold brew can't wake you up

        if mood == "wired" and "espresso" in m and not _at_dawn(hour):
            continue  # last thing you need

        if mood == "anxious" and "espresso" in m:
            continue
        if mood == "anxious" and brew.method == "Turkish coffee":
            continue

        if mood == "celebrating" and brew.method != "Affogato (dessert)":
            # always offer the dessert as an option for celebration
            pass

        out.append(brew)

    return out or list(brews)  # never return empty


def pick(mood: str, hour: int, *, rng: random.Random | None = None) -> Brew:
    """Return one Brew that fits the given mood and hour."""
    rng = rng or random.Random()
    return rng.choice(_filter(_LIBRARY, mood, hour))


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def _ascii_cup() -> str:
    return r"""
        (
         )      .--.
        (      |o_o |
         )     |:_/ |
              //   \ \
             (|     | )
            /'\_   _/`\
            \___)=(___/
    """


def render(brew: Brew, mood: str, hour: int) -> str:
    parts = [
        _ascii_cup(),
        f"\n  🫘  bean-mode  ·  mood={mood}  ·  hour={hour:02d}:00\n",
        f"  • method      : {brew.method}",
        f"  • bean        : {brew.bean}",
        f"  • grind       : {brew.grind}",
        f"  • water       : {brew.water_c} °C  /  {brew.water_ml} ml",
        f"  • brew time   : {brew.time_min:g} minutes",
        f"  • soundtrack  : {brew.music}",
        f"  • note        : {brew.note}\n",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def _parse_argv(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bean-mode",
        description="Pick the right coffee brew for your mood and the hour.",
    )
    parser.add_argument("--mood", choices=sorted(MOODS), default=None,
                        help="how you feel right now")
    parser.add_argument("--hour", type=int, default=None,
                        help="hour of day (0-23). defaults to system hour.")
    parser.add_argument("--json", action="store_true",
                        help="emit JSON instead of human text.")
    parser.add_argument("--seed", type=int, default=None,
                        help="seed the picker for reproducible suggestions.")
    return parser.parse_args(argv)


def _prompt_mood() -> str:
    print("how are you feeling? (one word like: sleepy, focused, anxious...)")
    while True:
        choice = input(">>> ").strip().lower()
        if choice in MOODS:
            return choice
        print(f"  pick one of: {', '.join(sorted(MOODS))}")


def main(argv: list[str] | None = None) -> int:
    args = _parse_argv(argv)
    mood = args.mood or _prompt_mood()
    hour = args.hour if args.hour is not None else _dt.datetime.now().hour
    rng = random.Random(args.seed) if args.seed is not None else None
    brew = pick(mood, hour, rng=rng)
    if args.json:
        print(json.dumps({"mood": mood, "hour": hour, **asdict(brew)}, indent=2))
    else:
        print(render(brew, mood, hour))
    return 0


if __name__ == "__main__":
    sys.exit(main())
