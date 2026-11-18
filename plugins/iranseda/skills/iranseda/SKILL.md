---
name: iranseda
description: "Read-only Iranseda (IRIB audio): radio channels, live streams, schedules, audiobooks, music, Quran. Use when the user asks about Iranseda Radio Archive (iranseda.ir) or wants online videos, TV channels and schedules or radio and audio archives in Iran."
---

# Iranseda Radio Archive

Read-only Iranseda (IRIB audio): radio channels, live streams, schedules, audiobooks, music, Quran.

The tools below come from the `iranseda-mcp` MCP server. If they are not available, install it with `claude mcp add iranseda -- uvx iranseda-mcp`, or add `"iranseda": {"command": "uvx", "args": ["iranseda-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sd_library_search`: Search Iranseda's audiobooks, music, kids, speeches, nava and Quran recitations.
- `sd_library_item`: Get an audiobook, song, speech, nava or recitation's details and its tracks.
- `sd_library_file`: Get the mp3 and mp4 download links and sizes of one library track.
- `sd_channels`: List IRIB radio channels with the program playing now.
- `sd_live_now`: Get a radio channel's public live stream URL and what is on now and next.
- `sd_schedule`: List a radio channel's programs for one day, with episode ids.
- `sd_search_programs`: Find programs of one radio channel by name (the site has no global search).
- `sd_program`: Get a radio program's description, broadcast time and its latest episodes.
- `sd_episode`: Get one episode's date, description and the audio file URL of each part.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRANSEDA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
