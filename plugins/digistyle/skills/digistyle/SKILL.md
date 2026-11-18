---
name: digistyle
description: "Read-only Digistyle (digistyle.com) fashion store: search, filters, product details, brands, deals. Use when the user asks about Digistyle Fashion (digistyle.com) or wants clothes, shoes or bags in Iran."
---

# Digistyle Fashion

Read-only Digistyle (digistyle.com) fashion store: search, filters, product details, brands, deals.

The tools below come from the `digistyle-mcp` MCP server. If they are not available, install it with `claude mcp add digistyle -- uvx digistyle-mcp`, or add `"digistyle": {"command": "uvx", "args": ["digistyle-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ds_search`: Search Digistyle fashion products with filters for category, brand, size, color and price (Toman).
- `ds_product`: Get a Digistyle product: price, discount, every size and color with stock, seller, specs, rating, comments.
- `ds_categories`: List Digistyle categories (from the site menu) with the code to pass to ds_search, ds_filters and ds_deals.
- `ds_brands`: List Digistyle brands with their code (for ds_search's brand argument); search by name.
- `ds_filters`: Show what a Digistyle category can be filtered by: sizes, colors, top brands, price range, other attributes.
- `ds_deals`: Find discounted Digistyle products, biggest discount first, from a category, brand or campaign.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DIGISTYLE_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
