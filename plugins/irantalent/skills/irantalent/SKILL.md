---
name: irantalent
description: "Read-only IranTalent (irantalent.com) job portal: search jobs, ad details, companies, reviews. Use when the user asks about IranTalent Jobs (irantalent.com) or wants job ads, employers or salaries in Iran."
---

# IranTalent Jobs

Read-only IranTalent (irantalent.com) job portal: search jobs, ad details, companies, reviews.

The tools below come from the `irantalent-mcp` MCP server. If they are not available, install it with `claude mcp add irantalent -- uvx irantalent-mcp`, or add `"irantalent": {"command": "uvx", "args": ["irantalent-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `it_salary_reports`: List IranTalent salary reports: one per job specialty and seniority level (about 200).
- `it_salary`: Read the salary figures of one IranTalent salary report, or of every seniority level of one specialty.
- `it_search_jobs`: Search IranTalent job ads by keyword and filters, newest first.
- `it_job`: Read one IranTalent job ad in full: description, requirements, salary, location, employer, views.
- `it_companies`: List or search IranTalent's employer directory, most open jobs first.
- `it_top_companies`: List IranTalent's 50 top companies by employee rating (1-5).
- `it_company`: Read a company profile: about, industry, size, address, website, rating breakdown and newest open jobs.
- `it_company_reviews`: Read anonymous employee reviews of a company on IranTalent: ratings, pros, cons, reviewer's job title.
- `it_lookups`: List the valid filter values (slug, English and Persian name) for it_search_jobs.
- `it_job_market`: Count IranTalent's open jobs by category, industry, seniority, employment type, location or hiring company.
- `it_similar_jobs`: Find open jobs similar to one ad: same job category (and city), newest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRANTALENT_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
