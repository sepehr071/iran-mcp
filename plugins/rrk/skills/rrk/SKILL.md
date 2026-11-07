---
name: rrk
description: "Read-only Official Gazette of Iran (rrk.ir): search laws and rulings, read their text. Use when the user asks about Official Gazette of Iran (rrk.ir) or wants laws, regulations, court votes, legal opinions or Official Gazette texts in Iran."
---

# Official Gazette of Iran

Read-only Official Gazette of Iran (rrk.ir): search laws and rulings, read their text.

The tools below come from the `rrk-mcp` MCP server. If they are not available, install it with `claude mcp add rrk -- uvx rrk-mcp`, or add `"rrk": {"command": "uvx", "args": ["rrk-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `rk_exchange_offices`: List the licensed currency exchange offices (صرافی مجاز) the Central Bank published in the Official Gazette (rrk.ir).
- `rk_search_laws`: Search the Official Gazette's laws and regulations database (rrk.ir) by title, full text, group, approver, special number or gazette date.
- `rk_law_filters`: List the law groups (categories) and approving authorities that rk_search_laws can filter by.
- `rk_latest_laws`: List the newest laws, rulings and regulations published in the Official Gazette (rrk.ir), newest gazette first.
- `rk_law_text`: Read the full text of one law or ruling from the Official Gazette (rrk.ir): approver, gazette number and date, body.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `RRK_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- The portal is slow (a full-text search can take 10 s). Prefer one good query over many. It has no company registration notices.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
