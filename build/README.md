# Build scripts

These run against `site/index.html` and are idempotent. Apply them in this order:

1. `interview-cracker/build.py`: Interview Cracker case study and card
2. `trugen/build.py`: TruGen AI case study and card
3. `thumbs-dark/build.py`: dark-mode card thumbnails, plus light overrides for BookJoy
4. `polish-1031/build.py`: keeps the dotted side rails visible behind the sticky top bar

Usage: `python3 <script> site/index.html`. The thumbnail generators (`*/thumbs/*.py`, `thumbs-dark/make.py`, `bookjoy-thumbs/options.py`) were written against the original project-files layout and need the source screens and fonts, which aren't in this repo.
