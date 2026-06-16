# import streamlit as st


# from repositories.company_repository import CompanyRepository

# st.set_page_config(
#     page_title="Social Missing Data",
#     layout="wide"
# )

# st.title("Social Missing Data")

# companies_df = CompanyRepository.get_companies()

# company_map = dict(
#     zip(
#         companies_df["company_name"],
#         companies_df["id"]
#     )
# )


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

# st.write("""
# ### GRI 401-1: New employee hires and employee turnover

# """)

# col1, col2 = st.columns(2)

# with col1:
#     st.text_area(
#         label="A. Total number and rate of new employee hires during the reporting period, by age group,gender and region.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 401-1A",
#         type=["pdf", "docx", "xlsx"]
#     )

# col1, col2 = st.columns(2)

# with col1:
#     st.text_area(
#         label="B. Total number and rate of employee turnover during the reporting period, by age group,gender and region.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 401-1B",
#         type=["pdf", "docx", "xlsx"]
#     )    


# if st.button("Save Data-401-1"):
#     st.success("GRI 401-1 data saved successfully.")             

# st.write("""
# ### GRI 402-1: Minimum notice periods regarding operational changes

# """)    

# col1, col2 = st.columns(2)

# with col1:
#     st.text_area(
#         label="A. Minimum number of weeks’ notice typically provided to employees and their representatives prior to the implementation of significant operational changes that could substantially affect them.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 402-1A",
#         type=["pdf", "docx", "xlsx"]
#     )

# col1, col2 = st.columns(2)

# with col1:
#     st.text_area(
#         label="B. For organizations with collective bargaining agreements, report whether the notice period and provisions for consultation and negotiation are specified in collective agreements.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 402-1B",
#         type=["pdf", "docx", "xlsx"]
#     )    


# if st.button("Save Data-402-1"):
#     st.success("GRI 402-1 data saved successfully.")  


# st.write("""
# ### GRI 403-8: Workers covered by an occupational health and safety management system
         
# A. If the organization has implemented an occupational health and safety management
# system based on legal requirements and/or recognized standards/guidelines:
# """)    
# st.write("""
# A-i The number and percentage of all employees and workers who are not employees but whose work and/or workplace is controlled by the organization, who are covered by such a system",

# """)    

# st.write("""
# EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_employees = st.number_input(
#         "Total Number of workers covered ",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_employees = st.number_input(
#         "Percentage of workers covered (cover% = (workers cover/totalworkers )*100)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  




# st.write("""
# NON-EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_non_employees = st.number_input(
#         "Total Number of Non employed workers covered ",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_non_employees = st.number_input(
#         "Percentage of Non employed workers covered (cover% = (workers cover/totalworkers )*100)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  


 
# st.write("""
# A-ii The number and percentage of all employees and workers who are not employees
# but whose work and/or workplace is controlled by the organization, who are
# covered by such a system that has been internally audited

# """)    

# st.write("""
# EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_employees_internally = st.number_input(
#         "Total Number of workers covered (Internally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_employees_internally = st.number_input(
#         "Percentage of workers covered  (cover% = (workers cover/totalworkers )*100) (Internally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  




# st.write("""
# NON-EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_non_employees_internally = st.number_input(
#         "Total Number of Non employed workers covered (Internally audited) ",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_non_employees_internally = st.number_input(
#         "Percentage of Non employed workers covered (cover% = (workers cover/totalworkers )*100) (Internally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  










# st.write("""
# A-iii The number and percentage of all employees and workers who are not employees
# but whose work and/or workplace is controlled by the organization, who are
# covered by such a system that has been audited or certified by an external party

# """)    

# st.write("""
# EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_employees_externally = st.number_input(
#         "Total Number of workers covered (Extrernally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_employees_externally = st.number_input(
#         "Percentage of workers covered  (cover% = (workers cover/totalworkers )*100) (Externally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  




# st.write("""
# NON-EMPLOYEES ONLY

# """)  

# col1, col2 = st.columns(2)

# with col1:

#      number_and_percentage_of_all_non_employees_externally = st.number_input(
#         "Total Number of Non employed workers covered (Externally audited) ",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
#      percentage_of_all_non_employees_externally = st.number_input(
#         "Percentage of Non employed workers covered (cover% = (workers cover/totalworkers )*100) (Externally audited)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )  



# st.write("""
# ###                  
# B. Whether and, if so, why any workers have been excluded from this disclosure, including
# the types of worker excluded.
# """)  




