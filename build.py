#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the Brass Tack Communications website.

Run it with:      python3 build.py

It reads the copy from src/content.py and src/work.py, wraps it in the shared
header/footer/SEO markup, and writes plain .html files into this folder.
Nothing here needs a server or an internet connection.
"""
import json, os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))
import content as C
import work as W

S = C.SITE
BASE = S["domain"]
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- helpers --
def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))

def plain(t):
    """Strip entities/markup back to readable text for meta + schema."""
    t = re.sub(r"<[^>]+>", "", t)
    return (t.replace("&amp;", "&").replace("&quot;", '"')
             .replace("&lt;", "<").replace("&gt;", ">"))

def mark(heading, phrase):
    """Wrap `phrase` inside `heading` with the brass underline."""
    if phrase and phrase in heading:
        return heading.replace(phrase, '<span class="mark">%s</span>' % phrase, 1)
    return heading

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
DIAG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M7 17 17 7M8 7h9v9"/></svg>')
BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M19 12H5M11 18l-6-6 6-6"/></svg>')
PLAY = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M8 5.14v13.72a1 1 0 0 0 1.54.84l10.3-6.86a1 1 0 0 0 0-1.68L9.54 4.3A1 1 0 0 0 8 5.14Z"/></svg>')

# ------------------------------------------------------------ shared chrome --
def header(active):
    links = []
    for label, href in C.NAV:
        cur = ' aria-current="page"' if href == active or (
              active.startswith("work-") and href == "work.html") else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cur, esc(label)))
    return """<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap-wide header-inner">
    <a class="brand" href="index.html" aria-label="Brass Tack Communications, home">
      <img src="assets/img/brass-tack-logo.png" width="1500" height="404"
           alt="Brass Tack Communications" fetchpriority="high" decoding="async">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false"
            aria-controls="primary-nav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
      %s
      <a class="btn btn-primary header-cta" href="contact.html">Let&rsquo;s chat %s</a>
    </nav>
  </div>
</header>""" % ("\n      ".join(links), ARROW)


def cta_band():
    return """<section class="section-tight band-dark cta-band">
  <div class="wrap-wide cta-inner">
    <h2>Let&rsquo;s put your story to work.</h2>
    <div class="cta-actions">
      <a class="btn btn-on-dark" href="contact.html">Start a conversation %s</a>
      <a class="btn btn-outline-dark" href="mailto:%s">%s</a>
    </div>
  </div>
</section>""" % (ARROW, S["email"], S["email"])


def footer():
    work_links = "\n        ".join(
        '<li><a href="work-%s.html">%s</a></li>' % (c["slug"], esc(c["nav"]))
        for c in W.CATEGORIES)
    return """<footer class="site-footer">
  <div class="wrap-wide">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/img/brass-tack-logo-light.png" width="1500" height="404"
             alt="Brass Tack Communications" loading="lazy" decoding="async">
        <p>%s</p>
      </div>
      <div class="footer-col">
        <h2>Work</h2>
        <ul>
        %s
        </ul>
      </div>
      <div class="footer-col">
        <h2>Company</h2>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="mailto:%s">%s</a></li>
          <li><a href="tel:%s">%s</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; %s Brass Tack Communications. All rights reserved.</p>
      <address>%s, %s, %s %s</address>
    </div>
  </div>
