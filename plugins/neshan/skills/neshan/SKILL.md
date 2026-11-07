---
name: neshan
description: "Read-only Neshan map of Iran: places, reviews, photos, routes, travel times, zones, air quality. Use when the user asks about Neshan Maps (neshan.org) or wants places, addresses, routes or travel times on a map in Iran."
---

# Neshan Maps

Read-only Neshan map of Iran: places, reviews, photos, routes, travel times, zones, air quality.

The tools below come from the `neshan-mcp` MCP server. If they are not available, install it with `claude mcp add neshan -- uvx neshan-mcp`, or add `"neshan": {"command": "uvx", "args": ["neshan-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ns_search`: Find places, businesses, streets and squares on the Neshan map by name or category near a city or point.
- `ns_place`: Get one place's details on Neshan: address, coordinates, phones, website, rating, opening hours and photos.
- `ns_reviews`: List visitors' reviews of a place on Neshan: star rating, Persian date, comment, likes and owner reply.
- `ns_photos`: List a place's photos on Neshan as image URLs, 10 per page, with date and uploader, including menu photos.
- `ns_nearby`: List what is around a place on Neshan by category: restaurants, cafes, parks, toilets, banks, ATMs, parking.
- `ns_reverse_geocode`: Turn a latitude/longitude into Neshan's street address and province (reverse geocoding).
- `ns_air_quality`: Get today's air quality index (AQI) of an Iranian city from Neshan, with pollutants and the readings of each station.
- `ns_route`: Get car, motorcycle, bicycle or walking directions on Neshan: distance, travel time and turn-by-turn steps.
- `ns_travel_times`: Get the travel time from one point to several places on Neshan, fastest first.
- `ns_zone_check`: Check whether a point is inside Tehran's traffic-plan zone or odd-even (air-pollution) zone, with plan hours.
- `ns_transit_route`: Get bus, BRT and metro options between two points on Neshan, with lines, stops, walking and fares.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `NESHAN_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Coordinates are `lat,lng` (latitude first). `ns_nearby` answers only Iranian connections; outside Iran set NESHAN_MCP_PROXY or use `ns_search` with `near`.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
