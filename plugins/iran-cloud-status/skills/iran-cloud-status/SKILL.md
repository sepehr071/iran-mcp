---
name: iran-cloud-status
description: "Read-only status, incidents and prices of Iranian clouds: Arvan, Hamravesh, Chabokan, Liara, more. Use when the user asks about Iran Cloud Status (arvancloud.ir) or wants the status, outages or prices of cloud providers in Iran."
---

# Iran Cloud Status

Read-only status, incidents and prices of Iranian clouds: Arvan, Hamravesh, Chabokan, Liara, more.

The tools below come from the `iran-cloud-status-mcp` MCP server. If they are not available, install it with `claude mcp add iran-cloud-status -- uvx iran-cloud-status-mcp`, or add `"iran-cloud-status": {"command": "uvx", "args": ["iran-cloud-status-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `cs_status`: Show the live status of every covered Iranian cloud provider in one call.
- `cs_providers`: List the providers covered, what each publishes, and which are not covered.
- `cs_components`: List one provider's status components (services, regions, clusters, servers) with current status.
- `cs_regions`: Summarise status per region or group: component count, worst status and what is not operational.
- `cs_incidents`: List recent incidents (outages, degradations, announcements) of the Iranian cloud providers, newest first, with their latest update.
- `cs_incident`: Show one incident with its full update timeline, affected components and the status each was set to.
- `cs_maintenance`: List announced maintenance windows that are upcoming or running, per provider, optionally with recent finished ones.
- `cs_reliability`: Count incidents and add up incident time per provider over the last days, with the most affected components.
- `cs_pricing`: Show a provider's public price list in Toman, read from its own pricing page.
- `cs_compare_prices`: Price one server size (vCPU, RAM, disk) per month at Hamravesh and Liara, cheapest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_CLOUD_STATUS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: ArvanCloud, Hamravesh, Chabokan, Liara.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
