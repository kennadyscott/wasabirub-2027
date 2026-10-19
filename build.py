# Builds the WasabiRub 2027 store (variant B) with shared nav/footer.
import os, re
HERE=os.path.dirname(os.path.abspath(__file__))
REAL_REPO=os.path.expanduser("~/Documents/Claude/wasabirub-redesign")

def nav(active):
    def a(href,label,key):
        on=' class="on"' if key==active else ''
        return f'<a{on} href="{href}">{label}</a>'
    return f'''<div class="ticker" aria-hidden="true"><div class="run">
<span>MADE FOR EVERY BODY THAT MOVES</span><span>•</span><span>PAIN RELIEF THAT KEEPS YOU MOVING</span><span>•</span><span>MOVE SERIOUSLY. LIVE PLAYFULLY.</span><span>•</span><span>BELONG IN MOTION</span><span>•</span><span>MADE FOR EVERY BODY THAT MOVES</span><span>•</span><span>PAIN RELIEF THAT KEEPS YOU MOVING</span><span>•</span><span>MOVE SERIOUSLY. LIVE PLAYFULLY.</span><span>•</span>
</div></div>
<nav class="bar"><div class="wrap bar-in">
  <a class="wm" href="index.html">wasabi<span class="wr">rub<sup>&reg;</sup></span></a>
  <div class="links">{a("wasabirub-shop.html","Shop","shop")}{a("how-it-works.html","Why WasabiRub","why")}{a("quality.html","Quality","quality")}{a("articles.html","Articles","articles")}<a href="https://sportpharm.com" target="_blank" rel="noopener">For Pros &#8599;</a></div>
  <span class="spacer"></span>
  <span class="nav-right"><a class="pill-btn" href="wasabirub-shop.html">Shop &rarr;</a></span>
</div></nav>'''

FOOTER='''<footer><div class="wrap">
  <div class="foot-top">
    <div><span class="wm">wasabi<span class="wr">rub<sup>&reg;</sup></span></span><p class="foot-tag">pain relief that keeps you moving.</p></div>
    <div class="foot-cols">
      <div class="foot-col"><h4>Shop</h4><a href="wasabirub.html">WasabiRub</a><a href="wasabirub-super-hot.html">Super Hot</a><a href="wasabirub-super-cold.html">Super Cold</a><a href="wasabirub-shop.html">All rubs</a><a href="wasabirub-shop.html#bundles">Bundles</a></div>
      <div class="foot-col"><h4>Learn</h4><a href="how-it-works.html">Why WasabiRub</a><a href="quality.html">Quality</a><a href="articles.html">Articles</a><a href="https://sportpharm.com" target="_blank" rel="noopener">For Professionals</a></div>
      <div class="foot-col"><h4>Support</h4><a href="contact.html">Contact</a><a href="shipping-returns.html">Shipping &amp; Returns</a><a href="privacy-policy.html">Privacy Policy</a><a href="terms-and-conditions.html">Terms of Service</a></div>
    </div>
  </div>
  <p class="foot-fine">&copy; 2026 SportPharm. For external use only. Temporarily relieves minor aches and pains of muscles and joints. Use only as directed and read the Drug Facts label. Formulated by sports pharmacists. Lifestyle imagery shown for brand direction.</p>
</div></footer>'''

HEAD_ANALYTICS = '''<!-- GA4 + Meta Pixel, gated to the production host only (preview links stay out of prod analytics) -->
<script>(function(){
  if(!/(^|\\.)wasabirub\\.com$/.test(location.hostname)) return;
  var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-J0Z8PMBZCV';document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments);};
  gtag('js',new Date());gtag('config','G-J0Z8PMBZCV');gtag('set',{ab_variant:'b_2027'});dataLayer.push({ab_variant:'b_2027'});
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
  fbq('init','3080251875460548');fbq('track','PageView');
})();</script>'''

def page(title, active, main, head_extra="", scripts_extra=""):
    return f'''<!doctype html><html lang="en" data-hero="split"><head>
{HEAD_ANALYTICS}
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex,nofollow">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png">
<meta name="theme-color" content="#04342a">
<link rel="stylesheet" href="assets/css/cart.css">
<link rel="stylesheet" href="assets/css/popup.css">
<link rel="stylesheet" href="assets/css/reviews.css">
<link rel="stylesheet" href="css/site.css">{head_extra}
</head><body>
{nav(active)}
{main}
{FOOTER}
<script src="assets/js/cart.js" defer></script>
<script src="assets/js/popup.js" defer></script>
<script src="assets/js/reviews.js" defer></script>{scripts_extra}
<script src="proto.js" defer></script>
</body></html>'''

PRODUCTS={
 "og":{"name":"WasabiRub","file":"wasabirub.html","id":"original","sku":"WASABIRUB","jar":"jar-og.png","cls":"og","tag":"Everyday","move":"Cool + heat","price":"29.95","em":"everyday.",
   "tagline":"The original triple-action rub — balanced cooling and warming for the aches of everyday movement.",
   "actives":[("Menthol","10%","Cools"),("Capsaicin",".0375%","Warms"),("Methyl Salicylate","20%","Targets")],
   "band":"life-stretch.jpg","band_line":"For the people who keep <em>coming back.</em>"},
 "hot":{"name":"Super Hot","file":"wasabirub-super-hot.html","id":"super-hot","sku":"SUPERHOT","jar":"jar-hot.png","cls":"hot","tag":"Max heat","move":"Double capsaicin","price":"39.95","em":"hard.",
   "tagline":"Cools first, then heats up — twice the capsaicin for deep, lasting warmth when you push hard.",
   "actives":[("Menthol","10%","Cools"),("Capsaicin",".075%","Double heat"),("Methyl Salicylate","20%","Targets")],
   "band":"life-climb.jpg","band_line":"When you <em>push harder.</em>"},
 "cold":{"name":"Super Cold","file":"wasabirub-super-cold.html","id":"super-cold","sku":"ICETRARUB","jar":"jar-cold.png","cls":"cold","tag":"Pure cooling","move":"16% menthol","price":"39.95","em":"cool.",
   "tagline":"A high-strength menthol cream — pure, fast cooling with no warming phase, for fresh aches.",
   "actives":[("Menthol","16%","Cools hard"),("Cream base","—","Absorbs fast"),("Muscles + joints","—","Targets")],
   "band":"life-swim.jpg","band_line":"Cool it <em>down.</em>"},
}
ORDER=["og","hot","cold"]
DESC={"og":"The original triple-action rub — balanced cooling and warming for daily aches.",
 "hot":"Cools first, then heats up — twice the capsaicin for deep, lasting warmth.",
 "cold":"High-strength menthol cream — pure, fast cooling with no warming phase."}

