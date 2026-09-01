# -*- coding: utf-8 -*-
"""
Portfolio content. Every title and description is VERBATIM from the original
brass-tack.com portfolio pages, including original punctuation.

Item keys:
  title    heading shown for the piece
  body     list of paragraphs
  media    "image" or "video"
  img      file in assets/work/
  alt      image alt text (NEW - written for accessibility + AI/image search)
  video    {id, duration, uploaded, name} for Vimeo pieces
  links    list of (label, href, is_external)
  wide     True renders the piece full width instead of two columns
"""

F = "assets/files/"

CATEGORIES = [
    {
        "slug": "video",
        "nav": "Video",
        "h1": "Video",
        "cover": "cover-video.webp",
        "cover_alt": "Frame from a Brass Tack scripted brand video",
        "blurb": "Scripts and story direction for brand films, explainers, customer stories, "
                 "and social video.",  # NEW
        "meta": "Video scripting and story direction by Brass Tack Communications for "
                "Publicis Sapient, Malwarebytes, Neumont College, SUSE, the University of "
                "Utah, and Rio Tinto.",  # NEW
        "items": [
            {
                "title": "Publicis Sapient + Adobe overview",
                "body": ["How do you tell a customer success story when you can’t name the "
                         "customer? Here’s one idea."],
                "media": "video", "img": "poster-publicis-sapient.webp",
                "alt": "Title frame from the Publicis Sapient and Adobe customer story video",
                "video": {"id": "473235199", "h": "ea96187d0c", "duration": "PT1M29S",
                          "uploaded": "2020-10-28", "name": "Publicis Sapient + Adobe overview"},
            },
            {
                "title": "Malwarebytes 2022 Threat Review teasers",
                "body": ["This series of three short social videos highlights key findings from "
                         "Malwarebytes’ 2022 Threat Review and encourages viewers to download "
                         "the report."],
                "media": "video", "img": "poster-malwarebytes-teasers.webp",
                "alt": "Animated Malwarebytes 2022 Threat Review social teaser reading "
                       "“There used to be three big headaches”",
                "video": {"id": "720431362", "h": "b64672084d", "duration": "PT45S",
                          "uploaded": "2022-06-14",
                          "name": "Malwarebytes 2022 Threat Review teasers"},
            },
            {
                "title": "Neumont College of Computer Science promo",
                "body": ["Sometimes, it’s better to let people tell their own stories in their "
                         "own words (with a bit of expert direction). This piece weaves "
                         "perspectives from Neumont faculty, staff, and students into an "
                         "authentic story about who they are and the experience they offer."],
                "media": "video", "img": "poster-neumont.webp",
                "alt": "Neumont College of Computer Science logo over a Salt Lake City skyline",
                "video": {"id": "236423254", "h": "0099bb50dd", "duration": "PT2M59S",
                          "uploaded": "2017-10-02",
                          "name": "Neumont College of Computer Science promo"},
            },
            {
                "title": "SUSE Embedded explainer",
                "body": ["Describing complex technical products and concepts with approachable, "
                         "conversational, jargon-free language is deceptively difficult. It’s "
                         "also what we do best."],
                "media": "video", "img": "poster-suse.webp",
                "alt": "Illustrated connected devices from the SUSE Embedded explainer video",
                "video": {"id": "208531122", "h": "4a640d4409", "duration": "PT2M13S",
                          "uploaded": "2017-03-15", "name": "SUSE Embedded explainer"},
            },
            {
                "title": "University of Utah Arts Pass explainer",
                "body": ["Ambitious goals and a limited budget gave us the perfect opportunity "
                         "to get creative and have some fun with this video promoting the "
                         "University of Utah Arts Pass."],
                "media": "video", "img": "poster-arts-pass.webp",
                "alt": "Silhouetted musicians on a red background with the words "
                       "“You might never forget”",
                "video": {"id": "164493566", "h": "5b42ac2c19", "duration": "PT2M4S",
                          "uploaded": "2016-04-27",
                          "name": "University of Utah Arts Pass explainer"},
            },
            {
                "title": "Rio Tinto educational video",
                "body": ["Rio Tinto has been using this award-winning video—which describes the "
                         "process of turning raw copper ore into useful products—in classrooms "
                         "and at their visitor’s center for more than 8 years."],
                "media": "video", "img": "poster-rio-tinto.webp",
                "alt": "Title card reading “From Ore to More: The Story of Copper”",
                "video": {"id": "164493151", "h": "6322381483", "duration": "PT6M",
                          "uploaded": "2016-04-27", "name": "Rio Tinto educational video"},
            },
        ],
    },
    {
        "slug": "articles",
        "pos": "50% 12%",
        "nav": "Articles, white papers, and e-books",
        "h1": "Articles, white papers, &amp; e-books",
        "cover": "cover-articles.webp",
        "cover_alt": "Spread from a Brass Tack white paper",
        "blurb": "Long-form thought leadership that makes technical subject matter readable.",
        "meta": "Ghostwritten white papers, e-books, and thought leadership articles by "
                "Brass Tack Communications for Lucem Health, Broadcom, and RizePoint.",
        "items": [
            {
                "title": "Lucem Health White Papers",
                "body": ["Are you looking to make highly technical content more relevant and "
                         "approachable for a broader audience? Here are two examples of how "
                         "Brass Tack accomplished that goal for Lucem Health:"],
                "media": "image", "img": "art-lucem.webp",
                "alt": "Cover pages of two Lucem Health white papers on AI in healthcare",
                "links": [
                    ("Five Key Challenges that Are Slowing the Progress of AI in Healthcare",
                     F + "Lucem-White-Paper_Five-Key-Challenges.pdf", False),
                    ("Challenge Accepted: Turning AI’s Massive Potential into Real Healthcare Value",
                     F + "Lucem-Health_Challenge-Accepted_WP_Aug23.pdf", False),
                ],
            },
            {
                "title": "Broadcom e-book",
                "body": ["This long-form e-book highlights important security considerations as "
                         "businesses move more of their systems and content to the cloud—and "
                         "outlines best practices for “rethinking security for the cloud "
                         "generation.”"],
                "media": "image", "img": "art-broadcom.webp",
                "alt": "Interior spread of the Broadcom cloud security e-book",
                "links": [("View the complete e-book",
                           "https://www.broadcom.com/info/symantec/eight-essentials-cloud-generation-ebook",
                           True)],
            },
            {
                "title": "RizePoint white paper",
                "body": ["How do you create and maintain consistent, unified brand experiences "
                         "and impressions across different geographies, facilities, and "
                         "cultures? This thought leadership white paper explores the answers."],
                "media": "image", "img": "art-rizepoint.webp",
                "alt": "Cover of the RizePoint brand building white paper",
                "links": [("View the complete paper", F + "RizePoint_BrandBldgWP.pdf", False)],
            },
        ],
    },
    {
        "slug": "collateral",
        "pos": "50% 8%",
        "nav": "Collateral",
        "h1": "Online and Print Collateral",
        "cover": "cover-collateral.webp",
        "cover_alt": "Printed info sheet written by Brass Tack",
        "blurb": "Info sheets, datasheets, brochures, and infographics that make a complicated "
                 "product easy to understand.",
        "meta": "Info sheets, datasheets, brochures, and infographics written by Brass Tack "
                "Communications for Cybersource, Malwarebytes, and NetDocuments.",
        "items": [
            {
                "title": "Cybersource Decision Manager info sheet",
                "body": ["This approachable, visual info sheet focuses on showcasing the "
                         "business value of a highly technical product in clear, conversational "
                         "language."],
                "media": "image", "img": "print-cybersource-dm.webp",
                "alt": "Two-page Cybersource Decision Manager info sheet",
                "links": [("View the full info sheet",
                           F + "DecisionManager_Info-sheet_two-page.pdf", False)],
            },
            {
                "title": "Malwarebytes infographic",
                "body": ["This short scrolling info graphic makes key findings of Malwarebytes "
                         "2022 Threat Review clear and relatable."],
                "media": "image", "img": "print-malwarebytes-infographic.webp",
                "alt": "Malwarebytes 2022 Threat Review scrolling infographic",
                "links": [("View the full infographic",
                           F + "MWB_ThreatRevew2022_GeneralInfographic_FINAL.pdf", False)],
            },
            {
                "title": "NetDocuments solution  brochure",
                "body": ["This longer-form print brochure places NetDocuments’ full family of "
                         "solutions in the context of the comprehensive “Work Inspired” "
                         "campaign Brass Tack developed."],
                "media": "image", "img": "print-netdocuments.webp",
                "alt": "Pages from the NetDocuments Work Inspired solution brochure",
                "links": [("View the full brochure",
                           F + "NetDocuments-Product-Brochure-REV06.pdf", False)],
            },
            {
                "title": "Cybersource datasheet",
                "body": ["This datasheet uses simple, approachable, (mostly) non-jargon filled "
                         "language to highlight the capabilities of a particularly complex and "
                         "technical product."],
                "media": "image", "img": "print-cybersource-datasheet.webp",
                "alt": "Cybersource Flex Microform datasheet",
                "links": [("View the full datasheet",
                           F + "CyberSource_DataSheet_FlexMicroform_v1.pdf", False)],
            },
        ],
    },
    {
        "slug": "advertising",
        "pos": "50% 6%",
        "nav": "Advertising",
        "h1": "Advertising",
        "cover": "cover-advertising.webp",
        "cover_alt": "Advertising campaign artwork written by Brass Tack",
        "blurb": "Brand-level campaigns that run across print, web, social, and video.",
        "meta": "Advertising and brand awareness campaign copy by Brass Tack Communications, "
                "including the NetDocuments “Work Inspired” campaign and Legends Motorcycle.",
        "items": [
            {
                "title": "NetDocuments “Work Inspired” campaign",
                "body": ["This broad, brand-level awareness campaign combined print, web, "
                         "social, video, and more to show how NetDocuments document and email "
                         "management tools can unlock legal professionals’ best, most inspired "
                         "work."],
                "media": "image", "img": "ad-netdocuments.webp",
                "alt": "NetDocuments Work Inspired campaign ads and web pop-ups",
                "links": [("View the website",
                           "https://www.netdocuments.com/solutions/document-knowledge-management/", True)],
            },
            {
                "title": "Legends Motorcycle campaign",
                "body": ["This campaign tapped into the spirit that fuels millions of people’s "
                         "passion for vintage motorcycles for a company that makes custom, "
                         "high-end chrome and leather accessories for Harley Davidson bikes."],
                "media": "image", "img": "ad-legends.webp",
                "alt": "Legends Motorcycle print advertisement",
                "links": [("Read more copy", F + "legends3.png", False)],
            },
        ],
    },
    {
        "slug": "events",
        "nav": "Events",
        "h1": "Events",
        "cover": "cover-events.webp",
        "cover_alt": "Conference general session stage produced with Brass Tack content",
        "blurb": "General sessions, theater presentations, and virtual conferences, written "
                 "and content-managed end to end.",
        "meta": "Live and virtual event content by Brass Tack Communications for Malwarebytes "
                "at RSA Conference, DigiCert, Ivanti Interchange, Veritas Vision, and Symantec.",
        "items": [
            {
                "title": "Malwarebytes 2022 RSA Conference theater presentation",
                "body": ["How do you draw the right people into your booth, get them excited "
                         "about your #NODRAMA cybersecurity story, and convert them into "
                         "qualified leads—all in a noisy, intense, and highly-competitive expo "
                         "environment? At the 2022 RSA Conference, Brass Tack did all three "
                         "with an engaging, relevant, and dynamic live theater presentation "
                         "that played a key role in helping Malwarebytes exceed all of their "
                         "lead targets and engagement goals."],
                "media": "image", "img": "events-malwarebytes-rsa.webp",
                "alt": "Malwarebytes #NODRAMA booth theater presentation at RSA Conference 2022",
            },
            {
                "title": "DigiCert Virtual Security Summit 2022",
                "body": ["As we all know, virtual events suddenly became a thing in 2020, as "
                         "businesses were forced to quickly pivot from large in-person events "
                         "to virtual conferences in the face of the COVID-19 pandemic. Brass "
                         "Tack worked with Event Marketing Partners to make sure “virtual” did "
                         "NOT equal “stale and boring” with a polished, fast-paced, "
                         "highly-produced virtual production that overcame two years of Zoom "
                         "fatigue with compelling content and a uniquely engaging and visual "
                         "user experience."],
                "media": "image", "img": "events-digicert.webp",
                "alt": "DigiCert Virtual Security Summit 2022 broadcast set",
            },
            {
                "title": "Ivanti Interchange",
                "body": ["All too often, general sessions at corporate conferences turn into a "
                         "stale parade of talking heads that no amount of expensive lighting, "
                         "staging, graphics and production can rescue. At Ivanti Interchange, "
                         "Brass Tack turned this convention on its head with a fresh late night "
                         "talk show format that featured a live band, short segments, and "
                         "plenty of entertainment. The result was a week of highly-rated "
                         "general sessions that brought Ivanti’s story to life in a memorable "
                         "and approachable way."],
                "media": "image", "img": "events-ivanti.webp",
                "alt": "Late night talk show style general session stage at Ivanti Interchange",
            },
            {
                "title": "Veritas Vision",
                "body": ["For years, Brass Tack worked with Veritas to imagine, write, and "
                         "produce fresh, innovative general sessions that kept audiences "
                         "interested and engaged—and presented their company vision and story "
                         "in unexpected ways."],
                "media": "image", "img": "events-veritas.webp",
                "alt": "Veritas Vision conference general session stage",
            },
            {
                "title": "Symantec RSA theater presentation",
                "body": ["This fun, fast-paced in-theater game experience drew huge crowds, "
                         "delighted the audience, and brought Symantec’s cybersecurity story to "
                         "life."],
                "media": "video", "img": "events-symantec.webp",
                "alt": "Symantec game show style theater presentation at RSA Conference",
                "video": {"id": "720820700", "h": "4bec7bb16a", "duration": "PT42S",
                          "uploaded": "2022-06-15",
                          "name": "Symantec RSA theater presentation"},
            },
        ],
    },
    {
        "slug": "web",
        "nav": "Web",
        "h1": "Web",
        "cover": "cover-web.webp",
        "cover_alt": "Web page written by Brass Tack",
        "blurb": "Product pages and ghostwritten blog programs that keep a site working.",
        "meta": "Web copy and ghostwritten blog posts by Brass Tack Communications for "
                "Cybersource and Lucidworks.",
        "items": [
            {
                "title": "Cybersource Token Management Service web page",
                "body": ["This product overview page highlights the benefits and capabilities "
                         "of Cybersource’s innovative tokenization solution."],
                "media": "image", "img": "web-cybersource.webp",
                "alt": "Cybersource Token Management Service product overview web page",
                "links": [("View the page",
                           "https://www.cybersource.com/en-us/solutions/payment-acceptance/token-management-service.html",
                           True)],
            },
            {
                "title": "Lucidworks Blog Posts",
                # Original site read "a steady stream fresh insights" (missing "of").
                # Corrected on Andrew's instruction, 2026-09-01. Otherwise verbatim.
                "body": ["Brass Tack helped Lucidworks add a steady stream of fresh insights "
                         "to their website with a series of ghostwritten thought leadership "
                         "blog posts."],
                "media": "image", "img": "web-lucidworks.webp",
                "alt": "Lucidworks blog post ghostwritten by Brass Tack",
                "links": [
                    ("What Do Search Abandonment and ChatGPT Have in Common?",
                     F + "What-Do-Search-Abandonment-and-ChatGPT-Have-in-Common-Lucidworks.pdf",
                     False),
                    ("4 Emerging AI Trends in Retail",
                     F + "4-Emerging-AI-Trends-in-Retail-Lucidworks.pdf", False),
                ],
            },
        ],
    },
]

# NEW - intro for the Work hub page
WORK_HUB = {
    "h1": "Work",
    "lead": "A selection of the video, writing, collateral, campaign, event, and web work "
            "Brass Tack has produced for clients across technology, healthcare, finance, "
            "and education.",
}
