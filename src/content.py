# -*- coding: utf-8 -*-
"""
All site copy lives here.

RULE: everything marked VERBATIM is lifted word-for-word from the original
brass-tack.com and must not be edited (including its original punctuation
and the occasional typo). Anything marked NEW was written to fill a gap in
the new layout and is safe to change.
"""

SITE = {
    "name": "Brass Tack Communications",
    "domain": "https://www.brass-tack.com",
    "email": "todd@brass-tack.com",
    "phone_display": "+1 (801) 318-0191",
    "phone_href": "+18013180191",
    "street": "37 W. 200 S., #352",
    "city": "Salt Lake City",
    "region": "UT",
    "postal": "84101",
    "country": "US",
    "founded": "2011",
    # NEW - footer blurb
    "footer_blurb": "Content strategy, messaging, copywriting, and scriptwriting "
                    "for companies and creative agencies. Based in Salt Lake City, Utah.",
}

NAV = [
    ("Work", "work.html"),
    ("Services", "services.html"),
    ("About", "about.html"),
    ("Contact", "contact.html"),
]

# --------------------------------------------------------------------------
# HOME  (all VERBATIM unless noted)
# --------------------------------------------------------------------------
HOME = {
    "h1": "Putting words, ideas, and stories to work for your business",
    # the phrase given the brass underline in the H1
    "h1_mark": "your business",
    "lead": "Brass Tack Communications has been creating crisp, creative, and effective "
            "messaging and copy for production companies, ad agencies, graphic design firms, "
            "and corporations for more than 20 years. We’re ready to do the same for you.",
    "clients_h2": "Clients",
}

# NEW - the "professional writing in the age of AI" section.
# No em dashes in new copy, per Andrew. Todd's original copy keeps its own.
AI_SECTION = {
    "h2": "In the age of AI, quality control matters more than ever.",
    "body": [
        "It has never been easier to produce a large volume of content, or harder to "
        "produce content worth reading.",
        "We use AI where it earns its place, for research, early drafts, and structure. "
        "Everything is then directed, revised, and cross-checked by an experienced human, "
        "because judgment is what decides whether any of it is worth reading.",
        "We build in responsible AI search optimization too, so your content is found, "
        "read, and cited correctly by the assistants people now search with. Strong "
        "writing first, everything else in service of it.",
    ],
}

# --------------------------------------------------------------------------
# CLIENTS  (logo wall, alphabetical)
# --------------------------------------------------------------------------
CLIENTS = [
    ("Broadcom", "broadcom.webp"),
    ("Commvault", "commvault.webp"),
    ("Cybersource", "cybersource.webp"),
    ("DFIN", "dfin.webp"),
    ("DigiCert", "digicert.webp"),
    ("Event Marketing Partners", "event-marketing-partners.webp"),
    ("Gantry", "gantry.webp"),
    ("Henry Schein", "henry-schein.webp"),
    ("Ivanti", "ivanti.webp"),
    ("Malwarebytes", "malwarebytes.webp"),
    ("Micro Focus", "micro-focus.webp"),
    ("Optum Financial", "optum-financial.webp"),
    ("Publicis Sapient", "publicis-sapient.webp"),
    ("Red Rider", "red-rider.webp"),
    ("ServiceNow", "servicenow.webp"),
]

# --------------------------------------------------------------------------
# SERVICES  (VERBATIM)
# --------------------------------------------------------------------------
SERVICES = {
    "h1": "Skill, creativity, and experience when you need it",
    "lead": "Whether it’s developing a detailed messaging framework for a full brand "
            "awareness campaign, creating a detailed production script for your next user "
            "conference general session, or ghostwriting a short blog article, Brass Tack has "
            "the skills and experience to complement and enhance your internal content and "
            "marketing teams. Check out the range of content  services we offer and contact "
            "us to learn more.",
    "cta": "Let’s chat",
    "items": [
        ("Content strategy",
         "Brass Tack is prepared to work with your team to build the kinds of sound, "
         "thoughtful, and cohesive content and messaging strategies that lead to successful "
         "outcomes."),
        ("Messaging development",
         "Every successful product launch, campaign, or program starts with a strong, unified "
         "messaging foundation that feeds and informs every deliverable. Brass Tack can help "
         "you build messaging structures and frameworks that communicate the right story, the "
         "right way, to the right audience."),
        ("Concept development",
         "Content strategy and messaging define your story. A strong creative concept brings "
         "it to life, gives it a personality, and makes it real and compelling for your "
         "audience. Brass Tack works with trusted design and production partners to create "
         "memorable creative concepts that make an impression and get results."),
        ("Copywriting and scriptwriting",
         "You can always count on Brass Tack to write crisp, compelling, and professional copy "
         "that captures your brand voice, relates to your audience, and clearly communicates "
         "the right message—from short-form ad copy, web content, and video scripts to "
         "longer-form blog articles, e-books, and white papers."),
        ("Event content management",
         "Live and virtual conferences often feature dozens of speakers sharing content and "
         "engaging with audiences in general sessions, breakouts, and other activities. Brass "
         "Tack will make sure they’re prepared to represent your brand well and tell an "
         "authentic story in a clear, cohesive, and professional way."),
        ("Onsite support",
         "Successful events are defined by relevant and engaging content. We’ll help make "
         "sure your executives and subject matter experts deliver—with onsite scripting, "
         "speaker coaching, speaker management, and other content-related services."),
    ],
}

