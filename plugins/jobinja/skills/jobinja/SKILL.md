---
name: jobinja
description: "Read-only Jobinja (jobinja.ir) job search, ad details, companies and top-50 scores for Iran. Use when the user asks about Jobinja Jobs (jobinja.ir) or wants job ads, employers or salaries in Iran."
---

# Jobinja Jobs

Read-only Jobinja (jobinja.ir) job search, ad details, companies and top-50 scores for Iran.

The tools below come from the `jobinja-mcp` MCP server. If they are not available, install it with `claude mcp add jobinja -- uvx jobinja-mcp`, or add `"jobinja": {"command": "uvx", "args": ["jobinja-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `jj_search_jobs`: Search Jobinja job ads by keyword, province, city, category, remote, contract type, experience, benefits and minimum salary.
- `jj_job`: Read one Jobinja job ad: title, company, salary, contract, experience, skills, degree, gender, military status and the full description.
- `jj_company`: Read a company's Jobinja profile: name, founding year, industry, size, website, open job count and its intro, culture and benefits text.
- `jj_company_jobs`: List a company's open job ads on Jobinja (or, with expired_page, its past ads, which show its hiring history).
- `jj_search_companies`: Find companies on Jobinja by name, or browse one industry (8 per page).
- `jj_top_companies`: Jobinja's yearly list of the 50 best companies to work for, with each one's score out of 10 and its three sub-scores.
- `jj_market`: Count the open Jobinja ads right now per job category, province, company industry and top skill (live site statistics).
- `jj_skills`: Find skills on Jobinja matching a word, with how many ads ever listed each (a demand signal).
- `jj_salary_stats`: Estimate monthly salaries (Toman) for a kind of job by reading the ad pages of the top search results.
- `jj_filters`: List every value the Jobinja search accepts: provinces, job categories, industries, experience levels, salary steps, sort orders.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `JOBINJA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- jobinja.ir answers only Iranian connections (HTTP 403 elsewhere); outside Iran the user needs JOBINJA_MCP_PROXY.
