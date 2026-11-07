---
name: masterkala
description: "Unofficial read-only MasterKala: search gadgets, compare prices and specs, stock, delivery, deals. Use when the user asks about MasterKala (masterkala.com) or wants electronics, appliances or other goods in Iran."
---

# MasterKala

Unofficial read-only MasterKala: search gadgets, compare prices and specs, stock, delivery, deals.

The tools below come from the `masterkala-mcp` MCP server. If they are not available, install it with `claude mcp add masterkala -- uvx masterkala-mcp`, or add `"masterkala": {"command": "uvx", "args": ["masterkala-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `mk_blog_posts`: List MasterKala blog posts (buying guides, comparisons, how-tos), newest first, with links.
- `mk_blog_comments`: Read the comments of a blog post as threads, with the store writer's answers as replies.
- `mk_search`: Search MasterKala products by keyword: price, discount and stock of each match.
- `mk_find_cheapest`: Find the cheapest in-stock products for a keyword, one flat list sorted by final_price.
- `mk_browse`: List the products of a category, brand or tag with sorting, price range and filters.
- `mk_filters`: List the filters of a category, brand or tag page with their ids, and its price range.
- `mk_categories`: List MasterKala's product categories with their ids (about 100).
- `mk_brands`: List the brands MasterKala sells with their slugs (about 135).
- `mk_deals`: List products on MasterKala's discount page, biggest discount first.
- `mk_product`: Get one product's full record: price (Toman), stock count, colors, category path, rating, branches.
- `mk_specs`: Get the spec table of 1-4 products side by side, with stock counts.
- `mk_reviews`: Read customer reviews of a product (newest first) with store replies and the star breakdown.
- `mk_shipping`: Get the nearest delivery slot and shipping fee for one product: Tehran courier and post to other cities.
- `mk_branches`: List MasterKala's physical shops in Tehran with address, phone and map location.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `MASTERKALA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
