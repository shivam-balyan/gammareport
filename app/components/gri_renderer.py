import streamlit as st

from components.form_components import text_with_upload


def render_number_calculation(section):

    st.subheader(section["title"])

    if section.get("description"):
        st.write(section["description"])

    cols = st.columns(len(section["fields"]))

    values = {}

    for col, field in zip(cols, section["fields"]):

        with col:

            values[field["id"]] = st.number_input(
                field["label"],
                min_value=0.0,
                step=0.01,
                format="%.2f",
                key=f"{section['id']}_{field['id']}"
            )

    total = sum(values.values())

    st.metric(
        section["metric_label"],
        f"{total:.2f}"
    )

    values["total"] = total

    st.session_state.environment_data[
        section["id"]
    ] = values


def render_percentage_calculation(section):

    st.subheader(section["title"])

    if section.get("description"):
        st.write(section["description"])

    cols = st.columns(len(section["fields"]))

    values = {}

    for col, field in zip(cols, section["fields"]):

        with col:

            values[field["id"]] = st.number_input(
                field["label"],
                min_value=0.0,
                step=0.01,
                format="%.2f",
                key=f"{section['id']}_{field['id']}"
            )

    numerator = values[
        section["fields"][0]["id"]
    ]

    denominator = values[
        section["fields"][1]["id"]
    ]

    percentage = (
        (numerator / denominator) * 100
        if denominator > 0
        else 0
    )

    st.metric(
        section["metric_label"],
        f"{percentage:.2f}%"
    )

    values["percentage"] = percentage

    st.session_state.environment_data[
        section["id"]
    ] = values


def render_text_upload(section):

    st.subheader(section["title"])

    text, file = text_with_upload(
        text_label=section["label"],
        placeholder=section["placeholder"],
        upload_label="Upload Supporting Document",
        key=section["id"]
    )

    st.session_state.environment_data[
        section["id"]
    ] = {
        "text": text,
        "file": file
    }


def render_gri_sections(sections):

    for section in sections:

        if section["type"] == "number_calculation":

            render_number_calculation(section)

        elif section["type"] == "percentage_calculation":

            render_percentage_calculation(section)

        elif section["type"] == "text_upload":

            render_text_upload(section)