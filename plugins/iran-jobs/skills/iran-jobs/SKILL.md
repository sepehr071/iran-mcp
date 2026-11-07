---
name: iran-jobs
description: "Read-only Iran jobs: IranTalent, Jobinja, Jobvision side by side. Ads, companies, reviews, pay. Use when the user asks about Iran Jobs (IranTalent + Jobinja + Jobvision) (irantalent.com) or wants job ads, employers or salaries in Iran."
---

# Iran Jobs (IranTalent + Jobinja + Jobvision)

Read-only Iran jobs: IranTalent, Jobinja, Jobvision side by side. Ads, companies, reviews, pay.

The tools below come from the `iran-jobs-mcp` MCP server. If they are not available, install it with `claude mcp add iran-jobs -- uvx iran-jobs-mcp`, or add `"iran-jobs": {"command": "uvx", "args": ["iran-jobs-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `job_irantalent_salary_reports`: List IranTalent salary reports (salary.irantalent.com): one per job specialty and seniority level.
- `job_irantalent_salary`: Read the salary figures of one IranTalent salary report, or of every seniority level of one specialty.
- `job_irantalent_search_jobs`: Search IranTalent job ads by keyword and filters, newest first.
- `job_irantalent_job`: Read one IranTalent job ad in full: description, requirements, salary, location, employer, view counts.
- `job_irantalent_company`: Read a company profile: about text, industry, size, address, website, rating breakdown and newest open jobs.
- `job_irantalent_company_reviews`: Read anonymous employee reviews of a company on IranTalent: ratings, pros, cons, reviewer's job title.
- `job_irantalent_lookups`: List the valid filter values (slug, English and Persian name) for job_irantalent_search_jobs.
- `job_irantalent_job_market`: Count IranTalent's open jobs by category, industry, seniority, employment type, location or hiring company.
- `job_irantalent_similar_jobs`: Find open jobs similar to one ad: same job category (and city), newest first, without the ad itself.
- `job_jobinja_search_jobs`: Search Jobinja job ads by keyword, province, city, category, remote, contract type, experience, benefits and minimum salary.
- `job_jobinja_job`: Read one Jobinja job ad: title, company, salary, contract, experience, skills, degree, gender, military status and the full description.
- `job_jobinja_company`: Read a company's Jobinja profile: name, founding year, industry, size, website, open job count and its intro, culture and benefits text.
- `job_jobinja_company_jobs`: List a company's open job ads on Jobinja (or, with expired_page, its past ads, which show its hiring history).
- `job_jobinja_search_companies`: Find companies on Jobinja by name, or browse one industry (8 per page).
- `job_jobinja_market`: Count the open Jobinja ads right now per job category, province, company industry and top skill (live site statistics).
- `job_jobinja_skills`: Find skills on Jobinja matching a word, with how many ads ever listed each (a demand signal).
- `job_jobinja_salary_stats`: Estimate monthly salaries (Toman) for a kind of job by reading the ad pages of the top search results.
- `job_jobinja_filters`: List every value the Jobinja search accepts: provinces, job categories, industries, experience levels, salary steps, sort orders.
- `job_jobvision_careers`: Rank the ~100 job titles in Jobvision's career guide by satisfaction, median salary or open ads.
- `job_jobvision_career`: Get Jobvision's career-guide profile of one job title: salary distribution, demand, duties, skills, path.
- `job_jobvision_companies`: Find companies on Jobvision by name or filters, best rated first (the site's company ranking).
- `job_jobvision_interviews`: Get what candidates report about interviewing at a company: scores, difficulty, process and questions.
- `job_jobvision_search`: Search Jobvision job ads (استخدام) with filters and return one page of compact job cards.
- `job_jobvision_job`: Get the full text and requirements of one Jobvision job ad.
- `job_jobvision_similar_jobs`: List job ads Jobvision considers similar to one ad.
- `job_jobvision_company`: Get an employer's profile and its currently open job ads.
- `job_jobvision_pay_stats`: Estimate pay for a role from the salaries open Jobvision ads advertise (million Toman per month).
- `job_jobvision_suggest`: Autocomplete job titles the way Jobvision's search box does, most used first.
- `job_jobvision_locations`: Find the province, city or Tehran area names and slugs that job_jobvision_search's city filter accepts.
- `job_jobvision_options`: List the values of one Jobvision filter: ids and slugs with Persian and English names.
- `job_jobvision_market`: Count open Jobvision ads per category, province, work type, seniority, experience, pay band or age.
- `job_jobvision_government_news`: List Jobvision's recruitment announcements for a public-sector group (banks, ministries, oil and gas...).
- `job_search`: Search job ads on IranTalent, Jobinja and Jobvision at once, one block of results per site.
- `job_companies`: Find a company by name on IranTalent, Jobinja and Jobvision at once, one block per site.
- `job_top_companies`: List each site's best-rated employers side by side: IranTalent top 50, Jobinja top 50, Jobvision top ranked.
- `job_market`: Count open job ads per job category on IranTalent, Jobinja and Jobvision, one block per site.
- `job_salary`: Compare monthly pay for a role from three sources: IranTalent's salary survey and the pay in Jobinja and Jobvision ads.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_JOBS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: IranTalent, Jobinja, Jobvision. Jobinja answers only Iranian connections; outside Iran the user needs IRAN_JOBS_MCP_PROXY.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
