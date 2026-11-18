---
name: aparat
description: "Read-only Aparat (aparat.com) Iranian video platform: search, videos, channels, trending, comments. Use when the user asks about Aparat Videos (aparat.com) or wants online videos, TV channels and schedules or radio and audio archives in Iran."
---

# Aparat Videos

Read-only Aparat (aparat.com) Iranian video platform: search, videos, channels, trending, comments.

The tools below come from the `aparat-mcp` MCP server. If they are not available, install it with `claude mcp add aparat -- uvx aparat-mcp`, or add `"aparat": {"command": "uvx", "args": ["aparat-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `apr_search`: Search Aparat videos and channels by text.
- `apr_video`: Get one Aparat video: title, description, views, likes, duration, tags, category, channel, publish date.
- `apr_comments`: Read the top comments under an Aparat video (10 per page, most liked first as the site orders them).
- `apr_related`: List videos Aparat recommends next to a video (about 10).
- `apr_channel`: Get an Aparat channel: name, followers, video count, total views, description, start date.
- `apr_channel_videos`: List a channel's videos, newest first or most viewed (10 per page).
- `apr_categories`: List the category names Aparat's trending tabs use.
- `apr_trending`: List trending Aparat videos, overall or in one category (up to 40).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `APARAT_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
