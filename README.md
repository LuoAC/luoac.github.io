# Aocheng Luo · Personal Homepage

Source of **https://luoac.github.io**, the academic homepage of Aocheng Luo (Luo Aocheng),
Ph.D. student at Peking University and Navigation Algorithm Intern at Light Origins.

The site is plain HTML + CSS with no build step and no dependencies. GitHub Pages serves it as-is,
and you can preview it with any local web server.

## Structure

```
.
├── index.html              # all page content (each section has a comment banner)
├── 404.html                # "page not found" page
├── assets/
│   ├── css/style.css       # styles; colors and fonts are tokens at the top
│   ├── js/main.js          # small enhancements (active nav link, footer year)
│   └── img/                # project images, favicon, social-share card
├── tools/make_og_card.py   # regenerates assets/img/og-card.png
├── favicon.ico
├── site.webmanifest
├── robots.txt              # lets search engines crawl, points to the sitemap
├── sitemap.xml             # tells search engines which URL to index
└── .nojekyll               # serve files as-is (skip GitHub's Jekyll build)
```

## Preview locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Publish on GitHub Pages

The local repository is already initialized on branch `main`, with the first commit made. Its commit
identity is set for this repo only (`Aocheng Luo` with your GitHub no-reply address), so your personal
email never appears in the public history.

> **OneDrive note.** This folder sits inside OneDrive. Syncing a `.git` folder can occasionally cause
> conflicts or lock errors. After the first push, the safest setup is to clone the repo into a folder
> outside OneDrive (for example `D:\code`) and work there. GitHub keeps every version anyway.

1. On GitHub, click **+ → New repository**. Set the owner to `LuoAC` and the name to **`luoac.github.io`**.
   The name must be all lowercase: GitHub requires this for a user site when the username has capitals.
   Make it **Public**, and leave *Add README*, *.gitignore* and *license* **off** so the repository is empty.
2. In a terminal in this folder:

   ```bash
   git remote add origin https://github.com/LuoAC/luoac.github.io.git
   git push -u origin main
   ```

   If you accidentally created the repository with a README, run `git push -u origin main --force` once.
   The repository is new, so nothing is lost.
3. In the repository, open **Settings → Pages → Build and deployment**. Set *Source* to
   **Deploy from a branch**, *Branch* to `main` and the folder to `/ (root)`, then click **Save**.
4. Open the **Actions** tab and wait for a green *pages build and deployment* run. Settings → Pages then
   shows "Your site is live at https://luoac.github.io/". The first deploy can take up to 10 minutes.

### Everyday updates

```bash
git add -A
git commit -m "Describe the change"
git push
```

Changes go live within a few minutes. Browsers may show the old page for a while; press Ctrl+F5 to reload.

## Updating content

All content is in `index.html`. Each section starts with a comment banner such as
`<!-- ===================== News ===================== -->`.

| To do this | Edit |
| --- | --- |
| Add a news item | Copy one `<li>` in **News** and put it at the top (newest first). |
| Add a featured project | Copy one `<article class="project">` block in **Featured Research**. Put the image in `assets/img/` (about 1200 px wide; 16:10 looks best) and update the links. |
| Show a diagram without cropping | Use `<a class="project-media contain" …>` for that project's image. |
| Add a publication | Copy one `<li class="pub">` in **Selected Publications**. Wrap your own name in `<span class="me">…</span>`. Numbering is automatic. |
| Add experience / education | Copy one `<li>` in the matching `.timeline` (newest first). `class="current"` draws the filled dot; remove it when a role ends. |
| Add an award | Copy one `<li>` in **Honors & Awards** and put the year in `<span class="year">`. |
| Add a profile link (LinkedIn, etc.) | Add an `<li>` to the `.social` list in **About**, and add the same URL to `sameAs` in the JSON-LD block in `<head>` (keep the commas valid). |
| Add a photo | Save a square photo (at least 400 px) as `assets/img/profile.jpg` and follow the comment inside `<div class="avatar">`. Also add `"image": "https://luoac.github.io/assets/img/profile.jpg"` to the Person in the JSON-LD block. |
| Add a CV | Put an **English** PDF at `assets/cv.pdf` and add `<li><a href="assets/cv.pdf" title="CV (PDF)" aria-label="CV"><svg aria-hidden="true"><use href="#i-paper"/></svg></a></li>` to the `.social` list. Never publish the Chinese CV: it contains a phone number and birth date. |
| Post an accepted manuscript | IEEE lets authors post their accepted version (not the IEEE-formatted PDF) on a personal site with the copyright notice and DOI. Save it under `assets/papers/` and add a `PDF` button next to the paper's links. |
| Change colors | Edit the tokens under `:root` at the top of `assets/css/style.css`. |

