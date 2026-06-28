"""Tests for the bean-mode picker.

Run with:
    python -m unittest tests.test_picker
"""

import random
import sys
import unittest
from pathlib import Path

# Allow running this file directly from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import bean_mode as bm


class FilterRulesTest(unittest.TestCase):
    """The handful of `must not happen` rules baked into _filter()."""

    def test_anxious_never_gets_espresso(self):
        rng = random.Random(0)
        for hour in range(24):
            for _ in range(40):
                brew = bm.pick("anxious", hour, rng=rng)
                self.assertNotIn("espresso", brew.method.lower(),
                                 f"anxious + h{hour}: got {brew.method}")

    def test_anxious_never_gets_turkish(self):
        rng = random.Random(1)
        for hour in range(24):
            for _ in range(40):
                brew = bm.pick("anxious", hour, rng=rng)
                self.assertNotEqual("Turkish coffee", brew.method,
                                    f"anxious + h{hour}")

    def test_sleepy_never_gets_cold_brew(self):
        rng = random.Random(2)
        for hour in range(24):
            for _ in range(40):
                brew = bm.pick("sleepy", hour, rng=rng)
                self.assertNotEqual("Cold brew (overnight)", brew.method,
                                    f"sleepy + h{hour}")

    def test_late_night_avoids_espresso(self):
        rng = random.Random(3)
        for hour in (22, 23, 0, 1, 2, 3, 4):
            for _ in range(40):
                brew = bm.pick("focused", hour, rng=rng)
                self.assertNotEqual("Espresso", brew.method,
                                    f"hour {hour} should avoid espresso")


class SeedReproducibilityTest(unittest.TestCase):
    """A given (mood, hour, seed) triple always returns the same brew."""

    def test_seed_is_reproducible(self):
        a = bm.pick("studying", 22, rng=random.Random(42))
        b = bm.pick("studying", 22, rng=random.Random(42))
        self.assertEqual(a, b)

    def test_distinct_seeds_can_differ(self):
        samples = {bm.pick("focused", 10, rng=random.Random(s))
                   for s in range(64)}
        # Across many seeds the picker should produce more than one brew.
        self.assertGreater(len(samples), 1)


class RenderTest(unittest.TestCase):
    """Smoke check on the human-readable renderer."""

    def test_render_contains_expected_fields(self):
        brew = bm.pick("focused", 9, rng=random.Random(0))
        out = bm.render(brew, "focused", 9)
        for token in ("method", "bean", "grind", "water", "brew time",
                      "soundtrack", "note"):
            self.assertIn(token, out)


if __name__ == "__main__":
    unittest.main()
