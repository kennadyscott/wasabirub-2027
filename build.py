# Builds the WasabiRub 2027 secondary site (5 pages) with shared nav/footer.
import os
HERE=os.path.dirname(os.path.abspath(__file__))

def nav(active):
    def a(href,label,key):
        on=' class="on"' if key==active else ''
        return f'<a{on} href="{href}">{label}</a>'
    return f'''<div class="ticker" aria-hidden="true"><div class="run">
<span>MADE FOR EVERY BODY THAT MOVES</span><span>•</span><span>PAIN RELIEF THAT KEEPS YOU MOVING</span><span>•</span><span>MOVE SERIOUSLY. LIVE PLAYFULLY.</span><span>•</span><span>BELONG IN MOTION</span><span>•</span><span>MADE FOR EVERY BODY THAT MOVES</span><span>•</span><span>PAIN RELIEF THAT KEEPS YOU MOVING</span><span>•</span><span>MOVE SERIOUSLY. LIVE PLAYFULLY.</span><span>•</span>
</div></div>
<nav class="bar"><div class="wrap bar-in">
  <a class="wm" href="index.html">wasabi<span class="wr">rub<sup>&reg;</sup></span></a>
  <div class="links">{a("shop.html","The rubs","shop")}{a("index.html#idea","The idea","idea")}{a("index.html#cred","Why trust it","cred")}{a("index.html#belong","The movement","move")}</div>
  <span class="spacer"></span>
  <a class="pill-btn" href="shop.html">Shop &rarr;</a>
</div></nav>'''

FOOTER='''<footer><div class="wrap">
  <span class="concept-flag">2027 Direction concept &middot; secondary site option &middot; not the live site</span>
  <div class="foot-top">
    <div><span class="wm">wasabi<span class="wr">rub<sup>&reg;</sup></span></span><p class="foot-tag">pain relief that keeps you moving.</p></div>
    <div class="foot-cols">
      <div class="foot-col"><h4>Shop</h4><a href="product-wasabirub.html">WasabiRub</a><a href="product-super-hot.html">Super Hot</a><a href="product-super-cold.html">Super Cold</a><a href="shop.html">All rubs</a></div>
      <div class="foot-col"><h4>Brand</h4><a href="index.html#idea">The idea</a><a href="index.html#cred">Why trust it</a><a href="index.html#belong">The movement</a></div>
    </div>
  </div>
  <p class="foot-fine">Concept exploration of the 2027 movement-brand direction for WasabiRub by SportPharm &mdash; a secondary site option, not the live store. For external use only. For the temporary relief of minor aches and pains of muscles and joints; use only as directed and read the Drug Facts label. Product photography is real; lifestyle imagery is AI-generated for direction.</p>
</div></footer>'''

def page(title, active, main):
    return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="css/site.css">
</head><body>
{nav(active)}
{main}
{FOOTER}
</body></html>'''

PRODUCTS={
 "og":{"name":"WasabiRub","file":"product-wasabirub.html","jar":"jar-og.png","cls":"og","tag":"Everyday","move":"Cool + heat","price":"29.95","em":"everyday.",
   "tagline":"The original triple-action rub — balanced cooling and warming for the aches of everyday movement.",
   "actives":[("Menthol","10%","Cools"),("Capsaicin",".0375%","Warms"),("Methyl Salicylate","20%","Targets")],
   "band":"life-stretch.jpg","band_line":"For the people who keep <em>coming back.</em>"},
 "hot":{"name":"Super Hot","file":"product-super-hot.html","jar":"jar-hot.png","cls":"hot","tag":"Max heat","move":"Double capsaicin","price":"39.95","em":"hard.",
   "tagline":"Cools first, then heats up — twice the capsaicin for deep, lasting warmth when you push hard.",
   "actives":[("Menthol","10%","Cools"),("Capsaicin",".075%","Double heat"),("Methyl Salicylate","20%","Targets")],
   "band":"life-climb.jpg","band_line":"When you <em>push harder.</em>"},
 "cold":{"name":"Super Cold","file":"product-super-cold.html","jar":"jar-cold.png","cls":"cold","tag":"Pure cooling","move":"16% menthol","price":"39.95","em":"cool.",
   "tagline":"A high-strength menthol cream — pure, fast cooling with no warming phase, for fresh aches.",
   "actives":[("Menthol","16%","Cools hard"),("Cream base","—","Absorbs fast"),("Muscles + joints","—","Targets")],
   "band":"life-swim.jpg","band_line":"Cool it <em>down.</em>"},
}
ORDER=["og","hot","cold"]
DESC={"og":"The original triple-action rub — balanced cooling and warming for daily aches.",
 "hot":"Cools first, then heats up — twice the capsaicin for deep, lasting warmth.",
 "cold":"High-strength menthol cream — pure, fast cooling with no warming phase."}

def card(k):
    p=PRODUCTS[k]
    return f'''<article class="card {p['cls']}">
  <div class="shot"><span class="tag">{p['tag']}</span><img src="assets/{p['jar']}" alt="{p['name']} jar" loading="lazy"></div>
  <div class="body"><span class="move">{p['move']}</span><h3 class="serif">{p['name']}</h3><p>{DESC[k]}</p>
  <div class="foot"><span class="price serif">${p['price']}</span><a class="shop-link" href="{p['file']}">View &rarr;</a></div></div>
