---
name: iran-dictionary
description: "Read-only Persian dictionaries: Abadis and Vajehyab. Meanings, synonyms, translation, names. Use when the user asks about Iran Dictionary (Abadis + Vajehyab) (abadis.ir) or wants Persian word meanings, synonyms, translations or encyclopedia articles in Iran."
---

# Iran Dictionary (Abadis + Vajehyab)

Read-only Persian dictionaries: Abadis and Vajehyab. Meanings, synonyms, translation, names.

The tools below come from the `iran-dictionary-mcp` MCP server. If they are not available, install it with `claude mcp add iran-dictionary -- uvx iran-dictionary-mcp`, or add `"iran-dictionary": {"command": "uvx", "args": ["iran-dictionary-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dic_abadis_names`: Search Abadis's Persian first-name list by name, gender, origin, theme or first letter.
- `dic_lookup`: Look a word up in the Persian dictionaries of Abadis and Vajehyab, one block per site.
- `dic_synonyms`: Find synonyms, antonyms and pure-Persian equivalents (برابر پارسی) of a Persian word, one block per site.
- `dic_translate`: Translate a single word or short phrase between Persian and English, Arabic or Turkish, one block per site.
- `dic_suggest`: Complete the start of a word into dictionary headwords, one list per site; use it to find the exact spelling.
- `dic_vajehyab_search`: Search Vajehyab's dictionaries with a scope: exact entries, entries naming it a synonym or antonym, rhymes, sound-alikes.
- `dic_vajehyab_entry`: Read one whole Vajehyab entry (for example the full Dehkhoda text with its poetry), cut at `max_chars`.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_DICTIONARY_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: Abadis, Vajehyab.

## Maintainer

<a href="https://www.linkedin.com/in/sepehr-radmard"><img src="https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" width="100%"></a>

Built and maintained by **Sepehr Radmard** (سپهر رادمرد): [LinkedIn](https://www.linkedin.com/in/sepehr-radmard) · [GitHub](https://github.com/sepehr071). More servers for Iranian websites: [iran-mcp](https://github.com/sepehr071/iran-mcp).
