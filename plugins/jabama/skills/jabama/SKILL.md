---
name: jabama
description: "Unofficial read-only Jabama: villas and stays with exact prices, group tours, events and theater. Use when the user asks about Jabama (jabama.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Jabama

Unofficial read-only Jabama: villas and stays with exact prices, group tours, events and theater.

The tools below come from the `jabama-mcp` MCP server. If they are not available, install it with `claude mcp add jabama -- uvx jabama-mcp`, or add `"jabama": {"command": "uvx", "args": ["jabama-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `jb_search_events`: Search Jabama Events: concerts, shows, workshops, exhibitions and experiences, with prices in Toman.
- `jb_event`: One event or experience: details, address, rules, price, sessions with seats left, reviews, organizer.
- `jb_event_seats`: Live seat availability of one seated event session: free seats per section and row, with section prices in Toman.
- `jb_theaters`: List theater plays on sale on Jabama Events (Tehran): venue, address, from-price in Toman, rating, crew.
- `jb_theater`: One theater play: venue, crew, reviews, showtimes with seats left; with showtime_id also free seats by row and prices.
- `jb_event_filters`: Cities and categories of Jabama Events with event counts, for the city and category filters of jb_search_events.
- `jb_help`: Answer questions about Jabama's rules: cancellation and refunds, payment, tax, check-in, host and guest duties.
- `jb_travel_guide`: Search Jabama's travel magazine (/mag): guides on attractions, best time to visit, how to get there, food.
- `jb_find_destination`: Turn a place name into ready jb_search_stays arguments (keyword and filters).
- `jb_parse_request`: Turn a free-text stay request into jb_search_stays arguments with Jabama's own AI parser.
- `jb_search_stays`: Search Jabama stays (villas, suites, apartments, cottages, eco-lodges) with prices for your dates and guests.
- `jb_categories`: List Jabama's themed stay categories (special pool, A-frame, luxury, cheap, sea view, pet friendly, ...).
- `jb_stay`: Get one listing: capacity, rooms, times, house rules, amenities, cancellation policy, host, review scores.
- `jb_stay_calendar`: Nightly availability and price of one listing for the next ~76 days, with day types.
- `jb_price_quote`: Get the exact amount to pay (Toman) for one listing, dates and guests, with per-night lines and cancellation windows.
- `jb_similar_stays`: Find alternatives to a listing: similar stays nearby, and other units of the same property.
- `jb_reviews`: Read guest reviews of a listing: stars 1-5, text, when they stayed, nights, and the host's reply.
- `jb_host`: A host's listings (rating, from-price per night) and guest reviews, newest first.
- `jb_search_tours`: Search Jabama group tours (nature, desert, hiking, history, food tours across Iran) with price per person in Toman.
- `jb_tour`: One group tour: packages, departures with free seats and per-person package prices, day plan, inclusions, cancellation, guide, reviews.
- `jb_tour_places`: Turn a place name into a Jabama Tours place id for jb_search_tours (destination_id / origin_id).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `JABAMA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: jabama.com (stays), jabama.tours (group tours), jabama.events (events and theater).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
