#!/usr/bin/env python3
from pathlib import Path

def sub(path, pairs):
    p = Path(path)
    if not p.exists():
        print('MISSING', path)
        return 0
    t = p.read_text(encoding='utf-8')
    n = 0
    for old, new in pairs:
        c = t.count(old)
        if c == 0:
            print('MISS', path, old[:80])
        else:
            t = t.replace(old, new)
            n += c
            print('OK', path, c)
    if n:
        p.write_text(t, encoding='utf-8')
    return n

n = 0
n += sub('eighth-day-reality.html', [
    ('<a href="/Bible/new-creation-last-adam.html">Last Adam</a> |\n  <a href="#top">Top</a>',
     '<a href="/Bible/new-creation-last-adam.html">Last Adam</a> |\n  <a href="/Bible/the-parousia.html">Parousia</a> |\n  <a href="#top">Top</a>'),
    ('<p><a href="new-creation-last-adam.html">New Creation in the Last Adam</a> — a covenantal fulfillment reading of redemptive history from first Adam to Last Adam.</p>',
     '<p><a href="new-creation-last-adam.html">New Creation in the Last Adam</a> — a covenantal fulfillment reading of redemptive history from first Adam to Last Adam.</p>\n  <p><a href="the-parousia.html">The Parousia</a> — the day the old age closed and the new creation opened.</p>'),
])
n += sub('new-creation-last-adam.html', [
    ('<a href="/Bible/eighth-day-reality.html">Eighth Day</a> |\n  <a href="#top">Top</a>',
     '<a href="/Bible/eighth-day-reality.html">Eighth Day</a> |\n  <a href="/Bible/the-parousia.html">Parousia</a> |\n  <a href="#top">Top</a>'),
    ('<p><a href="eighth-day-reality.html">The Eighth Day Reality: From Slavery to Sonship</a> — the companion map from the seven-day loop of performance into the Eighth Day of inheritance.</p>',
     '<p><a href="eighth-day-reality.html">The Eighth Day Reality: From Slavery to Sonship</a> — the companion map from the seven-day loop of performance into the Eighth Day of inheritance.</p>\n  <p><a href="the-parousia.html">The Parousia</a> — the day the old age closed and the new creation opened.</p>'),
])
n += sub('index.html', [
    ('<a href="/Bible/new-creation-last-adam.html">Last Adam</a>\n      <a href="/Bible/about.html">About</a>',
     '<a href="/Bible/new-creation-last-adam.html">Last Adam</a>\n      <a href="/Bible/the-parousia.html">Parousia</a>\n      <a href="/Bible/about.html">About</a>'),
    ('''      <div class="card">
        <h3>New Creation in the Last Adam</h3>
        <p>A covenantal fulfillment reading of redemptive history — first Adam to Last Adam, old house closed, one new man standing.</p>
        <p style="margin-top:0.9em"><a href="/Bible/new-creation-last-adam.html">Last Adam launch page →</a></p>
      </div>
    </div>''',
     '''      <div class="card">
        <h3>New Creation in the Last Adam</h3>
        <p>A covenantal fulfillment reading of redemptive history — first Adam to Last Adam, old house closed, one new man standing.</p>
        <p style="margin-top:0.9em"><a href="/Bible/new-creation-last-adam.html">Last Adam launch page →</a></p>
      </div>
      <div class="card">
        <h3>The Parousia</h3>
        <p>The day the old age closed and the new creation opened. One light through the Gospels, the letters, and the Apocalypse.</p>
        <p style="margin-top:0.9em"><a href="/Bible/the-parousia.html">Parousia launch page →</a></p>
      </div>
    </div>'''),
])
n += sub('about.html', [
    ('<a href="/Bible/eighth-day-reality.html">Eighth Day</a>',
     '<a href="/Bible/eighth-day-reality.html">Eighth Day</a>\n      <a href="/Bible/the-parousia.html">Parousia</a>'),
])
n += sub('begin.html', [
    ('<li><a href="/Bible/eighth-day-reality.html">Eighth Day Reality</a></li>',
     '<li><a href="/Bible/eighth-day-reality.html">Eighth Day Reality</a></li>\n      <li><a href="/Bible/the-parousia.html">The Parousia</a></li>'),
])
n += sub('sitemap.xml', [
    ('<loc>https://fpbible.github.io/Bible/new-creation-last-adam.html</loc>',
     '<loc>https://fpbible.github.io/Bible/new-creation-last-adam.html</loc></url>\n  <url><loc>https://fpbible.github.io/Bible/the-parousia.html</loc>'),
])
print('TOTAL', n)
