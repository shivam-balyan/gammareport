import streamlit as st
# from repositories.company_repository import CompanyRepository

st.set_page_config(page_title="Environment Missing Data", layout="wide")
st.title("Environment Missing Data")

# ─────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────

def text_upload_row(text_label, text_placeholder, upload_label, key_suffix, height=150):
    """Renders a (text_area | file_uploader) two-column row."""
    col1, col2 = st.columns(2)
    with col1:
        st.text_area(label=text_label, placeholder=text_placeholder, height=height, key=f"ta_{key_suffix}")
    with col2:
        st.file_uploader(label=upload_label, type=["pdf", "docx", "xlsx"], key=f"fu_{key_suffix}")


def number_upload_row(number_label, upload_label, key_suffix, height=150):
    """Renders a (number_input | file_uploader) two-column row."""
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input(number_label, min_value=0.0, step=0.01, format="%.2f", key=f"ni_{key_suffix}")
    with col2:
        st.file_uploader(label=upload_label, type=["pdf", "docx", "xlsx"], key=f"fu_{key_suffix}")
    return value


def save_button(label, success_msg, key):
    if st.button(label, key=key):
        st.success(success_msg)


def conditional_text_upload(question_label, yes_text_label, yes_text_placeholder,
                             yes_upload_label, select_key):
    """Renders a Yes/No selectbox; if Yes shows text area + file uploader."""
    col1, col2, col3 = st.columns(3)
    with col1:
        answer = st.selectbox(question_label, ["Select", "Yes", "No"], key=f"sel_{select_key}")
    with col2:
        if answer == "Yes":
            st.text_area(label=yes_text_label, placeholder=yes_text_placeholder,
                         height=150, key=f"ta_{select_key}")
    with col3:
        if answer == "Yes":
            st.file_uploader(label=yes_upload_label, type=["pdf", "docx", "xlsx"],
                             key=f"fu_{select_key}")


# ─────────────────────────────────────────
# Company / Year Filters
# ─────────────────────────────────────────

# companies_df = CompanyRepository.get_companies()
# company_map = dict(zip(companies_df["company_name"], companies_df["id"]))

# col1, col2 = st.columns(2)
# with col1:
#     selected_company = st.selectbox("Select Company", companies_df["company_name"])
# with col2:
#     selected_year = st.selectbox("Select Year", [2021, 2022, 2023, 2024, 2025, 2026])

# selected_company_id = company_map[selected_company]

# ─────────────────────────────────────────
# GRI 301 : Materials
# ─────────────────────────────────────────

st.title("GRI 301 : Materials")

# 301-1
st.write("""
### GRI 301-1: Materials Used by Weight or Volume
Enter the total weight or volume of materials used to produce and package the
organization's primary products and services during the reporting period.
""")

col1, col2 = st.columns(2)
with col1:
    non_renewable = st.number_input("I. Non-renewable materials used",  min_value=0.0, step=0.01, format="%.2f")
with col2:
    renewable = st.number_input("II. Renewable materials used", min_value=0.0, step=0.01, format="%.2f")

st.metric("Total Weight or Volume", f"{non_renewable + renewable:.2f}")
save_button("Save Data", "GRI 301-1 data saved successfully.", key="save_301_1")

# 301-2
st.write("""
### GRI 301-2: Recycled Input Materials Used
Percentage of recycled input materials used to manufacture the organization's primary
products and services.
""")

col1, col2 = st.columns(2)
with col1:
    recycled = st.number_input("Total recycled input materials used", min_value=0.0, step=0.01, format="%.2f")
with col2:
    total_input = st.number_input("Total input materials used", min_value=0.0, step=0.01, format="%.2f")

recycled_pct = (recycled / total_input * 100) if total_input > 0 else 0.0
st.metric("Percentage of recycled input materials used", f"{recycled_pct:.2f}%")
save_button("Save Data-2", "GRI 301-2 data saved successfully.", key="save_301_2")