# col1, col2, col3 = st.columns(3)

# with col1:
#     has_internal_standards = st.selectbox(
#         "Workers excluded?",
#         ["Select", "Yes", "No"]
#     )

# with col2:
#     if has_internal_standards == "Yes":
#         internal_standards_explain = st.text_area(
#             label="Description of excluded workers",
#             placeholder="Describe who they are and why were they excluded",
#             height=150
#         )

# with col3:
#     if has_internal_standards == "Yes":
#         internal_standards_file = st.file_uploader(
#             label="Upload Supporting Document",
#             type=["pdf", "docx", "xlsx"],
#             key="internal_standard_upload"
#         )



# st.write("""
# ###                  
# C. Any contextual information necessary to understand how the data have been compiled,
# such as any standards, methodologies, and assumptions used.
# """)  



# col1, col2 = st.columns(2)

# with col1:
#     st.text_area(
#         label="Describe how were the numbers calculated.",
#         placeholder="Any standards and assumptions used....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-8C",
#         type=["pdf", "docx", "xlsx"]
#     )



# st.write("""
# ### GRI 403-9: Work-related injuries

# A. For All Employees
# """)

# st.write("""
# A-i The number and rate of fatalities as a result of work-related injury

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of fatalities as a result of work-related injury",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of fatalities as a result of work-related injury",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of fatalities as a result of work-related injury / Number of hours worked) × 200,000 or 1,000,000"
#     )  
     
# st.write("""
# A-ii The number and rate of high-consequence work-related injuries (excluding fatalities)

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of high-consequence work-related injuries (excluding fatalities)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of high-consequence work-related injuries (excluding fatalities)",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of high-consequence work-related injuries (excluding fatalities) / Number of hours worked) × 200,000 or 1,000,000"
#     )  
          

# st.write("""
# A-iii The number and rate of recordable work-related injuries

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of recordable work-related injuries",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of recordable work-related injuries",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of recordable work-related injuries / Number of hours worked) × 200,000 or 1,000,000"
#     )            
     
# st.write("""
# A-iv The main types of work-related injury

# """)    

# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label="Describe the main types of work-related injury.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-iv",
#         type=["pdf", "docx", "xlsx"]
#     )    


# st.write("""
# A-v The number of hours worked.

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of hours worked",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )










# st.write("""
# ###
# B. For all workers who are not employees but whose work and/or workplace is controlled by the organization
# """)

# st.write("""
# B-i The number and rate of fatalities as a result of work-related injury

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of fatalities as a result of work-related injury for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of fatalities as a result of work-related injury for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of fatalities as a result of work-related injury / Number of hours worked) × 200,000 or 1,000,000"
#     )  
     
# st.write("""
# B-ii The number and rate of high-consequence work-related injuries (excluding fatalities)

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of high-consequence work-related injuries (excluding fatalities) for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of high-consequence work-related injuries (excluding fatalities) for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of high-consequence work-related injuries (excluding fatalities) / Number of hours worked) × 200,000 or 1,000,000"
#     )  
          

# st.write("""
# B-iii The number and rate of recordable work-related injuries

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of recordable work-related injuries for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
# with col2:
     
#      work_related_injuries_rate = st.number_input(
#         "Rate of recordable work-related injuries for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f",
#         help="Rate = (Number of recordable work-related injuries / Number of hours worked) × 200,000 or 1,000,000"
#     )            
     
# st.write("""
# B-iv The main types of work-related injury

# """)    

# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label="Describe the main types of work-related injury for non employees.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-B-iv",
#         type=["pdf", "docx", "xlsx"]
#     )    


# st.write("""
# B-v The number of hours worked.

# """)    

# col1, col2 = st.columns(2)

# with col1:

#      work_related_injuries = st.number_input(
#         "Total Number of hours worked for non employees",
#         min_value=0.0,
#         step=0.01,
#         format="%.2f"
#     )
   




# st.write("""
# ###
# C. The work-related hazards that pose a risk of high-consequence injury, including
# """)
   
# st.write("""
# C-i how these hazards have been determined

# """)   


# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label=" Describe how the work-related hazards that pose a risk of high-consequence injury have been determined.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-c-i",
#         type=["pdf", "docx", "xlsx"]
#     )  

# st.write("""
# C-ii which of these hazards have caused or contributed to high-consequence injuries during the reporting period

