---
name: eghamat24
description: "Read-only Eghamat24 (eghamat24.com) Iran hotels: search, room prices, deals, reviews, facilities. Use when the user asks about Eghamat24 Hotels (eghamat24.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Eghamat24 Hotels

Read-only Eghamat24 (eghamat24.com) Iran hotels: search, room prices, deals, reviews, facilities.

The tools below come from the `eghamat24-mcp` MCP server. If they are not available, install it with `claude mcp add eghamat24 -- uvx eghamat24-mcp`, or add `"eghamat24": {"command": "uvx", "args": ["eghamat24-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `eg_tours`: Find flight-plus-hotel tour packages to a city, or the packages of one hotel with flight times.
- `eg_tour_calendar`: Show the cheapest flight-plus-hotel package price per departure day.
- `eg_attractions`: List the sights, shrines, malls and other places of a city, or read one.
- `eg_photos`: List a hotel's photo URLs: main picture, gallery and each room type.
- `eg_similar`: List the hotels the site suggests as alternatives to one hotel, with a starting price.
- `eg_specials`: List hotels on one of the site's offer pages: free cancellation, one-night offers or latest discounts.
- `eg_cities`: List the destinations Eghamat24 has hotels in, with hotel and stay counts.
- `eg_search`: Search hotels in a city for given dates and filters; returns cards with the lowest price.
- `eg_deals`: List a city's bookable hotels with the biggest discounts for the dates.
- `eg_hotel`: Get one hotel's profile: address, stars, times, facilities, rules, guest scores, extras and nearby places.
- `eg_rooms`: List a hotel's bookable rooms with the stay price, cheapest first.
- `eg_price_calendar`: Show the cheapest bookable room price per night over a date range.
- `eg_reviews`: Read guest reviews of a hotel, newest first.
- `eg_questions`: Read the public questions guests asked about a hotel and the answers, if any.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `EGHAMAT24_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