def card(k, buy=False):
    p=PRODUCTS[k]
    action=(f'<button class="shop-link add" type="button" data-add-to-cart="{p["id"]}">Add &rarr;</button>'
            if buy else f'<a class="shop-link" href="{p["file"]}">View &rarr;</a>')
    return f'''<article class="card {p['cls']}">
  <a class="shot" href="{p['file']}"><span class="tag">{p['tag']}</span><img src="assets/{p['jar']}" alt="{p['name']} jar" loading="lazy"></a>
  <div class="body"><span class="move">{p['move']}</span><h3 class="serif"><a href="{p['file']}">{p['name']}</a></h3><p>{DESC[k]}</p>
  <div class="foot"><span class="price serif">${p['price']}</span>{action}</div></div>
</article>'''

BUNDLES=[
 {"id":"fire-ice-duo","name":"Fire &amp; Ice Duo","price":"64.99","was":"79.90","thumb":"bundle-fire-ice.png","contains":"1 Super Hot &middot; 1 Super Cold","desc":"Max heat meets pure cooling — the two strongest sensations, together."},
 {"id":"og-heat-duo","name":"OG Heat Duo","price":"59.99","was":"69.90","thumb":"bundle-og-heat.png","contains":"1 Original &middot; 1 Super Hot","desc":"Double the heat, double the recovery — balanced relief plus intensified warmth."},
 {"id":"recovery-duo","name":"Recovery Duo","price":"64.99","was":"69.90","thumb":"bundle-recovery.png","contains":"1 Original &middot; 1 Super Cold","desc":"Warm and cool in one kit — support for warm-up and recovery alike."},
 {"id":"team-trifecta","name":"Team Trifecta","price":"269.95","was":"329.55","thumb":"bundle-trifecta.png","contains":"3 Original &middot; 3 Super Hot &middot; 3 Super Cold","desc":"Stock the whole training room — all three rubs, three deep."},
]
def bundle_card(b):
    return f'''<article class="card bundle">
  <div class="shot"><span class="tag">Bundle</span><img src="assets/{b['thumb']}" alt="{b['name']}" loading="lazy"></div>
  <div class="body"><span class="move">{b['contains']}</span><h3 class="serif">{b['name']}</h3><p>{b['desc']}</p>
  <div class="foot"><span class="price serif">${b['price']} <s>${b['was']}</s></span><button class="shop-link add" type="button" data-add-to-cart="{b['id']}">Add &rarr;</button></div></div>
</article>'''

# ---------------- HOME ----------------
home=f'''<header class="hero"><img id="hero-bg" class="hero-bg" src="assets/life-finish.jpg" alt="" aria-hidden="true"><div class="wrap hero-grid">
  <div class="hero-copy"><p class="eyebrow">We exist to keep people moving</p>
    <h1>Pain relief that keeps you <em>moving.</em></h1>
    <p class="hero-sub">Triple-action relief, formulated by pharmacists. Recovery is the means — movement is the end. Made for every body that moves.</p>
    <div class="hero-cta"><a class="btn-lime" href="wasabirub-shop.html">Shop the rubs &rarr;</a><a class="btn-ghost" href="#idea">See the idea</a></div>
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
  <div class="cards">{card("og",buy=True)}{card("hot",buy=True)}{card("cold",buy=True)}</div>
</div></header>
<section class="range sec-pad" id="bundles"><div class="wrap">
  <p class="kicker">Bundles &amp; duos</p><h2 class="serif">Pair the sensations. <em>Save on the set.</em></h2>
  <p class="lede">Stock up or mix the feels and save versus buying each on its own. Free shipping over $75 applies to individual items only — bundles ship at the flat $7.99 rate.</p>
  <div class="cards">{''.join(bundle_card(b) for b in BUNDLES)}</div>
</div></section>
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
    <div class="pdp-buy"><span class="pdp-price serif">${p['price']}</span><span class="pdp-size">4 oz (113.4 g)</span>
      <div class="qty" data-qty><button type="button" data-qty-minus aria-label="Decrease quantity">&minus;</button><span data-qty-value>1</span><button type="button" data-qty-plus aria-label="Increase quantity">+</button></div>
      <button class="btn-lime" type="button" data-add-to-cart="{p['id']}">Add to cart</button></div>
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

# ---------------- ARTICLES ----------------
ART_META=[
 ("article-green-whistle-penthrox","Medical","Green Whistle: What Sports Medicine Teams Should Know About Penthrox","art-sideline-ready.jpg"),
 ("article-sportpharm-trushield-partnership","Clean Sport","SportPharm Partners With TruShield&trade; To Advance Clean Sport and Athlete Safety","art-ketorub.png"),
 ("article-evidence-based-recovery","Recovery","Recovery Isn&rsquo;t One-Size-Fits-All: Routine, Sleep, and Choosing the Right Supplements","art-recovery.jpg"),
 ("article-cuts-and-lacerations","Medical","Why Athletic Trainers Need to Be Ready for Cuts and Lacerations","art-cuts-lacerations.jpg"),
 ("article-sideline-ready-emergency-preparedness","Medical","Sideline Ready: A Pharmacist&rsquo;s Guide to Emergency Medication Preparedness","art-sideline-ready.jpg"),
 ("article-summer-pain-management","Pain Relief","5 Essential Summer Pain Management Tips","art-icetrarub.jpg"),
 ("article-preventing-treating-blisters","Medical","How Baseball Players Can Prevent and Treat Blisters","art-blisters.jpg"),
 ("article-anti-inflammatory-compounds","Pain Relief","A More Targeted Approach to Anti-Inflammatory Care","art-anti-inflammatory.jpg?v=2"),
 ("article-in-house-dispensing-playbook","Sports Pharmacy","The In-House Pharmacy Dispensing Playbook","art-dispensing.jpg?v=3"),
]
def acard(m):
    slug,cat,title,thumb=m
    return (f'<a class="acard" href="{slug}.html">'
            f'<span class="acard-img"><img src="assets/{thumb}" alt="" loading="lazy"></span>'
            f'<span class="acard-body"><span class="acard-cat">{cat}</span>'
            f'<span class="acard-title serif">{title}</span>'
            f'<span class="acard-more">Read &rarr;</span></span></a>')
articles_main=f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">The reading room</p><h1 class="serif">Articles</h1>
  <p class="lede">Practical, evidence-informed guidance on recovery, medication, and getting back to what moves you.</p>
</div></header>
<section class="sec-pad artindex"><div class="wrap"><div class="acards">
{''.join(acard(m) for m in ART_META)}
</div></div></section>'''

