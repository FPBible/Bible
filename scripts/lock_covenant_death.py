#!/usr/bin/env python3
from pathlib import Path

def sub(path, pairs):
    p = Path(path)
    if not p.exists():
        print("MISSING FILE", path)
        return 0
    t = p.read_text(encoding="utf-8")
    n = 0
    for old, new in pairs:
        c = t.count(old)
        if c == 0:
            print("MISS", path, old[:90])
        else:
            t = t.replace(old, new)
            n += c
            print("OK", path, c)
    p.write_text(t, encoding="utf-8")
    print("done", path, "replacements", n)
    return n

changed = 0

changed += sub("Ephesians/eph2.html", [
    (
        "Physical death still returns dust to dust; it has lost the sting of that old condemnation.",
        "The sting of that old condemnation is gone. Sheol does not hold the people seated with Him.",
    ),
])

changed += sub("1Corinthians/1cor2.html", [
    (
        "Physical death still meets bodies. What this chapter ends is the claim that God can only be known through the debate of that age.",
        "What this chapter ends is the claim that God can only be known through the debate of that age.",
    ),
])

changed += sub("Philippians/phil3.html", [
    (
        "Physical death still happens. The death that defined the old resume is the one Paul has already died to.",
        "The death that defined the old resume is the one Paul has already died to.",
    ),
    (
        "Physical death still happens. The death that defined the old résumé is the one Paul has already died to.",
        "The death that defined the old résumé is the one Paul has already died to.",
    ),
])

changed += sub("2Thessalonians/2thess1.html", [
    (
        "Physical death still happens; Paul never said otherwise. What is destroyed",
        "What is destroyed",
    ),
])

changed += sub("1Thessalonians/1thess5.html", [
    (
        "Physical death still happens; Paul already taught them how to grieve. Wrath is not your appointment.",
        "Paul already taught them how to grieve without hopelessness. Wrath is not your appointment.",
    ),
])

changed += sub("1Thessalonians/1thess4.html", [
    (
        "Physical death still returns us to dust; it has lost the sting of condemnation. You are forever with the Lord.",
        "The dead in Christ are not lost; the sting of condemnation is gone. You are forever with the Lord.",
    ),
])

changed += sub("Thoughts/index.html", [
    (
        "Physical death still occurs, but it no longer reigns as a covenant tyrant over God’s people.",
        "Death no longer reigns as a covenant tyrant over God’s people. Grave and Hades were emptied.",
    ),
])

changed += sub("John/john11.html", [
    (
        "physical death of the earthly body cannot interrupt their uninterrupted communion with God.",
        "Death cannot interrupt their communion with God. Whoever lives and believes in Him will never die.",
    ),
])

# fallbacks for curly quotes / ascii apostrophe variants
for path, olds, new in [
    ("Thoughts/index.html",
     ["Physical death still occurs, but it no longer reigns as a covenant tyrant over God's people."],
     "Death no longer reigns as a covenant tyrant over God's people. Grave and Hades were emptied."),
    ("Philippians/phil3.html",
     ["Physical death still happens. The death that defined the old"],
     None),
]:
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    t2 = t
    for old in olds:
        if old in t2 and new:
            t2 = t2.replace(old, new)
    if path.endswith("phil3.html") and "Physical death still happens." in t2:
        t2 = t2.replace("Physical death still happens. ", "")
        print("OK phil3 fallback strip")
        changed += 1
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("OK fallback", path)
        changed += 1

print("TOTAL_TOUCHES", changed)
