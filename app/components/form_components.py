import streamlit as st


def text_with_upload(
    text_label,
    placeholder,
    upload_label,
    key
):
    col1, col2 = st.columns(2)

    with col1:
        text = st.text_area(
            label=text_label,
            placeholder=placeholder,
            height=150,
            key=f"{key}_text"
        )

    with col2:
        file = st.file_uploader(
            label=upload_label,
            type=["pdf", "docx", "xlsx"],
            key=f"{key}_file"
        )

    return text, file


def number_field(
    label,
    key
):
    return st.number_input(
        label,
        min_value=0.0,
        step=0.01,
        format="%.2f",
        key=key
    )


def save_button(
    label,
    key
):
    return st.button(
        label,
        key=key
    )