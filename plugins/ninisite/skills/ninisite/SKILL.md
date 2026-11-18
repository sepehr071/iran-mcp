---
name: ninisite
description: "Read-only Ninisite (ninisite.com) parenting forum topics, articles and pregnancy weeks. Use when the user asks about Ninisite Parenting (ninisite.com) or wants Persian blog posts, forum topics or parenting articles in Iran."
---

# Ninisite Parenting

Read-only Ninisite (ninisite.com) parenting forum topics, articles and pregnancy weeks.

The tools below come from the `ninisite-mcp` MCP server. If they are not available, install it with `claude mcp add ninisite -- uvx ninisite-mcp`, or add `"ninisite": {"command": "uvx", "args": ["ninisite-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `nn_forums`: List every forum category and its forums (id and name) on ninisite.com/discussion.
- `nn_forum_topics`: List the topics of one forum, most recently active first; pinned admin topics come first on page 1.
- `nn_hot_topics`: List the site-wide hottest or recently updated forum topics.
- `nn_topic`: Read a forum topic: the opening post plus one page of replies (about 15 posts per page).
- `nn_article_categories`: List magazine article categories (ids for nn_articles); pass a top-level id to see its sub-categories.
- `nn_articles`: List magazine articles, newest first, for all categories or one category.
- `nn_article`: Read one magazine article: title, date, tags, text and counts.
- `nn_pregnancy_week`: Read the week-by-week pregnancy guide for one week: symptoms, nutrition, fetus size, care, checklist.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `NINISITE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Forum posts are users' own words, not medical advice: tell the user to ask a doctor.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