</article>'''

# ---------------- HOME ----------------
home=f'''<header class="hero"><div class="wrap hero-grid">
  <div><p class="eyebrow">We exist to keep people moving</p>
    <h1>Pain relief that keeps you <em>moving.</em></h1>
    <p class="hero-sub">Triple-action relief, formulated by pharmacists. Recovery is the means — movement is the end. Made for every body that moves.</p>
    <div class="hero-cta"><a class="btn-lime" href="shop.html">Shop the rubs &rarr;</a><a class="btn-ghost" href="#idea">See the idea</a></div>
    <div class="badges"><span class="badge"><b>&check;</b> Pharmacist formulated</span><span class="badge"><b>&check;</b> TruShield Certified</span><span class="badge"><b>&check;</b> Tested for sport</span></div>
  </div>
  <div class="jar-vis"><span class="jar-disc"></span><span class="jar-shadow"></span><span class="geo g1">34.0195&deg;N</span><span class="geo g2">IN MOTION</span>
    <img id="hero-jar" src="assets/jar-og.png" alt="WasabiRub Original jar"></div>
</div></header>

<section class="band"><img id="band-photo" src="assets/life-finish.jpg" alt="Runners celebrating at a sunny finish line">
  <div class="band-in"><span class="band-tag">In motion &middot; everywhere</span><h2 class="serif">We exist to keep people <em>moving.</em></h2></div>
</section>

<section class="idea sec-pad" id="idea"><div class="wrap">
  <div class="idea-top"><div><p class="kicker">What we're becoming</p>
    <h2 class="serif">We&rsquo;re not moving away from pain relief. We&rsquo;re building a <em>world around it.</em></h2></div>
    <figure class="idea-photo"><img src="assets/life-recover.jpg" alt="Applying WasabiRub after a run"></figure></div>
  <div class="ladder">
    <div class="rung"><span class="n">01 / PRODUCT</span><h3>Pain relief</h3><p>The triple-action formula that goes to work on sore muscles and joints.</p></div>
    <div class="rung"><span class="n">02 / ROLE</span><h3>Recovery</h3><p>The role we play &mdash; helping you bounce back for the next one.</p></div>
    <div class="rung"><span class="n">03 / WORLD</span><h3>Movement</h3><p>The world we belong in: the gym bag, the locker room, the start line.</p></div>
    <div class="rung"><span class="n">04 / MEANING</span><h3>Resilience</h3><p>What we stand for &mdash; a brand for the people who keep coming back.</p></div>
  </div>
  <p class="idea-foot serif">Pain relief is the product. <b>Recovery is the means. Movement is the end.</b></p>
</div></section>

<section class="range sec-pad" id="range"><div class="wrap">
  <p class="kicker">The range</p><h2 class="serif">One rub for every way you <em>move.</em></h2>
  <p class="lede">Same pharmacy-grade thinking, three ways to feel it. Cool, warm, or both &mdash; pick the relief that fits how you move.</p>
  <div class="cards">{card("og")}{card("hot")}{card("cold")}</div>
</div></section>

<section class="voice sec-pad"><div class="wrap">
  <p class="kicker">How we show up</p><h2 class="serif">We take movement seriously. <em>Life? Not so much.</em></h2>
  <p class="sub">We make recovery serious, so you can have the fun. Show up, sweat a little, smile a lot &mdash; and roll with it. Part of the fun is the burn.</p>
  <div class="chips"><span class="chip">Move seriously</span><span class="chip">Live playfully</span><span class="chip">Life gets spicy</span><span class="chip">Roll with it</span><span class="chip">Trying is cool</span></div>
