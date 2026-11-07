---
name: sheypoor
description: "Read-only Sheypoor (sheypoor.com) classifieds: search ads, ad details, price summaries. Use when the user asks about Sheypoor Classifieds (sheypoor.com) or wants classified ads for homes, cars, phones and more in Iran."
---

# Sheypoor Classifieds

Read-only Sheypoor (sheypoor.com) classifieds: search ads, ad details, price summaries.

The tools below come from the `sheypoor-mcp` MCP server. If they are not available, install it with `claude mcp add sheypoor -- uvx sheypoor-mcp`, or add `"sheypoor": {"command": "uvx", "args": ["sheypoor-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sp_search`: Search Sheypoor classified ads (cars, real estate, goods, jobs, services) by words, city, category and price.
- `sp_ad`: Get one Sheypoor ad in full: description, price, location, seller, every attribute and photo links.
- `sp_price_summary`: Summarise asking prices of the newest ads for a search: count, min, median, quartiles, max, plus cheapest and priciest ads.
- `sp_categories`: List Sheypoor's categories with the slug sp_search and sp_filters take, grouped under 11 top-level groups.
- `sp_cities`: Find the city or province slug that sp_search, sp_price_summary and sp_filters take.
- `sp_filters`: List the filters, sort orders, sub-categories (car brands, models) and neighbourhoods Sheypoor offers in one category.
- `sp_similar`: Find ads comparable to one ad: same city and deepest category (car model...), price within a percent band.
- `sp_shops`: List Sheypoor's internet shops and agencies (real-estate offices, car dealers...) in a city and group.
- `sp_shop`: Get one internet shop or agency: name, hours, group, its agents and its current ads.
- `sp_car_prices`: Get Sheypoor's daily car price list (قیمت روز خودرو): market price and factory price per model and year, with the day's change.
- `sp_area_prices`: Compare asking prices between neighbourhoods of a city: median price, price per square metre, rent and deposit.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SHEYPOOR_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
