---
name: ganjoor
description: "Read-only Ganjoor (ganjoor.net) Persian poetry: poems with meanings, search, meters, audio. Use when the user asks about Ganjoor Poetry (ganjoor.net) or wants classical Persian poems, poets, couplet meanings or poetic meters in Iran."
---

# Ganjoor Poetry

Read-only Ganjoor (ganjoor.net) Persian poetry: poems with meanings, search, meters, audio.

The tools below come from the `ganjoor-mcp` MCP server. If they are not available, install it with `claude mcp add ganjoor -- uvx ganjoor-mcp`, or add `"ganjoor": {"command": "uvx", "args": ["ganjoor-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `gj_meters`: List poetic meters (وزن) with couplet counts, biggest first; filter by name.
- `gj_similar`: Find poems that share a meter and rhyme, with their first couplet; 10 per page.
- `gj_recitations`: List poem recitations (خوانش) with reciter, mp3 link, size and votes; give exactly one of poem_id, cat_id, latest.
- `gj_literary`: Show rhetorical devices (آرایه: tashbih, esteare...) and concepts tagged in poems; coverage is partial, mostly Hafez.
- `gj_words`: Count word use in a poet's or book's poems: the most frequent words, or how often one word appears.
- `gj_people`: Look up people and characters of epic poems (Shahnameh...): search, relations, family tree, or a book's cast.
- `gj_places`: Find geotagged places (locations with latitude and longitude) named in poems, a book, or by name.
- `gj_museum`: Browse Ganjoor museum manuscripts and scans (گنجینه): search, one manuscript's details, or one page image.
- `gj_search`: Full-text search of poems by the words they contain, with the matching couplet.
- `gj_semantic_search`: Find poems by meaning or theme (embedding search), with score, summary and first couplets.
- `gj_find_verse`: Locate which poem and couplet a quoted line comes from, with the couplet's meaning.
- `gj_poem`: Read a poem: text by couplet with meanings, summary, meter, rhyme, source and previous/next poem.
- `gj_poem_extras`: Recitations with mp3 links, manuscript images, songs, related poems, quoting poems and reader comments.
- `gj_faal`: Draw a Hafez faal (a random ghazal of Hafez) or, with random=True, a random poem, read with meanings.
- `gj_poets`: List poets with ids, nicknames, life years (Hijri) and birthplace, filtered by name or century.
- `gj_poet`: A poet's biography (shortened) and the top-level books to open with gj_book.
- `gj_book`: Sub-books and the poems of one book or section, each with its first couplet, paged by 30.
- `gj_tajik`: Search or read poems in Tajik Cyrillic transliteration (titles Cyrillic, poet names Persian).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `GANJOOR_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Site: ganjoor.net. A couplet meaning that starts with «هوش مصنوعی:» is AI-written: say so when you quote it.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
