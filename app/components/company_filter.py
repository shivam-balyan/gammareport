"""Reusable company + reporting-year selector.

Renders the two filters and returns the selection. The chosen company id and
year are also stored in session state so that downstream forms (and any save
action) can link the entered data to the right company/period.
"""

import streamlit as st

from app import constants
from repositories.company_repository import CompanyRepository

# Session-state keys holding the active selection for the Environment forms.
SELECTED_COMPANY_ID = "selected_company_id"
SELECTED_COMPANY_NAME = "selected_company_name"
SELECTED_YEAR = "selected_year"


def select_company_and_year(key_prefix):
    """Render Company + Reporting year selectboxes; return (name, id, year)."""
    companies_df = CompanyRepository.get_companies()
    company_map = dict(
        zip(companies_df["company_name"], companies_df["id"])
    )

    col1, col2 = st.columns(2)
    with col1:
        company_name = st.selectbox(
            "Company",
            companies_df["company_name"],
            key=f"{key_prefix}_company",
        )
    with col2:
        year = st.selectbox(
            "Reporting year",
            constants.REPORTING_YEARS,
            key=f"{key_prefix}_year",
        )

    company_id = company_map[company_name]

    st.session_state[SELECTED_COMPANY_NAME] = company_name
    st.session_state[SELECTED_COMPANY_ID] = company_id
    st.session_state[SELECTED_YEAR] = year

    return company_name, company_id, year