def port_article(slug):
    html=open(f"{REAL_REPO}/{slug}.html",encoding="utf-8").read()
    title=(re.search(r'<title>(.*?)</title>',html,re.S) or [None,"WasabiRub"])[1]
    desc=(re.search(r'<meta name="description" content="([^"]*)"',html) or [None,""])[1]
    m=re.search(r'</header>(.*?)<footer',html,re.S)
    region=m.group(1).strip() if m else "<p>Article unavailable.</p>"
    # strip the article's own inline <style>/<script> so only the 2027 CSS styles it
    region=re.sub(r'<style\b[^>]*>.*?</style>','',region,flags=re.S)
    region=re.sub(r'<script\b[^>]*>.*?</script>','',region,flags=re.S)
    head_extra=('\n<meta name="description" content="'+desc+'">') if desc else ""
    return page(title,"articles",region,head_extra=head_extra)

# ---------------- CART ----------------
cart_main='''<section class="sec-pad cart-sec"><div class="wrap">
  <p class="eyebrow">Your cart</p><h1 class="serif cart-h1">Ready when you <em>are.</em></h1>
  <p class="cart-intro">Mix the sensations in one order. Flat $7.99 shipping in the U.S., free over $75 on individual items.</p>
  <div id="wr-cart-page"></div>
</div></section>'''

# ---- write ----
open(f"{HERE}/index.html","w").write(page("WasabiRub | Triple-Action Topical Pain Relief Gel", "home", home))
open(f"{HERE}/wasabirub-shop.html","w").write(page("Shop WasabiRub, Super Hot & Super Cold | Topical Pain Relief", "shop", shop))
open(f"{HERE}/cart.html","w").write(page("Your cart | WasabiRub", "", cart_main))
PTITLE={"og":"WasabiRub | Triple-Action Topical Pain Relief Gel",
 "hot":"WasabiRub Super Hot | Maximum Warming Relief",
 "cold":"WasabiRub Super Cold | Pure Cooling Relief"}
for k in ORDER:
    open(f"{HERE}/{PRODUCTS[k]['file']}","w").write(page(PTITLE[k], "shop", pdp(k)))
# articles
open(f"{HERE}/articles.html","w").write(page("Articles | WasabiRub","articles",articles_main))
for slug,_,_,_ in ART_META:
    open(f"{HERE}/{slug}.html","w").write(port_article(slug))
print("wrote: index.html wasabirub-shop.html cart.html articles.html +9 articles", *[PRODUCTS[k]['file'] for k in ORDER])

# ==================== CONTENT PAGES ====================
def mlead(t):  # muted lead paragraph under a section head
    return f'<p class="mlead">{t}</p>'

howitworks_main=f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">Why WasabiRub</p><h1 class="serif">One formula. <em>Three ways to feel it.</em></h1>
  <p class="lede">The three WasabiRub rubs share the same pharmacist-formulated thinking &mdash; what changes is the balance of cool and heat. Here&rsquo;s how it works.</p>
</div></header>
<section class="idea sec-pad"><div class="wrap">
  <p class="kicker">The mechanism</p><h2 class="serif">Counterirritation, <em>made simple.</em></h2>
  {mlead("A counterirritant creates a noticeable surface sensation&mdash;cooling, warming, or tingling&mdash;to stimulate sensory receptors and temporarily alter how deeper discomfort is perceived.")}
  <div class="feel-steps" style="margin-top:34px">
    <div class="feel-step"><span class="pct">01 &middot; Apply</span><h3>Massage it in</h3><p>Massage a thin layer onto the sore area.</p></div>
    <div class="feel-step"><span class="pct">02 &middot; Feel</span><h3>Cool, then warm</h3><p>Cooling arrives first; warmth develops as you move.</p></div>
    <div class="feel-step"><span class="pct">03 &middot; Reset</span><h3>Shift the signal</h3><p>Competing sensory input helps change pain perception.</p></div>
  </div></div></section>
