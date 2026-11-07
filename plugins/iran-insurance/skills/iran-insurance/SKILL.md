---
name: iran-insurance
description: "Read-only Iran insurance: BimeBazar and Azki side by side. Quotes, ratings, travel prices, guides. Use when the user asks about Iran Insurance (BimeBazar + Azki) (bimebazar.com) or wants insurance quotes, insurer ratings or how an insurance line works in Iran."
---

# Iran Insurance (BimeBazar + Azki)

Read-only Iran insurance: BimeBazar and Azki side by side. Quotes, ratings, travel prices, guides.

The tools below come from the `iran-insurance-mcp` MCP server. If they are not available, install it with `claude mcp add iran-insurance -- uvx iran-insurance-mcp`, or add `"iran-insurance": {"command": "uvx", "args": ["iran-insurance-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ins_azki_company`: Read what Azki publishes about an insurance company: profile facts, FAQ, claim help, or one product page.
- `ins_azki_blog`: Read posts from the Azki insurance blog (azki.com/blog, Persian), newest first, 10 per page.
- `ins_azki_products`: List the insurance products Azki sells through its generic product engine (30 types such as life, elevator, fire).
- `ins_azki_car_value`: Estimate a car's market value the way Azki does before pricing body insurance.
- `ins_azki_body_options`: List the optional covers and no-claim discount steps one company offers for car body insurance.
- `ins_insurer_reviews`: Read BimeBazar customer reviews of insurers: four 1-5 ratings and the text, newest first.
- `ins_claim_centers`: Find insurers' damage-claim branches with address, phone numbers and map position, filtered by insurer, place and claim type.
- `ins_glossary`: Look up short explanations of insurance and car-card terms (VIN, chassis number, liability cover and more).
- `ins_quote_third_party`: Get live third-party (شخص ثالث) car insurance prices from every insurer BimeBazar sells, cheapest first.
- `ins_quote_motorcycle`: Get live motorcycle third-party insurance prices from every insurer, cheapest first.
- `ins_quote_car_body`: Get live car body (بدنه) insurance prices from every insurer, cheapest first.
- `ins_quote_fire`: Get live home fire insurance (آتش‌سوزی) prices from every insurer, cheapest first.
- `ins_quote_health`: Get live supplementary health (تکمیلی درمان) insurance prices for one person, several people or a family.
- `ins_insurers`: List insurers with each marketplace's own ratings, side by side (BimeBazar and Azki).
- `ins_vehicles`: Find brand and model identifiers in BimeBazar's and Azki's vehicle catalogs, side by side.
- `ins_places`: Look up provinces and cities with each marketplace's own identifiers, side by side.
- `ins_quote_travel`: Get live travel insurance prices from BimeBazar and Azki for the same trip, cheapest first per provider.
- `ins_content`: Read what BimeBazar and Azki publish about one insurance line: short explanation, guide steps and FAQ.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_INSURANCE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- BimeBazar allows about 25 to 30 calls a minute per IP; a travel comparison uses about five. Do not loop. Sites: BimeBazar, Azki.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
