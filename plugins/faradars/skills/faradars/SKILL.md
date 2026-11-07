---
name: faradars
description: "Read-only Faradars (faradars.org) courses: search, prices, syllabus, reviews, instructors, magazine. Use when the user asks about Faradars Courses (faradars.org) or wants online courses, lessons or certificates in Iran."
---

# Faradars Courses

Read-only Faradars (faradars.org) courses: search, prices, syllabus, reviews, instructors, magazine.

The tools below come from the `faradars-mcp` MCP server. If they are not available, install it with `claude mcp add faradars -- uvx faradars-mcp`, or add `"faradars": {"command": "uvx", "args": ["faradars-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `fr_search_courses`: Search Faradars (faradars.org) courses and videos by text, category, price, length, certificate or instructor.
- `fr_course`: Get one Faradars course: price and current discount, duration, rating, students, instructors, syllabus.
- `fr_course_reviews`: Get student reviews (stars and comment text) of a Faradars course, newest first.
- `fr_categories`: List Faradars course categories (برنامه‌نویسی, زبان, ...) as a tree of slugs and names.
- `fr_instructors`: Find Faradars instructors (مدرس) by name, or the leading instructors of a category.
- `fr_instructor`: Get a Faradars instructor's profile (field, university, students, total hours) and their courses.
- `fr_learning_paths`: Find Faradars learning paths (مسیر یادگیری): curated course collections for a topic, beginner to advanced.
- `fr_learning_path`: Get one Faradars learning path (مسیر یادگیری): its ordered course list, totals and related paths.
- `fr_related_courses`: Get courses related to one Faradars course: more by the same instructor, recommended next steps, similar topics.
- `fr_compare_courses`: Compare 2-4 Faradars courses side by side: price, sale, length, lessons, students, rating, certificate, exams.
- `fr_offers`: List the current Faradars discount campaigns, public coupon codes and subscription plans.
- `fr_faq`: Get Faradars' general help answers: buying and subscription, access validity, certificates, support, refunds.
- `fr_suggest`: Get Faradars search-box suggestions for the start of a phrase (autocomplete).
- `fr_articles`: Search Faradars Magazine (مجله فرادرس, blog.faradars.org) articles by text, category or tag, or list the newest.
- `fr_article`: Read one Faradars Magazine article: summary points, outline, readable text, author, views and rating.
- `fr_article_topics`: List Faradars Magazine categories or tags with their article counts, biggest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `FARADARS_MCP_PROXY` to an HTTP proxy with an Iranian IP.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