<section class="range sec-pad"><div class="wrap">
  <p class="kicker">One formula, three balances</p><h2 class="serif">Pick a rub, <em>feel the difference.</em></h2>
  <div class="rubexplain">
    <div class="rubx og"><span class="move">Balanced &middot; Everyday</span><h3 class="serif">Cool, then heat.</h3>
      <ul class="rsteps"><li><b>Menthol 10%</b> &mdash; cools on contact</li><li><b>Capsaicin .0375%</b> &mdash; brings the heat</li><li><b>Methyl salicylate 20%</b> &mdash; targets the sore spot</li></ul>
      <a class="shop-link" href="wasabirub.html">Shop WasabiRub &middot; $29.95 &rarr;</a></div>
    <div class="rubx hot"><span class="move">Max heat &middot; Double capsaicin</span><h3 class="serif">Cools first. Then heats up.</h3>
      <ul class="rsteps"><li><b>Menthol 10%</b> &mdash; cooling still lands first</li><li><b>Capsaicin .075%</b> &mdash; twice the heat</li><li><b>Methyl salicylate 20%</b> &mdash; targets the sore spot</li></ul>
      <a class="shop-link" href="wasabirub-super-hot.html">Shop Super Hot &middot; $39.95 &rarr;</a></div>
    <div class="rubx cold"><span class="move">Pure cooling &middot; No warming phase</span><h3 class="serif">One active. Pure cooling.</h3>
      <ul class="rsteps"><li><b>Menthol 16%</b> &mdash; the highest in the range</li><li><b>Cream base</b> &mdash; absorbs fast</li><li><b>No capsaicin</b> &mdash; no warming phase</li></ul>
      <a class="shop-link" href="wasabirub-super-cold.html">Shop Super Cold &middot; $39.95 &rarr;</a></div>
  </div></div></section>
<section class="feel sec-pad" id="ingredients"><div class="wrap">
  <p class="kicker">The actives</p><h2 class="serif">Three active ingredients. <em>One smart formula.</em></h2>
  <div class="ingrid">
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-menthol.jpg" alt="Menthol / mint leaf" loading="lazy"></span><span class="inglabel">The cool signal</span><h3 class="serif">Menthol 10%</h3><p>Menthol activates TRPM8&mdash;cold-sensitive receptors in the skin&mdash;creating an immediate cooling sensation that can temporarily shift attention away from soreness.</p></div>
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-capsaicin.jpg" alt="Capsaicin / chili pepper" loading="lazy"></span><span class="inglabel">The heat signal</span><h3 class="serif">Capsaicin .0375%</h3><p>Capsaicin activates heat-sensitive TRPV1 receptors. The first warm or tingling feeling gives way to local desensitization with continued use, quieting the intensity of pain signaling.</p></div>
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-wintergreen.jpg" alt="Methyl salicylate / wintergreen sprig" loading="lazy"></span><span class="inglabel">The targeted signal</span><h3 class="serif">Methyl salicylate 20%</h3><p>Methyl salicylate is a topical counterirritant used for temporary relief of minor muscle and joint aches&mdash;delivering localized action right where it is applied.</p></div>
  </div></div></section>
<section class="idea sec-pad" id="story"><div class="wrap">
  <div class="idea-top"><div><p class="kicker">The origin</p>
    <h2 class="serif">From professional clubhouses <em>to yours.</em></h2>
    {mlead("WasabiRub was developed by Robert Nickell, the first sports pharmacist for the U.S. Olympic Team. It first found a following with professional league pitchers in the late &rsquo;90s, then spread through college, minor league, and high school locker rooms.")}
    <p class="idea-foot" style="margin-top:22px">&ldquo;It goes on cool. As your body warms up, so does the rub.&rdquo;</p>
    {mlead("Today, that same pharmacist-formulated blend is made for athletic trainers, sports medicine professionals, and active individuals who take recovery seriously.")}</div>
    <figure class="idea-photo"><img src="assets/wasabirub-og-trushield-clear.png" alt="WasabiRub jar with TruShield certification"></figure></div></div></section>
<section class="cred sec-pad"><div class="wrap">
  <p class="kicker" style="color:var(--amber)">What&rsquo;s behind the jar</p>
  <div class="truststrip">
    <div class="ts"><b>&check;</b><span>Third-party tested</span><small>For safety and clean substances</small></div>
    <div class="ts"><b>&#8478;</b><span>Pharmacist formulated</span><small>Purpose-built for active bodies</small></div>
    <div class="ts"><b>&#9678;</b><span>Targeted relief</span><small>Apply only where you need it</small></div>
    <div class="ts"><b>4oz</b><span>Professional strength</span><small>Trusted from warm-up to recovery</small></div>
  </div></div></section>
<section class="idea sec-pad"><div class="wrap" style="max-width:760px">
  <p class="kicker">Use it right</p><h2 class="serif">Feel the formula. <em>Respect the heat.</em></h2>
  {mlead("Use only as directed on the product label. For external use only. Avoid contact with eyes and damaged skin; do not bandage tightly or use with a heating pad. Stop use if excessive irritation occurs.")}
  {mlead("Ask a healthcare professional before use if you have an underlying condition, take blood-thinning medication, are pregnant or breastfeeding, or have questions about whether this product is right for you.")}
</div></section>
<section class="wr-cta"><div class="wr-cta-in"><div class="wr-cta-txt"><p class="wr-cta-ey">Cool. Heat. Target.</p><p class="wr-cta-h">Ready to feel the <em>difference?</em></p><a class="btn-lime" href="wasabirub.html">Shop WasabiRub &rarr;</a></div><img src="assets/wr-wasabirub.png" alt="WasabiRub jar"></div></section>
<section class="sci sec-pad"><div class="wrap" style="max-width:760px">
  <p class="kicker">Science notes</p>
  <p class="sci-note">Mechanism summaries are based on the FDA External Analgesic Drug Products monograph and peer-reviewed literature on menthol/TRPM8 and capsaicin/TRPV1. This page is educational and does not replace product labeling or medical advice.</p>
