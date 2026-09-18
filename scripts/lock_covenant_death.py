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

changed += sub("1Thessalonians/1thess4.html", [
    (
        "not annihilation and not the erasure of physical mortality as a created limit.",
        "not annihilation. Sleep is hope-language inside the covenant, not a still-open Sheol.",
    ),
    (
        "Physical death was not abolished; dust still returns to dust. What is being promised is that covenantal death and exclusion do not hold the people of Jesus.",
        "What is being promised is that covenantal death and exclusion do not hold the people of Jesus. Sheol does not keep them.",
    ),
    (
        "Physical graves remaining in the earth does not empty that victory.",
        "The last enemy was covenantal Death. That enemy does not empty the victory.",
    ),
    (
        "Grief is real, because physical death remains part of our mortal nature. Grief is not final, because covenantal exclusion is finished.",
        "Grief is real. Grief is not final, because covenantal exclusion is finished and Sheol does not hold them.",
    ),
])

changed += sub("Ephesians/eph2.html", [
    (
        "not a denial of biological life. The old order’s death is what Christ deals with.",
        "not a comment on breath. The old order’s death is what Christ deals with.",
    ),
    (
        "Paul is not saying Gentiles had no biological life. He is saying they lived under the old Adamic order",
        "Paul is not talking about stopped breath. He is saying they lived under the old Adamic order",
    ),
])

changed += sub("Isaiah/isa65-66.html", [
    (
        "Proof that biological death still exists <em>inside</em> the New Heavens and New Earth. It is a spiritual/covenantal renewal, not a literal abolition of physical mortality.",
        "Ordinary aging language inside the New Covenant world. The subject is covenant order, not the last enemy still on the throne.",
    ),
    (
        "3) Biological Life Inside the New Creation (65:20)",
        "3) Aging Language Inside the New Creation (65:20)",
    ),
    (
        "Because Isaiah is not describing the end of physical reality. He is describing a <em>new order of life</em>. It is a poetic vision of massive blessing, longevity, and stability. The curse of covenantal exile is broken. Believers live their natural, biological lives under the immense blessing and peace of the New Covenant, but physical death and the ongoing reality of sin still exist in the world.",
        "Because Isaiah is not describing a later rebuilt planet. He is describing a <em>new order of life</em>: massive blessing, longevity, and stability. The curse of covenantal exile is broken. Aging and sinner-language in 65:20 belong to that world as ordinary covenant speech, not as proof that Death still reigns.",
    ),
])

print("TOTAL_TOUCHES", changed)