# --------------------------------------------------------------------------
# PACKAGES  (NEW - concrete deliverables and pricing placeholders.
#            Every price line is a placeholder for Todd to replace.)
# --------------------------------------------------------------------------
PACKAGES = {
    "h2": "What you can hire us to do",
    "framer": "What you actually get.",
    "lead": "Most engagements start as one of these. Every one is scoped to the project, "
            "so the number depends on length, complexity, and how much of the work is "
            "yours to hand over.",
    # Each package maps 1:1 to a portfolio category, so the card can show real
    # work and link straight to it.
    "items": [
        {"name": "Video scripts and story direction",
         "desc": "Concept, script, and story direction for brand films, explainers, "
                 "customer stories, and social video. From a thirty-second teaser to a "
                 "six-minute feature.",
         "price": "Pricing available upon request",
         "work": "video", "cover": "cover-video.webp", "pos": "50% 50%",
         "alt": "Frame from a Brass Tack scripted brand video"},
        {"name": "Articles, white papers, and e-books",
         "desc": "Ghostwritten long-form content, from research and subject matter "
                 "interviews through drafting and revisions, published under your byline "
                 "or your executive’s.",
         "price": "Priced per piece, quote available upon request",
         "work": "articles", "cover": "cover-articles.webp", "pos": "50% 12%",
         "alt": "Spread from a Brass Tack white paper"},
        {"name": "Online and print collateral",
         "desc": "Info sheets, datasheets, brochures, and infographics that make a "
                 "complicated product easy to understand and easy to hand to a customer.",
         "price": "Pricing available upon request",
         "work": "collateral", "cover": "cover-collateral.webp", "pos": "50% 8%",
         "alt": "Printed info sheet written by Brass Tack"},
        {"name": "Web copy and blog programs",
         "desc": "Product and solution pages, site sections, and a steady stream of "
                 "ghostwritten thought leadership on a schedule you can count on.",
         "price": "Per project or monthly retainer, quote available upon request",
         "work": "web", "cover": "cover-web.webp", "pos": "50% 50%",
         "alt": "Web page written by Brass Tack"},
        # renamed from "Event content management" so it no longer collides
        # word-for-word with the service of that name above
        {"name": "Live and virtual event content",
         "desc": "General sessions, theater presentations, and virtual conferences, "
                 "scripted and content-managed end to end, with speaker coaching and "
                 "onsite support.",
         "price": "Scoped per event, quote available upon request",
         "work": "events", "cover": "cover-events.webp", "pos": "50% 50%",
         "alt": "Conference general session stage produced with Brass Tack content"},
        {"name": "Advertising campaigns",
         "desc": "Concept and copy for brand-level campaigns that run across print, web, "
                 "social, and video, built on a messaging foundation that holds the whole "
                 "thing together.",
         "price": "Pricing available upon request",
         "work": "advertising", "cover": "cover-advertising.webp", "pos": "50% 6%",
         "alt": "Advertising campaign artwork written by Brass Tack"},
    ],
}

# NEW - the website offering, featured separately because it is new.
WEBSITES = {
    "h2": "Websites, designed and built",
    "new": True,          # renders the small brass "New" marker beside the heading
    "lead": "A new offering. Sites built with AI in the loop and structured so both search "
            "engines and AI assistants can read, understand, and cite them correctly. Then "
            "reviewed and revised line by line by a human, because that is the part that "
            "decides whether any of it is worth reading. This site was built exactly that way.",
    "items": [
        {"name": "Design only",
         "desc": "A complete top-to-bottom design for your site: structure, page-by-page "
                 "layout, and the words that go in them. Hand it to whoever builds it.",
         "price": "$3,000"},
        {"name": "Build and handoff",
         "desc": "We design it, build it, and hand you the finished site along with "
                 "everything it runs on. It is yours to host, own, and change whenever "
                 "you like.",
         "price": "$5,000"},
        {"name": "Ongoing care and content",
         "desc": "Everything in the handoff option, plus we keep it running: updates, new "
                 "pages, fresh content, fixes, and continued search and AI optimization as "
                 "things change.",
         "price": "$250/month"},
    ],
}