</div></section>'''

quality_main=f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">Quality &amp; science</p><h1 class="serif">Confidence <em>in every rep.</em></h1>
  <p class="lede">WasabiRub is formulated by sports pharmacists, certified for clean sport, and built on three active ingredients that each have a clear job to do. Here&rsquo;s what&rsquo;s behind the jar.</p>
</div></header>
<section class="idea sec-pad"><div class="wrap">
  <p class="kicker">The heritage</p><h2 class="serif">From the mound to the podium &mdash; <em>now on your shelf.</em></h2>
  {mlead("WasabiRub wasn&rsquo;t born on a store shelf. It was compounded in a pharmacy over 25 years ago for professional athletes who needed relief they could count on &mdash; and it carried that same standard into Olympic competition before becoming the over-the-counter jar you can buy today.")}
  <div class="ladder" style="margin-top:40px">
    <div class="rung"><span class="n">01</span><h3>Compounded for the pros</h3><p>Originally compounded as a prescription for Major League Baseball pitchers &mdash; built to prep and recover the arms that make a living throwing.</p></div>
    <div class="rung"><span class="n">02</span><h3>Trusted at the highest level</h3><p>Used as an Rx compound across professional sports and at the 2004 Olympic Games, where clean, reliable formulation isn&rsquo;t optional.</p></div>
    <div class="rung"><span class="n">03</span><h3>Now OTC &mdash; same standard</h3><p>Today it&rsquo;s manufactured as an over-the-counter topical using only pure active pharmaceutical ingredients, and third-party tested for banned substances.</p></div>
  </div></div></section>
<section class="cred sec-pad"><div class="wrap cred-grid">
  <div><p class="kicker" style="color:var(--amber)">The standard</p><h2 class="serif">What TruShield&trade; certification means</h2>
    <p>TruShield&trade; is an independent certification focused on clean sport and athlete safety. Carrying the mark is our commitment that what&rsquo;s printed on the Drug Facts label is what&rsquo;s in the jar.</p>
    <img src="assets/trushield-logo.png" alt="TruShield Certified" class="tslogo"></div>
  <div class="cred-list">
    <div class="cred-item"><span class="ic">&check;</span><div><b>Certified by a third party</b><span>Verified, not self-declared.</span></div></div>
    <div class="cred-item"><span class="ic">&#9678;</span><div><b>Tested for banned substances</b><span>Made with pure active pharmaceutical ingredients &mdash; built for clean sport.</span></div></div>
    <div class="cred-item"><span class="ic">&#8478;</span><div><b>Formulated with athletes in mind</b><span>So it can be used with confidence at every level of sport.</span></div></div>
    <div class="cred-item"><span class="ic">&equiv;</span><div><b>Clear, consistent labeling</b><span>The actives and their percentages are stated on every jar.</span></div></div>
  </div></div></section>
<section class="cred sec-pad cred-dark"><div class="wrap">
  <p class="kicker">Formulated by sports pharmacists</p><h2 class="serif">Formulated by the pharmacists <em>who serve athletes.</em></h2>
  <div class="story-grid">
    <div><p>WasabiRub is made by SportPharm and has been trusted by athletes and sports-medicine professionals since 1995, when it was first formulated and compounded by pharmacist Robert Nickell, R.Ph. Robert was the first pharmacist to serve as the official sports pharmacist for the U.S. Olympic Training facilities and the 2004 Athens Games, and was designated to the USA Medical Team.</p>
    <p>He is a past president of the California Pharmacists Association, spent years as lead instructor for pharmaceutical compounding at USC&rsquo;s School of Pharmacy, and helped launch the first Entrepreneur Pharmaceutical Program in the U.S.</p></div>
    <div class="cred-list">
      <div class="cred-item"><span class="ic">1995</span><div><b>Founded</b><span>Sports pharmacy, East &amp; West divisions.</span></div></div>
      <div class="cred-item"><span class="ic">&#9733;</span><div><b>Olympic pharmacist</b><span>First official sports pharmacist, US Olympic Training facilities &amp; Athens 2004.</span></div></div>
      <div class="cred-item"><span class="ic">&#8478;</span><div><b>Licensed &amp; accredited</b><span>Compounding, repackaging and dispensing under pharmacy standards.</span></div></div>
    </div>
  </div>
  <p class="kicker" style="margin-top:40px">Robert&rsquo;s awards &amp; honors</p>
  <div class="awards">
    <div class="award"><b>Pharmacist of the Year (2000)</b><span>California Pharmacists Association</span></div>
    <div class="award"><b>Innovative Pharmacist of the Year (2005)</b><span>California Pharmacists Association</span></div>
    <div class="award"><b>Godfather of Sports Pharmacy (2024)</b><span>Sports Pharmacy Network</span></div>
    <div class="award"><b>Lifetime Achievement (2025)</b><span>Sports Pharmacy Network</span></div>
  </div></div></section>
<section class="feel sec-pad"><div class="wrap">
  <p class="kicker">The science</p><h2 class="serif">Three active ingredients, <em>three jobs.</em></h2>
  {mlead("WasabiRub layers a cooling active, a warming active and a topical analgesic. Together they create the cool-then-warm sensation the formula is known for.")}
  <div class="ingrid" style="margin-top:30px">
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-menthol.jpg" alt="Menthol / mint leaf" loading="lazy"></span><span class="inglabel">The cool signal</span><h3 class="serif">Menthol &middot; 10%</h3><p>Activates the skin&rsquo;s cold-sensing receptors (TRPM8), producing an immediate cooling sensation that helps take the edge off how soreness feels.</p></div>
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-capsaicin.jpg" alt="Capsaicin / chili pepper" loading="lazy"></span><span class="inglabel">The warm signal</span><h3 class="serif">Capsaicin &middot; .0375%</h3><p>The compound behind chili-pepper heat works on heat-sensitive nerve endings (TRPV1) to build a gradual, lasting warming sensation where you apply it.</p></div>
    <div class="ingcard"><span class="ingimg"><img src="assets/ing-wintergreen.jpg" alt="Methyl salicylate / wintergreen" loading="lazy"></span><span class="inglabel">The relief</span><h3 class="serif">Methyl salicylate &middot; 20%</h3><p>A salicylate related to aspirin, it works topically as a counterirritant to temporarily relieve minor aches and pains of muscles and joints.</p></div>
  </div>
  <p class="sci-note">Uses: for the temporary relief of minor aches and pains of muscles and joints. Sensation and intensity vary by person and application area. Always read and follow the Drug Facts label.</p></div></section>
<section class="cred sec-pad cred-dark"><div class="wrap">
  <p class="kicker">The professional protocol</p><h2 class="serif">How the pros <em>put it to work.</em></h2>
  {mlead("The same routine athletes and sports-medicine staff follow &mdash; one application to prep, one to recover.")}
  <div class="feel-steps" style="margin-top:30px">
    <div class="feel-step phase"><span class="pct">Before &middot; Prep for game time</span><h3>Prime the muscle</h3><p>Apply sparingly 10&ndash;15 minutes before activity to activate muscle tissue, increase blood flow, and reduce stiffness. WasabiRub goes on cool, then heats up &mdash; massage deeply to stimulate the heating effect.</p></div>
    <div class="feel-step phase"><span class="pct">After &middot; Post-game recovery</span><h3>Recover faster</h3><p>Use immediately after activity to help reduce soreness and inflammation and support faster recovery &mdash; so you&rsquo;re ready for the next session.</p></div>
  </div>
  <div class="protip"><b>Pro tip for activation</b><p>Massage deeply into the tissue using gloved hands, a massage tool, or after applying a warm towel to the area. This increases local blood flow and enhances the heating effect for better performance and mobility.</p></div>
  <p class="sci-note">For external use only. Use only as directed. Sensation and intensity vary by person and application area.</p></div></section>
<section class="belong sec-pad"><div class="wrap">
  <p class="kicker">Our mission</p><h2 class="serif">Pharmaceutical excellence, built for performance.</h2>
  <p class="sub">SportPharm is dedicated to delivering pharmaceutical excellence for athletes, high-performing individuals and the sports-medicine professionals who support them &mdash; blending clinical expertise, advanced technology and a deep understanding of performance demands to provide safe, effective and compliant solutions.</p>
  <div class="hero-cta" style="justify-content:center;margin-top:28px"><a class="btn-lime" href="wasabirub-shop.html">Shop WasabiRub &rarr;</a></div>
</div></section>'''

