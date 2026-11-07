---
name: hamrah-mechanic
description: "Read-only Hamrah Mechanic (hamrah-mechanic.com) car prices, used cars for sale, inspection fees. Use when the user asks about Hamrah Mechanic Cars (hamrah-mechanic.com) or wants used or new car ads and prices in Iran."
---

# Hamrah Mechanic Cars

Read-only Hamrah Mechanic (hamrah-mechanic.com) car prices, used cars for sale, inspection fees.

The tools below come from the `hamrah-mechanic-mcp` MCP server. If they are not available, install it with `claude mcp add hamrah-mechanic -- uvx hamrah-mechanic-mcp`, or add `"hamrah-mechanic": {"command": "uvx", "args": ["hamrah-mechanic-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `hm_brands`: List the car brands Hamrah Mechanic knows, with the slug the other tools take.
- `hm_models`: List the models of one brand with their slugs.
- `hm_prices`: Get today's market (used and zero-km) prices of cars from Hamrah Mechanic's daily price list.
- `hm_price_estimate`: Get the market price range and recent monthly change for one trim in one model year.
- `hm_search_cars`: Search the used and zero-km cars Hamrah Mechanic's showrooms sell, with filters.
- `hm_car`: Get the full details of one car for sale: price, specs, condition, inspection notes, photos and showroom.
- `hm_inspection_prices`: Get what Hamrah Mechanic charges to inspect a given car at its location, for each inspection package.
- `hm_branches`: List Hamrah Mechanic's car showrooms and inspection centers in a province with address, hours and cars in stock.
- `hm_price_history`: Get the monthly market-price history of one trim and year, with today's price range and the same trim's other years.
- `hm_price_list`: List the market price of every car on Hamrah Mechanic's front price list, filtered by budget or brand.
- `hm_reviews`: Get Hamrah Mechanic's expert review of a model (pros, cons, engine and safety notes) with owner scores and comments.
- `hm_articles`: Search the Hamrah Mechanic magazine (3,000+ Persian articles) or read one article.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `HAMRAH_MECHANIC_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
