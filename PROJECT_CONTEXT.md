# Gamma Report Interface — Project Context

> A single reference document describing **what this project is**, **how it is
> structured**, and **what each file does**. Intended to be handed to an AI
> assistant (ChatGPT / Claude) as project context.

---

## 1. What this project is

**Gamma ESG (Gamma Report Interface)** is a **Streamlit web application** for
**GRI-aligned ESG (Environmental, Social, Governance) sustainability
reporting**.

It does two main things:

1. **Dashboard** — Query and export existing ESG data for a company from a
   PostgreSQL database (filter by company, ESG category, reporting year, and
   Environment KPI), view it as a table, and download it as CSV.
2. **Environment data entry** — Interactive forms for entering GRI
   environmental disclosures with dynamic add/delete rows and automatic total
   calculations. Currently implements three GRI disclosures:
   - **GRI 301-1** — Materials used by weight or volume
   - **GRI 301-2** — Recycled input materials used
   - **GRI 302-2** — Energy consumption outside of the organization

### Tech stack

| Concern            | Choice                                          |
| ------------------ | ----------------------------------------------- |
| Language           | Python `>=3.10` (pinned to `3.10`)              |
| UI framework       | Streamlit `>=1.57`                              |
| Database           | PostgreSQL (via SQLAlchemy `>=2.0` + psycopg2)  |
| Data handling      | pandas `>=2.3`                                   |
| Config / settings  | pydantic + pydantic-settings + python-dotenv    |
| Package manager    | `uv` (lockfile `uv.lock`, config `pyproject.toml`) |

---

## 2. How to run it

```bash
# 1. Install dependencies (uv)
uv sync

# 2. Configure the database connection in .env
#    DATABASE_URL=postgresql://user:password@host:port/dbname

# 3. Launch the Streamlit app
uv run streamlit run app/main.py
```

The app requires a reachable PostgreSQL database that already contains the ESG
tables (this project is a **reporting/entry interface**, not the schema owner).

---

## 3. Directory & file structure

```
gammareportinterface/
├── pyproject.toml            # Project metadata + dependencies (uv)
├── uv.lock                   # Locked dependency versions
├── requirements.txt          # (empty — uv is the source of truth)
├── .python-version           # Pins Python 3.10
├── .env                      # DATABASE_URL (SECRET — not committed)
├── .gitignore                # Ignores __pycache__, build artifacts, .venv
├── README.md                 # (currently empty)
├── PROJECT_CONTEXT.md         # This document
│
├── .streamlit/
│   └── config.toml           # Streamlit theme (green ESG palette) + client opts
│
├── core/                     # Cross-cutting infrastructure
│   ├── config.py             # pydantic Settings — loads DATABASE_URL from .env
│   └── database.py           # SQLAlchemy engine (single shared connection pool)
│
├── repositories/             # Data-access layer (Repository pattern)
│   ├── company_repository.py # Fetch list of companies
│   └── esg_repository.py     # Fetch ESG data across env/social/governance tables
│
├── utils/
│   └── constants.py          # ESG_TABLE_MAPPING: ESG category/KPI → DB table name
│
├── app/                      # Streamlit application
│   ├── main.py               # Entry point — page config, theme, sidebar routing
│   ├── constants.py          # App-wide UI constants (titles, nav, filters, years)
│   │
│   ├── ui/
│   │   └── theme.py          # Global CSS design system + page_header helper
│   │
│   ├── components/           # Reusable UI building blocks
│   │   ├── company_filter.py # Company + reporting-year selector (writes session)
│   │   └── dynamic_rows.py   # Add/delete dynamic form rows (stable-id tracking)
│   │
│   └── views/                # Page-level views
│       ├── dashboard.py      # Dashboard page (query + export ESG data)
│       ├── environment.py    # Environment page (composes the GRI forms)
│       └── gri/              # Individual GRI disclosure forms
│           ├── gri_301_1.py  # Materials used by weight or volume
│           ├── gri_301_2.py  # Recycled input materials used
│           └── gri_302_2.py  # Energy consumption outside the organization
│
└── (reference images)
    ├── gri301-2.jpeg         # UI/spec reference for GRI 301-2 form
    ├── gri302-2.jpeg         # UI/spec reference for GRI 302-2 form
    └── environment.jpeg      # UI/spec reference for the Environment page
```

