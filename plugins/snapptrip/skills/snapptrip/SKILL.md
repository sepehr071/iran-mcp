---
name: snapptrip
description: "Read-only SnappTrip: Iranian hotel search, rooms, reviews, calendar prices and domestic flights. Use when the user asks about SnappTrip Hotels and Flights (snapptrip.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# SnappTrip Hotels and Flights

Read-only SnappTrip: Iranian hotel search, rooms, reviews, calendar prices and domestic flights.

The tools below come from the `snapptrip-mcp` MCP server. If they are not available, install it with `claude mcp add snapptrip -- uvx snapptrip-mcp`, or add `"snapptrip": {"command": "uvx", "args": ["snapptrip-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `st_flight_airports`: List the cities SnappTrip offers flights from, with IATA codes and airports.
- `st_flight_search`: Search one-way domestic economy flights for a date, cheapest first.
- `st_flight_prices`: Show the lowest one-way price per day for the next weeks and the cheapest days.
- `st_hotel_places`: Find a SnappTrip hotel city or a hotel by name.
- `st_hotel_search`: Search hotels in a city for dates with star, price and facility filters.
- `st_hotel_filters`: List the filters a city offers for dates: facilities (ids), categories, accommodation types, price range, stars.
- `st_hotel_detail`: Get a hotel's description, location, facilities, policies, photos and guest rating breakdown.
- `st_hotel_rooms`: List the rooms of a hotel with prices for the dates.
- `st_hotel_calendar`: Show a room's per-night price and rooms left for each day, with the cheapest bookable nights.
- `st_hotel_reviews`: Read guest reviews of a hotel, newest first, with pros, cons and the room stayed in.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SNAPPTRIP_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