contact_main=f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">Contact</p><h1 class="serif">Get <em>in touch.</em></h1>
  <p class="lede">Questions about WasabiRub, an order, or bulk and team pricing? Send us a note and our team will get back to you &mdash; usually within one business day.</p>
</div></header>
<section class="sec-pad"><div class="wrap contact-grid">
  <div class="contact-reach"><h2 class="serif">Reach us directly</h2>
    <div class="cline"><span>Email</span><a href="mailto:info@sportpharm.com">info@sportpharm.com</a></div>
    <div class="cline"><span>Phone</span><a href="tel:+18334263797">(833) 426-3797</a></div>
    <div class="cline"><span>Hours</span><b>Mon&ndash;Fri, 8 AM &ndash; 6 PM ET</b></div>
    <div class="cline"><span>Response time</span><b>Within one business day</b></div>
    <p class="cnote">WasabiRub is an over-the-counter product. Please don&rsquo;t include sensitive medical details in your message &mdash; for prescription or clinical questions, our pharmacy team will follow up directly.</p>
  </div>
  <form class="wform" onsubmit="return false">
    <div class="field"><label for="cf_name">Name</label><input id="cf_name" required></div>
    <div class="field"><label for="cf_email">Email</label><input id="cf_email" type="email" required></div>
    <div class="field"><label for="cf_phone">Phone (optional)</label><input id="cf_phone"></div>
    <div class="field"><label for="cf_message">Message</label><textarea id="cf_message" required></textarea></div>
    <button class="btn-lime" type="submit">Send message &rarr;</button>
  </form>
</div></section>'''

conf_main=f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">Order confirmed</p><h1 class="serif">Thank you for <em>your order!</em></h1>
  <p class="lede" id="orderNo"></p>
</div></header>
<section class="sec-pad"><div class="wrap" style="max-width:760px">
  <div id="summary"></div>
  <div class="conf-steps">
    <div class="conf-step"><b>Receipt on the way</b><p>Stripe emailed a receipt to the address you used at checkout.</p></div>
    <div class="conf-step"><b>Packed &amp; shipped</b><p>Your order is prepared and ships within 1&ndash;2 business days within the U.S.</p></div>
    <div class="conf-step"><b>On its way</b><p>We&rsquo;ll email you as soon as your order ships.</p></div>
  </div>
  <div class="hero-cta" style="margin-top:30px"><a class="btn-lime" href="wasabirub-shop.html">Continue shopping &rarr;</a></div>
  <p class="cnote" style="margin-top:20px">Questions? <a href="mailto:info@sportpharm.com">info@sportpharm.com</a></p>
</div></section>'''

def legal(eyebrow,h1,eff,intro,body):
    effp=f'<p class="eff">Effective date: {eff}</p>' if eff else ''
    return f'''<header class="pagehead"><div class="wrap">
  <p class="eyebrow">{eyebrow}</p><h1 class="serif">{h1}</h1>{effp}
  <p class="lede">{intro}</p></div></header>
<section class="sec-pad"><div class="legal">{body}</div></section>'''

def nb(t): return f'<div class="notebox">{t}</div>'

