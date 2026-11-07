---
name: karnameh
description: "Read-only Karnameh (karnameh.com) Iran car data: used ads, new-car prices, specs, comparisons, blog. Use when the user asks about Karnameh Cars (karnameh.com) or wants used or new car ads and prices in Iran."
---

# Karnameh Cars

Read-only Karnameh (karnameh.com) Iran car data: used ads, new-car prices, specs, comparisons, blog.

The tools below come from the `karnameh-mcp` MCP server. If they are not available, install it with `claude mcp add karnameh -- uvx karnameh-mcp`, or add `"karnameh": {"command": "uvx", "args": ["karnameh-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `kn_specs_search`: Find car variants in Karnameh's specs catalog and return the `slug` that kn_specs and kn_compare_specs take.
- `kn_specs`: Get one car variant's technical specs, Karnameh's expert review score, pros and cons and web reviews.
- `kn_compare_specs`: Compare two to four car variants side by side: review score, pros, cons and every spec row.
- `kn_articles`: Search or list articles of the Karnameh car magazine: news, reviews, maintenance, laws.
- `kn_article`: Read one article of the Karnameh car magazine as plain text.
- `kn_price_movers`: Rank new (zero-km) car variants by the percent change of their latest price quote.
- `kn_city_stats`: Count Karnameh's used-car ads in every city, optionally for one brand, model or price ceiling.
- `kn_inspection_centers`: List Karnameh's walk-in car inspection and paint-check centers in a city, with address and map coordinates.
- `kn_cars`: Search Karnameh's used-car ads by brand, model, city, price, year and mileage.
- `kn_car`: Get one Karnameh used-car ad: price, specs, seller's description, strengths and the inspection summary.
- `kn_brands`: Look up Karnameh's car brands and models, Persian and English, to get the names the other tools expect.
- `kn_cities`: List the cities Karnameh serves, with the slug kn_cars takes as `city` and the id kn_inspection_centers takes.
- `kn_price_list`: List today's market prices of new (zero-km) cars from Karnameh's car-price pages.
- `kn_latest_prices`: List the most recent price quotes of new cars with the day's percent change.
- `kn_price_history`: Get the daily average market price history of one new-car variant, per production year.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `KARNAMEH_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
