---
name: iran-brokers
description: "Read-only Iran broker data from Mofid and Agah: stocks, funds, options, bonds, gold, education. Use when the user asks about Iran Brokers Market Data (emofid.com) or wants stock exchange quotes, company filings, funds, bonds or commodity exchange trades in Iran."
---

# Iran Brokers Market Data

Read-only Iran broker data from Mofid and Agah: stocks, funds, options, bonds, gold, education.

The tools below come from the `iran-brokers-mcp` MCP server. If they are not available, install it with `claude mcp add iran-brokers -- uvx iran-brokers-mcp`, or add `"iran-brokers": {"command": "uvx", "args": ["iran-brokers-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `br_screener`: Filter, sort and compare all stocks or funds on any column, like Agah's screener pages (900 stocks, 330 ETFs, 475 funds).
- `br_stocks`: Rank all listed stocks (about 750) by today's change, traded value, money flow, buyer power, queue or past returns.
- `br_stock_events`: List a stock's cash dividend history, capital increases, recent exchange notices and major shareholders.
- `br_technical`: Show Agah's technical-indicator summary (moving averages and oscillators vote, RSI, MACD and others) for a stock or industry.
- `br_mofid_funds`: List the 19 investment funds managed under the Mofid brand with type, risk level, dividend policy and asset mix.
- `br_bonds`: List exchange-traded bonds, sukuk and treasury bills with maturity, coupon, price and yield to maturity.
- `br_news`: Return the newest market news items: exchange notices, Codal letters, Telegram channel posts or Mofid research reports.
- `br_announcements`: Search Codal filings (financial statements, board notices, AGM invitations, monthly activity) by company, report type and date.
- `br_scores`: Return Bourse View's valuation scores: theoretical vs market price, a Buy/Neutral/Sell technical rating and a fundamental score out of 10.
- `br_quotes`: Return live price rows for 1 to 30 symbols at once: last and closing price, change, volume, limits, bid and ask, returns.
- `br_market_top`: Return one of the market's live top-N lists (most traded, buy queues, best return, lowest P/E, net individual buying, ...).
- `br_search`: Find the id of a stock, fund, option or index by name or symbol, in Mofid and Agah.
- `br_stock`: Show one stock (or, on Mofid, an ETF) in detail: price, ratios, returns, real vs legal flows, from Mofid and Agah.
- `br_history`: Return price history of a stock: Mofid OHLC candles (1 minute to weekly) or Agah daily rows with buy and sell flows.
- `br_market`: Show today's market snapshot: indices, traded value, money flow and buy/sell queues, from Mofid and Agah.
- `br_industries`: Rank the bourse industries by value, return, market cap, P/E or money flow, from Mofid and Agah.
- `br_index`: Show a market index (Mofid: market cap, free float, ratios, intraday move, members) and its daily history.
- `br_etfs`: List exchange-traded funds with price, NAV and the gap between them (bubble), traded value and returns.
- `br_learn`: Search the Mofid learning blog and Agah Pedia for bourse, fund, option and gold explainers, or read one article.
- `br_fund`: Show an investment fund from Agah: type, NAV, returns, asset mix and holdings, a daily history, or a side-by-side comparison.
- `br_options`: List stock-option contracts (about 1,600) with strike, expiry, moneyness, open interest and flows, or show one contract.
- `br_rates`: Return free-market prices of currencies, crypto, coins, 18k gold, the global ounce, oil and metals, or one code's daily history.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_BROKERS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Prices are Rial (divide by 10 for Toman), not Toman. Sites: Mofid (emofid.com), Agah (agah.com).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
