---
name: jobinja
description: "Read-only Jobinja (jobinja.ir) job search, ad details, companies and top-50 scores for Iran. Use when the user asks about Jobinja Jobs (jobinja.ir) or wants job ads, employers or salaries in Iran."
---

# Jobinja Jobs

Read-only Jobinja (jobinja.ir) job search, ad details, companies and top-50 scores for Iran.

The tools below come from the `jobinja-mcp` MCP server. If they are not available, install it with `claude mcp add jobinja -- uvx jobinja-mcp`, or add `"jobinja": {"command": "uvx", "args": ["jobinja-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `jj_search_jobs`: Search Jobinja job ads by keyword and filters (AND).
- `jj_job`: Read one Jobinja job ad: salary, skills, degree and the full description.
- `jj_company`: Read a company's Jobinja profile: industry, size, website, open job count and intro/culture text.
- `jj_company_jobs`: List a company's open job ads (or past ads with expired_page).
- `jj_search_companies`: Find companies on Jobinja by name, or browse one industry (8 per page).
- `jj_top_companies`: Jobinja's top-50 companies with score out of 10 and three sub-scores.
- `jj_market`: Count open Jobinja ads now per category, province, industry and top skill.
- `jj_skills`: Find skills matching a word, with how many ads ever listed each (demand signal).
- `jj_salary_stats`: Estimate monthly salaries (Toman) from the ad pages of the top search results.
- `jj_filters`: List every value the search accepts: provinces, categories, industries, experience, salary steps, sort.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `JOBINJA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- jobinja.ir answers only Iranian connections (HTTP 403 elsewhere); outside Iran the user needs JOBINJA_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
