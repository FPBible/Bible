#!/usr/bin/env python3
from pathlib import Path
p = Path("1Thessalonians/1thess4.html")
t = p.read_text(encoding="utf-8")
old = "The dead in Christ are not lost. The dead in Christ are not lost; the sting of condemnation is gone."
new = "The dead in Christ are not lost; the sting of condemnation is gone."
if old in t:
    p.write_text(t.replace(old, new), encoding="utf-8")
    print("OK 1thess4 dedupe")
else:
    print("MISS 1thess4 dedupe")
