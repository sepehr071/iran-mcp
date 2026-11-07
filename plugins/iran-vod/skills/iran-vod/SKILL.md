---
name: iran-vod
description: "Read-only Filimo and Namava catalogs: search, title details, episodes, new, genres, where to watch. Use when the user asks about Filimo and Namava (filimo.com) or wants films and series to stream on Filimo or Namava, or where to watch a title in Iran."
---

# Filimo and Namava

Read-only Filimo and Namava catalogs: search, title details, episodes, new, genres, where to watch.

The tools below come from the `iran-vod-mcp` MCP server. If they are not available, install it with `claude mcp add iran-vod -- uvx iran-vod-mcp`, or add `"iran-vod": {"command": "uvx", "args": ["iran-vod-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `vod_search`: Search the Filimo and Namava catalogs by title and return matching movies and series with a ref for each.
- `vod_where`: Tell which of Filimo and Namava carries a title, by searching both and matching the title text.
- `vod_title`: Get full details of one movie or series on Filimo or Namava: synopsis, genres, year, rating, age rating, cast, director.
- `vod_episodes`: List the seasons of a series and the episodes of one season (title, summary, length, publish date).
- `vod_new`: List the newest titles added to Filimo and Namava, most recent first.
- `vod_featured`: Show what Filimo and Namava promote right now: Filimo's front-page rows (new, popular, box office, genres) and Namava's top slider and top list.
- `vod_genres`: List the genre names vod_browse accepts for Filimo and Namava, with the English aliases.
- `vod_browse`: List movies and series of one genre on Filimo and Namava, with Filimo's sort and country filters.
- `vod_person`: Look up an actor, director or writer on Filimo and Namava: short bio and the titles they appear in.
- `vod_related`: List titles similar to one movie or series on Filimo or Namava ("viewers also watch").
- `vod_collections`: List the curated lists vod_collection can open on Filimo and Namava: IMDb top 250, Oscar, kids, coming soon and more.
- `vod_collection`: Show the titles of one curated list on Filimo or Namava, such as the IMDb top 250 or coming soon.
- `vod_plans`: Show Namava's public subscription plans and prices (Filimo's prices are not available in its JSON API).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_VOD_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
