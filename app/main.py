import streamlit as st

from repositories.company_repository import CompanyRepository
from repositories.esg_repository import ESGRepository


st.set_page_config(
    page_title="Gamma ESG Export",
    layout="wide"
)

st.title("Gamma ESG Export")



companies_df = CompanyRepository.get_companies()

company_map = dict(
    zip(
        companies_df["company_name"],
        companies_df["id"]
    )
)



col1, col2, col3 = st.columns(3)

with col1:

    selected_company = st.selectbox(
        "Select Company",
        companies_df["company_name"]
    )

with col2:

    selected_esg = st.selectbox(
        "Select ESG",
        [
            "ALL",
            "ENVIRONMENT",
            "SOCIAL",
            "GOVERNANCE"
        ]
    )

with col3:

    selected_year = st.selectbox(
        "Select Year",
        [
            2021,
            2022,
            2023,
            2024,
            2025,
            2026
        ]
    )


selected_kpi = None

if selected_esg == "ENVIRONMENT":

    selected_kpi = st.selectbox(
        "Select Environment KPI",
        [
            "ALL",
            "ENERGY",
            "WATER",
            "EMISSION",
            "WASTE"
        ]
    )



company_id = company_map[selected_company]



if st.button("Fetch Data"):

    with st.spinner("Fetching ESG data..."):

        df = ESGRepository.fetch_data(
            company_id=company_id,
            year=selected_year,
            esg_type=selected_esg,
            kpi=selected_kpi
        )


    st.success(f"Fetched {len(df)} records")

    st.dataframe(
        df,
        use_container_width=True
    )



    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"{selected_company}_{selected_esg}_{selected_year}.csv",
        mime="text/csv"
    )




st.divider()

st.write("Selected Company:", selected_company)
st.write("Selected ESG:", selected_esg)
st.write("Selected Year:", selected_year)

if selected_kpi:
    st.write("Selected KPI:", selected_kpi)