</footer>
<script src="assets/js/site.js" defer></script>""" % (
        esc(S["footer_blurb"]), work_links, S["email"], S["email"],
        S["phone_href"], S["phone_display"], datetime.date.today().year,
        esc(S["street"]), S["city"], S["region"], S["postal"])


# ------------------------------------------------------------------ shell --
def page(filename, title, description, body, schema=None, og_image="assets/work/cover-video.webp"):
    url = BASE + "/" + ("" if filename == "index.html" else filename)
    blocks = ""
    if schema:
        for s in schema:
            blocks += ('\n<script type="application/ld+json">%s</script>'
                       % json.dumps(s, ensure_ascii=False, separators=(",", ":")))
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="author" content="Brass Tack Communications">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Brass Tack Communications">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(base)s/%(og)s">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(base)s/%(og)s">
<meta name="theme-color" content="#0F1012">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/css/site.css">%(schema)s
</head>
<body>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
</body>
</html>
""" % {"title": esc(title), "desc": esc(description), "url": url, "base": BASE,
       "og": og_image, "schema": blocks, "header": header(filename),
       "body": body, "footer": footer()}
    with open(os.path.join(HERE, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename


# ------------------------------------------------------------- structured --
ORG = {
    "@context": "https://schema.org",
    "@type": ["Organization", "ProfessionalService"],
    "@id": BASE + "/#organization",
    "name": S["name"],
    "alternateName": "Brass Tack",
    "url": BASE + "/",
    "logo": {"@type": "ImageObject", "url": BASE + "/assets/img/brass-tack-logo.png",
             "width": 1500, "height": 404},
    "image": BASE + "/assets/img/brass-tack-logo.png",
    "foundingDate": S["founded"],
    "slogan": "Putting words, ideas, and stories to work for your business",
    "description": ("Brass Tack Communications is a content and messaging shop that creates "
                    "crisp, creative, and effective messaging and copy for production "
                    "companies, ad agencies, graphic design firms, and corporations."),
    "email": S["email"],
    "telephone": S["phone_display"],
    "address": {"@type": "PostalAddress", "streetAddress": S["street"],
                "addressLocality": S["city"], "addressRegion": S["region"],
                "postalCode": S["postal"], "addressCountry": S["country"]},
    "areaServed": {"@type": "Country", "name": "United States"},
    "knowsAbout": ["Content strategy", "Messaging development", "Concept development",
                   "Copywriting", "Scriptwriting", "Ghostwriting", "White papers",
                   "Event content management", "Corporate speechwriting",
                   "Video scriptwriting", "Technical marketing content"],
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales",
                      "email": S["email"], "telephone": S["phone_display"],
                      "availableLanguage": "English"}],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Content services",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n,
                                               "description": d}}
            for n, d in C.SERVICES["items"]],
    },
}

WEBSITE = {
    "@context": "https://schema.org", "@type": "WebSite",
    "@id": BASE + "/#website", "url": BASE + "/", "name": S["name"],
    "publisher": {"@id": BASE + "/#organization"},
    "inLanguage": "en-US",
}


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n,
                 "item": BASE + "/" + ("" if u == "index.html" else u)}
                for i, (n, u) in enumerate(trail)]}


def video_schema(item, cat):
    v = item["video"]
    return {
        "@context": "https://schema.org", "@type": "VideoObject",
        "name": plain(item["title"]),
        "description": plain(" ".join(item["body"])),
        "thumbnailUrl": [BASE + "/assets/work/" + item["img"]],
        "uploadDate": v["uploaded"],
        "duration": v["duration"],
        "embedUrl": "https://player.vimeo.com/video/%s" % v["id"],
        "contentUrl": "https://vimeo.com/%s" % v["id"],
        "publisher": {"@id": BASE + "/#organization"},
        "creator": {"@id": BASE + "/#organization"},
        "isPartOf": {"@type": "CollectionPage", "@id": "%s/work-%s.html" % (BASE, cat["slug"])},
    }


def collection_schema(cat):
    items = []
    for i, it in enumerate(cat["items"]):
        node = {"@type": "CreativeWork", "position": i + 1,
                "name": plain(it["title"]),
                "description": plain(" ".join(it["body"])),
                "image": BASE + "/assets/work/" + it["img"],
                "creator": {"@id": BASE + "/#organization"}}
        if it["media"] == "video":
            node["@type"] = "VideoObject"
            node["embedUrl"] = "https://player.vimeo.com/video/%s" % it["video"]["id"]
            node["uploadDate"] = it["video"]["uploaded"]
            node["duration"] = it["video"]["duration"]
            node["thumbnailUrl"] = BASE + "/assets/work/" + it["img"]
        items.append(node)
    return {"@context": "https://schema.org", "@type": "CollectionPage",
            "@id": "%s/work-%s.html" % (BASE, cat["slug"]),
            "name": plain(cat["h1"]),
            "description": cat["meta"],
            "isPartOf": {"@id": BASE + "/#website"},
            "about": {"@id": BASE + "/#organization"},
            "mainEntity": {"@type": "ItemList", "numberOfItems": len(items),
                           "itemListElement": items}}