# """)    

# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label=" Describe which of these hazards have caused or contributed to high-consequence injuries during the reporting period.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-c-ii",
#         type=["pdf", "docx", "xlsx"]
#     )  


# st.write("""
# C-iii Actions taken or underway to eliminate these hazards and minimize risks using the hierarchy of controls.

# """)    

# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label=" Describe actions taken or underway to eliminate these hazards and minimize risks using the hierarchy of controls.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-c-iii",
#         type=["pdf", "docx", "xlsx"]
#     )   


# st.write("""
# ###
# D. Any actions taken or underway to eliminate other work-related hazards and minimize risks using the hierarchy of controls.
# """)



# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label=" Describe actions taken or underway to eliminate other work-related hazards and minimize risks using the hierarchy of controls.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-d",
#         type=["pdf", "docx", "xlsx"]
#     )   

# st.write("""
# ###
# E. Whether the rates have been calculated based on 200,000 or 1,000,000 hours worked
# """)    

# col1 = st.columns(2)[0]   

# with col1:
#     hierarchy_control_rate = st.selectbox(
#         "Select the calculation factor",
#         options=["select",200000, 1000000]
#     )

# st.write("""
# ###
# F. Whether and, if so, why any workers have been excluded from this disclosure, including the types of worker excluded.
# """)



# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label="Describe whether and, if so, why any workers have been excluded from this disclosure, including the types of worker excluded.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-F",
#         type=["pdf", "docx", "xlsx"]
#     )   

# st.write("""
# ###
# G. Any contextual information necessary to understand how the data have been compiled such as any standards, methodologies, and assumptions used.
# """)



# col1, col2 = st.columns(2)     

# with col1:
#     st.text_area(
#         label="Describe any contextual information necessary to understand how the data have been compiled such as any standards, methodologies, and assumptions used.",
#         placeholder="....",
#         height=150
#     )
# with col2:
#     st.uploaded_file = st.file_uploader(
#         label="Upload Supporting Document 403-9-G",
#         type=["pdf", "docx", "xlsx"]
#     )   



# st.write("""
# ### GRI 404-1: Average hours of training per year per employee

# A.  Average hours of training that the organization’s employees have undertaken during the reporting period, by:
# """)    

# col1,col2 = st.columns(2)

# with col1:
#     hierarchy_control_rate = st.selectbox(
#         "Gender",
#         options=["select","male", "female","others"]
#     )
# with col2:
     
#      genders = st.number_input(
#         "total number",
#         min_value=0.0,
#         step=0.01,
#     )            
     



import streamlit as st
# from repositories.company_repository import CompanyRepository

st.set_page_config(page_title="Social Missing Data", layout="wide")
st.title("Social Missing Data")

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


def number_rate_row(number_label, rate_label, rate_help, key_suffix):
    """Renders a (number_input | rate_input) two-column row."""
    col1, col2 = st.columns(2)
    with col1:
        st.number_input(number_label, min_value=0.0, step=0.01, format="%.2f", key=f"ni_{key_suffix}")
    with col2:
        st.number_input(rate_label, min_value=0.0, step=0.01, format="%.2f",
                        help=rate_help, key=f"ni_rate_{key_suffix}")


def worker_coverage_row(group_label, key_suffix):
    """Renders a (total number | percentage) two-column row for worker coverage."""
    st.write(f"**{group_label}**")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input(f"Total Number of {group_label} covered",
                        min_value=0.0, step=0.01, format="%.2f", key=f"ni_num_{key_suffix}")
    with col2:
        st.number_input(f"Percentage of {group_label} covered (cover% = workers covered / total workers × 100)",
                        min_value=0.0, step=0.01, format="%.2f", key=f"ni_pct_{key_suffix}")


def conditional_text_upload(question_label, yes_text_label, yes_text_placeholder,
                             yes_upload_label, select_key):
    """Yes/No selectbox; if Yes shows text_area + file_uploader."""
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


def save_button(label, success_msg, key):
    if st.button(label, key=key):
        st.success(success_msg)


RATE_HELP = "Rate = (Number / Hours worked) × 200,000 or 1,000,000"

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
# GRI 401-1
# ─────────────────────────────────────────

st.write("### GRI 401-1: New employee hires and employee turnover")

