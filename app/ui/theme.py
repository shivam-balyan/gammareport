"""Design system for the app — global CSS and reusable layout helpers.

The CSS implements a small set of design-engineering details that make the
interface feel production-grade: concentric radii, subtle layered shadows,
tabular numerals on metrics, balanced text wrapping, antialiased font smoothing,
tactile (but restrained) button states, and comfortable hit areas.
"""

import streamlit as st

_GLOBAL_CSS = """
<style>
:root {
  --brand-50:  #ECFDF5;
  --brand-100: #D1FAE5;
  --brand-500: #16A34A;
  --brand-600: #15803D;
  --brand-700: #166534;

  --surface: #FFFFFF;
  --canvas:  #F6F8FA;

  --ink:      #0F172A;
  --ink-soft: #475569;
  --muted:    #94A3B8;

  --border:        rgba(15, 23, 42, 0.10);
  --border-strong: rgba(15, 23, 42, 0.16);
  --ring:          rgba(22, 163, 74, 0.32);
  --danger:        #DC2626;
  --danger-soft:   rgba(220, 38, 38, 0.10);

  --shadow-sm: 0 1px 2px rgba(15,23,42,0.05), 0 1px 3px rgba(15,23,42,0.04);
  --shadow-md: 0 2px 4px rgba(15,23,42,0.05), 0 8px 24px rgba(15,23,42,0.08);

  --radius-card:    14px;
  --radius-control: 9px;
}

/* Font smoothing (macOS) at the root layout. */
html, body, .stApp {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Roomier, centered content column; quieter chrome. */
div[data-testid="stMainBlockContainer"] {
  padding-top: 2.25rem;
  padding-bottom: 4rem;
  max-width: 1180px;
}
header[data-testid="stHeader"] { background: transparent; }
footer { display: none; }

/* Typography. */
.stApp h1 {
  font-weight: 800;
  letter-spacing: -0.021em;
  text-wrap: balance;
}
.stApp h2, .stApp h3 { text-wrap: balance; }
.stApp p, .stApp li, [data-testid="stCaptionContainer"] { text-wrap: pretty; }

/* ---- Sidebar ------------------------------------------------------------- */
section[data-testid="stSidebar"] {
  border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] .brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--ink);
  padding: 4px 4px 0;
}

/* Turn the nav radio group into tactile menu items. */
section[data-testid="stSidebar"] div[role="radiogroup"] { gap: 6px; }
section[data-testid="stSidebar"] div[role="radiogroup"] label {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 42px;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  color: var(--ink-soft);
  transition-property: background-color, color;
  transition-duration: 150ms;
  transition-timing-function: ease-out;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
  background: var(--brand-50);
  color: var(--brand-700);
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
  background: var(--brand-500);
  color: #FFFFFF;
}
/* Hide the raw radio dot; the whole row is the control. */
section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
  display: none;
}

/* ---- Cards (st.container(border=True)) ----------------------------------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: var(--surface);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-sm);
}

/* ---- Metrics ------------------------------------------------------------- */
div[data-testid="stMetric"] {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-card);
  padding: 16px 18px;
  box-shadow: var(--shadow-sm);
}
div[data-testid="stMetricValue"] {
  font-variant-numeric: tabular-nums;
  font-weight: 700;
  letter-spacing: -0.01em;
}
div[data-testid="stMetricLabel"] { color: var(--ink-soft); }

/* ---- Buttons ------------------------------------------------------------- */
.stButton > button, .stDownloadButton > button {
  min-height: 42px;
  border-radius: var(--radius-control);
  border: 1px solid var(--border-strong);
  font-weight: 600;
  transition-property: transform, background-color, box-shadow, border-color;
  transition-duration: 150ms;
  transition-timing-function: ease-out;
}
.stButton > button:hover, .stDownloadButton > button:hover {
  box-shadow: var(--shadow-sm);
  border-color: var(--brand-500);
}
.stButton > button:active, .stDownloadButton > button:active {
  transform: scale(0.98);
}
.stButton > button:focus-visible, .stDownloadButton > button:focus-visible {
  box-shadow: 0 0 0 3px var(--ring);
}

/* Delete-row buttons (keys end with `_del_<id>`) read as quiet danger. */
div[class*="_del_"] .stButton > button {
  color: var(--muted);
  border-color: var(--border);
}
div[class*="_del_"] .stButton > button:hover {
  color: var(--danger);
  border-color: var(--danger);
  background: var(--danger-soft);
}

/* ---- Inputs -------------------------------------------------------------- */
.stTextInput input,
.stNumberInput input,
div[data-baseweb="select"] > div {
  border-radius: var(--radius-control) !important;
}
.stTextInput input:focus,
.stNumberInput input:focus {
  border-color: var(--brand-500);
  box-shadow: 0 0 0 3px var(--ring);
}

/* ---- Popover (ℹ️ Info) --------------------------------------------------- */
div[data-testid="stPopover"] button {
  min-height: 42px;
  border-radius: var(--radius-control);
}
</style>
"""


def apply():
    """Inject the global stylesheet. Call once, right after set_page_config."""
    st.markdown(_GLOBAL_CSS, unsafe_allow_html=True)


def page_header(title, subtitle=None):
    """Render a consistent page title with an optional subtitle."""
    st.title(title)
    if subtitle:
        st.caption(subtitle)