</div></section>

<section class="cred sec-pad" id="cred"><div class="wrap cred-grid">
  <div><p class="kicker">Credible by design</p><h2 class="serif">Formulated by pharmacists. Trusted by the pros.</h2>
    <p>Desirable enough to throw in your bag, credible enough for the people who work with athletes every day. The fun is earned by the formula behind it.</p></div>
  <div class="cred-list">
    <div class="cred-item"><span class="ic">&#8478;</span><div><b>Pharmacist formulated</b><span>Built with pharmaceutical expertise behind every active and percentage.</span></div></div>
    <div class="cred-item"><span class="ic">&check;</span><div><b>TruShield Certified</b><span>Third-party certification supporting product integrity and trust.</span></div></div>
    <div class="cred-item"><span class="ic">&#9678;</span><div><b>Tested for sport</b><span>Screened so you can train and compete with confidence. Always read the Drug Facts label.</span></div></div>
  </div>
</div></section>

<section class="belong sec-pad" id="belong"><div class="wrap">
  <p class="kicker">Belong in motion</p><h2 class="serif">Made for every body that moves.</h2>
  <p class="sub">No one thinks &ldquo;I&rsquo;m a pain-cream person.&rdquo; They think runner, lifter, pickleball-on-Sunday, keeping-up-with-the-kids. Whatever yours is &mdash; you belong here.</p>
  <div class="belong-grid">
    <div class="btile"><img src="assets/life-sprint.jpg" alt=""></div><div class="btile"><img src="assets/life-cycle.jpg" alt=""></div>
    <div class="btile"><img src="assets/life-climb.jpg" alt=""></div><div class="btile"><img src="assets/life-team.jpg" alt=""></div>
    <div class="btile"><img src="assets/life-swim.jpg" alt=""></div><div class="btile"><img src="assets/life-yoga.jpg" alt=""></div>
  </div>
  <div class="movewords"><span class="lime">runners</span><span>lifters</span><span class="hot">picklers</span><span>skaters</span><span>swimmers</span><span class="lime">climbers</span><span>cyclists</span><span>hoopers</span><span class="hot">yogis</span><span>weekend warriors</span><span class="lime">comeback kids</span><span>every body</span></div>
  <form class="join" onsubmit="return false"><input type="email" placeholder="Join the movement &mdash; your email" aria-label="Email"><button type="submit">Join</button></form>
  <p class="join-note">First to hear about drops, the Athletic Club, and new ways to move. Concept only.</p>
</div></section>'''

# ---------------- SHOP ----------------
shop=f'''<header class="sec-pad"><div class="wrap shop-head">
  <p class="eyebrow">The range</p><h2 class="serif">Find your <em style="font-style:italic;color:var(--lime)">rub.</em></h2>
  <p>Three ways to feel it, one standard behind them. Flat $7.99 shipping, free over $75.</p>
  <div class="cards">{card("og")}{card("hot")}{card("cold")}</div>
</div></header>
<section class="band"><img src="assets/life-cycle.jpg" alt="Cyclists on an open road">
  <div class="band-in"><span class="band-tag">Made for every body</span><h2 class="serif">Pick the relief that fits how you <em>move.</em></h2></div>
</section>
<section class="cred sec-pad"><div class="wrap cred-grid">
  <div><p class="kicker">Credible by design</p><h2 class="serif">Formulated by pharmacists. Trusted by the pros.</h2>
  <p>Every rub is built on the same pharmacy-grade thinking &mdash; desirable enough for your bag, credible enough for the pros.</p></div>
  <div class="cred-list">
    <div class="cred-item"><span class="ic">&#8478;</span><div><b>Pharmacist formulated</b><span>Pharmaceutical expertise behind every active and percentage.</span></div></div>
    <div class="cred-item"><span class="ic">&check;</span><div><b>TruShield Certified</b><span>Third-party certification supporting product integrity.</span></div></div>
    <div class="cred-item"><span class="ic">&#9678;</span><div><b>Tested for sport</b><span>Train and compete with confidence. Read the Drug Facts label.</span></div></div>
  </div>
