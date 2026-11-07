---
name: alibaba-ir
description: "Read-only Alibaba (alibaba.ir) Iran travel: trains, buses, flights, hotels, villas and tours. Use when the user asks about Alibaba Travel (alibaba.ir) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Alibaba Travel

Read-only Alibaba (alibaba.ir) Iran travel: trains, buses, flights, hotels, villas and tours.

The tools below come from the `alibaba-ir-mcp` MCP server. If they are not available, install it with `claude mcp add alibaba-ir -- uvx alibaba-ir-mcp`, or add `"alibaba-ir": {"command": "uvx", "args": ["alibaba-ir-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `al_flights_international`: Search international flights between Iran and abroad (or any two cities Alibaba sells) on one day.
- `al_stays`: Search villas, suites, cottages and other holiday homes for rent in a city, with price, rating and capacity.
- `al_stay_detail`: Show one villa or holiday home in full: capacity, beds, amenities, house rules, cancellation terms, calendar, reviews.
- `al_hotels`: Search hotels in a city for a stay: stars, rating, price for the whole stay, meal plan, perks (domestic and abroad).
- `al_tours`: Search tour packages (round trip plus hotel) from a city to a destination such as Kish, Mashhad, Istanbul or Dubai.
- `al_tours_cheapest`: List the lowest tour price per person for 11 departure days around a date (5 before, 5 after), to pick the cheapest day.
- `al_cities`: Look up the city codes the other tools take (THR for Tehran, MHD for Mashhad) and what is sold for each city.
- `al_trains`: Search train tickets between two Iranian cities on one day: company, class, times, price and seats left.
- `al_trains_cheapest`: List the lowest train price for each day from a start date, to pick the cheapest day to travel.
- `al_buses`: Search intercity bus tickets between two Iranian cities on one day: company, bus type, times, price, seats.
- `al_buses_cheapest`: List the lowest bus price and the number of buses for each day from a start date (the site has no bus calendar).
- `al_bus_seats`: Show which seats are free on one bus: counts per status and the free seat numbers (no booking).
- `al_flights`: Search domestic flights between two Iranian airports on one day: airline, flight number, times, fare, seats.
- `al_flights_cheapest`: List the lowest domestic fare for each day from a start date, to pick the cheapest day to fly.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `ALIBABA_IR_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