text_upload_row(
    "A. Total number and rate of new employee hires during the reporting period, by age group, gender and region.",
    "....", "Upload Supporting Document 401-1A", "401_1a"
)
text_upload_row(
    "B. Total number and rate of employee turnover during the reporting period, by age group, gender and region.",
    "....", "Upload Supporting Document 401-1B", "401_1b"
)
save_button("Save Data-401-1", "GRI 401-1 data saved successfully.", key="save_401_1")

# ─────────────────────────────────────────
# GRI 402-1
# ─────────────────────────────────────────

st.write("### GRI 402-1: Minimum notice periods regarding operational changes")

text_upload_row(
    "A. Minimum number of weeks' notice typically provided to employees and their representatives "
    "prior to the implementation of significant operational changes that could substantially affect them.",
    "....", "Upload Supporting Document 402-1A", "402_1a"
)
text_upload_row(
    "B. For organizations with collective bargaining agreements, report whether the notice period "
    "and provisions for consultation and negotiation are specified in collective agreements.",
    "....", "Upload Supporting Document 402-1B", "402_1b"
)
save_button("Save Data-402-1", "GRI 402-1 data saved successfully.", key="save_402_1")

# ─────────────────────────────────────────
# GRI 403-8
# ─────────────────────────────────────────

st.write("""
### GRI 403-8: Workers covered by an occupational health and safety management system

A. If the organization has implemented an OHS management system based on legal requirements
and/or recognized standards/guidelines:
""")

# A-i, A-ii, A-iii share the same structure — two worker groups × audit type
AUDIT_SECTIONS = [
    (
        "A-i The number and percentage of all employees and workers covered by such a system",
        [("workers", "403_8_ai_emp"), ("Non-employed workers", "403_8_ai_non")]
    ),
    (
        "A-ii Covered by such a system that has been **internally audited**",
        [("workers (Internally audited)", "403_8_aii_emp"), ("Non-employed workers (Internally audited)", "403_8_aii_non")]
    ),
    (
        "A-iii Covered by such a system **audited or certified by an external party**",
        [("workers (Externally audited)", "403_8_aiii_emp"), ("Non-employed workers (Externally audited)", "403_8_aiii_non")]
    ),
]

for section_title, groups in AUDIT_SECTIONS:
    st.write(section_title)
    for group_label, key in groups:
        worker_coverage_row(group_label, key)
    st.write("")

st.write("### B. Whether and, if so, why any workers have been excluded from this disclosure.")
conditional_text_upload(
    question_label="Workers excluded?",
    yes_text_label="Description of excluded workers",
    yes_text_placeholder="Describe who they are and why were they excluded",
    yes_upload_label="Upload Supporting Document",
    select_key="403_8b"
)

st.write("### C. Any contextual information necessary to understand how the data have been compiled.")
text_upload_row(
    "Describe how were the numbers calculated.",
    "Any standards and assumptions used....",
    "Upload Supporting Document 403-8C",
    "403_8c"
)
save_button("Save Data-403-8", "GRI 403-8 data saved successfully.", key="save_403_8")
# ─────────────────────────────────────────
# GRI 403-9
# ─────────────────────────────────────────

st.write("### GRI 403-9: Work-related injuries")

# A (Employees) and B (Non-employees) share identical sub-structure
WORKER_GROUPS = [
    ("A. For All Employees",
     "A", "", [
         ("A-i  Fatalities as a result of work-related injury",
          "fatalities as a result of work-related injury",
          "fatalities as a result of work-related injury",
          "403_9_a_i"),
         ("A-ii  High-consequence work-related injuries (excluding fatalities)",
          "high-consequence work-related injuries (excluding fatalities)",
          "high-consequence work-related injuries (excluding fatalities)",
          "403_9_a_ii"),
         ("A-iii  Recordable work-related injuries",
          "recordable work-related injuries",
          "recordable work-related injuries",
          "403_9_a_iii"),
     ],
     "A-iv  Main types of work-related injury",
     "Describe the main types of work-related injury.",
     "Upload Supporting Document 403-9-iv",
     "403_9_a_iv",
     "A-v  Number of hours worked",
     "Total Number of hours worked",
     "403_9_a_v"),

    ("B. For all workers who are not employees but whose work and/or workplace is controlled by the organization",
     "B", " for non employees", [
         ("B-i  Fatalities as a result of work-related injury",
          "fatalities as a result of work-related injury for non employees",
          "fatalities as a result of work-related injury for non employees",
          "403_9_b_i"),
         ("B-ii  High-consequence work-related injuries (excluding fatalities)",
          "high-consequence work-related injuries (excluding fatalities) for non employees",
          "high-consequence work-related injuries (excluding fatalities) for non employees",
          "403_9_b_ii"),
         ("B-iii  Recordable work-related injuries",
          "recordable work-related injuries for non employees",
          "recordable work-related injuries for non employees",
          "403_9_b_iii"),
     ],
     "B-iv  Main types of work-related injury",
     "Describe the main types of work-related injury for non employees.",
     "Upload Supporting Document 403-9-B-iv",
     "403_9_b_iv",
     "B-v  Number of hours worked",
     "Total Number of hours worked for non employees",
     "403_9_b_v"),
]

