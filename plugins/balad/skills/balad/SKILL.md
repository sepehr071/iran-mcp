---
name: balad
description: "Read-only Balad (balad.ir) Iran map: places nearby or on the way, details, reviews, driving routes. Use when the user asks about Balad Maps (balad.ir) or wants places, addresses, routes or travel times on a map in Iran."
---

# Balad Maps

Read-only Balad (balad.ir) Iran map: places nearby or on the way, details, reviews, driving routes.

The tools below come from the `balad-mcp` MCP server. If they are not available, install it with `claude mcp add balad -- uvx balad-mcp`, or add `"balad": {"command": "uvx", "args": ["balad-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bl_search`: Search Balad (Iranian map) for places, streets, neighbourhoods and cities by name, with coordinates and address.
- `bl_nearby`: List places of one kind (pharmacy, restaurant, gas station...) around a point, with address, phone and rating.
- `bl_place`: Get one place's full details from Balad: address, phones, hours, open now, rating, amenities, photos, reviews.
- `bl_reviews`: Get one page of user reviews of a place on Balad, newest first, with stars and the rating breakdown.
- `bl_reverse_geocode`: Turn coordinates into a Persian street address with city, county and neighbourhood (reverse geocoding).
- `bl_route`: Get driving routes in Iran with distance, travel time in current traffic, tolls, roads and traffic-zone warnings.
- `bl_nearest_by_drive`: Rank places of one kind around a point by driving time from it in current traffic, quickest first.
- `bl_along_route`: Find places of one kind (gas station, restaurant, pharmacy...) along the suggested driving route between two points.
- `bl_categories`: List Balad's place categories with the slug bl_nearby takes, grouped (food, health, shopping, services...).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `BALAD_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Coordinates are `lat`/`lng` (latitude first). Directions are car routes only: no walking or transit (use neshan-mcp for those).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
