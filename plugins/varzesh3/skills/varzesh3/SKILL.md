---
name: varzesh3
description: "Read-only Varzesh3 (varzesh3.com) Iranian sports: live scores, tables, fixtures, teams, news. Use when the user asks about Varzesh3 Sports (varzesh3.com) or wants live scores, league tables, fixtures or sports news in Iran."
---

# Varzesh3 Sports

Read-only Varzesh3 (varzesh3.com) Iranian sports: live scores, tables, fixtures, teams, news.

The tools below come from the `varzesh3-mcp` MCP server. If they are not available, install it with `claude mcp add varzesh3 -- uvx varzesh3-mcp`, or add `"varzesh3": {"command": "uvx", "args": ["varzesh3-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `v3_scores`: Get the live scores, results and fixtures of one day across leagues.
- `v3_match`: Get one match: score, status, goals, cards, penalties, substitutions, lineups, referee, stadium, summary video.
- `v3_league`: List the football leagues with their ids, or get one league's current season id and past seasons with winners.
- `v3_standings`: Get a league table (rank, played, won, drawn, lost, goals, points, form), group tables or a cup bracket.
- `v3_league_matches`: Get a league's matches round by round: scores of played rounds and dates of coming ones.
- `v3_top_players`: Get the best players of a football (or futsal) league by one statistic, e.g. top scorers or most assists.
- `v3_team`: Get a football team's page: name, followers, recent form, squad by position and optionally transfers.
- `v3_team_matches`: Get a football team's latest results or upcoming matches across all competitions.
- `v3_news`: Get Varzesh3 news headlines with a short summary: latest, most read, most commented, or about a team, league, player, match or sport.
- `v3_article`: Read one news story: title, publish time, full text (up to 6000 characters), tags and the match it is about.
- `v3_videos`: Get Varzesh3 videos (goals, match summaries, interviews): latest, or about one team, league, match or player.
- `v3_search`: Search Varzesh3 for teams, people, leagues, news and videos by name; the way to turn a name into an id.
- `v3_player`: Get a player's profile (team, position, shirt number, age, country) with his latest news and videos.
- `v3_team_players`: Get the season statistics of one football team's players: goals, assists, appearances, minutes, cards.
- `v3_head_to_head`: Get the past meetings of two football teams with a won/drawn/lost summary for team_id.
- `v3_transfers`: Get the football transfer list of a window, club by club: players signed and players who left.
- `v3_tv_schedule`: Get the live broadcast schedule (جدول پخش زنده) of sports matches for the next days, with start times and stream links.
- `v3_league_stats`: Get a football league's season statistics: goals per match, cards per match, goal timing, streak notes and team rankings.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `VARZESH3_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