for (group_title, _, _suffix, injury_rows,
     types_label, types_text_label, types_upload_label, types_key,
     hours_label, hours_num_label, hours_key) in WORKER_GROUPS:

    st.write(f"### {group_title}")
    for sub_label, num_label, _rate_suffix, key in injury_rows:
        st.write(sub_label)
        number_rate_row(
            f"Total Number of {num_label}",
            f"Rate of {num_label}",
            RATE_HELP,
            key
        )

    st.write(types_label)
    text_upload_row(types_text_label, "....", types_upload_label, types_key)

    st.write(hours_label)
    col1 = st.columns(2)[0]
    with col1:
        st.number_input(hours_num_label, min_value=0.0, step=0.01, format="%.2f", key=f"ni_{hours_key}")

# C — hazard sub-sections
st.write("### C. Work-related hazards that pose a risk of high-consequence injury")

HAZARD_SECTIONS = [
    ("C-i  How these hazards have been determined",
     "Describe how the work-related hazards that pose a risk of high-consequence injury have been determined.",
     "Upload Supporting Document 403-9-c-i", "403_9_c_i"),
    ("C-ii  Which hazards caused or contributed to high-consequence injuries during the reporting period",
     "Describe which of these hazards have caused or contributed to high-consequence injuries during the reporting period.",
     "Upload Supporting Document 403-9-c-ii", "403_9_c_ii"),
    ("C-iii  Actions taken or underway to eliminate these hazards and minimize risks using the hierarchy of controls",
     "Describe actions taken or underway to eliminate these hazards and minimize risks using the hierarchy of controls.",
     "Upload Supporting Document 403-9-c-iii", "403_9_c_iii"),
]

for title, label, upload_label, key in HAZARD_SECTIONS:
    st.write(title)
    text_upload_row(label, "....", upload_label, key)

# D–G simple text/upload rows
CLOSING_SECTIONS = [
    ("### D. Actions taken or underway to eliminate other work-related hazards and minimize risks.",
     "Describe actions taken or underway to eliminate other work-related hazards and minimize risks using the hierarchy of controls.",
     "Upload Supporting Document 403-9-d", "403_9_d"),
    ("### F. Whether and, if so, why any workers have been excluded from this disclosure.",
     "Describe whether and, if so, why any workers have been excluded from this disclosure, including the types of worker excluded.",
     "Upload Supporting Document 403-9-F", "403_9_f"),
    ("### G. Any contextual information necessary to understand how the data have been compiled.",
     "Describe any contextual information necessary to understand how the data have been compiled such as any standards, methodologies, and assumptions used.",
     "Upload Supporting Document 403-9-G", "403_9_g"),
]

st.write("### E. Whether the rates have been calculated based on 200,000 or 1,000,000 hours worked")
col1 = st.columns(2)[0]
with col1:
    st.selectbox("Select the calculation factor", options=["select", 200000, 1000000], key="sel_403_9_e")

for title, label, upload_label, key in CLOSING_SECTIONS:
    st.write(title)
    text_upload_row(label, "....", upload_label, key)

save_button("Save Data-403-9", "GRI 403-9 data saved successfully.", key="save_403_9")

# ─────────────────────────────────────────
# GRI 404-1
# ─────────────────────────────────────────

st.write("### GRI 404-1: Average hours of training per year per employee")
st.write("A. Average hours of training that the organization's employees have undertaken during the reporting period, by:")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Gender", options=["select", "male", "female", "others"], key="sel_404_1_gender")
with col2:
    st.number_input("Total number", min_value=0.0, step=0.01, key="ni_404_1_total")

save_button("Save Data-404-1", "GRI 404-1 data saved successfully.", key="save_404_1")