FAQ_SCHEMA = {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a}}
                   for q, a in C.FAQ],
}


# --------------------------------------------------------------- fragments --
def work_card(cat, priority=False):
    return """      <a class="work-card reveal" href="work-%s.html">
        <span class="work-card-media">
          <img src="assets/work/%s" alt="%s" width="1600" height="900"
               loading="%s" decoding="async" style="object-position:%s">
        </span>
        <span class="work-card-body">
          <span>
            <h3>%s</h3>
            <span class="work-card-note">%s</span>
          </span>
          <span class="work-card-arrow">%s</span>
        </span>
      </a>""" % (cat["slug"], cat["cover"], esc(cat["cover_alt"]),
                 "eager" if priority else "lazy", cat.get("pos", "50% 50%"),
                 cat["h1"], esc(cat["blurb"]), ARROW)


def logo_wall():
    cells = "\n      ".join(
        '<div class="logo-cell"><img src="assets/logos/%s" alt="%s logo" '
        'width="560" height="336" loading="lazy" decoding="async"></div>'
        % (f, esc(n)) for n, f in C.CLIENTS)
    return cells


def clock(iso):
    """PT1M29S -> 1:29 ; PT45S -> 0:45 ; PT6M -> 6:00"""
    m = re.match(r"PT(?:(\d+)M)?(?:(\d+)S)?$", iso)
    mins = int(m.group(1) or 0)
    secs = int(m.group(2) or 0)
    return "%d:%02d" % (mins, secs)


def media_block(item):
    """Either a still image or a click-to-play Vimeo facade."""
    if item["media"] == "video":
        v = item["video"]
        return """<div class="vid" data-src="https://player.vimeo.com/video/%s?h=%s&amp;app_id=122963"
             data-title="%s">
          <img src="assets/work/%s" alt="%s" width="1500" height="844"
               loading="lazy" decoding="async">
          <button class="vid-btn" type="button">
            <span class="vid-play">%s</span>
            <span class="sr-only">Play &ldquo;%s&rdquo;</span>
          </button>
          <span class="vid-time">%s</span>
        </div>
        <noscript><p><a class="tlink" href="https://vimeo.com/%s">Watch &ldquo;%s&rdquo; on Vimeo %s</a></p></noscript>""" % (
            v["id"], v["h"], esc(plain(item["title"])), item["img"], esc(item["alt"]),
            PLAY, esc(plain(item["title"])), clock(v["duration"]),
            v["id"], esc(plain(item["title"])), DIAG)
    return """<figure>
          <img src="assets/work/%s" alt="%s" width="1500" height="1000"
               loading="lazy" decoding="async">
        </figure>""" % (item["img"], esc(item["alt"]))


def pkg_grid(items):
    return "\n".join(
        """      <div class="pkg-card reveal">
        <h3>%s</h3>
        <p>%s</p>
        <p class="pkg-price">%s</p>
      </div>""" % (esc(n), esc(d), esc(pr)) for n, d, pr in items)


def links_block(item):
    out = []
    for label, href, external in item.get("links", []):
        attrs = ' target="_blank" rel="noopener"' if external else ""
        icon = DIAG if external else ARROW
        out.append('<a class="tlink" href="%s"%s>%s %s</a>' % (href, attrs, esc(label), icon))
    if not out:
        return ""
    return '\n        <div class="piece-actions">%s</div>' % "".join(out)


