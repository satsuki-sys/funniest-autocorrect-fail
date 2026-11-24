#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes one funny autocorrect fail to /output/entry.txt.
"""
import os

LINE = "Babe, I left your penis pasta in the fridge, heat it up for 2 minutes"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