privacy_body=f'''<h2>Information we collect</h2>
<h3>Information you provide</h3><p>When you place an order, create an account, sign up for updates, or contact us, we may collect your name, email address, phone number, shipping and billing address, payment details (handled by our payment provider), your communication preferences, and anything you choose to include in a message to us.</p>
<h3>Information collected automatically</h3><p>When you browse the site, we and our service providers use cookies and similar technologies to collect information such as your IP address, browser and device type, referring URLs, the pages you view, and the time you spend on the site.</p>
{nb("WasabiRub is an over-the-counter consumer product. This website is not intended to collect health or medical information, and we ask that you not include sensitive medical details in messages to us. If you contact the SportPharm pharmacy for prescription or other healthcare services, that interaction is handled separately under SportPharm&rsquo;s healthcare privacy and HIPAA practices.")}
<h2>How we use your information</h2><p>We use the information we collect to:</p>
<ul><li>Fulfill and manage your orders and process payments</li><li>Respond to your questions and customer-service requests</li><li>Personalize and improve your experience on the site</li><li>Send you updates or marketing emails when you&rsquo;ve asked to receive them</li><li>Analyze how the site is used and improve its performance</li><li>Meet our legal and regulatory obligations</li></ul>
<h2>How we share your information</h2><p>We do <b>not</b> sell your personal information. We share it only in these cases:</p>
<ul><li><b>Service providers</b> &mdash; companies that help us operate, such as payment processing, shipping and fulfillment, email, and analytics &mdash; under confidentiality obligations and only for the services they provide to us.</li><li><b>Legal requirements</b> &mdash; when required by law, such as a subpoena, court order, or lawful government request.</li><li><b>Protection</b> &mdash; to protect the rights, property, or safety of WasabiRub, SportPharm, our customers, or others.</li></ul>
<h2>Cookies and tracking</h2><p>We use cookies and similar technologies to keep the site working, remember your preferences, and understand how the site is used. You can disable cookies through your browser settings, though some features may not work as intended.</p>
<h2>Data security</h2><p>We use administrative, technical, and physical safeguards to protect your information, including HTTPS encryption, secure hosting, and limited internal access to personal data. No method of transmission or storage is completely secure, so we cannot guarantee absolute security.</p>
<h2>Your choices</h2><ul><li>Unsubscribe from marketing emails at any time using the link in the email, or by contacting us.</li><li>Ask us to access, correct, or delete the personal information we hold about you.</li><li>Control cookies through your browser settings.</li></ul><p>To make a request, email us at <a href="mailto:info@sportpharm.com">info@sportpharm.com</a>.</p>
<h2>Children&rsquo;s privacy</h2><p>WasabiRub is intended for adults. This site is not directed to children under 13, and we do not knowingly collect personal information from children. If you believe a child has provided us information, please contact us and we&rsquo;ll remove it.</p>
<h2>Changes to this policy</h2><p>We may update this policy from time to time. When we do, we&rsquo;ll revise the effective date above, and any significant changes will be posted on this page.</p>
<h2>Contact us</h2><p>Questions about this policy or your information? Reach us at:<br><b>WasabiRub</b> &mdash; a product of SportPharm<br>Email: info@sportpharm.com<br>Phone: (833) 426-3797<br>Mailing address: 379 Van Ness Ave, Torrance, CA 90501</p>'''

terms_body=f'''<h2>Using the site</h2><p>You agree to use wasabirub.com only for lawful purposes. You may not use the site to:</p>
<ul><li>Break any applicable law or regulation</li><li>Engage in fraudulent or harmful activity</li><li>Send spam or unauthorized advertising</li><li>Impersonate WasabiRub, SportPharm, or anyone else</li></ul><p>We may restrict or end your access to the site if you violate these terms.</p>
<h2>Products, orders, and pricing</h2><p>We describe our products as accurately as we can, but we don&rsquo;t warrant that descriptions, pricing, or other content are error-free. We may correct errors, change prices, or limit quantities at any time, and we may refuse or cancel an order &mdash; including after it&rsquo;s placed &mdash; if we suspect an error or unauthorized activity. Prices are shown in U.S. dollars.</p>
<h2>Payment</h2><p>Payment is handled by our third-party payment provider. By placing an order, you authorize us, through that provider, to charge your payment method for the order total, including any applicable taxes and shipping.</p>
<h2>Returns and refunds</h2><p>Because of the nature of our products, opened or used items are not eligible for return or refund. To be eligible for a return, a product must be <b>unused, unopened, and in its original condition</b>, and the request must be made within <b>14 days of delivery</b>. Refunds are issued only after we&rsquo;ve received and inspected the returned item and confirmed it&rsquo;s unused and unopened. If you&rsquo;re unsure which product is right for you, contact us before you buy &mdash; we&rsquo;re happy to help.</p>
<h2>Product use and disclaimer</h2><p>WasabiRub products are over-the-counter topical analgesics. Information on this site is for general education and is not medical advice; it does not replace the product&rsquo;s Drug Facts label or the guidance of a qualified healthcare provider. Always read and follow the Drug Facts label. Talk to your physician or pharmacist before use if you have a medical condition, take medication, or are pregnant or nursing. This site does not provide emergency medical services.</p>
{nb("This website is not intended to collect health or medical information. If you contact the SportPharm pharmacy for prescription or healthcare services, that interaction is handled under SportPharm&rsquo;s healthcare and HIPAA practices &mdash; see our Privacy Policy.")}
<h2>Intellectual property</h2><p>All content on this site &mdash; text, graphics, logos, images, and software &mdash; belongs to WasabiRub, SportPharm, or our licensors and is protected by copyright, trademark, and other laws. You may not reproduce, distribute, modify, or publicly display it without our prior written permission, except for personal, non-commercial use.</p>
<h2>Disclaimers</h2><p>The site and our products are provided &ldquo;as is&rdquo; and &ldquo;as available.&rdquo; To the fullest extent permitted by law, we disclaim all warranties, express or implied, including merchantability, fitness for a particular purpose, and non-infringement. You use the site at your own risk.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, WasabiRub, SportPharm, and their owners, employees, and affiliates will not be liable for any indirect, incidental, or consequential damages arising out of or in connection with your use of the site or products &mdash; including loss or corruption of data, errors or omissions in content, or outcomes from relying on site content.</p>
<h2>Indemnification</h2><p>You agree to indemnify, defend, and hold harmless WasabiRub, SportPharm, and their affiliates from any claims, liabilities, damages, losses, or expenses (including reasonable attorneys&rsquo; fees) arising out of your use of the site or your violation of these terms.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of California, without regard to its conflict-of-laws rules.</p>
<h2>Changes to these terms</h2><p>We may update these terms from time to time. When we do, we&rsquo;ll revise the effective date above, and your continued use of the site means you accept the updated terms.</p>
<h2>Contact us</h2><p>Questions about these terms? Reach us at:<br><b>WasabiRub</b> &mdash; a product of SportPharm<br>Email: info@sportpharm.com<br>Phone: (833) 426-3797<br>Mailing address: 379 Van Ness Ave, Torrance, CA 90501</p>'''