# NEW - framer for the (verbatim) six services, now shown as expandable cards
CAPABILITIES = {
    "h2": "What we do",
    "framer": "How the work gets done.",
}

# --------------------------------------------------------------------------
# ABOUT  (VERBATIM)
# --------------------------------------------------------------------------
ABOUT = {
    "h1": "Your story is powerful. Tell it the right way.",
    "h1_mark": "the right way",
    "lead": "Since 2011, Brass Tack Communications has worked with dozens of companies and "
            "creative agencies to develop smart content strategies, build effective messaging "
            "foundations, and apply the full power of strong writing and effective "
            "storytelling to a diverse range of projects and deliverables. Find out how we can "
            "bring the perfect blend of talent, creativity, experience, and professionalism to "
            "your next project.",
    "values_h2": "When you work with Brass Tack, you always get a team that is:",
    "values": [
        ("Skilled",
         "Our team is made up exclusively of content creators with backgrounds as agency "
         "copywriters, creative directors, corporate speechwriters, social marketers, and live "
         "presenters. We understand the specialized nuances of corporate content creation, so "
         "we can step in and add value to your team immediately."),
        ("Experienced",
         "At Brass Tack, there are no junior writers. Every member of the team has years (or "
         "decades) of experience developing creative, effective, professional content that "
         "matches your brand voice and gets results."),
        ("Easy",
         "We’re a small, specialized shop that focuses exclusively on content, messaging, "
         "and writing—without all the usual layers of business development teams, account "
         "managers, and other peripheral departments standing between you and the content "
         "services you need. That means your team always works directly with the person or "
         "team actually doing the work."),
    ],
}

# --------------------------------------------------------------------------
# CONTACT  (VERBATIM)
# --------------------------------------------------------------------------
CONTACT = {
    "h1": "Contact Us",
    "lead": "Learn more about what we can bring to your next project.",
}

# --------------------------------------------------------------------------
# FAQ  (NEW - written only from facts already stated elsewhere on the site.
#       Included because AI search engines lean heavily on Q&A structure.)
# --------------------------------------------------------------------------
FAQ = [
    ("What does Brass Tack Communications do?",
     "Brass Tack Communications is a content and messaging shop that creates crisp, creative, "
     "and effective messaging and copy for production companies, ad agencies, graphic design "
     "firms, and corporations. Services include content strategy, messaging development, "
     "concept development, copywriting and scriptwriting, event content management, and "
     "onsite event support."),
    ("How long has Brass Tack Communications been in business?",
     "Brass Tack Communications has been creating messaging and copy for more than 20 years, "
     "and has worked with dozens of companies and creative agencies under the Brass Tack name "
     "since 2011."),
    ("What kinds of content does Brass Tack write?",
     "Everything from short-form ad copy, web content, and video scripts to longer-form blog "
     "articles, e-books, and white papers, plus production scripts and general session content "
     "for live and virtual events."),
    ("Who does Brass Tack Communications work with?",
     "Clients have included ServiceNow, Ivanti, Malwarebytes, DigiCert, Commvault, Broadcom, "
     "Cybersource, Optum Financial, Publicis Sapient, Henry Schein, DFIN, Micro Focus, Red "
     "Rider, Gantry, and Event Marketing Partners."),
    ("How is Brass Tack different from a larger agency?",
     "Brass Tack is a small, specialized shop that focuses exclusively on content, messaging, "
     "and writing, without the usual layers of business development teams and account managers "
     "standing between you and the work. There are no junior writers, and your team always "
     "works directly with the person or team actually doing the work."),
    ("Why does professional writing still matter in the age of AI?",
     "It has never been easier to produce a large volume of content, or harder to produce "
     "content worth reading. Brass Tack uses AI where it earns its place, for research, "
     "early drafts, and structure, then directs, revises, and cross-checks everything with "
     "an experienced human. Responsible AI search optimization is built in, so the content "
     "is found, read, and cited correctly by the assistants people now search with."),
    ("Where is Brass Tack Communications located?",
     "Brass Tack Communications is located at 37 W. 200 S., #352, Salt Lake City, UT 84101. "
     "You can reach the team at todd@brass-tack.com or +1 (801) 318-0191."),
]
