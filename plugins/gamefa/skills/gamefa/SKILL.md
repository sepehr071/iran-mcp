---
name: gamefa
description: "Read-only Gamefa (gamefa.com) Persian game and film site: news, scored reviews, profiles, releases. Use when the user asks about Gamefa (gamefa.com) or wants game and film news, reviews or release dates in Iran."
---

# Gamefa

Read-only Gamefa (gamefa.com) Persian game and film site: news, scored reviews, profiles, releases.

The tools below come from the `gamefa-mcp` MCP server. If they are not available, install it with `claude mcp add gamefa -- uvx gamefa-mcp`, or add `"gamefa": {"command": "uvx", "args": ["gamefa-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `gf_search_articles`: Search Gamefa's news, reviews and features by keyword, newest matches first.
- `gf_latest_articles`: List the newest Gamefa articles, optionally for one section such as news, reviews, trailers or pc.
- `gf_article`: Read one Gamefa article as plain text, with the editors' score box when it is a review.
- `gf_reviews`: List Gamefa's game reviews newest first, each with the editors' score out of 10, label, pros and cons.
- `gf_popular`: List the most viewed Gamefa articles of the past week, month, season or year, most viewed first.
- `gf_games`: Browse or search Gamefa's game profiles with the editors' score, user score, genres, platforms and release date.
- `gf_upcoming_games`: List games that have not been released yet, soonest first (Gamefa's release calendar), with ISO release dates.
- `gf_films`: Browse or search Gamefa's film and TV series profiles with IMDb score, user score, genres, director and release date.
- `gf_game`: Get one game's Gamefa profile: editors' score, user score and votes, Metacritic, release date, description.
- `gf_film`: Get one film or series profile: IMDb and user score, genres, cast, director, writers, countries, runtime, release date.
- `gf_terms`: Find the slug of a platform, genre, developer, publisher, film person or studio, or an article topic tag.
- `gf_comments`: Read the public reader comments under a Gamefa article or a game/film profile, with likes and dislikes.
- `gf_related`: List the articles Gamefa links to a game or film profile, or the games/films it shows as similar.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `GAMEFA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
