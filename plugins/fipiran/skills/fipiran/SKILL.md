---
name: fipiran
description: "Read-only Fipiran (fipiran.ir) data on Iranian mutual funds and ETFs: NAV, returns, size, managers. Use when the user asks about Fipiran Funds (fipiran.ir) or wants stock exchange quotes, company filings, funds, bonds or commodity exchange trades in Iran."
---

# Fipiran Funds

Read-only Fipiran (fipiran.ir) data on Iranian mutual funds and ETFs: NAV, returns, size, managers.

The tools below come from the `fipiran-mcp` MCP server. If they are not available, install it with `claude mcp add fipiran -- uvx fipiran-mcp`, or add `"fipiran": {"command": "uvx", "args": ["fipiran-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `fp_search_funds`: Search Iranian mutual funds and ETFs by name, type or manager, and rank them by return or size.
- `fp_fund_types`: List fund types (equity, fixed income, gold, mixed...) with fund counts, total size and average returns.
- `fp_fund`: Get one fund in full: NAV, returns, size, allocation, investors, manager, auditor, custodian, website.
- `fp_history`: Get a fund's daily history: NAV, returns, size and flows, investor mix or dividends, at most 60 points.
- `fp_compare`: Put 2 to 8 funds side by side: type, size, NAV, returns for every period, allocation, manager.
- `fp_managers`: Rank fund management companies by total assets under management, with their fund count and typical return.
- `fp_indices`: Show the Tehran and Farabourse market summary and rank the 65 market and industry indices by return.
- `fp_index_history`: Get the daily history of one market or industry index, oldest first, at most 60 evenly spaced points.
- `fp_stocks`: Search and rank listed shares traded on the last trading day: top gainers, losers, most traded, by industry.
- `fp_stock`: Get one listed share in full: last trade, range, order book, buyers and sellers, period returns, industry.
- `fp_industries`: Rank the stock-market industries by trading on the last day: traded value, volume, number of trades.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `FIPIRAN_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- NAV is Rial per unit and fund sizes are billion Toman; returns are percent per period, not annualised. fipiran.ir answers only Iranian connections; outside Iran the user needs FIPIRAN_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
