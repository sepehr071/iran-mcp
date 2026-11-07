---
name: ponisha
description: "Read-only Ponisha (ponisha.ir) freelance market: projects, bids, freelancers, skill demand. Use when the user asks about Ponisha Freelance (ponisha.ir) or wants freelance projects, freelancers or services in Iran."
---

# Ponisha Freelance

Read-only Ponisha (ponisha.ir) freelance market: projects, bids, freelancers, skill demand.

The tools below come from the `ponisha-mcp` MCP server. If they are not available, install it with `claude mcp add ponisha -- uvx ponisha-mcp`, or add `"ponisha": {"command": "uvx", "args": ["ponisha-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `pn_search_projects`: Search Ponisha projects by text, skills, category, status and budget.
- `pn_project`: Get one Ponisha project: full description, budget, skills, deadline and the employer's track record.
- `pn_bids`: List the offers on a Ponisha project: price (Toman), days, pitch and each bidder's track record.
- `pn_search_freelancers`: Search Ponisha freelancers by text, skills, category, level and portfolio, ranked by score.
- `pn_profile`: Get a public Ponisha profile (freelancer or employer): level, skills, statistics, rating and activity.
- `pn_skills`: Find Ponisha skills (about 700 tags) by name for the skills filters of other tools.
- `pn_categories`: List Ponisha's top-level project categories, or the sub-categories of one.
- `pn_market`: Summarize demand and supply for one skill on Ponisha: open projects, budgets, competition, related skills.
- `pn_reviews`: Read the reviews employers wrote about a Ponisha user, or recent reviews for a whole skill.
- `pn_portfolios`: Search Ponisha portfolio items (about 500k work samples), or list one user's portfolio.
- `pn_services`: Browse Ponisha's ready-made fixed-price service packages (logo design, WordPress themes, ...).
- `pn_service`: Get one Ponisha service package: price (Toman), delivery time, inclusions, requirements and add-ons.
- `pn_user_projects`: List the projects a Ponisha user is attached to: an employer's own or a freelancer's finished work.
- `pn_trend`: Show how demand and budgets for one skill changed over time on Ponisha, newest to oldest.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `PONISHA_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
