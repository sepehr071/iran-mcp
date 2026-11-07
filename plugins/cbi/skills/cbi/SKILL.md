---
name: cbi
description: "Read-only Central Bank of Iran (cbi.ir): official FX rates, inflation, policy rates, news. Use when the user asks about Central Bank of Iran (cbi.ir) or wants official exchange rates, inflation, unemployment or other economic statistics in Iran."
---

# Central Bank of Iran

Read-only Central Bank of Iran (cbi.ir): official FX rates, inflation, policy rates, news.

The tools below come from the `cbi-mcp` MCP server. If they are not available, install it with `claude mcp add cbi -- uvx cbi-mcp`, or add `"cbi": {"command": "uvx", "args": ["cbi-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `cb_exchange_rates`: Get the Central Bank of Iran's official reference exchange rates for one day, in rials per currency unit.
- `cb_rate_history`: Get the official CBI rate of one currency over time, oldest first, with the total change.
- `cb_inflation`: Get Iran's inflation rate as published by the Central Bank: the monthly series for one year and annual history.
- `cb_policy_rates`: Get the Central Bank's weekly interest rates: interbank market rate and the standing-facility corridor.
- `cb_news`: List the Central Bank's latest news and announcements (title, date, id), optionally filtered by a word.
- `cb_news_item`: Read one Central Bank news item or announcement in full: title, date, text and attached files.
- `cb_liquidity`: Get Iran's liquidity (نقدینگی, M2) as numbers from the newest monthly report, plus the latest statements on it.
- `cb_publications`: List the newest Central Bank publications of one kind with download links (PDF/Excel), newest first.
- `cb_statistics`: Read one table of the Central Bank's monthly statistics Excel file as rows of numbers and Persian labels.
- `cb_bond_auctions`: Get the results of the Central Bank's weekly government Islamic securities (sukuk) auctions: sold amounts and yields.
- `cb_open_market`: List the Central Bank's weekly open market operation reports and read the newest one's repo auction figures.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `CBI_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Exchange rates are Rial per currency unit (`per_units`: JPY 100, KRW 1000), not Toman. Dates are Jalali.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
