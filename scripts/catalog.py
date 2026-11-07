"""Rebuild servers.json, TOOLS.md, .mcp.json and the Claude Code plugin marketplace from the submodules in servers/
(plus, for hosted servers, the server card each one publishes).

Run from the repo root after `git submodule update --init --remote`:  python scripts/catalog.py
"""

import ast
import json
import pathlib
import re
import shutil
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKETPLACE = "iran-mcp"
OWNER = {"name": "Sepehr Radmard", "email": "sepehrr80@gmail.com", "url": "https://github.com/sepehr071"}
HOME = "https://github.com/sepehr071/iran-mcp"
LINKEDIN = "https://www.linkedin.com/in/sepehr-radmard"
# absolute: a skill is read outside this repo
BANNER = "https://raw.githubusercontent.com/sepehr071/iran-mcp/main/assets/author-banner.png"

# category -> what a user wants when they need it; used in skill and bundle descriptions, so for read-only
# categories write a noun phrase that reads after both "wants ..." and "Everything for ..."
USE = {
    "food": "food or groceries delivered",
    "shopping": "electronics, appliances or other goods",
    "beauty": "cosmetics, skin and hair care or perfume",
    "fashion": "clothes, shoes or bags",
    "classifieds": "classified ads for homes, cars, phones and more",
    "cars": "used or new car ads and prices",
    "travel": "flights, trains, buses, hotels, villas or tours",
    "maps": "places, addresses, routes or travel times on a map",
    "health": "doctors, clinics, labs, appointments or pharmacy products",
    "books": "ebooks, audiobooks or printed books",
    "learning": "online courses, lessons or certificates",
    "jobs": "job ads, employers or salaries",
    "freelance": "freelance projects, freelancers or services",
    "software": "Android apps or software and game download listings",
    "cloud": "the status, outages or prices of cloud providers",
    "prices": "live gold, coin, currency or crypto prices",
    "stocks": "stock exchange quotes, company filings, funds, bonds or commodity exchange trades",
    "economy": "official exchange rates, inflation, unemployment or other economic statistics",
    "news": "news headlines or full news articles",
    "sports": "live scores, league tables, fixtures or sports news",
    "entertainment": "game and film news, reviews or release dates",
    "video": "films and series to stream on Filimo or Namava, or where to watch a title",
    "calendar": "Jalali, Gregorian or Hijri dates, holidays or prayer times",
    "quakes": "recent or past earthquake data",
    "law": "laws, regulations, court votes, legal opinions or Official Gazette texts",
    "tax": "e-invoice goods IDs, VAT rates, activity codes, property values or tax laws and circulars",
    "insurance": "insurance quotes, insurer ratings or how an insurance line works",
    "companies": "registered companies, their board members, gazette ads, products or brands",
    "business": "to manage their own PayPing merchant account",
    "messaging": "to run their own Bale messenger bot",
    "crypto": "to check or use their own SwapWallet crypto wallet",
}

