---
name: zoomit
description: "Read-only Zoomit (zoobin) product database: specs, shop prices in Toman, price history, comparisons. Use when the user asks about Zoomit Products (zoomit.ir) or wants electronics, appliances or other goods in Iran."
---

# Zoomit Products

Read-only Zoomit (zoobin) product database: specs, shop prices in Toman, price history, comparisons.

The tools below come from the `zoomit-mcp` MCP server. If they are not available, install it with `claude mcp add zoomit -- uvx zoomit-mcp`, or add `"zoomit": {"command": "uvx", "args": ["zoomit-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `zm_categories`: List the product categories of Zoomit's product database (slug and Persian name).
- `zm_search`: Find products by name across all categories (or one) and return cards with the lowest price in Toman.
- `zm_list`: List one category's products with the site's filters: brand, price, score, specs, stock, sort.
- `zm_filters`: Show what zm_list can filter by in a category: price range, brand slugs, spec filters with values, buying guides.
- `zm_product`: Get one product's full spec table, user score, Zoomit's pros and cons and its price range in Toman.
- `zm_prices`: List a product's seller offers (cheapest first, Toman, with listing title and link) and its price history.
- `zm_compare`: Compare 2-4 products: price, scores and a spec table where each row lists the values in the order of `products`.
- `zm_similar`: Suggest alternatives to a product: the ones people compare it with, others of its brand, or in its price range.
- `zm_articles`: Search Zoomit's news and review articles (title, lead, date, link).
- `zm_reviews`: Read what buyers say about a product: star breakdown, Zoomit's summary of strengths and weaknesses, reviews or Q&A.
- `zm_guides`: List Zoomit's buying guides ("best phones under...", "best gaming phones") of a category with their article links.
- `zm_rank`: Rank a category's popular products by one numeric spec (battery, weight, RAM, brightness) or by value for money.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `ZOOMIT_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
