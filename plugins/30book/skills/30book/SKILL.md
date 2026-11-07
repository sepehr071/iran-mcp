---
name: 30book
description: "Unofficial read-only 30book: search Iranian printed books, compare editions and prices. Use when the user asks about 30book (30book.com) or wants ebooks, audiobooks or printed books in Iran."
---

# 30book

Unofficial read-only 30book: search Iranian printed books, compare editions and prices.

The tools below come from the `30book-mcp` MCP server. If they are not available, install it with `claude mcp add 30book -- uvx 30book-mcp`, or add `"30book": {"command": "uvx", "args": ["30book-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sb_search`: Search books by title.
- `sb_browse`: Books of a category (bta-N-M or btf-N-M-K), genre, nation, award list or tag.
- `sb_publisher`: One publisher's books plus a short about text.
- `sb_author`: Books by one author or translator (default newest first).
- `sb_bestsellers`: Site-wide best sellers (10 pages).
- `sb_new_releases`: Newest books (10 pages).
- `sb_deals`: Best sellers (or one subject) by biggest discount.
- `sb_find_publisher`: Look up publisher ids by name.
- `sb_find_person`: Look up author / translator ids by name.
- `sb_book`: One book: authors, translators, publisher, prices, stock, ISBN, details, categories (codes for sb_browse), rating, tags, description.
- `sb_similar`: Similar books, more by the author and by the translator, up to 20 each.
- `sb_reviews`: Reader comments and the rating summary; only the first comments on the page are available.
- `sb_categories`: Category sections or, for one section, its subjects.
- `sb_collections`: Home-page genres, nations, award lists and tags; ids go to sb_browse(kind=...).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SIBOOK_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Lists are slow (2 to 5 s each). Prefer one good query over many.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
