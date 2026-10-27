---
name: iran-gold
description: "Unofficial read-only live 18k gold prices on Iranian sites: Milli.gold, Wallgold, Melligold, Daric. Use when the user asks about Iran Gold Prices (milli.gold) or wants live gold, coin, currency or crypto prices in Iran."
---

# Iran Gold Prices

Unofficial read-only live 18k gold prices on Iranian sites: Milli.gold, Wallgold, Melligold, Daric.

The tools below come from the `iran-gold-mcp` MCP server. If they are not available, install it with `claude mcp add iran-gold -- uvx iran-gold-mcp`, or add `"iran-gold": {"command": "uvx", "args": ["iran-gold-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `gold_prices`: Compare the live 18k melted-gold price on Milli.gold, Wallgold, Melligold and Daric, in Toman per gram.
- `gold_milli_history`: Get the Milli.gold 18k gold price series for a day, week or month, with high, low and change.
- `gold_milli_stats`: Get Milli.gold's headline numbers: users, trades, gold traded, gold held and branches.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_GOLD_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- gold_prices is Toman per gram; gold_milli_history is Rial per milligram (x100 = Toman per gram). Each price is that platform's own quote and excludes its trading fee (often about 0.5 %). Sites: Milli.gold, Wallgold, Melligold, Daric.
