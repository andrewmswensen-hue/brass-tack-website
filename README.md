# Brass Tack Communications — new website

**Live preview:** <https://andrewmswensen-hue.github.io/brass-tack-website/>
**Repo:** <https://github.com/andrewmswensen-hue/brass-tack-website>

Send your dad the preview link. It is the real site, fully working, just parked
at a temporary address until you point `brass-tack.com` at it.

Everything in this folder **is** the website. There is nothing to install.

---

## Updating the live preview

Make your change, rebuild, then push. The preview updates itself in about a minute.

```bash
cd ~/Documents/Claude/Projects/brass-tack-website && python3 build.py && git add -A && git commit -m "Update copy" && git push
```

---

## Look at it on your Mac

Double-click `index.html`. It opens in your browser and every page, link, and
video works.

If you'd rather see it exactly the way a real web server would serve it, open
Terminal, paste this, then visit <http://localhost:8777> in your browser:

```bash
cd ~/Documents/Claude/Projects/brass-tack-website && python3 -m http.server 8777
```

Press `Control + C` in Terminal when you're done.

---

## Put it online

Every page is a plain file, so this works on essentially any host. The two
easiest, both free for a site this size:

**Netlify (drag and drop, no account setup beyond signing in)**
1. Go to <https://app.netlify.com/drop>
2. Drag this whole `brass-tack-website` folder onto the page
3. It gives you a live URL in about ten seconds
4. Point `brass-tack.com` at it from Netlify's "Domain settings"

**Cloudflare Pages** works the same way and is also free.

Whichever you pick, the site will be faster than the old Squarespace version
because there's no page builder loading in the background.

> **About the preview address:** every page tells Google its "real" home is
> `https://www.brass-tack.com`, so the preview will not compete with the live
> site in search results. That is the correct setting for launch too, so nothing
> needs changing when you flip the domain over.
>
> One thing to do after it's live: the addresses inside `sitemap.xml`,
> `llms.txt`, and each page's "canonical" tag all assume the final home is
> `https://www.brass-tack.com`. If it lands somewhere else, change `domain` at
> the top of `src/content.py` and run `python3 build.py` again.

---

## Change the words

All the copy lives in two files you can open in any text editor:

- `src/content.py` — home, about, services, contact, the client list, the FAQ
- `src/work.py` — the 22 portfolio pieces

Edit the text between the quotes, save, then run this once:

```bash
cd ~/Documents/Claude/Projects/brass-tack-website && python3 build.py
```

That rewrites all the pages, the sitemap, and the AI file with your changes.
You never edit the `.html` files directly, because `build.py` overwrites them.

Anything marked `VERBATIM` in those files came straight off the old site and was
kept word for word. Anything marked `NEW` was written for this rebuild.

---

## What was added that wasn't on the old site

Todd's original words are all still here, unchanged. These pieces are new,
written to match his voice:

1. **"In the age of AI, quality control matters more than ever."** — a short
   section on the home and about pages. It makes the AI-slop point without using
   the word: every piece of work is written by a human, revised by a human, and
   cross-checked by a human, with responsible AI search optimization layered in
   on top. Makes the quality argument *and* explains the technical work in the
   same breath.
2. **Seven FAQs** on the About page. Every answer is assembled from facts already
   stated elsewhere on the site. AI assistants lean heavily on question-and-answer
   structure, so this is one of the highest-leverage things on the site.
3. **One-line descriptions** for each of the six work categories, so the cards on
   the home page say something instead of just showing a picture.
4. **Alt text** for all 40+ images, page titles, and search descriptions.

A note on punctuation: Todd's original copy uses em dashes and every one of
them is preserved. New copy written for this rebuild does not add any. So the
voice stays his, without spreading a habit into sentences he didn't write.

---

## Things worth mentioning to Todd

- The Web page used to read *"a steady stream fresh insights"* — the original was
  missing the word "of". That one word is now fixed. It is the only change made to
  his original wording anywhere on the site.
- The FAQ reconciles two statements that appear separately on the old site:
  writing "for more than 20 years," operating under the Brass Tack name "since
  2011." Worth a quick confirmation from him.
- The old Squarespace site still had two unused template pages sitting in its
  sitemap (`/home-1` and `/take-action`) full of placeholder text about a climate
  charity. Those were left behind on purpose.
- There's no contact form, same as the old site: just email and phone. Easy to add
  later if he wants one.
