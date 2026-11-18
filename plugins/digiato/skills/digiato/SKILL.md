---
name: digiato
description: "Read-only Digiato tech news: latest, by category, search, full articles, reviews and tags. Use when the user asks about Digiato Tech News (digiato.com) or wants news headlines or full news articles in Iran."
---

# Digiato Tech News

Read-only Digiato tech news: latest, by category, search, full articles, reviews and tags.

The tools below come from the `digiato-mcp` MCP server. If they are not available, install it with `claude mcp add digiato -- uvx digiato-mcp`, or add `"digiato": {"command": "uvx", "args": ["digiato-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dgt_latest`: Latest Digiato articles (news, reviews, guides), newest first.
- `dgt_categories`: List Digiato categories with article counts and parent, e.g. tech > mobile, artificial-intelligence, security.
- `dgt_category`: Newest articles of one category (children included), e.g. mobile, artificial-intelligence, car-news, security.
- `dgt_search`: Search Digiato articles by words in the title and text, best matches first.
- `dgt_reviews`: Newest Digiato product reviews (نقد و بررسی), optionally of one device type.
- `dgt_tags`: Find Digiato tags (companies, products, topics) with article counts, most used first.
- `dgt_tag`: Newest articles carrying one tag, e.g. apple, samsung, google, mobile.
- `dgt_article`: Read one Digiato article as plain text with title, author, summary, date, categories, tags and cover.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DIGIATO_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
