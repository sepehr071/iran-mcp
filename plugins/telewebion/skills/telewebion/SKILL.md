---
name: telewebion
description: "Read-only Telewebion (telewebion.ir) IRIB TV: channels, what aired, programs, episodes, live sports. Use when the user asks about Telewebion TV (telewebion.ir) or wants online videos, TV channels and schedules or radio and audio archives in Iran."
---

# Telewebion TV

Read-only Telewebion (telewebion.ir) IRIB TV: channels, what aired, programs, episodes, live sports.

The tools below come from the `telewebion-mcp` MCP server. If they are not available, install it with `claude mcp add telewebion -- uvx telewebion-mcp`, or add `"telewebion": {"command": "uvx", "args": ["telewebion-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tv_channels`: List Telewebion live channels (TV, provincial, radio) with the id the other tools take.
- `tv_channel_schedule`: What aired on a channel on a day, oldest first, with start/end (Tehran time) and episode page URLs.
- `tv_live_now`: Show the most recent program on each channel of a group (national TV by default), with live page URLs.
- `tv_search`: Search programs (TV shows) and movies/series by title, with their page URLs.
- `tv_program`: Show a program's summary and its episodes, newest first, with episode page URLs.
- `tv_episode`: Show one episode: title, program, channel, air time (Tehran), duration, quality variants and page URL.
- `tv_live_events`: List sports broadcasts (football, volleyball, ...) scheduled or live on Telewebion that day, with page URLs.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TELEWEBION_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