> Every package directory (`core/`, `repositories/`, `app/`, `app/ui/`,
> `app/components/`, `app/views/`, `app/views/gri/`) contains an empty
> `__init__.py` marking it as an importable Python package.

---

## 4. Architecture & layering

The app follows a clean layered structure:

```
┌─────────────────────────────────────────────┐
│  app/main.py  →  sidebar routing (PAGES map) │   Presentation entry
├─────────────────────────────────────────────┤
│  app/views/*  (dashboard, environment, gri/) │   Page views
│  app/components/*  (reusable widgets)         │   Reusable UI
│  app/ui/theme.py  (CSS design system)         │   Styling
├─────────────────────────────────────────────┤
│  repositories/*  (CompanyRepository, ESG…)    │   Data access (Repository)
├─────────────────────────────────────────────┤
│  core/database.py  →  SQLAlchemy engine       │   Infrastructure
│  core/config.py    →  pydantic Settings/.env  │
├─────────────────────────────────────────────┤
│  utils/constants.py  (ESG table mapping)      │   Shared config/data
└─────────────────────────────────────────────┘
                      ↓
              PostgreSQL database
```

**Design principles observed in the code** (aligned with the repo's coding
style rules):

- **Repository pattern** — all SQL is encapsulated in `repositories/`; views
  never touch the DB engine directly.
- **Immutability** — `dynamic_rows.py` rebuilds session-state lists instead of
  mutating in place; row ids are stable so deleting a row doesn't shift others.
- **Single source of truth** — UI constants live in `app/constants.py`;
  category→table mapping lives in `utils/constants.py`.
- **Small, focused files** — one GRI disclosure per file, one component per file.

---

## 5. File-by-file explanation

### Configuration & infrastructure

**`core/config.py`**
Defines a pydantic `Settings` class that reads `DATABASE_URL` from `.env`.
Exposes a module-level `settings` singleton. Fails fast at startup if the URL
is missing.

**`core/database.py`**
Creates the shared SQLAlchemy `engine` from `settings.DATABASE_URL`, with
`pool_pre_ping=True` so stale/dropped connections are detected and recycled.

**`utils/constants.py`**
`ESG_TABLE_MAPPING` — maps ESG categories and KPIs to the actual PostgreSQL
table names:
- `ENVIRONMENT` → `energy_management`, `add_water`, `emission_management`, `waste_management`
- `SOCIAL` → `social`
- `GOVERNANCE` → `governance`

**`.streamlit/config.toml`**
Streamlit theme (ESG green `#16A34A` primary, light canvas) and client options
(`showErrorDetails = true`, minimal toolbar).

### Data access layer

**`repositories/company_repository.py`**
`CompanyRepository.get_companies()` — returns a DataFrame of `id, company_name`
for rows in the `companies` table where `role = 'company'`, ordered by name.

**`repositories/esg_repository.py`**
`ESGRepository.fetch_data(company_id, year, esg_type, kpi=None)` — the core
query engine. Branches by `esg_type`:
- **ENVIRONMENT** — queries one or all environment tables (optionally filtered
  by a specific KPI), joining `fields_master` for human-readable field names,
  filtered on `frequency_year`.
- **SOCIAL** / **GOVERNANCE** — queries the `social` / `governance` tables,
  filtered on `year`.
- **ALL** — unions social + governance + all environment tables.
Concatenates all results into a single pandas DataFrame and de-duplicates
columns. Uses parameterized queries (`:company_id`, `:year`) for safety.

> ⚠️ Note for maintainers: the ENVIRONMENT/ALL branches build table names via
> f-strings from the trusted internal `ESG_TABLE_MAPPING` (not user input), so
> injection risk is contained — but values (`company_id`, `year`) are always
> passed as bound parameters.

### Application shell

**`app/main.py`**
Streamlit entry point. Adds the project root to `sys.path` so packages resolve
when launched via `streamlit run app/main.py`. Configures the page, applies the
theme, renders the sidebar navigation (a `st.radio`), and dispatches to the
selected page via the `PAGES` dict (`Dashboard` / `Environment`).