# ------------------------------------------------------------------ pages --
def build_home():
    cards = "\n".join(work_card(c, i < 2) for i, c in enumerate(W.CATEGORIES))
    svc = "\n".join(
        """    <li class="reveal">
      <div class="numlist-body">
        <h3>%s</h3>
        <p>%s</p>
      </div>
    </li>""" % (esc(n), esc(d)) for n, d in C.SERVICES["items"])
    ai = "\n        ".join("<p>%s</p>" % esc(p) for p in C.AI_SECTION["body"])

    body = """<section class="hero">
  <div class="wrap-wide">
    <h1>%(h1)s</h1>
    <div class="hero-foot">
      <p class="lead">%(lead)s</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="work.html">See the work %(arrow)s</a>
        <a class="btn btn-ghost" href="services.html">What we do</a>
      </div>
    </div>
  </div>
</section>

<section class="section-tight" aria-labelledby="work-h">
  <div class="wrap-wide">
    <div class="sec-head">
      <div class="sec-head-stack">
        <h2 id="work-h">Selected work</h2>
      </div>
      <a class="tlink" href="work.html">All work %(arrow)s</a>
    </div>
    <div class="work-grid">
%(cards)s
    </div>
  </div>
</section>

<section class="section band-dark" aria-labelledby="ai-h">
  <div class="wrap-wide">
    <div class="statement-grid">
      <h2 id="ai-h" class="reveal">%(ai_h2)s</h2>
      <div class="lead reveal">
        %(ai_body)s
      </div>
    </div>
  </div>
</section>

<section class="section-tight" aria-labelledby="clients-h">
  <div class="wrap-wide">
    <div class="sec-head">
      <div class="sec-head-stack"><h2 id="clients-h">%(clients_h2)s</h2></div>
    </div>
    <div class="logo-wall reveal">
      %(logos)s
    </div>
  </div>
</section>

<section class="section-tight" aria-labelledby="svc-h">
  <div class="wrap-wide">
    <div class="sec-head sec-head-col">
      <h2 id="svc-h">What we do</h2>
      <p class="lead">%(svc_lead)s</p>
      <a class="tlink" href="services.html">All services %(arrow)s</a>
    </div>
    <ol class="numlist">
%(svc)s
    </ol>
  </div>
</section>

%(cta)s""" % {
        "h1": mark(esc(C.HOME["h1"]), C.HOME["h1_mark"]),
        "lead": esc(C.HOME["lead"]),
        "arrow": ARROW, "cards": cards,
        "ai_h2": esc(C.AI_SECTION["h2"]), "ai_body": ai,
        "clients_h2": esc(C.HOME["clients_h2"]), "logos": logo_wall(),
        "svc_lead": esc(C.SERVICES["lead"]), "svc": svc, "cta": cta_band(),
    }

    return page("index.html",
                "Brass Tack Communications | Content Strategy, Messaging, and Copywriting",
                C.HOME["lead"], body,
                schema=[ORG, WEBSITE], og_image="assets/work/cover-video.webp")


def build_work_hub():
    cards = "\n".join(work_card(c, i < 2) for i, c in enumerate(W.CATEGORIES))
    body = """<section class="page-head">
  <div class="wrap-wide">
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">Work</li>
      </ol>
    </nav>
    <h1>%s</h1>
    <p class="lead" style="margin-top:24px">%s</p>
  </div>
</section>

<section class="section-tight" style="padding-top:0">
  <div class="wrap-wide">
    <div class="work-grid">
%s
    </div>
  </div>
</section>

%s""" % (esc(W.WORK_HUB["h1"]), esc(W.WORK_HUB["lead"]), cards, cta_band())

    listing = {"@context": "https://schema.org", "@type": "CollectionPage",
               "name": "Work | Brass Tack Communications",
               "description": W.WORK_HUB["lead"],
               "isPartOf": {"@id": BASE + "/#website"},
               "mainEntity": {"@type": "ItemList", "itemListElement": [
                   {"@type": "ListItem", "position": i + 1, "name": plain(c["h1"]),
                    "url": "%s/work-%s.html" % (BASE, c["slug"])}
                   for i, c in enumerate(W.CATEGORIES)]}}

    return page("work.html", "Work | Brass Tack Communications",
                W.WORK_HUB["lead"], body,
                schema=[listing, crumbs_schema([("Home", "index.html"), ("Work", "work.html")])],
                og_image="assets/work/" + W.CATEGORIES[0]["cover"])


