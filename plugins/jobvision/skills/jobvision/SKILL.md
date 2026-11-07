---
name: jobvision
description: "Read-only Jobvision (jobvision.ir) Iran jobs: search ads, job and company details, advertised pay. Use when the user asks about Jobvision Jobs (jobvision.ir) or wants job ads, employers or salaries in Iran."
---

# Jobvision Jobs

Read-only Jobvision (jobvision.ir) Iran jobs: search ads, job and company details, advertised pay.

The tools below come from the `jobvision-mcp` MCP server. If they are not available, install it with `claude mcp add jobvision -- uvx jobvision-mcp`, or add `"jobvision": {"command": "uvx", "args": ["jobvision-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `jv_careers`: Rank the ~100 job titles in Jobvision's career guide by satisfaction, median salary or open ads.
- `jv_career`: Get Jobvision's career-guide profile of one job title: salary distribution, demand, duties, skills, path.
- `jv_companies`: Find companies on Jobvision by name or filters, best rated first (the site's company ranking).
- `jv_interviews`: Get what candidates report about interviewing at a company: scores, difficulty, process and questions.
- `jv_search`: Search Jobvision job ads (استخدام) with filters and return one page of compact job cards.
- `jv_job`: Get the full text and requirements of one Jobvision job ad.
- `jv_similar_jobs`: List job ads Jobvision considers similar to one ad.
- `jv_company`: Get an employer's profile and its currently open job ads.
- `jv_pay_stats`: Estimate pay for a role from the salaries open Jobvision ads advertise (million Toman per month).
- `jv_suggest`: Autocomplete job titles the way Jobvision's search box does, most used first.
- `jv_locations`: Find the province, city or Tehran area names and slugs that jv_search's city filter accepts.
- `jv_options`: List the values of one Jobvision filter: ids and slugs with Persian and English names.
- `jv_market`: Count open Jobvision ads per category, province, work type, seniority, experience, pay band or age.
- `jv_government_news`: List Jobvision's recruitment announcements for a public-sector group (banks, ministries, oil and gas...).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `JOBVISION_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
