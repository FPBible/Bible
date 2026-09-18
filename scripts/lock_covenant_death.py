#!/usr/bin/env python3
from pathlib import Path

def sub(path, pairs):
    p = Path(path)
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

changed += sub("1Corinthians/1cor3.html", [
    (
        "Physical death still returns bodies to dust. What ends is death used as a threat-system of the old age.",
        "What ends is Death used as a threat-system of the old age — not a still-open Sheol.",
    ),
    (
        "Physical death still meets bodies. What this chapter ends is the need to build your name on a human foundation.",
        "What this chapter ends is the need to build your name on a human foundation.",
    ),
])

changed += sub("Isaiah/preface.html", [
    (
        "This is not a future, delayed utopian planet where physical death ceases to exist. Isaiah explicitly states that people will still age and die within this new creation (Isa 65:20). It is a present, spiritual reality where the condemnation of the Law has been removed, the Servant has made intercession for transgressors (Isa 53), and all flesh can worship God freely through the Spirit.",
        "This is not a later rebuilt planet. Isaiah's new heavens and new earth is the New Covenant world. Isa 65:20 uses ordinary aging inside that world because the subject is covenant order, not the last enemy. The covering and the rebuke end (Isa 25:7-8). Death as condemnation ends. The Servant has made intercession (Isa 53), and all flesh can worship God freely through the Spirit.",
    ),
])

changed += sub("Isaiah/isa25.html", [
    (
        'This is <strong>not</strong> a promise of biological immortality. Believers still undergo physical death, but physical death has lost its "sting" (separation from God).',
        "This is <strong>not</strong> a later biology programme. The covering destroyed and Death swallowed (Isa 25:7-8) is the covenantal enemy — Sheol emptied, condemnation ended — not a forecast that dust stops being dust.",
    ),
])

changed += sub("Philippians/phil1.html", [
    (
        "The chapter's centre is simple: to live is Christ, and to die is gain. Physical death remains real. It does not get the last word over a man whose life is already located in the Messiah.",
        "The chapter's centre is simple: to live is Christ, and to die is gain. Union is not interrupted. The last enemy is not breath stopping; it is the old condemnation — and that enemy does not hold him.",
    ),
    (
        "Paul does not treat physical death as abolished. He treats it as unable to unmake a life that is already Christ. Gain is communion, not escape-from-matter as the meaning of salvation. Remaining in the flesh is fruitful because the assembly still needs him before the Day. New Creation hope holds both: dust returns to dust, and the man in Christ is not at the mercy of that return. Magnified in my body — life and death are both locations of witness, not two different gospels.",
        "Paul treats departing as gain because communion is not cancelled. Remaining in the flesh is fruitful because the assembly still needs him before the Day. Life and death are both locations of witness in a man already located in Messiah — not two gospels, and not a still-reigning Sheol.",
    ),
])

# phil1 may use curly apostrophes
p = Path("Philippians/phil1.html")
t = p.read_text(encoding="utf-8")
t2 = t.replace(
    "Physical death remains real. It does not get the last word over a man whose life is already located in the Messiah.",
    "Union is not interrupted. The last enemy is not breath stopping; it is the old condemnation — and that enemy does not hold him.",
).replace(
    "Paul does not treat physical death as abolished. He treats it as unable to unmake a life that is already Christ. Gain is communion, not escape-from-matter as the meaning of salvation. Remaining in the flesh is fruitful because the assembly still needs him before the Day. New Creation hope holds both: dust returns to dust, and the man in Christ is not at the mercy of that return. Magnified in my body — life and death are both locations of witness, not two different gospels.",
    "Paul treats departing as gain because communion is not cancelled. Remaining in the flesh is fruitful because the assembly still needs him before the Day. Life and death are both locations of witness in a man already located in Messiah — not two gospels, and not a still-reigning Sheol.",
)
if t2 != t:
    p.write_text(t2, encoding="utf-8")
    print("OK phil1 fallback")
    changed += 1
