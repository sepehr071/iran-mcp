---
name: ponisha
description: "Read-only Ponisha (ponisha.ir) freelance market: projects, bids, freelancers, skill demand. Use when the user asks about Ponisha Freelance (ponisha.ir) or wants freelance projects, freelancers or services in Iran."
---

# Ponisha Freelance

Read-only Ponisha (ponisha.ir) freelance market: projects, bids, freelancers, skill demand.

The tools below come from the `ponisha-mcp` MCP server. If they are not available, install it with `claude mcp add ponisha -- uvx ponisha-mcp`, or add `"ponisha": {"command": "uvx", "args": ["ponisha-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `pn_search_projects`: Search Ponisha projects (Iran's freelance marketplace) by text, skills, category, status and budget.
- `pn_project`: Get one Ponisha project: full description, budget, skills, deadline and the employer's track record.
- `pn_bids`: List the offers freelancers made on a Ponisha project: price, days, pitch and each bidder's track record.
- `pn_search_freelancers`: Search Ponisha freelancers by text, skills, category, level and portfolio, ranked by score.
- `pn_profile`: Get a public Ponisha profile (freelancer or employer): level, skills, statistics, rating and activity.
- `pn_skills`: Find Ponisha skills (about 700 tags) by name to use in the skills filters of other tools.
- `pn_categories`: List Ponisha's top-level project categories, or the sub-categories of one.
- `pn_market`: Summarize demand and supply for one skill on Ponisha: open projects, budgets, competition, related skills.
- `pn_reviews`: Read the reviews employers wrote about a Ponisha user, or recent reviews for a whole skill.
- `pn_portfolios`: Search Ponisha portfolio items (about 500k work samples), or list one user's portfolio.
- `pn_services`: Browse Ponisha's ready-made service packages (fixed-price offers such as logo design or WordPress themes).
- `pn_service`: Get one Ponisha service package: price, delivery time, what is included, requirements and paid add-ons.
- `pn_user_projects`: List the projects a Ponisha user is attached to: an employer's own projects or a freelancer's finished work.
- `pn_trend`: Show how demand and budgets for one skill changed over time on Ponisha, from the newest to the oldest projects.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `PONISHA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
