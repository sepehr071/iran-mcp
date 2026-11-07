---
name: codal
description: "Read-only codal.ir: search disclosures of Iranian listed companies, read letters and statements. Use when the user asks about Codal (کدال) Disclosures (codal.ir) or wants stock exchange quotes, company filings, funds, bonds or commodity exchange trades in Iran."
---

# Codal (کدال) Disclosures

Read-only codal.ir: search disclosures of Iranian listed companies, read letters and statements.

The tools below come from the `codal-mcp` MCP server. If they are not available, install it with `claude mcp add codal -- uvx codal-mcp`, or add `"codal": {"command": "uvx", "args": ["codal-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `cd_search_letters`: Search codal.ir disclosures (letters) of Iranian listed companies, newest first, 20 per page.
- `cd_letter`: Read one codal.ir letter: its text or tables, plus links to its page, PDF, Excel and attachments.
- `cd_company`: Find companies and funds on codal.ir by symbol or name, with their market, industry and type.
- `cd_letter_types`: List codal.ir letter groups, or the letter types of one group with the ids cd_search_letters takes.
- `cd_financial_years`: List the fiscal year-end dates codal.ir knows for one company, newest first (Jalali).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `CODAL_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Report amounts are as published, usually million Rial (see `unit_note`), not Toman. codal.ir blocks an IP for up to an hour after a burst: make few, targeted calls, and stop when a tool says it is rate limiting. It often answers only Iranian connections; outside Iran the user needs CODAL_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
