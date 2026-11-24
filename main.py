#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Prints one original autocorrect fail, a single line under 200 characters.
The intended word was "condiments"; autocorrect had other ideas.
"""

LINE = "Don't forget to grab condoms for the barbecue tonight, we're almost out of ketchup too!"

print(LINE)

# The scorer reads /output/entry.txt: one line, 1-199 chars, nothing else.
import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
