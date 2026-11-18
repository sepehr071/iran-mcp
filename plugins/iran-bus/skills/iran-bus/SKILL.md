---
name: iran-bus
description: "Read-only Iranian bus tickets (Safar724): trips, Toman prices, free seats, cheapest ticket. Use when the user asks about Iran Bus Tickets (safar724.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Iran Bus Tickets

Read-only Iranian bus tickets (Safar724): trips, Toman prices, free seats, cheapest ticket.

The tools below come from the `iran-bus-mcp` MCP server. If they are not available, install it with `claude mcp add iran-bus -- uvx iran-bus-mcp`, or add `"iran-bus": {"command": "uvx", "args": ["iran-bus-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bus_cities`: Look up cities (name, code, province) that tickets can be bought for; use it to spell a city exactly.
- `bus_search`: List bus trips between two cities on one day: time, company, bus type, price in Toman, free seats, terminals.
- `bus_cheapest`: Cheapest bus trips between two cities on one day, merged across providers and sorted by price in Toman.
- `bus_terminals`: List the departure and arrival terminals that have trips on a route and the companies running them.
- `bus_trip`: Seat map summary and refund penalties of one trip: free seat numbers, seats taken by men or women.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_BUS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Site: Safar724.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