def build_category(idx, cat):
    pieces = []
    for i, item in enumerate(cat["items"]):
        alt = " piece-alt" if i % 2 else ""
        pieces.append("""    <article class="piece%s reveal">
      <div class="piece-media">
        %s
      </div>
      <div class="piece-text">
        <h3>%s</h3>
        %s%s
      </div>
    </article>""" % (alt, media_block(item), cat_title(item),
                     "\n        ".join("<p>%s</p>" % esc(p) for p in item["body"]),
                     links_block(item)))

    prev_c = W.CATEGORIES[idx - 1] if idx > 0 else None
    nxt_c = W.CATEGORIES[idx + 1] if idx < len(W.CATEGORIES) - 1 else None
    pager = ""
    if prev_c or nxt_c:
        parts = []
        if prev_c:
            parts.append('<a class="prev" href="work-%s.html"><span class="dir">Previous</span>'
                         '<span class="ttl">%s</span></a>' % (prev_c["slug"], prev_c["h1"]))
        if nxt_c:
            parts.append('<a class="next" href="work-%s.html"><span class="dir">Next</span>'
                         '<span class="ttl">%s</span></a>' % (nxt_c["slug"], nxt_c["h1"]))
        pager = ('\n    <nav class="pager" aria-label="More work">%s</nav>'
                 '\n    <p class="pager-all"><a class="tlink" href="work.html">%s Back to all work</a></p>'
                 % ("".join(parts), BACK))

    body = """<section class="page-head">
  <div class="wrap-wide">
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li><a href="work.html">Work</a></li>
        <li aria-current="page">%s</li>
      </ol>
    </nav>
    <h1>%s</h1>
    <p class="lead" style="margin-top:24px">%s</p>
  </div>
</section>

<section class="section-tight" style="padding-top:0">
  <div class="wrap-wide">
%s%s
  </div>
</section>

%s""" % (cat["h1"], cat["h1"], esc(cat["blurb"]), "\n".join(pieces), pager, cta_band())

    schema = [collection_schema(cat),
              crumbs_schema([("Home", "index.html"), ("Work", "work.html"),
                             (plain(cat["h1"]), "work-%s.html" % cat["slug"])])]
    for item in cat["items"]:
        if item["media"] == "video":
            schema.append(video_schema(item, cat))

    return page("work-%s.html" % cat["slug"],
                "%s | Brass Tack Communications" % plain(cat["h1"]),
                cat["meta"], body, schema=schema,
                og_image="assets/work/" + cat["cover"])


def cat_title(item):
    return item["title"] if "&" in item["title"] else esc(item["title"])


