"""Streamlit entry point — configures the app and routes between pages."""

import sys
from pathlib import Path

# Make the project root importable so `app`, `repositories`, `core`, etc.
# resolve when launched via `streamlit run app/main.py`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

from app import constants
from app.ui import theme
from app.views import dashboard, environment, universal

# Maps the sidebar navigation label to the page's render function.
PAGES = {
    constants.NAV_DASHBOARD: dashboard.render,
    constants.NAV_ENVIRONMENT: environment.render,
    constants.NAV_UNIVERSAL: universal.render,
}


def _configure_page():
    st.set_page_config(
        page_title=constants.PAGE_TITLE,
        page_icon="🌱",
        layout=constants.PAGE_LAYOUT,
    )
    theme.apply()


def _select_page():
    with st.sidebar:
        st.markdown(
            f'<div class="brand">🌱 {constants.APP_TITLE}</div>',
            unsafe_allow_html=True,
        )
        st.caption(constants.APP_TAGLINE)
        st.write("")
        selected = st.radio(
            "Navigation",
            list(PAGES.keys()),
            label_visibility="collapsed",
        )
        st.divider()
        st.caption("GRI-aligned ESG reporting")
        return selected


def main():
    _configure_page()
    selected_page = _select_page()
    PAGES[selected_page]()


main()
