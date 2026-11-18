---
name: iran-roads
description: "Read-only Iran road status (141.ir): bulletins, closures, restrictions, road works, weather. Use when the user asks about Iran Roads (141.ir) or wants places, addresses, routes, travel times or road closures in Iran."
---

# Iran Roads

Read-only Iran road status (141.ir): bulletins, closures, restrictions, road works, weather.

The tools below come from the `iran-roads-mcp` MCP server. If they are not available, install it with `claude mcp add iran-roads -- uvx iran-roads-mcp`, or add `"iran-roads": {"command": "uvx", "args": ["iran-roads-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `rd_provinces`: List the 31 provinces with the ids the other tools accept (and the province centre point).
- `rd_bulletin`: Latest official road weather and traffic status bulletin (northern axes, other axes) of the Road Maintenance Organization.
- `rd_closures`: List current road closures (blockades) with cause, direction, alternative route text and coordinates.
- `rd_restrictions`: List traffic restrictions announced by the traffic police (limited vehicle types or hours, road still open).
- `rd_workshops`: List road works (workshops) with work type, whether traffic can pass, period and alternative route.
- `rd_weather`: Current weather warnings for roads: hazard, affected provinces by day, and validity dates.
- `rd_main_routes`: List the 22 main intercity axes the 141 app tracks (Tehran-North, Tehran-Mashhad...) with endpoints.
- `rd_traffic_map`: Get the URL of the province's traffic status map image (updated by 141; the image shows live congestion).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_ROADS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Site: 141.ir (Iran Road Maintenance and Transportation Organization).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
