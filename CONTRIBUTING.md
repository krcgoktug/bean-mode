# Contributing to bean-mode

Pull requests for new brewing recipes, new mood entries, and small
rule tweaks are very welcome. The bar is low and the tone is friendly.

## What's easy to contribute

- **A new brew.** Add an entry to `_LIBRARY` in `bean_mode.py`. Be
  honest about temperature, grind size, and brew time.
- **A new mood.** Add the word to `MOODS`. If the new mood implies a
  hard exclusion (no espresso, no Turkish, no cold brew, etc.), add a
  rule under `_filter()` and a test in `tests/test_picker.py`.
- **A better soundtrack.** Open a PR with a different track for an
  existing brew. Bonus points if you can defend it in two sentences.

## Style

- Plain stdlib only. Zero third-party dependencies on the runtime path.
- Tests use `unittest`, no `pytest` needed.
- Keep `bean_mode.py` a single file. The point of this repo is that
  anyone can read it top to bottom in five minutes.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the same suite against Python 3.8, 3.10, and
3.12 on every push and PR. PRs are not merged with a red CI.

## Issues

If a brew suggestion makes no sense for your mood and hour, open an
issue with the exact CLI invocation and what you expected instead.
Reproducible reports get fixed faster than vague ones.

Thanks for stopping by.
