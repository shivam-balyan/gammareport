"""Dashboard page — fetch and export company ESG data."""

import streamlit as st

from app import constants
from app.ui import theme
from repositories.company_repository import CompanyRepository
from repositories.esg_repository import ESGRepository


def _render_filters(companies_df):
    with st.container(border=True):
        st.subheader("Filters")

        col1, col2, col3 = st.columns(3)

        with col1:
            selected_company = st.selectbox(
                "Company",
                companies_df["company_name"],
            )
        with col2:
            selected_esg = st.selectbox("ESG category", constants.ESG_TYPES)
        with col3:
            selected_year = st.selectbox("Reporting year", constants.REPORTING_YEARS)

        selected_kpi = None
        if selected_esg == constants.ESG_TYPE_ENVIRONMENT:
            selected_kpi = st.selectbox(
                "Environment KPI", constants.ENVIRONMENT_KPIS
            )

        fetch = st.button("Fetch data", type="primary", use_container_width=True)

    return selected_company, selected_esg, selected_year, selected_kpi, fetch


def _render_results(df, selected_company, selected_esg, selected_year):
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])
        col1.metric("Records", len(df))
        col2.write("")

        if df.empty:
            st.info("No records found for the selected filters.")
            return

        st.dataframe(df, use_container_width=True)

        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name=f"{selected_company}_{selected_esg}_{selected_year}.csv",
            mime="text/csv",
        )


def render():
    theme.page_header(constants.NAV_DASHBOARD, constants.DASHBOARD_SUBTITLE)

    companies_df = CompanyRepository.get_companies()
    company_map = dict(
        zip(companies_df["company_name"], companies_df["id"])
    )

    selected_company, selected_esg, selected_year, selected_kpi, fetch = (
        _render_filters(companies_df)
    )

    if fetch:
        company_id = company_map[selected_company]

        with st.spinner("Fetching ESG data..."):
            df = ESGRepository.fetch_data(
                company_id=company_id,
                year=selected_year,
                esg_type=selected_esg,
                kpi=selected_kpi,
            )

        _render_results(df, selected_company, selected_esg, selected_year)
