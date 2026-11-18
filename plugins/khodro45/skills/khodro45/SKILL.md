---
name: khodro45
description: "Read-only Khodro45 (khodro45.com) Iran used cars: listings, inspection reports, price estimate. Use when the user asks about Khodro45 Used Cars (khodro45.com) or wants used or new car ads and prices in Iran."
---

# Khodro45 Used Cars

Read-only Khodro45 (khodro45.com) Iran used cars: listings, inspection reports, price estimate.

The tools below come from the `khodro45-mcp` MCP server. If they are not available, install it with `claude mcp add khodro45 -- uvx khodro45-mcp`, or add `"khodro45": {"command": "uvx", "args": ["khodro45-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `k45_brands`: List the car brands Khodro45 knows, optionally filtered by name.
- `k45_models`: List the models of one brand, e.g.
- `k45_trims`: List the trims (types) of a model and the model years each one was built.
- `k45_price_estimate`: Estimate the used-car price of a trim and year, the same public estimate khodro45.com/carprice shows.
- `k45_cities`: List the cities where Khodro45 sells cars, optionally filtered by name.
- `k45_cars`: Search the used cars listed for sale on Khodro45 (inspected by the company).
- `k45_car`: Get one used-car listing in full: price, specs, ownership and document facts, photos.
- `k45_inspection`: Get the public Khodro45 expert inspection report of a listing: section scores and every found defect.
- `k45_deals`: List used cars Khodro45 really sold lately (the public deals hall), newest first, with the sale price.
- `k45_new_car_prices`: Get today's zero-km car prices (market, factory, dealer) of a brand, or the market price indexes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `KHODRO45_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
