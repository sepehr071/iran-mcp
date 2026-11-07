---
name: snappshop
description: "Read-only Snapp! Shop marketplace: search, categories, seller offers in Toman, reviews. Use when the user asks about Snapp! Shop (snappshop.ir) or wants electronics, appliances or other goods in Iran."
---

# Snapp! Shop

Read-only Snapp! Shop marketplace: search, categories, seller offers in Toman, reviews.

The tools below come from the `snappshop-mcp` MCP server. If they are not available, install it with `claude mcp add snappshop -- uvx snappshop-mcp`, or add `"snappshop": {"command": "uvx", "args": ["snappshop-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ss_search`: Search Snapp!
- `ss_suggest`: Complete a search phrase the way the site's search box does, most searched first.
- `ss_categories`: List Snapp!
- `ss_category`: List the products of one Snapp!
- `ss_product`: Get one product: specs, rating, and every seller's price, stock and delivery.
- `ss_reviews`: Read buyers' reviews of a product: score, title, text, pros and cons, helpful votes and date.
- `ss_similar`: Find alternatives to a product that Snapp!
- `ss_seller`: List the products one seller (فروشنده) offers on Snapp!
- `ss_filters`: Show the filters Snapp!
- `ss_brand`: List the products of one brand page on Snapp!
- `ss_collection`: List every product of one promotion collection (flash sale, carousel, 'see all' list) from ss_promotions.
- `ss_promotions`: Show what Snapp!
- `ss_compare`: Compare 2-4 products side by side: price, rating, seller count and the specs that differ.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SNAPPSHOP_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Snapp! Shop answers only Iranian connections (HTTP 403 elsewhere).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
