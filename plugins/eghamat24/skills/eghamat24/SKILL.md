---
name: eghamat24
description: "Read-only Eghamat24 (eghamat24.com) Iran hotels: search, room prices, deals, reviews, facilities. Use when the user asks about Eghamat24 Hotels (eghamat24.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Eghamat24 Hotels

Read-only Eghamat24 (eghamat24.com) Iran hotels: search, room prices, deals, reviews, facilities.

The tools below come from the `eghamat24-mcp` MCP server. If they are not available, install it with `claude mcp add eghamat24 -- uvx eghamat24-mcp`, or add `"eghamat24": {"command": "uvx", "args": ["eghamat24-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `eg_tours`: Find flight-plus-hotel tour packages to a city, or the packages of one hotel with their flight times.
- `eg_tour_calendar`: Show the cheapest flight-plus-hotel package price for each departure day, to pick the cheapest day to leave.
- `eg_attractions`: List the sights, shrines, malls and other places of a city, or read the description of one.
- `eg_photos`: List the photo URLs of a hotel: the main picture, the hotel gallery and the photos of each room type.
- `eg_similar`: List the hotels the site suggests as alternatives to one hotel, with a starting price.
- `eg_specials`: List hotels on one of the site's offer pages: free cancellation, one-night offers or the latest discounts.
- `eg_cities`: List the destinations Eghamat24 has hotels in, with how many hotels and stays each has.
- `eg_search`: Search hotels in a city for given dates, with the filters the site offers, and return cards with the lowest price.
- `eg_deals`: List the hotels of a city with the biggest discounts for the given dates, bookable ones only.
- `eg_hotel`: Get one hotel's profile: address, stars, check-in times, description, facilities, rules, guest scores, extras and nearby places.
- `eg_rooms`: List a hotel's bookable rooms with the price for the stay, cheapest first.
- `eg_price_calendar`: Show the cheapest bookable room price for each night over a date range, to find the cheapest days to stay.
- `eg_reviews`: Read guest reviews of a hotel, newest first, with the overall guest scores and who travelled.
- `eg_questions`: Read the public questions guests asked about a hotel and the answers, if any.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `EGHAMAT24_MCP_PROXY` to an HTTP proxy with an Iranian IP.
