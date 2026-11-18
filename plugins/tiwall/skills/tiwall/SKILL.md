---
name: tiwall
description: "Read-only Tiwall (tiwall.com) Iranian event tickets: theatre, concerts, venues, sessions, prices. Use when the user asks about Tiwall Events (tiwall.com) or wants cinema showtimes or theatre, concert and event tickets in Iran."
---

# Tiwall Events

Read-only Tiwall (tiwall.com) Iranian event tickets: theatre, concerts, venues, sessions, prices.

The tools below come from the `tiwall-mcp` MCP server. If they are not available, install it with `claude mcp add tiwall -- uvx tiwall-mcp`, or add `"tiwall": {"command": "uvx", "args": ["tiwall-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tw_categories`: List Tiwall's event categories, sort orders and main cities with the ids tw_events needs.
- `tw_events`: List current Tiwall events filtered by category, city, venue, date and sort order.
- `tw_popular`: List the best-selling, best-rated or newest Tiwall events, optionally per category or city.
- `tw_search`: Search Tiwall events by title, artist or venue words.
- `tw_event`: Get one event: venue and address, dates, time, duration, price, cast and crew, summary, tags, rating, sale status.
- `tw_sessions`: List the show times (sessions) of an event with date, time, seat status and ticket price in Toman.
- `tw_venues`: Search Tiwall venues and cities by name and get their ids, addresses, coordinates and ratings.
- `tw_venue`: Get a venue page (address, phones, social links, followers) and its current events.
- `tw_reviews`: Read the public rating breakdown and audience posts of an event (newest page only).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TIWALL_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
