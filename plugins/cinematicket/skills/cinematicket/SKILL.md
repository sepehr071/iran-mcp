---
name: cinematicket
description: "Read-only Cinematicket (cinematicket.org): cinemas, films, showtimes, prices, theatre, box office. Use when the user asks about Cinematicket Tickets (cinematicket.org) or wants cinema showtimes or theatre, concert and event tickets in Iran."
---

# Cinematicket Tickets

Read-only Cinematicket (cinematicket.org): cinemas, films, showtimes, prices, theatre, box office.

The tools below come from the `cinematicket-mcp` MCP server. If they are not available, install it with `claude mcp add cinematicket -- uvx cinematicket-mcp`, or add `"cinematicket": {"command": "uvx", "args": ["cinematicket-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ct_cities`: List the cities Cinematicket sells tickets in, with the city ids other tools take.
- `ct_now_showing`: Films and shows on sale now, grouped by category, nationwide (the site's home feed).
- `ct_film`: Cast, director, genre, rating, duration, summary and sales of one film or show, plus how widely it is screened.
- `ct_cinemas`: Cinemas and venues in a city, most popular first, with rating, address, facilities and coordinates.
- `ct_cinema`: One cinema's info (address, phone, halls, rules) and its full program for a day: films, halls, times, prices (Toman).
- `ct_showtimes`: Where and when a film or show plays: cinemas, halls, times and ticket prices (Toman) for one day.
- `ct_upcoming`: Films announced as coming soon, with release dates (the site's next-programs page; it is often empty).
- `ct_events`: List theatre plays, concerts or films with sessions on sale, with rating and director.
- `ct_box_office`: Top-grossing films by total ticket sales (Toman), with audience figures, cinemas and weeks on screen.
- `ct_search`: Search films, shows and cinemas by name; returns ids for ct_film, ct_showtimes and ct_cinema.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `CINEMATICKET_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
