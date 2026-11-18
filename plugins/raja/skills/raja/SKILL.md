---
name: raja
description: "Read-only Raja (raja.ir) Iranian trains: stations, search with prices and seats, timetables, news. Use when the user asks about Raja Train Tickets (raja.ir) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Raja Train Tickets

Read-only Raja (raja.ir) Iranian trains: stations, search with prices and seats, timetables, news.

The tools below come from the `raja-mcp` MCP server. If they are not available, install it with `claude mcp add raja -- uvx raja-mcp`, or add `"raja": {"command": "uvx", "args": ["raja-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `rj_stations`: Find Raja railway stations and their codes by Persian or English name.
- `rj_search_trains`: Search one-way trains between two stations on a date, with prices in Toman and free seats.
- `rj_train_stops`: List every stop of a train with its time, from a row's `ref` of rj_search_trains.
- `rj_announcements`: Read the notices Raja shows at the top of its site: presale dates, refund rules, boarding rules.
- `rj_news`: List the latest Raja company news (title, Jalali date, id) or read one story's text by id.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `RAJA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