# extra lines for a server's skill, beyond the shared rules
NOTES = {
    "okala-mcp": "One exception to no login: real text search needs the optional SMS login (`ok_login`), which stays "
    "read-only. Ask the user before starting it.",
    "flytoday-mcp": "Searches are rate-limited per IP. Do not repeat a search the user did not ask for.",
    "30book-mcp": "Lists are slow (2 to 5 s each). Prefer one good query over many.",
    "torob-mcp": "Torob blocks bursts of calls from one IP (HTTP 490), so calls are spaced 2 s apart. Ask for a few "
    "products at a time and do not repeat a search the user did not ask for.",
    "qavanin-mcp": "qavanin.ir is slow (1 to 15 s per call; a whole law can take 15 s). Prefer one good query over many.",
    "baneh-mcp": "Some prices are unusually low or high: they are the shop's own data, not a bug. Searches default to "
    "in-stock items only.",
    "iran-downloads-mcp": "Metadata only: it returns the item page URL on the source site and never a download link. "
    "Say that the user must check each item's licence on that page. Sites: Soft98, P30Download, Downloadly, VGDL.",
    "iran-news-mcp": "Sites: Mehr, Khabaronline, Hamshahri, Tabnak, Entekhab, Asriran, Zoomit, Digiato, Varzesh3, "
    "Khabarvarzeshi.",
    "iran-quake-mcp": "Sites: IRSC (Iranian Seismological Center), USGS, EMSC.",
    "snapp-mcp": "Sites: Snappfood (food delivery), SnappMarket (groceries).",
    "jabama-mcp": "Sites: jabama.com (stays), jabama.tours (group tours), jabama.events (events and theater).",
    "iran-apps-mcp": "Sites: Cafe Bazaar, Myket.",
    "tsetmc-mcp": "Prices here are Rial (divide by 10 for Toman), not Toman. tsetmc.com serves mostly Iranian lines: "
    "outside Iran the user needs TSETMC_MCP_PROXY. The market trades Saturday to Wednesday mornings; after the close "
    "the order book is empty. Sites: tsetmc.com (Tehran Stock Exchange and Iran Fara Bourse).",
    "iran-crypto-mcp": "Public market data only: no keys, no trading. Every IRT price is already Toman and USDT markets "
    "are USDT. Check the order book before treating a spread between exchanges as an opportunity. Sites: Nobitex, "
    "Wallex, Bitpin, Ramzinex, Tabdeal, OMPFinex, Exir.",
    "milligold-mcp": "Prices come as Rial per milligram, Rial per gram and Toman per gram: say which unit you quote. "
    "This is Milli.gold's own price, not a market-wide gold quote.",
    "iran-gold-mcp": "gold_prices is Toman per gram; gold_milli_history is Rial per milligram (x100 = Toman per "
    "gram). Each price is that platform's own quote and excludes its trading fee (often about 0.5 %). Sites: "
    "Milli.gold, Wallgold, Melligold, Daric, Taline. Taline answers only connections from Iran; outside Iran the user needs "
    "IRAN_GOLD_MCP_PROXY.",
    "iran-tax-mcp": "The first goods-ID search for a phrase takes 15 to 30 s; repeats are cached. The tax sites often "
    "refuse foreign connections; outside Iran the user needs IRAN_TAX_MCP_PROXY. Sites: tax.gov.ir, "
    "stuffid.tax.gov.ir (goods IDs), regulation.tax.gov.ir (laws and circulars).",
    "neshan-mcp": "Coordinates are `lat,lng` (latitude first). `ns_nearby` answers only Iranian connections; outside "
    "Iran set NESHAN_MCP_PROXY or use `ns_search` with `near`.",
    "balad-mcp": "Coordinates are `lat`/`lng` (latitude first). Directions are car routes only: no walking or transit "
    "(use neshan-mcp for those).",
    "codal-mcp": "Report amounts are as published, usually million Rial (see `unit_note`), not Toman. codal.ir blocks an "
    "IP for up to an hour after a burst: make few, targeted calls, and stop when a tool says it is rate limiting. It "
    "often answers only Iranian connections; outside Iran the user needs CODAL_MCP_PROXY.",
    "cbi-mcp": "Exchange rates are Rial per currency unit (`per_units`: JPY 100, KRW 1000), not Toman. Dates are Jalali.",
    "amar-mcp": "amar.org.ir answers only Iranian connections; outside Iran the user needs AMAR_MCP_PROXY. GDP levels are "
    "billion Rial.",
    "ifb-mcp": "Prices are Rial, not Toman; yields are percent a year; dates Jalali. ifb.ir answers only Iranian "
    "connections; outside Iran the user needs IFB_MCP_PROXY.",
    "ime-mcp": "Prices are Rial, not Toman (per kg for goods listed in tonnes; check `unit`). `value_k_rial` is thousand "
    "Rial, market summaries million Rial. Date ranges are limited to 45 days. ime.co.ir answers only Iranian "
    "connections; outside Iran the user needs IME_MCP_PROXY.",
    "fipiran-mcp": "NAV is Rial per unit and fund sizes are billion Toman; returns are percent per period, not "
    "annualised. fipiran.ir answers only Iranian connections; outside Iran the user needs FIPIRAN_MCP_PROXY.",
    "rrk-mcp": "The portal is slow (a full-text search can take 10 s). Prefer one good query over many. It has no "
    "company registration notices.",
    "jobinja-mcp": "jobinja.ir answers only Iranian connections (HTTP 403 elsewhere); outside Iran the user needs "
    "JOBINJA_MCP_PROXY.",
    "darukade-mcp": "Product text is the shop's, not medical advice: tell the user to ask a doctor or pharmacist.",
    "iran-cloud-status-mcp": "Sites: ArvanCloud, Hamravesh, Chabokan, Liara.",
    "iran-brokers-mcp": "Prices are Rial (divide by 10 for Toman), not Toman. Sites: Mofid (emofid.com), Agah (agah.com).",
    "iran-insurance-mcp": "BimeBazar allows about 25 to 30 calls a minute per IP; a travel comparison uses about five. "
    "Do not loop. Sites: BimeBazar, Azki.",
    "iran-jobs-mcp": "Sites: IranTalent, Jobinja, Jobvision. Jobinja answers only Iranian connections; outside Iran the "
    "user needs IRAN_JOBS_MCP_PROXY.",
    "rasmio-mcp": "Money is Rial, not Toman. Dates are Jalali.",
    "snappshop-mcp": "Snapp! Shop answers only Iranian connections (HTTP 403 elsewhere).",
}