def build_services():
    items = "\n".join(
        """    <li class="reveal">
      <div class="numlist-body">
        <h3>%s</h3>
        <p>%s</p>
      </div>
    </li>""" % (esc(n), esc(d)) for n, d in C.SERVICES["items"])

    body = """<section class="page-head">
  <div class="wrap-wide">
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">Services</li>
      </ol>
    </nav>
    <h1>%s</h1>
    <p class="lead" style="margin-top:24px">%s</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="contact.html">%s %s</a>
      <a class="btn btn-ghost" href="work.html">See the work</a>
    </div>
  </div>
</section>

<section class="section-tight" style="padding-top:0">
  <div class="wrap-wide">
    <ol class="numlist">
%s
    </ol>
  </div>
</section>

<section class="section-tight" aria-labelledby="pkg-h">
  <div class="wrap-wide">
    <div class="sec-head sec-head-col">
      <h2 id="pkg-h">%s</h2>
      <p class="lead">%s</p>
    </div>
    <div class="pkg-grid">
%s
    </div>
  </div>
</section>

<section class="section-tight band-alt" aria-labelledby="site-h">
  <div class="wrap-wide">
    <div class="sec-head sec-head-col">
      <h2 id="site-h">%s</h2>
      <p class="lead">%s</p>
    </div>
    <div class="pkg-grid">
%s
    </div>
  </div>
</section>

%s""" % (mark(esc(C.SERVICES["h1"]), "when you need it"), esc(C.SERVICES["lead"]),
         esc(C.SERVICES["cta"]), ARROW, items,
         esc(C.PACKAGES["h2"]), esc(C.PACKAGES["lead"]), pkg_grid(C.PACKAGES["items"]),
         esc(C.WEBSITES["h2"]), esc(C.WEBSITES["lead"]), pkg_grid(C.WEBSITES["items"]),
         cta_band())

    svc = {"@context": "https://schema.org", "@type": "WebPage",
           "name": "Services | Brass Tack Communications",
           "description": plain(C.SERVICES["lead"]),
           "isPartOf": {"@id": BASE + "/#website"},
           "about": {"@id": BASE + "/#organization"},
           "mainEntity": {"@type": "ItemList", "itemListElement": [
               {"@type": "ListItem", "position": i + 1,
                "item": {"@type": "Service", "name": n, "description": d,
                         "provider": {"@id": BASE + "/#organization"}}}
               for i, (n, d) in enumerate(C.SERVICES["items"])]},
           "hasPart": {"@type": "OfferCatalog", "name": "Packages",
                       "itemListElement": [
                           {"@type": "Offer",
                            "itemOffered": {"@type": "Service", "name": n,
                                            "description": d,
                                            "provider": {"@id": BASE + "/#organization"}},
                            "availability": "https://schema.org/InStock",
                            "priceSpecification": {"@type": "PriceSpecification",
                                                   "priceCurrency": "USD",
                                                   "description": pr}}
                           for n, d, pr in C.PACKAGES["items"] + C.WEBSITES["items"]]}}

    return page("services.html", "Services | Brass Tack Communications",
                plain(C.SERVICES["lead"])[:300], body,
                schema=[svc, crumbs_schema([("Home", "index.html"),
                                            ("Services", "services.html")])],
                og_image="assets/work/cover-collateral.webp")


def build_about():
    values = "\n".join(
        """      <div class="value-card reveal">
        <div class="value-rule" aria-hidden="true"></div>
        <h3>%s</h3>
        <p>%s</p>
      </div>""" % (esc(n), esc(d)) for n, d in C.ABOUT["values"])
    ai = "\n        ".join("<p>%s</p>" % esc(p) for p in C.AI_SECTION["body"])
    faq = "\n".join(
        """    <details%s>
      <summary>%s</summary>
      <div class="faq-a"><p>%s</p></div>
    </details>""" % (" open" if i == 0 else "", esc(q), esc(a))
        for i, (q, a) in enumerate(C.FAQ))

    body = """<section class="page-head">
  <div class="wrap-wide">
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">About</li>
      </ol>
    </nav>
    <h1>%(h1)s</h1>
    <p class="lead" style="margin-top:24px">%(lead)s</p>
  </div>
</section>

<section class="section-tight" style="padding-top:0" aria-labelledby="values-h">
  <div class="wrap-wide">
    <h2 id="values-h" style="font-size:clamp(1.35rem,2vw,1.75rem);margin-bottom:32px;max-width:46ch">%(values_h2)s</h2>
    <div class="value-grid">
%(values)s
    </div>
  </div>
</section>

<section class="section band-dark" aria-labelledby="ai-h">
  <div class="wrap-wide">
    <div class="statement-grid">
      <h2 id="ai-h" class="reveal">%(ai_h2)s</h2>
      <div class="lead reveal">
        %(ai_body)s
      </div>
    </div>
  </div>
</section>

<section class="section-tight" aria-labelledby="faq-h">
  <div class="wrap-wide">
    <div class="sec-head">
      <div class="sec-head-stack"><h2 id="faq-h">Common questions</h2></div>
    </div>
    <div class="faq">
%(faq)s
    </div>
  </div>
</section>

%(cta)s""" % {"h1": mark(esc(C.ABOUT["h1"]), C.ABOUT["h1_mark"]),
              "lead": esc(C.ABOUT["lead"]),
              "values_h2": esc(C.ABOUT["values_h2"]), "values": values,
              "ai_h2": esc(C.AI_SECTION["h2"]), "ai_body": ai,
              "faq": faq, "cta": cta_band()}

    about = {"@context": "https://schema.org", "@type": "AboutPage",
             "name": "About | Brass Tack Communications",
             "description": plain(C.ABOUT["lead"])[:300],
             "isPartOf": {"@id": BASE + "/#website"},
             "mainEntity": {"@id": BASE + "/#organization"}}

    return page("about.html", "About | Brass Tack Communications",
                plain(C.ABOUT["lead"])[:300], body,
                schema=[about, FAQ_SCHEMA,
                        crumbs_schema([("Home", "index.html"), ("About", "about.html")])],
                og_image="assets/work/cover-events.webp")