# 301-3
st.write("""
### GRI 301-3: Reclaimed Products and Their Packaging Materials

A. Percentage of reclaimed products and their packaging materials for each product category.
""")

col1, col2 = st.columns(2)
with col1:
    reclaimed = st.number_input(
        "Products and their packaging materials reclaimed within the reporting period",
        min_value=0.0, step=0.01, format="%.2f"
    )
with col2:
    sold = st.number_input(
        "Products sold within the reporting period",
        min_value=0.0, step=0.01, format="%.2f"
    )

reclaimed_pct = (reclaimed / sold * 100) if sold > 0 else 0.0
st.metric("Percentage of reclaimed products and their packaging materials", f"{reclaimed_pct:.2f}%")

st.write("B. How the data for this disclosure have been collected.")
text_upload_row(
    text_label="Data Collection Methodology",
    text_placeholder="Describe how the data for GRI 301-3 have been collected...",
    upload_label="Upload Supporting Document",
    key_suffix="301_3b"
)
save_button("Save Data-3", "GRI 301-3 data saved successfully.", key="save_301_3")

# ─────────────────────────────────────────
# GRI 302 : Energy
# ─────────────────────────────────────────

st.title("GRI 302 : Energy")

# 302-2
st.write("""
### GRI 302-2: Energy Consumption Outside of the Organization

A. Energy Consumption Outside of the Organization, in joules or multiples
""")

col1, col2 = st.columns(2)
with col1:
    st.number_input("Energy Consumption Outside of the Organization", min_value=0.0, step=0.01, format="%.2f")
with col2:
    st.selectbox("Select Energy Unit", ["Joules (J)", "Megajoules (MJ)", "Gigajoules (GJ)"])

st.write("B. Standards, methodologies, assumptions, and/or calculation tools used")
text_upload_row(
    text_label="Data Collection Methodology",
    text_placeholder="Standards, methodologies, assumptions...",
    upload_label="Upload Supporting Document for GRI 302-2B",
    key_suffix="302_2b"
)

st.write("C. Source of the conversion factors used.")
text_upload_row(
    text_label="Enter the sources",
    text_placeholder="Source of the conversion factors used...",
    upload_label="Upload Supporting Document for GRI 302-2C",
    key_suffix="302_2c"
)
save_button("Save Data-4", "GRI 302-2 data saved successfully.", key="save_302_2")

# 302-5
st.write("""
### GRI 302-5: Reductions in energy requirements of products and services

A. Reductions in energy requirements of sold products and services achieved during the
reporting period, in joules or multiples.
""")

col1, col2 = st.columns(2)
with col1:
    st.number_input("Energy Reductions in energy requirements", min_value=0.0, step=0.01, format="%.2f")
with col2:
    st.selectbox("Select Energy reduction Unit", ["Joules (J)", "Megajoules (MJ)", "Gigajoules (GJ)", "Terajoules (TJ)"])

st.write("""
B. Basis for calculating reductions in energy consumption, such as base year or baseline,
including the rationale for choosing it.
""")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Select Baseline Or BaseYear", ["Base Year", "Baseline"])
with col2:
    st.text_area(label="Justification for Baseline or Base Year",
                 placeholder="Enter the energy reductions...", height=150, key="ta_302_5b")

st.write("C. Standards, methodologies, assumptions, and/or calculation tools used.")
text_upload_row(
    text_label="Enter the Standards, methodologies, assumptions, and/or calculation tools used",
    text_placeholder="Standards, methodologies, assumptions...",
    upload_label="Upload Supporting Document for GRI 302-5C",
    key_suffix="302_5c"
)
save_button("Save Data-5", "GRI 302-5 data saved successfully.", key="save_302_5")

# ─────────────────────────────────────────
# GRI 303 : Water
# ─────────────────────────────────────────

st.title("GRI 303 : Water")

