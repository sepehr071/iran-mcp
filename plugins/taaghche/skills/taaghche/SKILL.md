---
name: taaghche
description: "Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews. Use when the user asks about Taaghche (taaghche.com) or wants ebooks, audiobooks or printed books in Iran."
---

# Taaghche

Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews.

The tools below come from the `taaghche-mcp` MCP server. If they are not available, install it with `claude mcp add taaghche -- uvx taaghche-mcp`, or add `"taaghche": {"command": "uvx", "args": ["taaghche-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tg_search`: Search ebooks and audiobooks by title, author or topic: price, discount, rating, format.
- `tg_suggest`: Typeahead: up to 10 matching book titles with id.
- `tg_book`: One book: price, format, pages or duration, people, rating breakdown, categories, ISBN.
- `tg_reviews`: Reader reviews, most liked first: rating, text, likes, reply count.
- `tg_similar`: Related books in lists (similar works, same author, same publisher): price, format, rating.
- `tg_browse`: List books of a category (or the whole catalog), 16 per page, by sort, format and price ceiling.
- `tg_bestsellers`: Hottest books now (trending ranking, no sales numbers), overall or per category.
- `tg_new_releases`: Newest books first, overall or per category.
- `tg_free_books`: Free books and audiobooks (price 0), most downloaded first by default.
- `tg_categories`: Category tree: top-level groups (id) and standalone categories, each with a slug.
- `tg_author`: An author's profile (with a slug: nationality, life dates, bio) and their books, 16 per page.
- `tg_publisher`: A publisher's description and its books, 16 per page.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TAAGHCHE_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
