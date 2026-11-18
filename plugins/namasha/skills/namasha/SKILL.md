---
name: namasha
description: "Read-only Namasha (namasha.com) Iranian video platform: search, videos, channels, categories. Use when the user asks about Namasha Videos (namasha.com) or wants online videos, TV channels and schedules or radio and audio archives in Iran."
---

# Namasha Videos

Read-only Namasha (namasha.com) Iranian video platform: search, videos, channels, categories.

The tools below come from the `namasha-mcp` MCP server. If they are not available, install it with `claude mcp add namasha -- uvx namasha-mcp`, or add `"namasha": {"command": "uvx", "args": ["namasha-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `nm_search`: Search Namasha videos by text.
- `nm_video`: Get one Namasha video: title, description, views, likes, comment count, duration, upload date, tags, channel.
- `nm_related`: List the videos Namasha suggests next to a video (page 1 about 12, later pages 20 each).
- `nm_comments`: List the public comments of a video (text, author, age, likes; replies follow their parent).
- `nm_channel`: Get a Namasha channel: name, verified flag, description, creation date, links.
- `nm_channel_videos`: List a channel's videos, newest first (60 per page).
- `nm_featured`: List the videos on Namasha's home page: editors' picks or the special row.
- `nm_categories`: List Namasha's video categories with the slug nm_category_videos takes.
- `nm_category_videos`: List the newest videos of a category (60 per page).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `NAMASHA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