shipping_body=f'''<div class="shipstrip"><b>Free over $75</b> &middot; <b>$7.99 flat otherwise</b> &mdash; free US shipping on orders over $75. Bundle orders ship at the $7.99 flat rate.</div>
<h2>Shipping</h2>
<h3>Shipping rates</h3><p>Shipping is a flat <b>$7.99</b> per order within the United States. Orders <b>over $75 ship free</b> &mdash; this applies to the single rubs and does not include bundle or duo orders, which always ship at the $7.99 flat rate.</p>
<h3>Processing</h3><p>Orders are processed and shipped within 1&ndash;2 business days. You&rsquo;ll receive a confirmation email as soon as your order is on its way.</p>
<h3>Delivery</h3><p>Once shipped, most orders arrive within 3&ndash;7 business days, depending on your location. Delivery times are estimates and can vary during holidays or peak periods.</p>
<h3>Where we ship</h3><p>We currently ship within the United States. If you&rsquo;re outside the U.S. and would like to order, <a href="mailto:info@sportpharm.com">get in touch</a> and we&rsquo;ll see what we can do.</p>
<h2>Returns &amp; refunds</h2><p>Because WasabiRub products are topical, opened or used items can&rsquo;t be returned or refunded &mdash; it&rsquo;s a safety and hygiene standard we hold to.</p>
<h3>What&rsquo;s eligible</h3><p>To be eligible for a return, a product must be <b>unused, unopened, and in its original condition</b>, and your request must be made within <b>14 days of delivery</b>.</p>
<h3>How to start a return</h3><p>Email us at <a href="mailto:info@sportpharm.com">info@sportpharm.com</a> with your order number and the item(s) you&rsquo;d like to return, and we&rsquo;ll reply with return instructions.</p>
<form class="wform" onsubmit="return false" style="margin:18px 0 0">
  <div class="field"><label>Order number</label><input placeholder="e.g. WR-10428" required></div>
  <div class="field"><label>Email on the order</label><input type="email" required></div>
  <div class="field"><label>Item(s) you&rsquo;d like to return</label><input placeholder="e.g. WasabiRub Super Hot 4 oz" required></div>
  <div class="field"><label>Reason for the return (optional)</label><textarea></textarea></div>
  <label class="checkrow"><input type="checkbox" required> I confirm the item(s) are <b>unopened, unused, and in their original condition.</b></label>
  <button class="btn-lime" type="submit">Request return &rarr;</button>
</form>
<h3>Refunds</h3><p>Once we receive your return and confirm it&rsquo;s unused and unopened, we&rsquo;ll issue a refund to your original payment method. Refunds are processed after inspection and typically post within a few business days.</p>
<h3>Damaged or incorrect orders</h3><p>If your order arrives damaged, or you received the wrong item, please contact us within 7 days of delivery and we&rsquo;ll make it right.</p>
{nb("Not sure which rub is right for you? Reach out before you order &mdash; we&rsquo;re happy to help you choose the right one so a return isn&rsquo;t needed. Full terms are in our Terms of Service.")}
<h2>Questions?</h2><p>Email <a href="mailto:info@sportpharm.com">info@sportpharm.com</a><br>Call (833) 426-3797, Mon&ndash;Fri</p>'''

# ---- write content pages ----
open(f"{HERE}/how-it-works.html","w").write(page("Why WasabiRub | How the Triple-Action Formula Works","why",howitworks_main))
open(f"{HERE}/quality.html","w").write(page("Quality &amp; TruShield Testing | WasabiRub","quality",quality_main))
open(f"{HERE}/contact.html","w").write(page("Contact | WasabiRub","",contact_main))
open(f"{HERE}/order-confirmation.html","w").write(page("Thank you for your order | WasabiRub","",conf_main,head_extra='\n<meta name="robots" content="noindex">',scripts_extra='\n<script src="assets/js/order-confirmation.js" defer></script>'))
open(f"{HERE}/privacy-policy.html","w").write(page("Privacy Policy | WasabiRub","",legal("Legal","Privacy Policy","July 3, 2025","WasabiRub, a product of SportPharm, is committed to protecting your privacy. This policy explains what information we collect when you visit wasabirub.com or contact us, how we use it, and the choices you have.",privacy_body)))
open(f"{HERE}/terms-and-conditions.html","w").write(page("Terms of Service | WasabiRub","",legal("Legal","Terms of Service","July 3, 2025","These terms govern your use of wasabirub.com and any purchase you make from us. By using the site or placing an order, you agree to these terms, our Shipping &amp; Returns, and our Privacy Policy. If you don&rsquo;t agree, please don&rsquo;t use the site.",terms_body)))
open(f"{HERE}/shipping-returns.html","w").write(page("Shipping &amp; Returns | WasabiRub","",legal("Orders","Shipping &amp; Returns","","Everything you need to know about getting your WasabiRub &mdash; and what to do if something isn&rsquo;t right.",shipping_body)))
print("wrote content pages: how-it-works quality contact order-confirmation privacy terms shipping-returns")