**`app/constants.py`**
App-wide UI constants: titles, taglines, navigation labels, page subtitles, ESG
category list, `ENVIRONMENT_KPIS` (`ALL, ENERGY, WATER, EMISSION, WASTE`), and
`REPORTING_YEARS` (2021–2026).

**`app/ui/theme.py`**
The design system. `apply()` injects a global CSS stylesheet (brand color
tokens, shadows, concentric radii, tactile buttons, styled sidebar nav radio,
metric cards, focus rings, quiet "danger" delete buttons). `page_header(title,
subtitle)` renders a consistent page heading.

### Reusable components

**`app/components/company_filter.py`**
`select_company_and_year(key_prefix)` — renders Company + Reporting-year
selectboxes, stores the selection in session state
(`selected_company_id/name/year`) so downstream forms can link entered data to
the right company/period, and returns `(name, id, year)`.

**`app/components/dynamic_rows.py`**
Helpers for dynamic, addable/deletable form rows. Each row group is keyed by a
`prefix`; rows are tracked by **stable integer ids** (not list indices) so
deleting a row never shifts other rows' widget values — a common Streamlit
pitfall. Functions: `init_section`, `add_row`, `delete_row`, `row_ids`,
`render_heading_with_info` (title + ℹ️ Info popover), `render_delete_button`,
`render_add_button`. Always keeps at least one row.

### Views (pages)

**`app/views/dashboard.py`**
The Dashboard page. Renders filters (company, ESG category, year, and — when
Environment is selected — a KPI selector), fetches data via `ESGRepository`,
shows a record count metric + dataframe, and offers a CSV download named
`{company}_{esg}_{year}.csv`.

**`app/views/environment.py`**
The Environment page. Renders the shared Company & reporting-period selector,
then composes the three GRI forms (`gri_301_1`, `gri_301_2`, `gri_302_2`) in
sequence.

### GRI disclosure forms

**`app/views/gri/gri_301_1.py` — Materials used by weight or volume**
Two sections (Renewable / Non-renewable materials). Each row: material name,
Purchased/Sourced-internally, unit (Tonnes / Kilo litres), amount. Auto-computes
totals by weight and by volume per section.

**`app/views/gri/gri_301_2.py` — Recycled input materials used**
Two sections (Solid / Liquid materials). Each row: material name, unit, amount,
% recycled. Auto-computes total input material and recycled amount
(`amount × pct / 100`) per section.

**`app/views/gri/gri_302_2.py` — Energy consumption outside the organization**
An electricity row (amount + unit KWH/MWH/GWH) auto-converted to its Joule
equivalent, plus dynamic "other fuel" rows (amount + unit Joules/Mega/Giga
Joules). Displays total energy consumption = electricity (J) + other fuel (J),
using conversion-factor lookup tables.

---

## 6. Current state & notes for future work

- **Data entry is not yet persisted.** The GRI forms compute and display totals
  but there is **no save/insert path** back to the database yet — the forms are
  input + live calculation only. `company_filter.py` already stashes the target
  company/year in session state in anticipation of a save action.
- **`README.md` is empty** — this `PROJECT_CONTEXT.md` currently serves as the
  primary documentation.
- **`requirements.txt` is empty** — dependencies are managed by `uv` via
  `pyproject.toml` / `uv.lock`.
- **Only the Environment domain is implemented as forms.** Social and
  Governance exist only on the read/Dashboard side (via `ESGRepository`), not as
  data-entry forms.
- **Reference images** (`gri301-2.jpeg`, `gri302-2.jpeg`, `environment.jpeg`)
  are the visual/spec source for the corresponding forms.

---

## 7. Quick glossary

| Term            | Meaning                                                            |
| --------------- | ----------------------------------------------------------------- |
| **ESG**         | Environmental, Social, Governance — sustainability reporting areas |
| **GRI**         | Global Reporting Initiative — the reporting standard being followed |
| **GRI 301-1/2** | Materials-related disclosures                                      |
| **GRI 302-2**   | Energy-related disclosure (energy consumed outside the org)        |
| **KPI**         | Key Performance Indicator (Energy, Water, Emission, Waste)         |
| **fields_master** | DB table mapping `field_id` → human-readable field name/group   |
```
