---
name: kilid
description: "Read-only Kilid (kilid.com) Iranian real estate: listings, districts, price per m2, agencies. Use when the user asks about Kilid Real Estate (kilid.com) or wants classified ads for homes, cars, phones and more in Iran."
---

# Kilid Real Estate

Read-only Kilid (kilid.com) Iranian real estate: listings, districts, price per m2, agencies.

The tools below come from the `kilid-mcp` MCP server. If they are not available, install it with `claude mcp add kilid -- uvx kilid-mcp`, or add `"kilid": {"command": "uvx", "args": ["kilid-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `kl_cities`: Find the city id and slug Kilid uses for a city (needed by kl_search_listings and kl_districts).
- `kl_districts`: List the districts or neighborhoods of a city with the ids kl_search_listings takes as region_ids.
- `kl_search_listings`: Search Kilid sale and rental listings with price, area, room and place filters.
- `kl_listing`: Get one Kilid listing: price, area, rooms, floor, facilities, description, location point and agency.
- `kl_price_stats`: Get median price per m2 for a city or area from Kilid's market report, with sub-areas and a 12-month trend.
- `kl_neighborhood_prices`: Rank a city's neighborhoods by median price per m2 (Toman), from Kilid's neighborhood guide.
- `kl_agencies`: Search real-estate agencies registered on Kilid by name; open one with kl_agency.
- `kl_agency`: Get a Kilid real-estate agency: address, district, location point, active listings and agent count.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `KILID_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