# 303-1 sub-sections A–D
GRI_303_1_SECTIONS = [
    (
        "A. A description of how the organization interacts with water, including how and where "
        "water is withdrawn, consumed, and discharged, and the water-related impacts the "
        "organization has caused or contributed to, or that are directly linked to its operations, "
        "products, or services by its business relationships",
        "Interactions with water and water-related impacts",
        "Describe how the organization interacts with water (withdrawn, consumed, discharged) "
        "and water-related impacts (Economy, Environment, People)...",
        "Upload Supporting Document for GRI 303-1A",
        "303_1a",
    ),
    (
        "B. A description of the approach used to identify water-related impacts, including the "
        "scope of assessments, their timeframe, and any tools or methodologies used.",
        "Approach used to identify water-related impacts",
        "Describe the Scope of assessments, their timeframe, and any tools or methodologies "
        "used to identify water-related impacts...",
        "Upload Supporting Document for GRI 303-1B",
        "303_1b",
    ),
    (
        "C. A description of how water-related impacts are addressed, including how the "
        "organization works with stakeholders to steward water as a shared resource, and how "
        "it engages with suppliers or customers with significant water-related impacts.",
        "How water-related impacts are addressed",
        "Describe how the organization works with stakeholders to steward water as a shared "
        "resource, and how it engages with suppliers or customers with significant water-related impacts...",
        "Upload Supporting Document for GRI 303-1C",
        "303_1c",
    ),
    (
        "D. An explanation of the process for setting any water-related goals and targets that are "
        "part of the organization's approach to managing water and effluents, and how they "
        "relate to public policy and the local context of each area with water stress.",
        "Process for setting water-related goals and targets",
        "Describe the process for setting water-related goals and targets, and how they relate "
        "to public policy and the local context of each area with water stress...",
        "Upload Supporting Document for GRI 303-1D",
        "303_1d",
    ),
]

st.write("### GRI 303-1: Interactions with water as a shared resource")
for description, label, placeholder, upload_label, key in GRI_303_1_SECTIONS:
    st.write(description)
    text_upload_row(label, placeholder, upload_label, key)

save_button("Save Data-6", "GRI 303-1 data saved successfully.", key="save_303_1")

# 303-2
st.write("""
### GRI 303-2: Management of water discharge-related impacts

A. A description of any minimum standards set for the quality of effluent discharge, and
how these minimum standards were determined.
""")
text_upload_row(
    "Minimum effluent discharge standards and determination method",
    "What minimum water quality standards do you follow before discharging waste water "
    "and how were those standards determined...",
    "Upload Supporting Document for GRI 303-2A",
    "303_2a"
)

st.write("A-i. How standards for facilities operating in locations with no local discharge requirements were determined.")
text_upload_row(
    "Basis for determining effluent discharge standards in absence of local regulations",
    "Describe the standards to determine the discharge of waste water in absence of local "
    "regulations and outdated laws...",
    "Upload Supporting Document for GRI 303-2A.i",
    "303_2a_i"
)

st.write("A-ii. Any internally developed water quality standards or guidelines.")
conditional_text_upload(
    question_label="Any internally developed standards?",
    yes_text_label="Explain internal standards/guidelines",
    yes_text_placeholder="Describe internally developed water quality standards or guidelines...",
    yes_upload_label="Upload Supporting Document",
    select_key="303_2a_ii"
)

st.write("A-iii. Any sector-specific standards considered.")
conditional_text_upload(
    question_label="Any sector-specific standards?",
    yes_text_label="Explain sector-specific standards/guidelines",
    yes_text_placeholder="Describe sector-specific water quality standards or guidelines...",
    yes_upload_label="Upload Supporting Document",
    select_key="303_2a_iii"
)

st.write("A-iv. Whether the profile of the receiving waterbody was considered.")
text_upload_row(
    "Assessment of receiving waterbody conditions before discharge",
    "Describe whether the profile of the receiving waterbody was considered before discharging "
    "waste water and how it influenced discharge standards...",
    "Upload Supporting Document for GRI 303-2A.iv",
    "303_2a_iv"
)
save_button("Save Data-7", "GRI 303-2 data saved successfully.", key="save_303_2")

# ─────────────────────────────────────────
# GRI 306 : Waste
# ─────────────────────────────────────────

