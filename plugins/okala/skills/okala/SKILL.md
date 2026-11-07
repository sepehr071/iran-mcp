---
name: okala
description: "Unofficial read-only Okala: grocery stores that deliver to you, compare prices across stores. Use when the user asks about Okala (okala.com) or wants food or groceries delivered in Iran."
---

# Okala

Unofficial read-only Okala: grocery stores that deliver to you, compare prices across stores.

The tools below come from the `okala-mcp` MCP server. If they are not available, install it with `claude mcp add okala -- uvx okala-mcp`, or add `"okala": {"command": "uvx", "args": ["okala-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ok_login`: Log in to the user's Okala account, unlocking real text search in ok_search.
- `ok_login_verify`: Finish a login started with ok_login with the SMS code.
- `ok_account`: Whether the server is logged in to Okala (phone masked); guest = category-only ok_search.
- `ok_logout`: Delete the saved Okala login on this machine; the server continues as a guest.
- `ok_categories`: Category tree (id, slug, Persian name, children) of everything sold near a point, or in one store.
- `ok_search`: Find products by text near a point (or in one store with store_id), best matches first, then cheapest (Toman).
- `ok_compare`: Which open nearby store sells the same product cheapest: a category and/or brand, grouped by product id, each store's price cheapest first; products sold by most stores come first.
- `ok_store_products`: A whole category of one store, sorted and optionally filtered by name, prices in Toman.
- `ok_product`: One product in one store: price and discount (Toman), stock, max per order, brand, category, images and description.
- `ok_brands`: Brand ids for ok_compare (`brand_id`) and slugs.
- `ok_deals`: Deal rows running now, with end time (UTC) and top products (Toman).
- `ok_offer`: Every product of one deal row (from ok_deals), Toman.
- `ok_locate`: Turn an address into coordinates (lat, lon) for every other tool, plus the street address of the best hit.
- `ok_stores`: Okala stores that deliver to a point, in the site's order: id, type, rating, distance, earliest slot and per-order fees (service, packaging, delivery; Toman).
- `ok_store`: One store as seen from the delivery point: whether it delivers there now, minimum order (Toman), rating, distance, location, earliest slot and open delivery slots of the next days (Tehran time).
- `ok_store_reviews`: Read customers' reviews of a store: 1-5 stars, comment, date and the reasons they ticked.

## Rules

- This server acts on the user's own account (a login from the chat with its `*_login` tool). Confirm with the user before any call that creates, sends, edits or deletes something.
- On timeouts or HTTP 403 outside Iran, set `OKALA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- One exception to no login: real text search needs the optional SMS login (`ok_login`), which stays read-only. Ask the user before starting it.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
