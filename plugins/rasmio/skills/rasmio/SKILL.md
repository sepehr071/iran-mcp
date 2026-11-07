---
name: rasmio
description: "Read-only Rasmio (rasmio.com): Iranian companies, board members, gazette ads, products, brands. Use when the user asks about Rasmio Company Registry (rasmio.com) or wants registered companies, their board members, gazette ads, products or brands in Iran."
---

# Rasmio Company Registry

Read-only Rasmio (rasmio.com): Iranian companies, board members, gazette ads, products, brands.

The tools below come from the `rasmio-mcp` MCP server. If they are not available, install it with `claude mcp add rasmio -- uvx rasmio-mcp`, or add `"rasmio": {"command": "uvx", "args": ["rasmio-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `rs_company`: Registry profile of one Iranian company: basics, board and CEO, shareholders, licenses, capital history, ads.
- `rs_ad`: Full text of one official gazette (روزنامه رسمی) ad: board changes, capital changes, founding, liquidation.
- `rs_person`: Companies one person manages, sits on the board of or audits, with role dates and their latest gazette ads.
- `rs_product`: One registered product: full specs (HS/ISIC codes, brand, maker, country), category and comparable suppliers.
- `rs_ip`: Registration details of an Iranian trademark, patent or industrial design: numbers, date, owner, description.
- `rs_search_companies`: Search Iranian companies by name or activity with filters; returns national ids for rs_company.
- `rs_search`: Search people (board members, managers), products, registered brands or patents and industrial designs.
- `rs_options`: List the ids and names the search filters take: legal forms, licenses, product categories, brand classes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `RASMIO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Money is Rial, not Toman. Dates are Jalali.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
