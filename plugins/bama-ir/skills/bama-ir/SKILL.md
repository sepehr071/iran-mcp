---
name: bama-ir
description: "Read-only Bama (bama.ir) Iran car marketplace: ad search, ad details, market prices, new-car prices. Use when the user asks about Bama Cars (bama.ir) or wants used or new car ads and prices in Iran."
---

# Bama Cars

Read-only Bama (bama.ir) Iran car marketplace: ad search, ad details, market prices, new-car prices.

The tools below come from the `bama-ir-mcp` MCP server. If they are not available, install it with `claude mcp add bama-ir -- uvx bama-ir-mcp`, or add `"bama-ir": {"command": "uvx", "args": ["bama-ir-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ba_search`: Search used and new car ads on Bama (bama.ir) with filters; up to 30 compact ads per page.
- `ba_ad`: Get one Bama ad (car, motorcycle or truck) in full: price, specs, condition, seller, description and photos.
- `ba_market_stats`: Price statistics (min, quartiles, median, max, per year) for a car model from live Bama ads.
- `ba_dealers`: List car dealers (showrooms) with ads for a model or city on Bama, with address, rating and how many ads match.
- `ba_vehicles`: Look up the brand, model and trim values that ba_search, ba_market_stats and ba_new_prices take.
- `ba_filters`: List the allowed values of one ba_search filter (states and cities, body types, fuels, colors, years...).
- `ba_new_prices`: Current price of every new-car trim of a brand or model on Bama's price list (market price or factory price).
- `ba_search_bikes_trucks`: Search motorcycle or truck (heavy vehicle, bus, machinery) ads on Bama with filters.
- `ba_dealer_ads`: List the ads of one dealer (showroom) on Bama: the dealer's whole inventory, up to the first 100 ads.
- `ba_price_list`: Search Bama's daily price list of new cars (or motorcycles) across all brands and rank it.
- `ba_market_pulse`: Today's car market mood from Bama (score, trend and a short analysis per market) plus the biggest price movers.
- `ba_car_specs`: Technical specifications and the editorial review score of a car or motorcycle model from Bama's research pages.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `BAMA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
