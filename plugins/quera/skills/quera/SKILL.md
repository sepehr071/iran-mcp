---
name: quera
description: "Read-only Quera (quera.org): Iranian tech jobs, companies, contests, problems, courses and blog. Use when the user asks about Quera (quera.org) or wants job ads, employers or salaries in Iran."
---

# Quera

Read-only Quera (quera.org): Iranian tech jobs, companies, contests, problems, courses and blog.

The tools below come from the `quera-mcp` MCP server. If they are not available, install it with `claude mcp add quera -- uvx quera-mcp`, or add `"quera": {"command": "uvx", "args": ["quera-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `qr_jobs`: Search the open tech jobs on Quera Magnet (Iran's developer job board), 15 per page.
- `qr_job`: Get one Quera job posting: description, requirements, benefits, skills, salary, deadline and related jobs.
- `qr_job_filters`: List the filter values qr_jobs and qr_companies accept: cities, industries, company sizes, popular tech codes and companies.
- `qr_companies`: Search the 3,000+ companies with a Quera Magnet profile, 15 per page.
- `qr_company`: Get a company's Quera profile (about, size, industry, tech stack, benefits, contacts) and its open jobs.
- `qr_contests`: List Quera programming contests: with no filter, those running or upcoming now plus the latest finished ones.
- `qr_problems`: Search Quera's public problemset (about 2,000 programming problems), 25 per page.
- `qr_problem`: Get one Quera problem: statement (Markdown with LaTeX), limits, difficulty, tags, solve stats and languages.
- `qr_courses`: List Quera College's paid programming courses (about 70) with level and price.
- `qr_salaries`: Summarize the salaries employers published in open Quera jobs, grouped by seniority level (Toman per month).
- `qr_problem_filters`: List the topic slugs, contest ids, origins and judging types that qr_problems accepts.
- `qr_event`: Get a Quera event or competition page (CodeCup, hackathon, contest series): schedule, prizes, price, sub-events.
- `qr_bootcamps`: List Quera's intensive paid bootcamps open for registration with price, dates and seats, or get one in full.
- `qr_blog`: Search or read the Quera blog (quera.org/blog): Persian programming articles, career and tech news.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `QUERA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
