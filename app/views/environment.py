"""Environment page — composes the GRI environmental disclosure forms."""

import streamlit as st

from app import constants
from app.components import company_filter
from app.ui import theme
from app.views.gri import gri_301_1, gri_301_2, gri_302_2, gri_302_5


def render():
    theme.page_header(constants.NAV_ENVIRONMENT, constants.ENVIRONMENT_SUBTITLE)

    with st.container(border=True):
        st.subheader("Company & reporting period")
        company_name, company_id, year = company_filter.select_company_and_year(
            key_prefix="env"
        )
        st.caption(
            f"Entries below will be saved for **{company_name}** · **{year}**."
        )

    gri_301_1.render()
    gri_301_2.render()
    gri_302_2.render()
    gri_302_5.render()
