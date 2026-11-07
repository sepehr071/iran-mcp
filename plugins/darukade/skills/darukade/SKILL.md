---
name: darukade
description: "Read-only Darukade (darukade.com) pharmacy: products, prices, ingredients, usage, reviews. Use when the user asks about Darukade Pharmacy (darukade.com) or wants doctors, clinics, labs, appointments or pharmacy products in Iran."
---

# Darukade Pharmacy

Read-only Darukade (darukade.com) pharmacy: products, prices, ingredients, usage, reviews.

The tools below come from the `darukade-mcp` MCP server. If they are not available, install it with `claude mcp add darukade -- uvx darukade-mcp`, or add `"darukade": {"command": "uvx", "args": ["darukade-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dr_search`: Search Darukade's pharmacy catalog (supplements, cosmetics, baby) by words, category, brand, form, price or stock.
- `dr_cheapest`: List the lowest-priced products of a category, brand or search, cheapest first, skipping unpriced items.
- `dr_product`: Get one product's price per variant, stock, brand, ingredients, usage and dosage, warnings and properties.
- `dr_reviews`: Get a product's user comments and its questions with the pharmacy's answers, plus the rating summary.
- `dr_related`: List products related to one: alternatives, similar, same-brand and complementary ones, with prices.
- `dr_categories`: List Darukade's product categories with the ids that dr_search and dr_cheapest take as `category`.
- `dr_brands`: Find a brand by name and get the id that dr_search and dr_cheapest take as `brand`, or read a brand's profile.
- `dr_forms`: List product forms (capsule, tablet, syrup, cream, spray, ampoule ...) with the ids dr_search takes as `form`.
- `dr_compare`: Compare 2 to 5 products side by side: price, stock, rating, properties, ingredient amounts and dosage.
- `dr_home`: Show what Darukade's home page promotes now: golden offers, newest, best-selling and most-loved products.
- `dr_articles`: Search the Darukade health magazine (illnesses, supplements, skin, drugs).
- `dr_article`: Read one Darukade magazine article as plain text, with its author, sources and the products it recommends.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DARUKADE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Product text is the shop's, not medical advice: tell the user to ask a doctor or pharmacist.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
