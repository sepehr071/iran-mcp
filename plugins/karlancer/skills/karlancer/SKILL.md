---
name: karlancer
description: "Read-only Karlancer (karlancer.com) freelance projects, freelancers and services in Iran. Use when the user asks about Karlancer Freelance (karlancer.com) or wants freelance projects, freelancers or services in Iran."
---

# Karlancer Freelance

Read-only Karlancer (karlancer.com) freelance projects, freelancers and services in Iran.

The tools below come from the `karlancer-mcp` MCP server. If they are not available, install it with `claude mcp add karlancer -- uvx karlancer-mcp`, or add `"karlancer": {"command": "uvx", "args": ["karlancer-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `kl_projects`: Search open freelance projects on Karlancer by keyword, skill, category and budget.
- `kl_project`: Get one Karlancer project in full: brief, budget, duration, hire deadline, skills, category path, city.
- `kl_skills`: Look up Karlancer skill ids by name, with how many freelancer profiles list each skill.
- `kl_categories`: List Karlancer's top-level categories with ids for `category_id`, and the provinces for kl_freelancers.
- `kl_freelancers`: Search Karlancer freelancers by keyword, skill and province, with rating and skills.
- `kl_top_freelancers`: List the freelancers Karlancer features on its home page as top rated, with rating and skills.
- `kl_freelancer`: Get a Karlancer freelancer's public profile: bio, rating, success rate, skills, experience and client reviews.
- `kl_services`: Search Karlancer services (ready-made gigs freelancers sell at a fixed price) by keyword, skill and price.
- `kl_service`: Get one Karlancer service in full: description, price, delivery time, requirements, FAQ, skills and seller stats.
- `kl_worksamples`: Search portfolio items (work samples) freelancers show on Karlancer, or list one freelancer's portfolio.
- `kl_worksample`: Get one Karlancer portfolio item in full: description, skills, price range, duration, owner and similar items.
- `kl_similar_projects`: List the projects Karlancer suggests as similar to one project, with budget and duration.
- `kl_market_rate`: Estimate what a skill pays on Karlancer: budget spread of recent projects, service prices and supply.
- `kl_trending_skills`: Show which skills employers ask for most in the newest Karlancer projects.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `KARLANCER_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
