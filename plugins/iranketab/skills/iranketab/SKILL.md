---
name: iranketab
description: "Read-only Iranketab (iranketab.ir) books: search, translations compared, ratings, reviews, prices. Use when the user asks about Iranketab Books (iranketab.ir) or wants ebooks, audiobooks or printed books in Iran."
---

# Iranketab Books

Read-only Iranketab (iranketab.ir) books: search, translations compared, ratings, reviews, prices.

The tools below come from the `iranketab-mcp` MCP server. If they are not available, install it with `claude mcp add iranketab -- uvx iranketab-mcp`, or add `"iranketab": {"command": "uvx", "args": ["iranketab-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ik_search`: Search Iranketab by name and return matching books, authors/translators, publishers or categories with their ids.
- `ik_book`: Read one book (a work): title, authors, categories, introduction, review count and a short list of every edition.
- `ik_editions`: Compare every translation and publisher edition of one book side by side: rating, votes, price, pages, year, ISBN.
- `ik_reviews`: Read reader comments about a book, 20 per page, newest first, with the publisher/edition when the reader named one.
- `ik_profile`: Read an author's or translator's profile (name, biography) and the books they wrote or translated.
- `ik_publisher_books`: List the books of one publisher (انتشارات) on Iranketab, best sellers first by default.
- `ik_browse`: List books of a category, bestseller list or award list, with sort, in-list search and sub-category filters.
- `ik_categories`: List Iranketab's menu categories, or the sub-category filter groups of one category.
- `ik_book_extras`: Read what else a book page offers: awards, series, praise quotes, excerpts, author bio, related books and articles.
- `ik_recommend`: Suggest books to read next from books the reader liked, using Iranketab's own recommender ("چی بخونم؟").
- `ik_lists`: List Iranketab's literary prizes, best-of lists, book series, countries, genres or literary movements with ids.
- `ik_articles`: Find articles on Iranketab's blog (book reviews, author profiles, reading lists), by search or newest first.
- `ik_article`: Read one Iranketab blog article (a book review or author essay) as plain text, with the book and author ids it links to.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRANKETAB_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