def build_contact():
    body = """<section class="page-head">
  <div class="wrap-wide">
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li aria-current="page">Contact</li>
      </ol>
    </nav>
  </div>
</section>

<section class="section-tight" style="padding-top:0">
  <div class="wrap-wide contact-grid">
    <div>
      <h1>%(h1)s</h1>
      <p class="lead" style="margin-top:24px">%(lead)s</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mailto:%(email)s">Email us %(arrow)s</a>
        <a class="btn btn-ghost" href="tel:%(tel)s">Call %(phone)s</a>
      </div>
    </div>
    <ul class="contact-list">
      <li>
        <span class="k">Email</span>
        <span class="v"><a href="mailto:%(email)s">%(email)s</a></span>
      </li>
      <li>
        <span class="k">Phone</span>
        <span class="v"><a href="tel:%(tel)s">%(phone)s</a></span>
      </li>
      <li>
        <span class="k">Mail</span>
        <span class="v"><address>%(street)s<br>%(city)s, %(region)s %(postal)s</address></span>
      </li>
    </ul>
  </div>
</section>""" % {"h1": esc(C.CONTACT["h1"]), "lead": esc(C.CONTACT["lead"]),
                 "email": S["email"], "tel": S["phone_href"],
                 "phone": S["phone_display"], "arrow": ARROW,
                 "street": esc(S["street"]), "city": S["city"],
                 "region": S["region"], "postal": S["postal"]}

    cp = {"@context": "https://schema.org", "@type": "ContactPage",
          "name": "Contact | Brass Tack Communications",
          "description": C.CONTACT["lead"],
          "isPartOf": {"@id": BASE + "/#website"},
          "mainEntity": {"@id": BASE + "/#organization"}}

    return page("contact.html", "Contact | Brass Tack Communications",
                "Learn more about what Brass Tack Communications can bring to your next "
                "project. Email todd@brass-tack.com or call +1 (801) 318-0191.", body,
                schema=[cp, ORG, crumbs_schema([("Home", "index.html"),
                                                ("Contact", "contact.html")])],
                og_image="assets/work/cover-articles.webp")


def build_404():
    body = """<section class="section" style="min-height:52vh;display:grid;place-items:center;text-align:center">
  <div class="wrap-wide">
    <h1>Page not found</h1>
    <p class="lead center" style="margin-top:20px">The page you were looking for
      isn&rsquo;t here. Try the work, or get in touch and we&rsquo;ll point you the right way.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary" href="work.html">See the work %s</a>
      <a class="btn btn-ghost" href="index.html">Back home</a>
    </div>
  </div>
</section>""" % ARROW
    return page("404.html", "Page not found | Brass Tack Communications",
                "That page could not be found.", body)