`.gitignore` blocks all PDFs and Word files except `assets/cv.pdf` and `assets/papers/*.pdf`, so private
material cannot be committed by accident.

After a meaningful update, bump the date in three places so search engines notice: the footer
(`Last updated`), `dateModified` in the JSON-LD block in `<head>`, and `<lastmod>` in `sitemap.xml`.

### When something changes

- **Internship ends or you start a new role.** In `index.html`, search for `Intern` and `Light Origins`.
  Update the meta, `og:` and `twitter:` descriptions, the JSON-LD `jobTitle` and `worksFor`, the hero
  tagline, the bio sentence, and the timeline entry (add the end year and remove `class="current"`).
  Then edit the text at the top of `tools/make_og_card.py` and run it (`pip install pillow`,
  `python tools/make_og_card.py`) to refresh the share image.
- **A preprint is accepted.** Change its chip in **Featured Research** (for example `arXiv 2026` →
  `IEEE T-RO 2026`), update the venue line in **Selected Publications**, add an `IEEE Xplore` button
  linking to the DOI, and add a News item.

## Getting found when people search "Luo Aocheng"

The page already has what search engines need: a descriptive `<title>` and meta description, both name
orders ("Aocheng Luo" and "Luo Aocheng") plus 罗奥成 in the metadata, `schema.org` data that links your
Scholar, GitHub and ORCID profiles, a sitemap and a canonical URL. The rest happens outside the code:

1. **Google Search Console** (https://search.google.com/search-console): add a *URL prefix* property for
   `https://luoac.github.io/`. Choose *HTML tag* verification, paste the token into the commented
   `google-site-verification` line in `index.html`, uncomment it and push. After verifying, submit
   `sitemap.xml` and use *URL inspection → Request indexing*.
2. **Bing Webmaster Tools** (https://www.bing.com/webmasters): import the site from Search Console. This
   also covers DuckDuckGo and Yahoo.
3. **Link to the homepage from your other profiles.** These links matter most for ranking a name:
   - GitHub → *Edit profile*: set *Name* to `Aocheng Luo` and *Website* to `https://luoac.github.io`.
   - On the `luoac.github.io` repository page, click the gear next to *About*: set *Website* to
     `https://luoac.github.io`, the description to
     `Personal homepage of Aocheng Luo (Luo Aocheng), Peking University`, and add the topics
     `homepage`, `embodied-navigation` and `robotics`.
   - Google Scholar → *Edit* → *Homepage*; ORCID → *Websites & social links*; your alphaXiv profile.
   - Your email signature and slides.
   - Ask the lab website and your co-authors' project pages to link your name to this site.
4. **Be patient.** A new site usually shows up for name searches within a few days to a few weeks after
   it is indexed.
5. **Optional, Baidu.** GitHub Pages blocks Baidu's crawler, so `github.io` sites rarely appear on Baidu.
   If Baidu matters, mirror the site on another host (for example Cloudflare Pages or Vercel) under a
   custom domain and submit it at https://ziyuan.baidu.com.
6. **Optional, custom domain.** A domain such as `aochengluo.com` tends to rank best for a name. If you
   add one, update the URL in `index.html` (canonical, `og:*`, JSON-LD), `robots.txt` and `sitemap.xml`,
   and add a `CNAME` file.

## Credits

Project images come from the corresponding papers and project pages
([LightNav-0](https://www.lightorigins.com/en/blog/lightnav-0),
[VLingNav](https://shaoanwang.github.io/VLingNav-web/), and the IEEE T-ASE paper on depth-based
quadruped locomotion and navigation).
