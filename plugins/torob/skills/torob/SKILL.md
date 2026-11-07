---
name: torob
description: "Unofficial read-only Torob: compare Iranian shop prices, price history, deal checks and baskets. Use when the user asks about Torob (torob.com) or wants electronics, appliances or other goods in Iran."
---

# Torob

Unofficial read-only Torob: compare Iranian shop prices, price history, deal checks and baskets.

The tools below come from the `torob-mcp` MCP server. If they are not available, install it with `claude mcp add torob -- uvx torob-mcp`, or add `"torob": {"command": "uvx", "args": ["torob-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tb_cheapest`: Cheapest trustworthy offer for a product named in words: searches, then looks at every shop's offer.
- `tb_compare`: Side-by-side comparison of 2-5 products: only the specs that differ, the price window, and which is cheapest.
- `tb_best_value`: Ranked product picks that fit a budget (Toman), for "best phone under 30 million".
- `tb_deal_check`: Is this a good price?
- `tb_basket`: Cheapest shop for a whole shopping list: best single shop that sells everything, and the split-cart total.
- `tb_product`: Full record of one product: name, price range (Toman), category, brand, key specs, cheapest offer.
- `tb_sellers`: Every online shop offer for a product, cheapest first, with trust, warranty, installment and delivery info.
- `tb_stores`: In-person shops that stock a product: address, opening hours, open now, shelf price and its age.
- `tb_presence`: How widely a product is sold: online shops, in-person stores, installment and warranty shops, price window.
- `tb_variants`: Sibling variants of a product (storage + RAM, colour, region ...) each with its own cheapest price.
- `tb_price_chart`: Price chart of a product (about a year, weekly): minimum and average price in Toman, with a buy-now verdict.
- `tb_price_history`: Notable price moves of a product, newest first, with the lowest and highest point.
- `tb_similar`: Products Torob shows as similar (alternatives in the same class), with cheapest price and shop count.
- `tb_product_url`: Clean torob.com URL for a product id, path or link (no request is sent).
- `tb_products_batch`: Short records (name, price window, shop counts, category, brand) for up to 10 products at once.
- `tb_search`: Search Torob for products; each card has the cheapest shop price (Toman) and the shop count.
- `tb_suggest`: Torob's autocomplete: up to 8 search phrases for typed text (fixes Finglish and colloquial wording).
- `tb_filters`: Which filters exist for a query/category: sub-categories, brands, price span, sort options, attributes.
- `tb_category`: A category page: its parents, sub-categories and top products.
- `tb_brands`: All brands of a category with their ids (for tb_search brand=).
- `tb_trends`: What people search on Torob right now, each with its category and one sample product.
- `tb_offers`: Torob's special-offers feed ("پیشنهاد ویژه"): themed rows with discounted or promoted products.
- `tb_cities`: City ids for `city` arguments (392 Tehran, 468 Mashhad, 240 Isfahan).
- `tb_shop`: A shop's trust profile: score and votes, e-Namad seal, time on Torob, city, website, delivery and payment terms.
- `tb_find_shops`: Find shops in Torob's directory by name or domain; returns ids for tb_shop and tb_shop_products.
- `tb_shop_products`: Products one shop sells on Torob, with the price range of the page.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TOROB_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Torob blocks bursts of calls from one IP (HTTP 490), so calls are spaced 2 s apart. Ask for a few products at a time and do not repeat a search the user did not ask for.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