# name -> (category, site url); order here is the order everywhere else
SERVERS = {
    "snapp-mcp": ("food", "https://snappfood.ir"),
    "okala-mcp": ("food", "https://okala.com"),
    "tapsifood-mcp": ("food", "https://tapsi.food"),
    "digikala-mcp": ("shopping", "https://www.digikala.com"),
    "technolife-mcp": ("shopping", "https://www.technolife.com"),
    "masterkala-mcp": ("shopping", "https://masterkala.com"),
    "baneh-mcp": ("shopping", "https://baaneeh.com"),
    "torob-mcp": ("shopping", "https://torob.com"),
    "basalam-mcp": ("shopping", "https://basalam.com"),
    "emalls-ir-mcp": ("shopping", "https://emalls.ir"),
    "mobile-ir-mcp": ("shopping", "https://www.mobile.ir"),
    "zoomit-mcp": ("shopping", "https://www.zoomit.ir"),
    "snappshop-mcp": ("shopping", "https://snappshop.ir"),
    "khanoumi-mcp": ("beauty", "https://www.khanoumi.com"),
    "asalbanoo-mcp": ("beauty", "https://asalbanooshop.com"),
    "shopino-mcp": ("fashion", "https://shopino.app"),
    "banimode-mcp": ("fashion", "https://www.banimode.com"),
    "divar-mcp": ("classifieds", "https://divar.ir"),
    "sheypoor-mcp": ("classifieds", "https://www.sheypoor.com"),
    "bama-ir-mcp": ("cars", "https://bama.ir"),
    "karnameh-mcp": ("cars", "https://karnameh.com"),
    "hamrah-mechanic-mcp": ("cars", "https://www.hamrah-mechanic.com"),
    "otaghak-mcp": ("travel", "https://www.otaghak.com"),
    "jabama-mcp": ("travel", "https://www.jabama.com"),
    "mrbilit-mcp": ("travel", "https://mrbilit.com"),
    "flytoday-mcp": ("travel", "https://www.flytoday.ir"),
    "alibaba-ir-mcp": ("travel", "https://www.alibaba.ir"),
    "eghamat24-mcp": ("travel", "https://www.eghamat24.com"),
    "neshan-mcp": ("maps", "https://neshan.org"),
    "balad-mcp": ("maps", "https://balad.ir"),
    "paziresh24-mcp": ("health", "https://www.paziresh24.com"),
    "doctoreto-mcp": ("health", "https://doctoreto.com"),
    "exiryab-mcp": ("health", "https://exiryab.com"),
    "darukade-mcp": ("health", "https://darukade.com"),
    "taaghche-mcp": ("books", "https://taaghche.com"),
    "fidibo-mcp": ("books", "https://fidibo.com"),
    "30book-mcp": ("books", "https://www.30book.com"),
    "iranketab-mcp": ("books", "https://www.iranketab.ir"),
    "maktabkhooneh-mcp": ("learning", "https://maktabkhooneh.org"),
    "faradars-mcp": ("learning", "https://faradars.org"),
    "jobinja-mcp": ("jobs", "https://jobinja.ir"),
    "jobvision-mcp": ("jobs", "https://jobvision.ir"),
    "irantalent-mcp": ("jobs", "https://www.irantalent.com"),
    "quera-mcp": ("jobs", "https://quera.org"),
    "iran-jobs-mcp": ("jobs", "https://www.irantalent.com"),
    "ponisha-mcp": ("freelance", "https://ponisha.ir"),
    "karlancer-mcp": ("freelance", "https://www.karlancer.com"),
    "iran-apps-mcp": ("software", "https://cafebazaar.ir"),
    "iran-downloads-mcp": ("software", "https://soft98.ir"),
    "iran-cloud-status-mcp": ("cloud", "https://www.arvancloud.ir"),
    "tgju-mcp": ("prices", "https://www.tgju.org"),
    "iran-crypto-mcp": ("prices", "https://nobitex.ir"),
    "milligold-mcp": ("prices", "https://milli.gold"),
    "iran-gold-mcp": ("prices", "https://milli.gold"),
    "tsetmc-mcp": ("stocks", "https://tsetmc.com"),
    "codal-mcp": ("stocks", "https://codal.ir"),
    "ifb-mcp": ("stocks", "https://www.ifb.ir"),
    "fipiran-mcp": ("stocks", "https://fipiran.ir"),
    "ime-mcp": ("stocks", "https://www.ime.co.ir"),
    "iran-brokers-mcp": ("stocks", "https://www.emofid.com"),
    "cbi-mcp": ("economy", "https://www.cbi.ir"),
    "amar-mcp": ("economy", "https://amar.org.ir"),
    "iran-news-mcp": ("news", "https://www.mehrnews.com"),
    "varzesh3-mcp": ("sports", "https://www.varzesh3.com"),
    "gamefa-mcp": ("entertainment", "https://gamefa.com"),
    "iran-vod-mcp": ("video", "https://www.filimo.com"),
    "time-ir-mcp": ("calendar", "https://www.time.ir"),
    "iran-quake-mcp": ("quakes", "https://irsc.ut.ac.ir"),
    "qavanin-mcp": ("law", "https://qavanin.ir"),
    "rrk-mcp": ("law", "https://rrk.ir"),
    "iran-tax-mcp": ("tax", "https://tax.gov.ir"),
    "iran-insurance-mcp": ("insurance", "https://bimebazar.com"),
    "rasmio-mcp": ("companies", "https://rasmio.com"),
    "payping-mcp": ("business", "https://www.payping.ir"),
    "bale-mcp": ("messaging", "https://bale.ai"),
}

