---
name: virgool
description: "Read-only Virgool (virgool.ir) Persian blog platform: search, posts, authors, topics, publications. Use when the user asks about Virgool Blog (virgool.io) or wants Persian blog posts, forum topics or parenting articles in Iran."
---

# Virgool Blog

Read-only Virgool (virgool.ir) Persian blog platform: search, posts, authors, topics, publications.

The tools below come from the `virgool-mcp` MCP server. If they are not available, install it with `claude mcp add virgool -- uvx virgool-mcp`, or add `"virgool": {"command": "uvx", "args": ["virgool-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `vg_search`: Search Virgool posts, authors, publications or tags.
- `vg_post`: Read one Virgool post: title, author, topics, tags, counts and the full story text (images are skipped).
- `vg_comments`: List the public top-level comments of a post, or the replies of one comment (`replies` counts them).
- `vg_user`: Get an author's public profile (bio, followers, post count, links) and the publications they belong to.
- `vg_user_posts`: List an author's published posts, newest first.
- `vg_feed`: List Virgool's front-page posts: editors' picks or the newest posts.
- `vg_topics`: List all Virgool topics (broad categories) with follower counts. vg_topic_posts takes `name` or `fa_name`.
- `vg_topic_posts`: List the latest posts of a topic (category) such as book, economy or psychology.
- `vg_tag_posts`: List the latest posts carrying a tag.
- `vg_publications`: Search or list Virgool publications (group blogs). vg_publication_posts reads one by its `name`.
- `vg_publication_posts`: List the latest posts of a publication, newest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `VIRGOOL_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
