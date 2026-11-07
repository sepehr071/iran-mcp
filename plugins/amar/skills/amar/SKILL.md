---
name: amar
description: "Read-only Statistical Centre of Iran (amar.org.ir): CPI inflation, unemployment, census, any table. Use when the user asks about Statistical Centre of Iran (amar.org.ir) or wants official exchange rates, inflation, unemployment or other economic statistics in Iran."
---

# Statistical Centre of Iran

Read-only Statistical Centre of Iran (amar.org.ir): CPI inflation, unemployment, census, any table.

The tools below come from the `amar-mcp` MCP server. If they are not available, install it with `claude mcp add amar -- uvx amar-mcp`, or add `"amar": {"command": "uvx", "args": ["amar-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `am_inflation`: Get Iran's official consumer price index (CPI) and inflation from the Statistical Centre of Iran, latest first.
- `am_inflation_groups`: Compare official inflation across CPI groups (food, housing, transport, health...) for one month.
- `am_labour_force`: Get Iran's official unemployment and labour-force participation rates by quarter, latest first.
- `am_population`: Get population and households by province, or by county within one province, from Iran's 1395 census.
- `am_table`: Read an Excel table of a statistical release as compact rows (works for any release with an xlsx/xls file).
- `am_indicators`: Read the Centre's monthly macro-indicators workbook: trade, housing, money, budget, prices by decile and more.
- `am_gdp`: Get Iran's official GDP growth by quarter or year, with the main sectors, latest first.
- `am_ppi`: Get Iran's producer price index (PPI, factory-gate prices) by quarter and sector, latest first.
- `am_search`: Search the Statistical Centre of Iran (amar.org.ir) catalog of releases: tables, time series, reports.
- `am_release`: Get one statistical release from amar.org.ir: title, topic path, period and its downloadable files.
- `am_calendar`: Get the Statistical Centre of Iran's publishing calendar: which statistics come out on which day of a month.
- `am_news`: List the latest news and press releases of the Statistical Centre of Iran, or read one item.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `AMAR_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- amar.org.ir answers only Iranian connections; outside Iran the user needs AMAR_MCP_PROXY. GDP levels are billion Rial.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