</div></section>'''

# ---------------- PDP ----------------
def pdp(k):
    p=PRODUCTS[k]; others=[o for o in ORDER if o!=k]
    actives="".join(f'<div class="a"><b>{n}</b><span>{pct} &middot; {role}</span></div>' for n,pct,role in p["actives"])
    feel=f'''<section class="feel sec-pad"><div class="wrap"><p class="kicker">How it feels</p>
      <h2 class="serif">Three actives, three jobs.</h2><div class="feel-steps">
      <div class="feel-step"><span class="pct">Menthol</span><h3>Cools on contact</h3><p>Activates the skin&rsquo;s cold receptors for an immediate cooling sensation that takes the edge off.</p></div>
      <div class="feel-step"><span class="pct">{'Capsaicin' if k!='cold' else 'Cream base'}</span><h3>{'Brings the heat' if k!='cold' else 'Absorbs fast'}</h3><p>{'Builds a gradual, lasting warmth where you apply it.' if k!='cold' else 'A smooth, non-greasy cream that spreads evenly and sinks in.'}</p></div>
      <div class="feel-step"><span class="pct">{'Methyl salicylate' if k!='cold' else 'Targeted'}</span><h3>Targets the sore spot</h3><p>Works topically to temporarily relieve minor aches and pains of muscles and joints.</p></div>
      </div></div></section>'''
    cross="".join(card(o) for o in others)
    return f'''<section class="pdp-hero"><div class="wrap pdp-grid">
  <div class="pdp-visual {p['cls']}"><span class="jar-shadow"></span><img src="assets/{p['jar']}" alt="{p['name']} jar"></div>
  <div class="pdp-copy"><span class="pill">{p['tag']} &middot; {p['move']}</span>
    <h1 class="serif">{p['name']}</h1>
    <p class="tagline">{p['tagline']}</p>
    <div class="pdp-actives">{actives}</div>
    <div class="pdp-buy"><span class="pdp-price serif">${p['price']}</span><span class="pdp-size">4 oz (113.4 g)</span><a class="btn-lime" href="shop.html">Add to cart &rarr;</a></div>
    <div class="badges"><span class="badge"><b>&check;</b> Pharmacist formulated</span><span class="badge"><b>&check;</b> TruShield Certified</span><span class="badge"><b>&check;</b> Tested for sport</span></div>
  </div>
</div></section>
{feel}
<section class="band"><img src="assets/{p['band']}" alt="Athlete in motion">
  <div class="band-in"><span class="band-tag">{p['name']}</span><h2 class="serif">{p['band_line']}</h2></div></section>
<section class="pdp-reviews sec-pad"><div class="wrap">
  <p class="kicker">From verified buyers</p><h2 class="serif">What movers say.</h2>
  <div class="rstars" aria-hidden="true">&starf;&starf;&starf;&starf;&starf;</div>
  <p class="rnote">Sample reviews &mdash; on the live site these pull from verified buyers who get an emailed link after their order ships.</p>
  <div class="rev-cards">
    <div class="rev-card"><span class="s">&starf;&starf;&starf;&starf;&starf;</span><span class="v">Verified buyer</span><p>Goes on cool, then the heat kicks in right where I need it. In my bag for every long run now.</p><p class="by">Jordan R.</p></div>
    <div class="rev-card"><span class="s">&starf;&starf;&starf;&starf;&starf;</span><span class="v">Verified buyer</span><p>Coach recommended it. Smells clean, not medicinal, and actually helps after lifting days.</p><p class="by">Dani M.</p></div>
    <div class="rev-card"><span class="s">&starf;&starf;&starf;&starf;&star;</span><span class="v">Verified buyer</span><p>Great for my shoulders. Wish the jar were bigger because I go through it fast.</p><p class="by">Sam T.</p></div>
  </div>
</div></section>
<section class="range cross sec-pad"><div class="wrap"><p class="kicker">Keep exploring</p><h2 class="serif">The rest of the range.</h2><div class="cards">{cross}</div></div></section>'''

# ---- write ----
open(f"{HERE}/index.html","w").write(page("WasabiRub 2027", "home", home))
open(f"{HERE}/shop.html","w").write(page("Shop | WasabiRub 2027", "shop", shop))
for k in ORDER:
    open(f"{HERE}/{PRODUCTS[k]['file']}","w").write(page(f"{PRODUCTS[k]['name']} | WasabiRub 2027", "shop", pdp(k)))
print("wrote: index.html shop.html", *[PRODUCTS[k]['file'] for k in ORDER])
