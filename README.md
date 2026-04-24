# Book-Elections

A [Jekyll](https://jekyllrb.com/) site that publishes **«ВЫБОРЫ — Технологии избирательных кампаний»** (*Elections: Technologies of election campaigns*): a structured book on running election campaigns, with chapters as collection posts in Russian and Ukrainian, plus English navigation and chapter guides under `/en/`.

## What’s in the repo

- **`_config.yml`** — Site title, `book_title`, URL/baseurl, and collections.
- **`_ru_posts/`**, **`_uk_posts/`**, **`_en_posts/`** — Chapter content (`/ru/`, `/uk/`) and English guide stubs with links to full texts (`/en/`).
- **`_layouts/`** — `default`, `chapter`, and related templates.
- **`index.html`**, **`about.md`**, **`en/`**, **`uk/`**, **`ru/`** — Home, language hub, and per-language table of contents / about pages.
- **`Gemfile`** / **`Gemfile.lock`** — Ruby dependencies for Jekyll 4 and plugins (`jekyll-seo-tag`, `jekyll-sitemap`).

`README.md` is listed under `exclude` in `_config.yml` so it is not processed as a page; it is only for the repository (e.g. GitHub).

## Local development

Prerequisites: Ruby and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Open the URL Jekyll prints (usually `http://127.0.0.1:4000/Book-Elections/` if using the configured `baseurl`).

A production build:

```bash
bundle exec jekyll build
```

Output is written to `_site/` (ignored in git via `.gitignore`).

## Deployment

The project is set up for **GitHub Pages** (`url` and `baseurl` in `_config.yml` point at the `book.lemik.github.io` / `Book-Elections` path). Push to the configured branch; Pages builds the site from this Jekyll project.

## Contributing / editing

- Chapters are ordinary Markdown files in the collections above; front matter includes `layout: chapter`, `title`, `lang`, and `collection`.
- After editing content, run `bundle exec jekyll build` or `serve` to confirm the site compiles.
