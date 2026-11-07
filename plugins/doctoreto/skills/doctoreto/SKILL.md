---
name: doctoreto
description: "Unofficial read-only Doctoreto: Iranian doctors, visit fees, free appointment times, clinics, labs. Use when the user asks about Doctoreto (doctoreto.com) or wants doctors, clinics, labs, appointments or pharmacy products in Iran."
---

# Doctoreto

Unofficial read-only Doctoreto: Iranian doctors, visit fees, free appointment times, clinics, labs.

The tools below come from the `doctoreto-mcp` MCP server. If they are not available, install it with `claude mcp add doctoreto -- uvx doctoreto-mcp`, or add `"doctoreto": {"command": "uvx", "args": ["doctoreto-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dt_search_centers`: Find hospitals, clinics, infirmaries, laboratories, imaging centers and pharmacies with filters.
- `dt_center`: A center's page: address, departments, services, insurances, hours, lab rules, bookable services with `consultation_id` (for dt_free_slots) and its doctors (hash ids, earliest free slot).
- `dt_doctor`: A doctor's profile with every bookable service, its price in Toman and its next free time.
- `dt_free_slots`: Free appointment times of one service (office visit, phone/video call, clinic offer, lab admission).
- `dt_reviews`: Patient reviews (doctors and centers newest first, offers oldest first): stars 1-5, text, date and reply.
- `dt_health_articles`: Search Doctoreto's health magazine for background on a condition, test or treatment.
- `dt_search_offers`: Search clinic offers: fixed-price procedures and packages (ultrasound, laser, dental, check-ups).
- `dt_offer`: One clinic offer in full: price, deposit, doctor, place, terms and bookable variants with `consultation_id`.
- `dt_suggest`: Search-box suggestions: doctors (hash id), speciality slugs, service tags and centers for a free phrase.
- `dt_search_doctors`: Search doctors by city, speciality, neighborhood, service tag, name, gender, insurance and visit type.
- `dt_specialities`: List specialities with the slug dt_search_doctors needs; `total` counts all matches.
- `dt_cities`: Find a city's slug (for search filters) and numeric id (for dt_suggest); main cities first.
- `dt_neighborhoods`: Neighborhoods of a city (most doctors first) and nearby cities, each with a doctor count.
- `dt_insurances`: List basic and supplementary insurers with the ids dt_search_doctors(insurance_ids=...) takes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DOCTORETO_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
