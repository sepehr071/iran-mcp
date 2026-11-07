---
name: quera
description: "Read-only Quera (quera.org): Iranian tech jobs, companies, contests, problems, courses and blog. Use when the user asks about Quera (quera.org) or wants job ads, employers or salaries in Iran."
---

# Quera

Read-only Quera (quera.org): Iranian tech jobs, companies, contests, problems, courses and blog.

The tools below come from the `quera-mcp` MCP server. If they are not available, install it with `claude mcp add quera -- uvx quera-mcp`, or add `"quera": {"command": "uvx", "args": ["quera-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `qr_jobs`: Search open tech jobs on Quera Magnet, 15 per page.
- `qr_job`: Get one Quera job posting in full: description, requirements, benefits, skills, salary, deadline.
- `qr_job_filters`: List the filter values qr_jobs and qr_companies accept: cities, industries, sizes, popular tech codes.
- `qr_companies`: Search the 3,000+ companies with a Quera Magnet profile, 15 per page.
- `qr_company`: Get a company's Quera profile (about, size, tech stack, benefits, contacts) and its open jobs.
- `qr_contests`: List Quera programming contests: running or upcoming plus the latest finished ones.
- `qr_problems`: Search Quera's public problemset (about 2,000 problems), 25 per page.
- `qr_problem`: Get one Quera problem: statement (Markdown with LaTeX), difficulty, tags, solve stats, languages.
- `qr_courses`: List Quera College's paid programming courses (about 70) with level and price.
- `qr_salaries`: Summarize salaries published in open Quera jobs, grouped by seniority level (Toman per month).
- `qr_problem_filters`: List the topic slugs, contest ids, origins and judging types that qr_problems accepts.
- `qr_event`: Get a Quera event page (CodeCup, hackathon, contest series): schedule, prizes, price, sub-events.
- `qr_bootcamps`: List Quera's paid bootcamps open for registration with price, dates and seats, or get one in full.
- `qr_blog`: Search or read the Quera blog: Persian programming articles, career and tech news.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `QUERA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
