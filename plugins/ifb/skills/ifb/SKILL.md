---
name: ifb
description: "Read-only Iran Fara Bourse (ifb.ir): bond, sukuk and treasury yields, IPOs, notices, market stats. Use when the user asks about Iran Fara Bourse (ifb.ir) or wants stock exchange quotes, company filings, funds, bonds or commodity exchange trades in Iran."
---

# Iran Fara Bourse

Read-only Iran Fara Bourse (ifb.ir): bond, sukuk and treasury yields, IPOs, notices, market stats.

The tools below come from the `ifb-mcp` MCP server. If they are not available, install it with `claude mcp add ifb -- uvx ifb-mcp`, or add `"ifb": {"command": "uvx", "args": ["ifb-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ifb_search`: Find Iran Fara Bourse instruments (stocks, bonds, sukuk, treasury bills, funds, options) by symbol or name.
- `ifb_yields`: List fixed-income papers on Fara Bourse with last price, maturity and yield to maturity (YTM), filtered and ranked.
- `ifb_instrument`: Describe one Fara Bourse instrument: name, ISIN, market, and for bonds the coupon rate, maturity, issuer, guarantor and payment schedule.
- `ifb_quote`: Get the live trading data of one instrument: last and closing price, change, volume, value, order book, and YTM for bonds.
- `ifb_history`: Get daily price history of one instrument: first, high, low and closing price and volume per trading day, newest first.
- `ifb_ipos`: List Fara Bourse initial public offerings (IPOs): finished ones with price and volume, or those upcoming and under way.
- `ifb_underwritings`: List securities offered through underwriting (پذیره‌نویسی) on Fara Bourse, newest first.
- `ifb_announcements`: Search Fara Bourse announcements, news and market messages by keyword and date, newest first.
- `ifb_article`: Read the text of one Fara Bourse news article (weekly trading statistics, listings, rule changes).
- `ifb_market_summary`: Summarise the Fara Bourse session: index, bond indices, total turnover, and each market's value traded with its top movers.
- `ifb_yield_curve`: Get Fara Bourse's fitted yield curves (Svensson/Nelson model) for government papers, non-government papers and treasury bills.
- `ifb_sukuk_flows`: Show daily trading value of Islamic financial securities (sukuk, treasury bills) by who bought and sold, newest day first.
- `ifb_market_watch`: Show the live Fara Bourse market watch: every symbol's price, change, volume and best bid and ask, ranked and filtered.
- `ifb_index_history`: Get the daily history of a Fara Bourse index since 2009, with change over a day, week, month and year.
- `ifb_corporate_actions`: List corporate actions on Fara Bourse: capital increases under way, board transfers, and moves to or from the Tehran Stock Exchange.
- `ifb_halted`: List the symbols halted on Fara Bourse with the date and reason, or the issuers flagged for weak disclosure.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IFB_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Prices are Rial, not Toman; yields are percent a year; dates Jalali. ifb.ir answers only Iranian connections; outside Iran the user needs IFB_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