# name -> (category, site url) for servers their owner hosts, listed after SERVERS. The submodule holds the server's
# MCP Registry server.json (with `remotes`); tools/list needs the user's sign-in, so the tools, sign-in and read-only
# status come from the server card the server publishes (card()).
REMOTE = {
    "pasavard-mcp": ("shopping", "https://pasavard.ir"),
    "swapwallet-mcp": ("crypto", "https://swapwallet.app"),
}


def tools(src: pathlib.Path) -> list[dict]:
    """Every function decorated with @tool("Title") under src, in file order."""
    out = []
    for path in sorted(src.rglob("*.py")):
        for node in ast.parse(path.read_text(encoding="utf-8")).body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and getattr(dec.func, "id", None) == "tool" and dec.args:
                    # first sentence of the first paragraph: a wrapped first line no longer cuts mid-sentence
                    para = " ".join((ast.get_docstring(node) or "").strip().split("\n\n")[0].split())
                    doc = re.split(r"(?<=[.?!])\s+(?=[A-Z`(])", para, maxsplit=1)[0]
                    kw = {k.arg: k.value for k in dec.keywords}
                    # @tool("Title", read_only=False) marks a tool that changes something (login, cart, booking, ...)
                    read_only = ast.literal_eval(kw["read_only"]) if "read_only" in kw else True
                    out.append(
                        {"name": node.name, "title": ast.literal_eval(dec.args[0]), "summary": doc, "read_only": read_only}
                    )
    return out


