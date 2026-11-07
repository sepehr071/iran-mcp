---
name: ime
description: "Read-only Iran Mercantile Exchange (ime.co.ir): physical trades, supply, prices, market totals. Use when the user asks about Iran Mercantile Exchange (ime.co.ir) or wants stock exchange quotes, company filings, funds, bonds or commodity exchange trades in Iran."
---

# Iran Mercantile Exchange

Read-only Iran Mercantile Exchange (ime.co.ir): physical trades, supply, prices, market totals.

The tools below come from the `ime-mcp` MCP server. If they are not available, install it with `claude mcp add ime -- uvx ime-mcp`, or add `"ime": {"command": "uvx", "args": ["ime-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ime_categories`: List the exchange's commodity groups: main groups, then groups, then subgroups, with their ids.
- `ime_producers`: Find producers and suppliers listed on the exchange by name, to get the producer id for the trade and supply tools.
- `ime_trades`: List commodity trades (price, volume, supply, demand, buyer broker) for a date range, with totals.
- `ime_supply`: List supply offers (اطلاعیه عرضه): what is up for sale on which session, volume and base price.
- `ime_price_history`: Daily price series (low, high, volume-weighted average, volume) per symbol over a date range.
- `ime_market_summary`: Exchange-wide trade value and volume for a date range: by market, by physical-market hall, plus the USD rate.
- `ime_daily_totals`: Day-by-day trade value and volume of one market over a date range (the site's market chart).
- `ime_news`: Latest news and notices from the exchange's news archive: title, lead, date and link.
- `ime_trade_stats`: Rank producers, commodities, brokers or halls by traded value over a date range, with each one's market share.
- `ime_weekly_reports`: List the exchange's weekly market reports (گزارش هفتگی), newest first, with the PDF link of each.
- `ime_options`: Options on gold, gold coin, gold funds and saffron futures (اختیار معامله): one day's board or one contract's history.
- `ime_securities`: Daily trades of the exchange's financial-market symbols: salaf, commodity deposit certificates and commodity funds.
- `ime_certificates`: Continuous commodity deposit certificates (گواهی سپرده پیوسته): gold bar, gold coin, silver, copper, steel and more.
- `ime_board`: Market-view board (cdn.ime.co.ir) with the best bid and ask: use it to see where a fund or certificate trades now.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IME_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Prices are Rial, not Toman (per kg for goods listed in tonnes; check `unit`). `value_k_rial` is thousand Rial, market summaries million Rial. Date ranges are limited to 45 days. ime.co.ir answers only Iranian connections; outside Iran the user needs IME_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
