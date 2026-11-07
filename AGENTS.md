# AGENTS.md

Guide for AI agents using or working on **iran-mcp**: 77 MCP servers for Iranian websites, 994 tools in
total. 68 are Python packages on PyPI, run as stdio servers with `uvx <package>`; all of them are unofficial except
`exiryab-mcp`, ExirYab's own server on its public API. Two are hosted by their sites:
`pasavard-mcp` (`https://pasavard.ir/api/mcp`, no sign-in) and `swapwallet-mcp` (`https://swapwallet.app/mcp`, OAuth
sign-in).

## Pick a server

| User wants to... | Server | Start with |
|---|---|---|
| Buy electronics, appliances, almost anything | `digikala-mcp` | `dk_find_cheapest`, `dk_best_for_budget`, then `dk_product`, `dk_price_history` |
| Snapp! Shop products, every seller's offer, flash sales | `snappshop-mcp` | `ss_search`, then `ss_product`, `ss_reviews`; `ss_promotions` |
| Every Iranian shop's price for one product, price history, whether now is a good time to buy | `torob-mcp` | `tb_cheapest`, `tb_sellers`, `tb_deal_check` |
| A product's offers across Iranian shops on Emalls, with price history | `emalls-ir-mcp` | `em_search`, `em_offers`, `em_price_history` |
| Phone specs, shop prices, used phones, SIM numbers; phone, laptop or GPU specs and prices | `mobile-ir-mcp`, `zoomit-mcp` | `mi_search`, `mi_phone`, `mi_shop_prices`; `zm_search`, `zm_product`, `zm_prices` |
| The best buy in a price range on Digikala or Snappshop, or whether today's price is good | `pasavard-mcp` | `best_lists`, then `best_list`; `search_products` |
| Find a flat, used car or phone in ads, or check if an ad's price is fair | `divar-mcp` | `dv_search`, `dv_cheapest`, `dv_best_for_budget`, `dv_appraise` |
| Ads on Sheypoor, or the price range of a car or home there | `sheypoor-mcp` | `sp_search`, `sp_ad`, `sp_price_summary` |
| A used or new car's price, car ads, car specs, inspection fees | `bama-ir-mcp`, `karnameh-mcp`, `hamrah-mechanic-mcp` | `ba_search`, `ba_new_prices`; `kn_latest_prices`, `kn_price_history`; `hm_prices`, `hm_price_estimate` |
| Compare a phone or laptop across sellers, with installments | `technolife-mcp` | `tl_find_cheapest`, `tl_product`, `tl_compare` |
| Gadgets and accessories | `masterkala-mcp` | `mk_find_cheapest`, `mk_product` |
| Home appliances, TVs, tools | `baneh-mcp` | `bn_find_cheapest`, `bn_product` |
| Clothes, shoes, bags | `shopino-mcp`, `banimode-mcp` | `sh_find_cheapest`, `sh_product`; `bm_search`, `bm_deals` |
| Cosmetics, skin and hair care, perfume | `khanoumi-mcp`, `asalbanoo-mcp` | `kh_find_cheapest`, `ab_find_cheapest` |
| Cheapest food delivered to an address (Snappfood) | `snapp-mcp` | `find_location`, then `food_find_cheapest`, `food_party_deals` |
| Groceries delivered to an address (SnappMarket, Okala) | `snapp-mcp`, `okala-mcp` | `market_find_cheapest`; `ok_locate`, `ok_stores`, `ok_compare` |
| Flights, trains, buses, taxis | `mrbilit-mcp`, `flytoday-mcp` | `mb_search_flights`, `mb_flight_price_calendar`; `ft_search_flights` |
| Hotels | `mrbilit-mcp`, `flytoday-mcp` | `mb_search_hotels`; `ft_search_hotels` |
| Villas, cottages, short stays | `jabama-mcp`, `otaghak-mcp` | `jb_search_stays`, `jb_price_quote`; `ot_search_rooms`, `ot_price_quote` |
| Tours, events, theater tickets (jabama.tours, jabama.events) | `jabama-mcp` | `jb_search_tours`, `jb_search_events` |
| CIP, eSIM, visas, activities abroad | `flytoday-mcp` | `ft_cip`, `ft_esim_plans`, `ft_visa`, `ft_activities` |
| Flights, trains, buses, hotels, villas and tours on Alibaba | `alibaba-ir-mcp` | `al_flights_cheapest`, `al_trains_cheapest`, `al_buses_cheapest`, `al_hotels` |
| Hotel room prices for given dates, hotel deals | `eghamat24-mcp` | `eg_search`, `eg_rooms`, `eg_price_calendar`, `eg_deals` |
| A place or address, places nearby, directions and travel time, air quality | `neshan-mcp`, `balad-mcp` | `ns_search`, `ns_route`, `ns_transit_route`; `bl_search`, `bl_nearby`, `bl_route` |
| A doctor with a free appointment | `paziresh24-mcp`, `doctoreto-mcp` | `pz_search_doctors`, `pz_first_available`; `dt_search_doctors`, `dt_free_slots` |
| A doctor by name, or a doctor's clinic address, phone, hours and map | `exiryab-mcp` | `ey_search_doctors`; `ey_cities`, `ey_specialties` for exact names |
| Clinics, labs, medical offers | `doctoreto-mcp` | `dt_search_centers`, `dt_search_offers` |
| Medicines, supplements and care products in an online pharmacy | `darukade-mcp` | `dr_search`, `dr_cheapest`, `dr_product` |
| Ebooks and audiobooks | `taaghche-mcp`, `fidibo-mcp` | `tg_search`, `tg_free_books`; `fd_search`, `fd_free` |
| Printed books | `30book-mcp` | `sb_search`, `sb_book`, `sb_deals` |
| A book's translations and editions compared, ratings, reviews | `iranketab-mcp` | `ik_search`, `ik_book`, `ik_editions` |
| Persian online courses, free courses | `maktabkhooneh-mcp` | `mkh_search`, `mkh_free_courses`, `mkh_cheapest`, `mkh_course` |
| Faradars courses, learning paths, instructors | `faradars-mcp` | `fr_search_courses`, `fr_course`, `fr_learning_paths` |
| Jobs in Iran, employers, advertised salaries, tech jobs and contests | `jobinja-mcp`, `jobvision-mcp`, `irantalent-mcp`, `quera-mcp` | `jj_search_jobs`, `jv_search`, `it_search_jobs`, `qr_jobs`; `jj_salary_stats`, `jv_pay_stats`, `it_salary` |
| Jobs, employers and pay on IranTalent, Jobinja and Jobvision in one call | `iran-jobs-mcp` | `job_search`, `job_companies`, `job_top_companies`, `job_salary` |
| Freelance projects, freelancers, market rates | `ponisha-mcp`, `karlancer-mcp` | `pn_search_projects`, `pn_market`; `kl_projects`, `kl_market_rate` |
| Android apps on Cafe Bazaar and Myket | `iran-apps-mcp` | `ap_search`, `ap_compare`, `ap_top` |
| Find software or a game on Soft98, P30Download, Downloadly and VGDL (metadata and item page only, no download links) | `iran-downloads-mcp` | `dl_search`, `dl_latest`, `dl_item` |
| Whether ArvanCloud, Hamravesh or Chabokan is down, past incidents, Liara or Hamravesh prices | `iran-cloud-status-mcp` | `cs_status`, `cs_incidents`, `cs_compare_prices` |
| Goods from thousands of small Iranian shops (handmade, local products) | `basalam-mcp` | `bs_find_cheapest`, `bs_search`, then `bs_product` |
| Food near an address on Tapsi Food, flash deals | `tapsifood-mcp` | `tf_find_location`, then `tf_search_dishes`, `tf_deals` |
| Live gold, coin, dollar or crypto prices, price history | `tgju-mcp` | `tj_get_prices`, `tj_market_summary`, `tj_price_history` |
| A coin's price on every Iranian crypto exchange (Nobitex, Wallex, Bitpin, Ramzinex, Tabdeal, OMPFinex, Exir), order books, candles | `iran-crypto-mcp` | `ic_compare_price`, then `ic_get_orderbook`, `ic_candles` |
| The live Milli.gold 18k gold price, its history, fees and the cost of a trade, Milli news and help | `milligold-mcp` | `mg_get_price`, `mg_price_history`, `mg_trade_quote`, `mg_latest_posts` |
| The live 18k gold price on Milli.gold, Wallgold, Melligold, Daric and Taline side by side, the cheapest place to buy | `iran-gold-mcp` | `gold_prices`, then `gold_milli_history` |
| Tehran Stock Exchange and Fara Bourse quotes, top movers, order book, indices, real versus legal trading | `tsetmc-mcp` | `ts_search_symbols`, then `ts_get_quote`, `ts_market_movers`, `ts_indices` |
| A listed company's filings: financial statements, EPS, monthly activity reports | `codal-mcp` | `cd_search_letters`, then `cd_letter` |
| Stocks, ETFs, options, bonds, gold and screeners through brokers Mofid and Agah | `iran-brokers-mcp` | `br_search`, then `br_stock`, `br_history`; `br_market`, `br_screener` |
| Bond, sukuk and treasury-bill yields, IPOs, Fara Bourse announcements | `ifb-mcp` | `ifb_yields`, `ifb_yield_curve`, `ifb_ipos` |
| Mutual funds and ETFs: NAV, returns, size | `fipiran-mcp` | `fp_search_funds`, `fp_fund`, `fp_compare` |
| Iran Mercantile Exchange trades, supply offers, commodity prices | `ime-mcp` | `ime_trades`, `ime_supply`, `ime_price_history` |
| Official exchange rates, inflation, policy rates | `cbi-mcp` | `cb_exchange_rates`, `cb_rate_history`, `cb_inflation` |
| Official statistics: CPI inflation, unemployment, population, GDP | `amar-mcp` | `am_inflation`, `am_labour_force`, `am_population`, `am_gdp` |
| Latest Iranian news (Mehr, Khabaronline, Hamshahri, Tabnak, Entekhab, Asriran, Zoomit, Digiato, Varzesh3, Khabarvarzeshi), a topic in the news, a full article | `iran-news-mcp` | `nw_latest_all`, `nw_search`, then `nw_article` |
| Live scores, league tables, fixtures, transfers | `varzesh3-mcp` | `v3_scores`, `v3_standings`, `v3_league_matches` |
| Game and film news, reviews and release dates | `gamefa-mcp` | `gf_latest_articles`, `gf_reviews`, `gf_upcoming_games` |
| A film or series on Filimo or Namava: where to watch, details, episodes, new releases | `iran-vod-mcp` | `vod_search`, `vod_where`, then `vod_title`, `vod_episodes` |
| Today's Jalali, Gregorian and Hijri date, date conversion, holidays, prayer times | `time-ir-mcp` | `ti_today`, `ti_convert_date`, `ti_holidays`, `ti_prayer_times` |
| Recent or strong earthquakes in Iran (IRSC, USGS, EMSC) | `iran-quake-mcp` | `eq_latest`, `eq_significant`, `eq_detail` |
| An Iranian law, regulation or court vote, one article, its amendments | `qavanin-mcp` | `qv_search`, then `qv_law`, `qv_amendments` |
| A law, regulation or ruling in the Official Gazette (rrk.ir) | `rrk-mcp` | `rk_search_laws`, `rk_latest_laws`, then `rk_law_text` |
| Insurance quotes and insurer ratings on BimeBazar and Azki | `iran-insurance-mcp` | `ins_insurers`, `ins_quote_third_party`, `ins_quote_car_body`, `ins_quote_travel` |
| A company's registration, board members, gazette ads, brands | `rasmio-mcp` | `rs_search_companies`, then `rs_company`; `rs_person`, `rs_ad` |
| E-invoice goods ID and VAT rate, activity code, property value, a tax law or circular | `iran-tax-mcp` | `tx_goods_search`, `tx_activity_codes`, `tx_regulations_search` |
| Merchant payments (user's own PayPing account) | `payping-mcp` | `payping_get_balance`, `payping_get_sales_summary` |
| User's own Bale bot | `bale-mcp` | `bot_get_new_messages`, `bot_send_message` |
| User's own crypto wallet: balances, history, swaps, withdrawals | `swapwallet-mcp` | `get_total_balance`, `get_transactions`; `request_swap`, then `get_action_request` |

For the best price, query every server in a category (all doctor servers, all travel servers) and compare.
Full tool list: [TOOLS.md](TOOLS.md). Machine-readable catalog with env vars: [servers.json](servers.json).

## Install

```bash
claude mcp add digikala -- uvx digikala-mcp          # Claude Code
```

```json
{ "mcpServers": { "digikala": { "command": "uvx", "args": ["digikala-mcp"] } } }
```

SwapWallet is hosted, so it is added by URL: `claude mcp add --transport http swapwallet https://swapwallet.app/mcp`.
Other clients take the URL in their own shape; its skill and its
[setup for each client](https://github.com/SwapWallet/swapwallet-mcp#connect) list them. The user then signs in with
OAuth, in the client: Claude Code doesn't open a browser by itself, so tell the user to run `/mcp`, pick the server
and choose Authenticate. Pasavard is hosted too, with no sign-in:
`claude mcp add --transport http pasavard https://pasavard.ir/api/mcp`.

As Claude Code plugins (MCP server plus a skill with usage rules), from the `iran-mcp` marketplace:

```bash
claude plugin install digikala --marketplace sepehr071/iran-mcp     # one server
claude plugin install iran-all --marketplace sepehr071/iran-mcp     # all read-only site servers
```

Bundles: `iran-all`, `iran-food`, `iran-shopping`, `iran-beauty`, `iran-fashion`, `iran-classifieds`, `iran-cars`,
`iran-travel`, `iran-maps`, `iran-health`, `iran-books`, `iran-learning`, `iran-jobs-bundle`, `iran-freelance`, `iran-software`,
`iran-prices`, `iran-stocks`, `iran-economy`, `iran-law`.
Skills only, for any agent: `npx skills add sepehr071/iran-mcp`.

The server key in config is the package name without `-mcp`. [`.mcp.json`](.mcp.json) holds all 77.
Requires [uv](https://docs.astral.sh/uv/) (`pasavard-mcp` and `swapwallet-mcp` don't). Add only the servers the task needs: each one adds 3 to 31 tools.

## Rules every server follows

- Prices are **Toman**. Convert before comparing with any Rial figure from elsewhere. Exceptions: `tsetmc-mcp`,
  `ifb-mcp`, `ime-mcp` and `cbi-mcp` quote **Rial**; `codal-mcp` reports amounts as published, usually million Rial;
  `fipiran-mcp` gives NAV in Rial per unit and fund sizes in billion Toman; `milligold-mcp` gives Rial per milligram,
  Rial per gram and Toman per gram.
- Site servers are **read-only**: no login, basket, booking, order or payment. Hand the user the link to buy.
- `okala-mcp` has an optional OTP login (`ok_login`), read-only, only for text search. Ask the user first.
- `pasavard-mcp` store links are affiliate links: say so when you share one. `cashback_url` returns part of the
  commission after a one-time phone sign-in on pasavard.ir; `buy_url` goes straight to the store.
- `payping-mcp` (`PAYPING_TOKEN`) and `bale-mcp` (`BALE_BOT_TOKEN`) write to the user's own account.
  Confirm with the user before any `payping_create_*`, `payping_send_invoice`, `bot_send_*`, `bot_edit_message`
  or `bot_delete_message` call.
- `swapwallet-mcp` acts on the user's own SwapWallet account. Its `request_*` tools only file a request that the
  user approves or cancels in Telegram within 15 minutes: tell them so, then call `get_action_request`, and never say
  a swap, transfer or withdrawal happened before it reports `EXECUTED`. Confirm a crypto withdrawal's network and
  address with the user first. Its skill covers the rest, including the `MCP_TELEGRAM_NOT_LINKED` and
  `MCP_TWO_FACTOR_ACTIVE` errors.
- Package servers, on timeouts or HTTP 403 outside Iran: set the server's `<NAME>_MCP_PROXY` env var (names in
  `servers.json`).
- Package servers call undocumented site APIs that can change or rate-limit. Keep request rates low.
  `exiryab-mcp` uses ExirYab's public API, limited to 60 requests per minute per IP.
- `30book-mcp` is slow (2 to 5 s per list), and so is `rrk-mcp` (up to 10 s per search). `flytoday-mcp` searches are
  rate-limited per IP. codal.ir blocks an IP for up to an hour after a burst: keep `codal-mcp` calls few.
- `amar-mcp`, `fipiran-mcp`, `ifb-mcp`, `ime-mcp` and `jobinja-mcp` answer only Iranian connections; outside Iran set
  their proxy variable.

## Working on this repo

```
servers/<name>-mcp/   git submodule, one per server (own repo, own issues, own releases)
scripts/catalog.py    rebuilds servers.json, TOOLS.md, .mcp.json, plugins/ and .claude-plugin/ from the submodules
plugins/              one Claude Code plugin per server (MCP server + skill) and bundle plugins (generated)
.claude-plugin/       marketplace.json for the `iran-mcp` plugin marketplace (generated)
PLUGINS.md            plugin layout, agent compatibility, and how a server release reaches users
scripts/banner.py     redraws the banners, social.svg and the release-<version> banners from servers.json
assets/               banners (generated)
README.md / README.fa.md   English (default) and Persian docs; keep both in sync
```

- Update servers: `git submodule update --init --remote && python scripts/catalog.py && python scripts/banner.py`,
  then commit the new pins and generated files.
- Never edit `servers.json`, `TOOLS.md`, `.mcp.json`, `plugins/`, `.claude-plugin/` or the banners by hand.
  Skill text comes from `skill()`, `USE` and `NOTES` in `scripts/catalog.py`, except the rules of a server whose repo
  ships its own `skills/<key>/SKILL.md`, which come from that file. Check with `claude plugin validate .`.
- Add a server: `git submodule add https://github.com/sepehr071/<name>-mcp servers/<name>-mcp`, add it to
  `SERVERS` in `scripts/catalog.py` (and to `GROUPS` in `scripts/banner.py` if its category is new), run both scripts, add a row to both
  READMEs and the table above. Update the 77 / 994 counts written in both READMEs.
- Add a hosted server: `git submodule add <its repo> servers/<name>-mcp` and an entry in `REMOTE` in
  `scripts/catalog.py`, then the same `GROUPS`, README, table and count steps. Its repo needs an MCP Registry
  `server.json` with `remotes` (name, version, description, repository), and the server must publish a server card
  at `<origin>/.well-known/mcp/server-card.json` with its `tools` (with annotations) and `authentication`.
  `catalog.py` reads the tools from the card, marks the server read-only only when it needs no sign-in and every tool
  is `readOnlyHint`, and stops on any sign-in other than OAuth.
- Code changes to a server belong in that server's repo. Inside one: `uv sync`, `uv run ruff check .`,
  `uv run pytest -q` (offline), `uv run pytest -m live -q` (real site).
- Release a server: bump `version` in its `pyproject.toml`, `server.json` and its own entry in `uv.lock`
  (`uv lock --check` passes), push a `v*` tag; CI publishes to PyPI, the MCP Registry and GitHub Releases.
  A README change reaches PyPI only with a release. Then re-pin the submodule here and rerun `catalog.py`.
- The repo is `sepehr071/iran-mcp`, renamed from `awesome-iran-mcp` on 2026-10-23; old URLs redirect. Use the new
  name in every link. A local checkout may still sit in an `awesome-iran-mcp` folder.
