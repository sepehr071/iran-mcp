---
name: time-ir
description: "Read-only Time.ir Iranian calendar: Jalali/Gregorian/Hijri dates, holidays, events, prayer times. Use when the user asks about Time.ir Calendar (time.ir) or wants Jalali, Gregorian or Hijri dates, holidays or prayer times in Iran."
---

# Time.ir Calendar

Read-only Time.ir Iranian calendar: Jalali/Gregorian/Hijri dates, holidays, events, prayer times.

The tools below come from the `time-ir-mcp` MCP server. If they are not available, install it with `claude mcp add time-ir -- uvx time-ir-mcp`, or add `"time-ir": {"command": "uvx", "args": ["time-ir-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ti_today`: Get today's date in the Jalali, Gregorian and Hijri calendars with the Tehran time, weekday, zodiac sign and today's events.
- `ti_convert_date`: Convert a date between the Jalali (Solar Hijri), Gregorian and Hijri (lunar) calendars, using time.ir's own converter.
- `ti_month`: Show one Jalali month: its Gregorian and Hijri month spans, weekday of day 1, holidays and every event of the month.
- `ti_events`: List the occasions (Persian: monasebat) and official holidays of one day, with a short description when time.ir has one.
- `ti_holidays`: List all official holidays (تعطیلات رسمی) of a Jalali year with Gregorian and Hijri dates and weekdays.
- `ti_upcoming_holidays`: List the next official holidays in Iran starting today (or from_date), with days until each.
- `ti_cities`: List Iran's provinces, or the cities of one province, with the ids ti_prayer_times takes.
- `ti_prayer_times`: Get the Islamic prayer times (اوقات شرعی) for an Iranian city and day: fajr, sunrise, noon, sunset, maghrib and Islamic midnight.
- `ti_qibla`: Get the qibla direction (bearing to the Kaaba in Mecca, degrees clockwise from true north) and distance for an Iranian city.
- `ti_on_this_day`: List today's historical events, birthdays and deaths of notable people, as Time.ir's "today" page shows them.
- `ti_search_events`: Search all occasions (monasebat) of a Jalali year by keyword and return each match with its dates.
- `ti_date_difference`: Count the days between two dates and give the span as Jalali years, months and days (age calculator).
- `ti_long_weekends`: Find runs of consecutive days off in a Jalali year: official holidays joined with Fridays (optionally Thursdays).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TIME_IR_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
