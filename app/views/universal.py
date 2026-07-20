"""Universal Standards page — GRI 2 General Disclosures (2-1 to 2-30).

Renders the disclosures defined in ``universal_spec`` as data-entry cards. The
spec is the single source of truth for wording; this module only handles layout
and session-state keys, mirroring the other GRI forms (bordered cards, an
ℹ️ Info popover per disclosure, and values preserved in session state).
"""

import streamlit as st

from app import constants
from app.components import company_filter, dynamic_rows
from app.ui import theme
from app.views.universal_spec import SECTIONS

DISCLOSURE_HELP_TEMPLATE = (
    "GRI {code} — {title}. Provide the information required for each lettered "
    "point below. Leave a point blank if it is not applicable."
)


def _field_key(code, req_key):
    """Stable session-state key for a disclosure requirement input."""
    return f"univ_{code}_{req_key}"


def _render_disclosure(disclosure):
    with st.container(border=True):
        dynamic_rows.render_heading_with_info(
            f"{disclosure.code}  {disclosure.title}",
            DISCLOSURE_HELP_TEMPLATE.format(
                code=disclosure.code, title=disclosure.title
            ),
            as_subheader=False,
        )
        for req in disclosure.requirements:
            st.text_area(
                f"{req.key}. {req.label}",
                key=_field_key(disclosure.code, req.key),
            )


def render():
    theme.page_header(constants.NAV_UNIVERSAL, constants.UNIVERSAL_SUBTITLE)

    with st.container(border=True):
        st.subheader("Company & reporting period")
        company_name, company_id, year = company_filter.select_company_and_year(
            key_prefix="univ"
        )
        st.caption(
            f"Entries below will be saved for **{company_name}** · **{year}**."
        )

    for section in SECTIONS:
        st.header(section.title)
        for disclosure in section.disclosures:
            _render_disclosure(disclosure)
