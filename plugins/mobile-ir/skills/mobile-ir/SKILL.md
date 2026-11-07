---
name: mobile-ir
description: "Read-only Mobile.ir: phone specs, shop prices and history, used phones, numbered SIM cards. Use when the user asks about Mobile.ir Phones (mobile.ir) or wants electronics, appliances or other goods in Iran."
---

# Mobile.ir Phones

Read-only Mobile.ir: phone specs, shop prices and history, used phones, numbered SIM cards.

The tools below come from the `mobile-ir-mcp` MCP server. If they are not available, install it with `claude mcp add mobile-ir -- uvx mobile-ir-mcp`, or add `"mobile-ir": {"command": "uvx", "args": ["mobile-ir-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `mi_compare`: Compare 2 to 4 phones, tablets or watches on Mobile.ir: price range, rating and each spec row side by side.
- `mi_comments`: Read what Mobile.ir users wrote about a phone, tablet or watch: comment text, date (Persian calendar), likes.
- `mi_articles`: List the news and the expert reviews on Mobile.ir, newest first, optionally for one phone or brand.
- `mi_article`: Read the text of one Mobile.ir news item, expert review or product introduction (Persian, images dropped).
- `mi_shop`: Show one Mobile.ir shop's profile and the phones it lists with their current prices in Toman.
- `mi_brand_models`: Page through every model Mobile.ir lists for one brand (id, rating, year, screen, camera, lowest shop price).
- `mi_sim_summary`: Summarise the numbered-SIM market on Mobile.ir per operator: ad counts and the three cheapest priced numbers.
- `mi_search`: Find phones, tablets and smartwatches on Mobile.ir by name and get their ids (autocomplete, up to about 20).
- `mi_find`: Filter Mobile.ir's phone database like its 'mobile finder': brand, shop price range, OS, camera, weight, name.
- `mi_phone`: Get the full specification sheet of one phone, tablet or smartwatch from Mobile.ir, with rating and price range.
- `mi_shop_prices`: List what each shop currently charges for a phone on Mobile.ir (price in Toman, shop, city, note, warranty).
- `mi_price_history`: Get a phone's shop-price history from Mobile.ir: per-shop first/last/min/max and the daily lowest price in Toman.
- `mi_market_prices`: List the newest price rows that shops posted on Mobile.ir (one row per shop and model), with filters.
- `mi_used_search`: Search the used and new phone ads that users post on Mobile.ir (price, condition, city, description).
- `mi_used_ad`: Read one used/new phone ad on Mobile.ir: price, market price, condition, box, city, description, photos, shops.
- `mi_sim_search`: Search the SIM card numbers users sell on Mobile.ir (Iran's numbered-SIM market): operator, number, price.
- `mi_options`: List the ids the other Mobile.ir tools take: brands, provinces, price-listing shops, SIM operator prefixes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `MOBILE_IR_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
