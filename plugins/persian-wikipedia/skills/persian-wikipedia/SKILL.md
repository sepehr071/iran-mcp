---
name: persian-wikipedia
description: "Read-only Persian Wikipedia (fa.wikipedia.org): search, summaries, article text, nearby places. Use when the user asks about Persian Wikipedia (fa.wikipedia.org) or wants Persian word meanings, synonyms, translations or encyclopedia articles in Iran."
---

# Persian Wikipedia

Read-only Persian Wikipedia (fa.wikipedia.org): search, summaries, article text, nearby places.

The tools below come from the `persian-wikipedia-mcp` MCP server. If they are not available, install it with `claude mcp add persian-wikipedia -- uvx persian-wikipedia-mcp`, or add `"persian-wikipedia": {"command": "uvx", "args": ["persian-wikipedia-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `wiki_search`: Search Persian Wikipedia articles by words; returns titles with a short snippet and the total hit count.
- `wiki_summary`: Get the lead summary of an article: one-line description, intro paragraph, image, coordinates and URL.
- `wiki_article`: Read an article as plain text with '== heading ==' lines, optionally one section, cut to max_chars.
- `wiki_sections`: List an article's section headings with their level and number (the table of contents).
- `wiki_languages`: Get the titles of the same article in other Wikipedia languages (e.g. the English title).
- `wiki_infobox`: Get an article's infobox facts (birth date, population, director...) and its visible categories.
- `wiki_random`: Get a random Persian Wikipedia article with its summary.
- `wiki_trending`: Get the most-read articles of a day and the picture of the day (fa has no 'on this day' or featured article).
- `wiki_nearby`: Find articles about places near a latitude/longitude, nearest first, with distance in metres.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `PERSIAN_WIKIPEDIA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