def card(url: str) -> dict:
    """The MCP server card (SEP-1649, SEP-2127) published next to a hosted server's endpoint."""
    u = urlparse(url)
    with urllib.request.urlopen(f"{u.scheme}://{u.netloc}/.well-known/mcp/server-card.json", timeout=30) as r:
        return json.load(r)


def main() -> None:
    catalog, mcp, md = [], {}, ["# Tool index", "", "Generated by `scripts/catalog.py`. Do not edit by hand.", ""]
    previous = {s["name"]: s for s in json.loads((ROOT / "servers.json").read_text(encoding="utf-8"))}
    for name, (category, site) in SERVERS.items():
        repo = ROOT / "servers" / name
        meta = json.loads((repo / "server.json").read_text(encoding="utf-8"))
        pkg = meta["packages"][0]
        env = [
            {k: v[k] for k in ("name", "isRequired", "isSecret", "description")}
            for v in pkg.get("environmentVariables", [])
        ]
        found = tools(repo / "src")
        catalog.append(
            {
                "name": name,
                "title": meta["title"],
                "category": category,
                "site": site,
                "description": meta["description"],
                "version": meta["version"],
                "pypi": pkg["identifier"],
                "repository": meta["repository"]["url"],
                "registry_name": meta["name"],
                "run": f"uvx {pkg['identifier']}",
                "read_only": not any(e["isRequired"] for e in env) and all(t["read_only"] for t in found),
                "env": env,
                "tool_count": len(found),
                "tools": found,
            }
        )
        entry = {"command": "uvx", "args": [pkg["identifier"]]}
        required = [e["name"] for e in env if e["isRequired"]]
        if required:
            entry["env"] = {e: "${" + e + ":-}" for e in required}
        mcp[name.removesuffix("-mcp")] = entry

    for name, (category, site) in REMOTE.items():
        meta = json.loads((ROOT / "servers" / name / "server.json").read_text(encoding="utf-8"))
        url = meta["remotes"][0]["url"]
        try:
            info = card(url)
        except (OSError, ValueError) as e:  # network errors and timeouts are OSError, bad JSON is ValueError
            # one server's outage must not stop the sync of the others: keep what the last good run read
            if name not in previous:
                raise
            print(f"warning: {name}: server card unavailable ({e}), keeping its tools from servers.json", file=sys.stderr)
            info = None
        if info is None:
            found, auth, read_only = previous[name]["tools"], previous[name]["auth"], previous[name]["read_only"]
        else:
            login = info.get("authentication", {})
            if login.get("required") and "oauth2" not in login.get("schemes", []):
                raise SystemExit(f"{name}: hosted servers must use OAuth or no sign-in, the card says {login}")
            found = []
            for t in info["tools"]:
                # the description's first sentence, like a package tool's first docstring line
                summary = re.split(r"(?<=\.)\s+", t["description"].strip(), maxsplit=1)[0]
                read_only = bool(t.get("annotations", {}).get("readOnlyHint"))
                found.append(
                    {"name": t["name"], "title": t.get("title") or t["name"], "summary": summary, "read_only": read_only}
                )
            auth = "oauth" if login.get("required") else "none"
            # like a package server with no required token: no sign-in, and no tool that changes anything
            read_only = not login.get("required") and all(t["read_only"] for t in found)
        catalog.append(
            {
                "name": name,
                "title": meta["title"],
                "category": category,
                "site": site,
                "description": meta["description"],
                "version": meta["version"],
                "url": url,
                "repository": meta["repository"]["url"],
                "registry_name": meta["name"],
                "auth": auth,
                "read_only": read_only,
                "env": [],
                "tool_count": len(found),
                "tools": found,
            }
        )
        mcp[name.removesuffix("-mcp")] = {"type": "http", "url": url}

    for s in catalog:
        md += [f"## {s['title']} (`{s['name']}`, {s['tool_count']} tools)", "", s["description"], ""]
        md += [f"- `{t['name']}`: {t['summary'] or t['title']}" for t in s["tools"]]
        md.append("")

    old_total = sum(s["tool_count"] for s in previous.values())
    total = sum(s["tool_count"] for s in catalog)
    (ROOT / "servers.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "TOOLS.md").write_text("\n".join(md), encoding="utf-8")
    pinned = plugins(catalog, mcp)
    (ROOT / ".mcp.json").write_text(json.dumps({"mcpServers": pinned}, indent=2) + "\n", encoding="utf-8")
    sync_docs(catalog, old_total, total)
    print(f"{len(catalog)} servers, {total} tools")


def skill(s: dict, key: str, entry: dict) -> str:
    """SKILL.md for one server: when to use it, how to get its tools, and the rules it follows."""
    host = urlparse(s["site"]).netloc.removeprefix("www.")
    # a server whose repo ships its own skill keeps its own rules, so the two skills can't disagree
    own = ROOT / "servers" / s["name"] / "skills" / key / "SKILL.md"
    intro, rules = "", ""
    if own.exists():
        body = own.read_text(encoding="utf-8").split("\n# ", 1)[1].split("\n", 1)[1]  # drop front matter and title
        intro, _, rules = body.strip().partition("\n## ")
    lines = [
        "---",
        f"name: {key}",
        # JSON string = valid YAML double-quoted scalar; descriptions contain ": "
        "description: " + json.dumps(
            f"{s['description']} Use when the user asks about {s['title']} ({host}) or wants {USE[s['category']]} in Iran.",
            ensure_ascii=False,
        ),
        "---",
        "",
        f"# {s['title']}",
        "",
        s["description"],
        "",
        *([intro.strip(), ""] if intro else []),
        install(s, key, entry),
        "",
        "## Tools",
        "",
        *[f"- `{t['name']}`: {t['summary'] or t['title']}" for t in s["tools"]],
        "",
    ]
    if rules:
        return "\n".join(lines) + "\n## " + rules + "\n" + maintainer(s)
    lines += ["## Rules", ""]
    if s["read_only"]:
        lines += [
            "- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.",
            "- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.",
            "- Keep request rates low. These are undocumented site APIs that can change or rate-limit.",
        ]
    else:
        access = ", ".join(f"`{e['name']}`" for e in s["env"] if e["isRequired"]) or (
            "OAuth sign-in" if s.get("auth") == "oauth" else "a login from the chat with its `*_login` tool"
        )
        lines.append(
            f"- This server acts on the user's own account ({access}). Confirm with the user before any call "
            "that creates, sends, edits or deletes something."
        )
    for e in s["env"]:
        if e["name"].endswith("_MCP_PROXY"):
            lines.append(f"- On timeouts or HTTP 403 outside Iran, set `{e['name']}` to an HTTP proxy with an Iranian IP.")
    if s["name"] in NOTES:
        lines.append(f"- {NOTES[s['name']]}")
    return "\n".join(lines) + "\n" + maintainer(s)


def maintainer(s: dict) -> str:
    """Credit and banner for servers we maintain; a server another team ships keeps its own credits."""
    if not s["repository"].startswith(OWNER["url"] + "/"):
        return ""
    return (
        "\n## Maintainer\n\n"
        f'<a href="{LINKEDIN}"><img src="{BANNER}" alt="Sepehr Radmard: open-source MCP servers for the Iranian web" '
        'width="100%"></a>\n\n'
        f"Built and maintained by **{OWNER['name']}** (سپهر رادمرد): [LinkedIn]({LINKEDIN}) · "
        f"[GitHub]({OWNER['url']}). More servers for Iranian websites: [iran-mcp]({HOME}).\n"
    )


def install(s: dict, key: str, entry: dict) -> str:
    """The skill's lines on where its tools come from and how to add the server."""
    if "url" not in s:
        return (
            f"The tools below come from the `{s['name']}` MCP server. If they are not available, install it with "
            f"`claude mcp add {key} -- {s['run']}`, or add `\"{key}\": {json.dumps(entry)}` to the client's "
            "MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing."
        )
    url = s["url"]
    # each client takes a remote server in its own shape
    lines = [
        f"The tools below come from {s['title']}'s hosted MCP server at {url} (Streamable HTTP). If they are not "
        "available, add it to the client:",
        "",
        f"- Claude Code: `claude mcp add --transport http {key} {url}`",
        f"- Codex CLI: `codex mcp add {key} --url {url}`",
        f"- Gemini CLI: `gemini mcp add --transport http {key} {url}`",
        f'- Cursor: `"{key}": {{"url": "{url}"}}` under `mcpServers` in `~/.cursor/mcp.json`',
        f'- VS Code: `"{key}": {json.dumps(entry)}` under `servers` in `.vscode/mcp.json`',
        f'- Windsurf: `"{key}": {{"serverUrl": "{url}"}}` under `mcpServers` in `~/.codeium/windsurf/mcp_config.json`',
        "- Claude Desktop and claude.ai: Settings → Connectors → Add custom connector, with the URL",
        "",
        "Restart the session after installing.",
    ]
    if s["auth"] == "oauth":
        lines[-1] += (
            " The user then signs in once with OAuth. The client runs the sign-in, not the agent, and Claude Code "
            "doesn't open the browser by itself: run `/mcp`, pick the server and choose Authenticate, or run "
            f"`claude mcp login <name>` with the name `claude mcp list` shows (`plugin:{key}:{key}` when installed as "
            f"a plugin). Codex: `codex mcp login {key}`. Gemini CLI: `/mcp auth {key}`. Other clients show a sign-in "
            "button or prompt."
        )
    return "\n".join(lines)


def released(package: str, version: str, ours: bool = True) -> str:
    """`version` if PyPI has it, else PyPI's newest release (main can be bumped before the release is published).

    A server we don't own gets no fallback: its newest release hasn't been reviewed, so only the pinned one ships.
    """
    try:
        urllib.request.urlopen(f"https://pypi.org/pypi/{package}/{version}/json", timeout=30).close()
        return version
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        if not ours:
            raise SystemExit(f"{package} {version} is not on PyPI; move the fork only to a published, reviewed release")
    with urllib.request.urlopen(f"https://pypi.org/pypi/{package}/json", timeout=30) as r:
        return json.load(r)["info"]["version"]


def plugins(catalog: list[dict], mcp: dict) -> dict:
    """One plugin per server (MCP server + skill), plus bundle plugins that only pull in others.

    Returns each server's MCP config pinned to the version its plugin runs, for .mcp.json.
    """
    out = ROOT / "plugins"
    shutil.rmtree(out, ignore_errors=True)
    entries, pinned = [], {}

    def write(name: str, manifest: dict, category: str) -> None:
        (out / name / ".claude-plugin").mkdir(parents=True)
        (out / name / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        entries.append({"name": name, "source": f"./plugins/{name}", "description": manifest["description"], "category": category})

    for s in catalog:
        key = s["name"].removesuffix("-mcp")
        if "url" in s:  # hosted: its owner deploys it, so there is no release to pin
            version, server = s["version"], mcp[key]
        else:
            # pin the exact release: bare `uvx pkg` keeps running its cached copy forever
            version = released(s["pypi"], s["version"], s["repository"].startswith(OWNER["url"] + "/"))
            server = {**mcp[key], "args": [f"{s['pypi']}@{version}"]}
        pinned[key] = server
        write(
            key,
            {
                "name": key,
                "displayName": s["title"],
                "version": version,
                "description": s["description"],
                "author": OWNER,
                "homepage": HOME,
                "repository": s["repository"],
                "license": "MIT",
                "keywords": ["iran", s["category"], urlparse(s["site"]).netloc.removeprefix("www.")],
                "mcpServers": {key: server},
            },
            s["category"],
        )
        (out / key / "skills" / key).mkdir(parents=True)
        (out / key / "skills" / key / "SKILL.md").write_text(skill(s, key, mcp[key]), encoding="utf-8")

    # bundles carry no version: Claude Code then versions them by commit, so a changed list reaches users
    # bundles hold servers that work with no setup: no required token and no OAuth (a login from the chat is optional)
    sites = [s for s in catalog if not any(e["isRequired"] for e in s["env"]) and s.get("auth", "none") == "none"]
    bundles = {"iran-all": (f"All {len(sites)} Iranian site servers that need no setup, in one install.", sites)}
    for cat in dict.fromkeys(s["category"] for s in sites):
        members = [s for s in sites if s["category"] == cat]
        if len(members) > 1:
            names = ", ".join(s["title"] for s in members)
            name = f"iran-{cat}"
            # a server plugin keeps its package name (iran-jobs-mcp -> iran-jobs), so the bundle steps aside
            if any(s["name"] == f"{name}-mcp" for s in catalog):
                name += "-bundle"
            bundles[name] = (f"Everything for {USE[cat]} in Iran: {names}.", members)
    for name, (description, members) in bundles.items():
        deps = [s["name"].removesuffix("-mcp") for s in members]
        write(name, {"name": name, "description": description, "author": OWNER, "homepage": HOME, "dependencies": deps}, "bundle")

    marketplace = {
        "name": MARKETPLACE,
        "description": "MCP servers and skills for Iranian websites: shopping, classifieds, cars, food, travel, maps, doctors, books, jobs, markets, crypto.",
        "owner": OWNER,
        "plugins": entries,
    }
    path = ROOT / ".claude-plugin" / "marketplace.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return pinned


def sync_docs(catalog: list[dict], old_total: int, total: int) -> None:
    """Keep the tool counts written in the docs in step with the catalog."""
    fa = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    for doc in ("README.md", "README.fa.md", "AGENTS.md", "llms.txt"):
        path = ROOT / doc
        text = path.read_text(encoding="utf-8")
        for s in catalog:
            n = s["tool_count"]
            count = str(n).translate(fa) if doc == "README.fa.md" else str(n)
            # table row: | [name](repo) | site | <count> |
            text = re.sub(rf"(^\| \[{s['name']}\]\([^)]*\) \| [^|]* \| )[^|]+( \|)", rf"\g<1>{count}\2", text, flags=re.M)
        if old_total != total:
            text = text.replace(str(old_total), str(total)).replace(str(old_total).translate(fa), str(total).translate(fa))
        path.write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
