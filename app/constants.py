"""Application-wide constants shared across pages and views.

Single source of truth for UI/config values (app titles, navigation labels and
the dashboard filter options such as reporting years). Keep values that are
used by more than one module here; values used by only a single form/view stay
local to that module.
"""

# --- App / page configuration -------------------------------------------------

APP_TITLE = "Gamma ESG"
APP_TAGLINE = "Sustainability reporting"
PAGE_TITLE = "Gamma ESG"
PAGE_LAYOUT = "wide"

# --- Navigation ---------------------------------------------------------------

NAV_DASHBOARD = "Dashboard"
NAV_ENVIRONMENT = "Environment"
NAV_UNIVERSAL = "Universal Standards"

# --- Page subtitles -----------------------------------------------------------

DASHBOARD_SUBTITLE = "Fetch and export company ESG data."
ENVIRONMENT_SUBTITLE = "GRI environmental disclosures — materials and energy."
UNIVERSAL_SUBTITLE = "GRI 2 General Disclosures (2-1 to 2-30)."

# --- ESG categories -----------------------------------------------------------

ESG_TYPE_ALL = "ALL"
ESG_TYPE_ENVIRONMENT = "ENVIRONMENT"
ESG_TYPE_SOCIAL = "SOCIAL"
ESG_TYPE_GOVERNANCE = "GOVERNANCE"

ESG_TYPES = [
    ESG_TYPE_ALL,
    ESG_TYPE_ENVIRONMENT,
    ESG_TYPE_SOCIAL,
    ESG_TYPE_GOVERNANCE,
]

# --- Dashboard filter options -------------------------------------------------

ENVIRONMENT_KPIS = ["ALL", "ENERGY", "WATER", "EMISSION", "WASTE"]

REPORTING_YEARS = [2021, 2022, 2023, 2024, 2025, 2026]
