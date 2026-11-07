---
name: emalls-ir
description: "Read-only Emalls (emalls.ir) price comparison: products, shop offers, price history, shops. Use when the user asks about Emalls Price Comparison (emalls.ir) or wants electronics, appliances or other goods in Iran."
---

# Emalls Price Comparison

Read-only Emalls (emalls.ir) price comparison: products, shop offers, price history, shops.

The tools below come from the `emalls-ir-mcp` MCP server. If they are not available, install it with `claude mcp add emalls-ir -- uvx emalls-ir-mcp`, or add `"emalls-ir": {"command": "uvx", "args": ["emalls-ir-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `em_search`: Search Emalls (Iranian price comparison) for products, with price range, category, brand, spec and sort filters.
- `em_categories`: Find Emalls category ids by words, or browse the category tree (top level, then children of a category id).
- `em_filters`: List the brands and spec filters (RAM, storage, ...) Emalls offers in one category, with their ids.
- `em_product`: Get one Emalls product: title, category path, lowest and highest shop price, rating and specs.
- `em_compare`: Compare 2-5 Emalls products: prices, rating and only the specs whose values differ.
- `em_similar`: List products Emalls shows as similar to one product, with lowest price and shop count.
- `em_offers`: List the shops selling one Emalls product with price, city, shop rating, warranty and buy link, cheapest first.
- `em_price_history`: Get the price history of one Emalls product: the average price over time in about 3-day steps (last ~3 months).
- `em_shop`: Get an Emalls shop's public profile: name, rating, website, address, phone, time with Emalls and trust badge.
- `em_shops`: Search Emalls' list of shops by name and return their ids.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `EMALLS_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
