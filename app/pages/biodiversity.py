
import streamlit as st

# from repositories.company_repository import CompanyRepository

# st.set_page_config(
#     page_title="Biodiversity Missing Data",
#     layout="wide"
# )

# st.title("Biodiversity Missing Data")

# companies_df = CompanyRepository.get_companies()

# company_map = dict(
#     zip(
#         companies_df["company_name"],
#         companies_df["id"]
#     )
# )



# Top Filters
# col1, col2 = st.columns(2)

# with col1:
#     selected_company = st.selectbox(
#         "Select Company",
#         companies_df["company_name"]
#     )

# with col2:
#     selected_year = st.selectbox(
#         "Select Year",
#         [
#             2021,
#             2022,
#             2023,
#             2024,
#             2025,
#             2026
#         ]
#     )


st.title("GRI 101 : Biodiveristy 2024")

st.write("""
### GRI 101-1: Policies to halt and reverse biodiversity loss


""")

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="A .Describe its policies or commitments to halt and reverse biodiversity loss, and how these are informed by the 2050 Goals and 2030 Targets in the Kunming-Montreal Global Biodiversity Framework",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-1A",
        type=["pdf", "docx", "xlsx"]
    )



col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="B. Report the extent to which these policies or commitments apply to the organization’s activities and to its business relationships;",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-1B",
        type=["pdf", "docx", "xlsx"]
    )    


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="C. Report the goals and targets to halt and reverse biodiversity loss, whether they are informed by scientific consensus, the base year, and the indicators used to evaluate progress.",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-1C",
        type=["pdf", "docx", "xlsx"]
    )    



st.write("""
### GRI 101-2: Management of biodiversity impacts   

A. Report how it applies the mitigation hierarchy by describing
""")



col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="i. Actions taken to avoid negative impacts on biodiversity",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Ai",
        type=["pdf", "docx", "xlsx"]
    )


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="ii. Actions taken to minimize negative impacts on biodiversity that were not avoided",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Aii",
        type=["pdf", "docx", "xlsx"]
    )

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="iii. Actions taken to restore and rehabilitate affected ecosystems, including the goals of the restoration and rehabilitation, and how stakeholders are engaged throughout the restoration and rehabilitation actions",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Aiii",
        type=["pdf", "docx", "xlsx"]
    )    

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="iv. Actions taken to offset residual negative impacts on biodiversity",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Aiv",
        type=["pdf", "docx", "xlsx"]
    )                             

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="v. Transformative actions taken and additional conservation actions taken",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Av",
        type=["pdf", "docx", "xlsx"]
    )                                

st.write("""

B. with reference to 101-2-a-iii, report for each site with the most significant impacts on biodiversity
""")


col1, col2 = st.columns(2)

with col1:
    hectares_of_the_area_under_restoration = st.number_input(
        """i. The size in hectares of the area under restoration or rehabilitation""",
        min_value=0.0,
        step=0.01,
    
    )


col1, col2 = st.columns(2)

with col1:
    hectares_of_the_area_restored = st.number_input(
        """ii. The size in hectares of the area restored or rehabilitated""",
        min_value=0.0,
        step=0.01,
    
    )

st.write("""

C. With reference to 101-2-a-iv, report for each offset
""")    

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="i. The goals",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Ci",
        type=["pdf", "docx", "xlsx"]
    ) 


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="ii. The geographic location",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Cii",
        type=["pdf", "docx", "xlsx"]
    ) 


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="iii. Whether and how principles of good offset practices are met",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Ciii",
        type=["pdf", "docx", "xlsx"]
    ) 


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="iv. Whether and how the offset is certified or verified by a third party",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2Civ",
        type=["pdf", "docx", "xlsx"]
    )   


st.write("""

D. List which of its sites with the most significant impacts on biodiversity have a
biodiversity management plan and explain why the other sites do not have a
management plan
""")       


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="Sites with biodiversity management plans and reasons for their absence at other impacted sites.",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2D",
        type=["pdf", "docx", "xlsx"]
    )   


st.write("""

E. Describe how it enhances synergies and reduces trade-offs between actions taken to
manage its biodiversity and climate change impacts
""")    




col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="Biodiversity climate synergies and trade-off management",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2E",
        type=["pdf", "docx", "xlsx"]
    )  


st.write("""

F. Describe how it ensures that the actions taken to manage its impacts on biodiversity
avoid and minimize negative impacts and maximize positive impacts for stakeholders.
""")        


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="Approach to managing stakeholder impacts from biodiversity actionst",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-2F",
        type=["pdf", "docx", "xlsx"]
    )  


st.write("""
### GRI 101-3: Management of biodiversity impacts   


""")


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="A. Describe the process to ensure compliance with access and benefit-sharing regulations and measures",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-3A",
        type=["pdf", "docx", "xlsx"]
    )  

col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="B. Describe voluntary actions taken to advance access and benefit-sharing that are additional to legal obligations or when there are no regulations and measures",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-3B",
        type=["pdf", "docx", "xlsx"]
    )      

st.write("""
### GRI 101-4: Identification of biodiversity impacts  


""")    


col1, col2 = st.columns(2)

with col1:
    st.text_area(
        label="A. explain how it has determined which of its sites and which products and services in its supply chain have the most significant actual and potential impacts on biodiversity.",
        placeholder="Enter your response here...",
        height=150
    )
with col2:
    st.uploaded_file = st.file_uploader(
        label="Upload Supporting Document 101-4A",
        type=["pdf", "docx", "xlsx"]
    )  

st.write("""
### GRI 101-5: Locations with biodiversity impacts  


""")   