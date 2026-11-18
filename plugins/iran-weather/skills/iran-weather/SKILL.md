---
name: iran-weather
description: "Read-only Iran Meteorological Org (irimo.ir): city forecasts, observations, warnings. Use when the user asks about Iran Weather (irimo.ir) or wants weather forecasts, observations or weather warnings in Iran."
---

# Iran Weather

Read-only Iran Meteorological Org (irimo.ir): city forecasts, observations, warnings.

The tools below come from the `iran-weather-mcp` MCP server. If they are not available, install it with `claude mcp add iran-weather -- uvx iran-weather-mcp`, or add `"iran-weather": {"command": "uvx", "args": ["iran-weather-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `wx_cities`: Today's forecast (condition, max and min temperature) for the main cities (about 35), with the ids wx_weather accepts.
- `wx_weather`: Current observation and 3-day forecast for one city or weather station.
- `wx_province`: Latest observations of every weather station in the province of a city.
- `wx_observations`: Current temperature, humidity and wind at the ~37 stations on the national map of irimo.ir.
- `wx_warnings`: Latest official warnings of the Iran Meteorological Organization, newest first.
- `wx_road`: Current weather of every city along a main road, from the road-weather service of irimo.ir.
- `wx_airports`: Aviation forecasts (TAF) of about 29 Iranian airports with their flight category (vfr, mvfr, ifr, lifr).
- `wx_bulletins`: Link to the latest official forecast bulletin (PDF): 5-day, weekly, seasonal, Tehran province or Tehran air quality.
- `wx_warning`: Full text of one warning: system description, start and end time, hazard, affected area, impact, advice.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_WEATHER_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Site: irimo.ir (Iran Meteorological Organization).

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