st.title("GRI 306 : Waste")

# 306-1
st.write("""
### GRI 306-1: Waste generation and significant waste-related impacts

A. Description of organization's significant actual and potential waste-related impacts:
""")
text_upload_row(
    "The inputs, activities, and outputs that lead or could lead to these impacts",
    "Describe the inputs, activities and output that lead or could lead to waste related impacts",
    "Upload Supporting Document for GRI 306-A1",
    "306_1a1"
)
text_upload_row(
    "Source of the waste-related impacts (own operations, upstream/downstream value chain).",
    "Describe the occurrence of waste-related impact due to organization activities or value chain (upstream/downstream)",
    "Upload Supporting Document for GRI 306-A2",
    "306_1a2"
)
save_button("Save Data-8", "GRI 306 data saved successfully.", key="save_306_1")

# 306-2
st.write("""
### GRI 306-2: Management of significant waste-related impacts

A. Actions, including circularity measures, taken to prevent waste generation in the
organization's own activities and upstream and downstream in its value chain, and to
manage significant impacts from waste generated.
""")
text_upload_row(
    "Actions & circularity measures taken to prevent and manage waste-related impacts across operations and the value chain.",
    "Describe the actions and circulatory measures taken.",
    "Upload Supporting Document for GRI 306-A",
    "306_2a"
)

st.write("""B. If the waste generated by the organization in its own activities is managed by a third
party, a description of the processes used to determine whether the third party
manages the waste in line with contractual or legislative obligations.""")
text_upload_row(
    "Processes used to ensure third parties manage waste in compliance with contractual and legal requirements.",
    "Processes used to ensure third-party waste management complies with contractual and legal requirements...",
    "Upload Supporting Document for GRI 306-B",
    "306_2b"
)

st.write("C. The processes used to collect and monitor waste-related data.")
text_upload_row(
    "The processes used to collect and monitor waste-related data.",
    "Describe the processes used to collect and monitor waste-related data.",
    "Upload Supporting Document for GRI 306-C",
    "306_2c"
)
save_button("Save Data-9", "GRI 306 data saved successfully.", key="save_306_2")

# ─────────────────────────────────────────
# GRI 308 : Supplier Environmental Assessment
# ─────────────────────────────────────────

st.title("GRI 308 : Supplier Environmental Assessment")

# 308-1
st.write("### GRI 308-1: New suppliers that were screened using environmental criteria")
text_upload_row(
    "Percentage of new suppliers that were screened using environmental criteria.",
    "(New suppliers screened / total number of suppliers) * 100",
    "Upload Supporting Document for GRI 308-1",
    "308_1"
)

# 308-2
st.write("### GRI 308-2: Negative environmental impacts in the supply chain and actions taken")

GRI_308_2_SECTIONS = [
    ("A. Number of suppliers assessed for environmental impacts",                                         "....", "Upload Supporting Document for GRI 308-2A", "308_2a"),
    ("B. Number of suppliers identified as having significant actual and potential negative environmental impacts.", "....", "Upload Supporting Document for GRI 308-2B", "308_2b"),
    ("C. Significant actual and potential negative environmental impacts identified in the supply chain.",  "....", "Upload Supporting Document for GRI 308-2C", "308_2c"),
    (
        "D. Percentage of suppliers identified as having significant actual and potential negative "
        "environmental impacts with which improvements were agreed upon as a result of assessment.",
        "After finding environment problems how many suppliers agreed to fix them...",
        "Upload Supporting Document for GRI 308-2D",
        "308_2d",
    ),
    (
        "E. Percentage of suppliers identified as having significant actual and potential negative "
        "environmental impacts with which relationships were terminated as a result of assessment, and why.",
        "How many suppliers were removed or had contracts cancelled due to environmental issues...",
        "Upload Supporting Document for GRI 308-2E",
        "308_2e",
    ),
]

for label, placeholder, upload_label, key in GRI_308_2_SECTIONS:
    text_upload_row(label, placeholder, upload_label, key)