# --------------------------------------------------- robots / sitemap / llms --
AI_AGENTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User",
             "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User",
             "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot",
             "meta-externalagent", "Amazonbot", "DuckAssistBot", "cohere-ai",
             "YouBot", "Bytespider", "MistralAI-User"]


def build_robots():
    lines = ["# Brass Tack Communications",
             "# Search engines and AI assistants are all welcome here.", "",
             "User-agent: *", "Allow: /", ""]
    for a in AI_AGENTS:
        lines += ["User-agent: %s" % a, "Allow: /", ""]
    lines += ["Sitemap: %s/sitemap.xml" % BASE, ""]
    open(os.path.join(HERE, "robots.txt"), "w").write("\n".join(lines))
    return "robots.txt"


def build_sitemap(pages):
    prio = {"index.html": "1.0", "work.html": "0.9", "services.html": "0.9",
            "about.html": "0.8", "contact.html": "0.7"}
    rows = []
    for p in pages:
        if p == "404.html":
            continue
        loc = BASE + "/" + ("" if p == "index.html" else p)
        rows.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                    "    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n"
                    "  </url>" % (loc, TODAY, prio.get(p, "0.8")))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(HERE, "sitemap.xml"), "w").write(xml)
    return "sitemap.xml"


def build_llms():
    """llms.txt - a plain-language map of the site for AI assistants."""
    out = ["# Brass Tack Communications", ""]
    out.append("> %s" % C.HOME["lead"])
    out.append("")
    out.append("Brass Tack Communications is a content and messaging shop in %s, %s. "
               "It has been creating messaging and copy for production companies, ad "
               "agencies, graphic design firms, and corporations for more than 20 years, "
               "and has operated under the Brass Tack name since %s. Contact: %s, %s."
               % (S["city"], S["region"], S["founded"], S["email"], S["phone_display"]))
    out.append("")
    out.append("## Services")
    out.append("")
    for n, d in C.SERVICES["items"]:
        out.append("- **%s**: %s" % (n, d))
    out.append("")
    out.append("## Work")
    out.append("")
    for c in W.CATEGORIES:
        out.append("- [%s](%s/work-%s.html): %s" % (plain(c["h1"]), BASE, c["slug"], c["blurb"]))
        for it in c["items"]:
            out.append("  - %s. %s" % (plain(it["title"]), plain(" ".join(it["body"]))))
    out.append("")
    out.append("## Clients")
    out.append("")
    out.append(", ".join(n for n, _ in C.CLIENTS) + ".")
    out.append("")
    out.append("## Pages")
    out.append("")
    for label, href in [("Home", "index.html")] + list(C.NAV):
        out.append("- [%s](%s/%s)" % (label, BASE, "" if href == "index.html" else href))
    out.append("")
    out.append("## Frequently asked questions")
    out.append("")
    for q, a in C.FAQ:
        out.append("### %s" % q)
        out.append("")
        out.append(a)
        out.append("")
    open(os.path.join(HERE, "llms.txt"), "w", encoding="utf-8").write("\n".join(out))
    return "llms.txt"


def build_icons():
    """Small brass favicon drawn inline so there is no binary to manage."""
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="13" fill="#0F1012"/>'
           '<text x="32" y="45" font-family="Archivo,Helvetica,Arial,sans-serif" '
           'font-size="38" font-weight="700" fill="#F78F1E" text-anchor="middle">b</text>'
           '</svg>')
    open(os.path.join(HERE, "assets/img/favicon.svg"), "w").write(svg)
    return "assets/img/favicon.svg"


# ------------------------------------------------------------------- main --
def main():
    built = [build_home(), build_work_hub()]
    for i, cat in enumerate(W.CATEGORIES):
        built.append(build_category(i, cat))
    built += [build_services(), build_about(), build_contact(), build_404()]
    build_icons()
    extras = [build_robots(), build_sitemap(built), build_llms()]

    print("Built %d pages:" % len(built))
    for p in built:
        print("   ", p)
    print("Plus:", ", ".join(extras))


if __name__ == "__main__":
    main()