else:
    print("phil1 fallback no extra change")

changed += sub("Resurrection/index.html", [
    (
        "You cannot understand the Resurrection until you understand that physical death is merely the shadow of the true enemy: the &ldquo;Ministry of Death&rdquo; (the Law) that kept man separated from God.",
        "The Death that reigned from Adam was never biology. It was exile and the Ministry of Death (the Law). Grave and Hades were emptied and cast into the lake of fire. You cannot understand resurrection until you use that dictionary.",
    ),
])

p = Path("Resurrection/index.html")
t = p.read_text(encoding="utf-8")
needle = "The Natural Body was the Law-system (flesh-driven). The Spiritual Body is the New Covenant system (Spirit-driven)."
insert = needle + """
      </p>
      <h3 style="margin-top: 30px;">Terrestrial and Celestial Bodies (1 Cor 15:40-49)</h3>
      <p>
        When Paul writes of celestial and terrestrial bodies he is not teaching astronomy. He reaches back to Genesis: kinds of glory, then two Adams
        (<a href="https://ebible.org/eng-web/1CO15.htm" target="_blank" rel="noopener">1 Cor 15:40-49</a>).
      </p>
      <ul>
        <li><strong>Terrestrial / earthy:</strong> the first man from the dust — the fading Adamic-Mosaic administration: earthly tabernacle, earthly priesthood, earthly Jerusalem, physical genealogy.</li>
        <li><strong>Celestial / heavenly:</strong> the second Man from heaven — the New Creation order. Believers bear that image now.</li>
      </ul>
      <p>
        Resurrection is covenantal migration out of the terrestrial age into the celestial reality. That is why the New Jerusalem needs no sun or moon as ruling lights. Full chapter:
        <a href="/Bible/1Corinthians/1cor15.html">1 Corinthians 15</a>."""
if needle in t and "Terrestrial and Celestial Bodies" not in t:
    t = t.replace(needle, insert, 1)
    print("OK celestial insert")
    changed += 1
elif "Terrestrial and Celestial Bodies" in t:
    print("SKIP celestial already present")
else:
    print("MISS celestial anchor")

if 'href="/Bible/1Corinthians/1cor15.html">1 Corinthians 15</a>' not in t:
    t = t.replace(
        '<a href="/Bible/Life/index.html">Life in the Spirit</a>',
        '<a href="/Bible/1Corinthians/1cor15.html">1 Corinthians 15</a> | <a href="/Bible/Prophecy/death.html">Covenant Death</a>',
        1,
    )
    print("OK resurrection nav")
    changed += 1
p.write_text(t, encoding="utf-8")

changed += sub("John/john11.html", [
    (
        "fully establishing the New Creation Kingdom where physical death no longer possesses covenantal sting or spiritual condemnation.",
        'fully establishing the New Creation Kingdom. Sheol and Hades were emptied. The Death that reigned — covenantal condemnation — was cast into the fire. "Whoever lives and believes in me will never die."',
    ),
    (
        "rendering physical death incapable of severing covenant life.",
        "rendering Death incapable of severing covenant life. Sheol does not hold those who live in Him.",
    ),
])

p = Path("John/john16.html")
if p.exists():
    t = p.read_text(encoding="utf-8")
    old = "Physical death, excommunication, and Roman oppression could not overturn the reality of Messiah's enthronement."
    new = "Killing, excommunication, and Roman oppression could not overturn the reality of Messiah's enthronement."
    if old in t:
        p.write_text(t.replace(old, new), encoding="utf-8")
        print("OK john16")
        changed += 1
    else:
        print("MISS john16 exact; scanning")
        if "Physical death, excommunication" in t:
            p.write_text(t.replace("Physical death, excommunication", "Killing, excommunication"), encoding="utf-8")
            print("OK john16 fallback")
            changed += 1

print("TOTAL_TOUCHES", changed)
