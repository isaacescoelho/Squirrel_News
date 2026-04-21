# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py

# Run production server
gunicorn app:app
```

No test suite or linter is configured.

## Architecture

**Squirrel News** is a single-file Flask news site. All routing and data logic lives in `app.py`.

### Data flow

Articles are fetched once at startup from an external JSON API (`npoint.io`) and cached in memory. The API response has two top-level keys: `main-headline` (a single featured article) and `other-stories` (a list). `other-stories` is sorted in reverse-chronological order by article ID before being passed to templates.

### Routes

| Route | Template | Notes |
|---|---|---|
| `GET /` | `index.html` | Featured article + reverse-chron list of others |
| `GET /about` | `about.html` | Static content |
| `GET /article/<id>` | `article.html` | `id` can be `"main"` or a numeric string |

### Templates

All templates use Jinja2. `header.html` and `footer.html` are included in each page template. Article body content is rendered with `{{ body | safe }}` — the API may return HTML markup. Image URLs are stripped of whitespace before use to handle API formatting quirks.

### Frontend

Static assets live in `static/assets/`. CSS is compiled from SASS sources in `static/assets/sass/`. The design is based on the "Massively" template from HTML5 UP (CCA 3.0 license), using jQuery for scroll effects.
