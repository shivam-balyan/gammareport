"""Reusable Streamlit helpers for dynamic, addable/deletable form rows.

Each logical group of rows is identified by a unique ``prefix``. Rows are
tracked by stable integer ids (not list indices) so that deleting a row never
shifts the widget values of the remaining rows — a common Streamlit pitfall
when widget keys are built from positional indices.

Widget values themselves are stored by Streamlit under their own keys
(``f"{prefix}_<field>_{row_id}"``); this module only owns the list of live row
ids and the id counter.
"""

import streamlit as st

ADD_BUTTON_LABEL = "➕ Add more fields"
DELETE_BUTTON_LABEL = "✖"
DELETE_BUTTON_HELP = "Delete this data field"


def _rows_key(prefix):
    return f"{prefix}_rows"


def _next_id_key(prefix):
    return f"{prefix}_next_id"


def init_section(prefix):
    """Ensure a section exists in session state, seeded with one row."""
    if _rows_key(prefix) not in st.session_state:
        st.session_state[_next_id_key(prefix)] = 0
        st.session_state[_rows_key(prefix)] = []
        add_row(prefix)


def add_row(prefix):
    """Append a new, uniquely-identified row to the section."""
    row_id = st.session_state[_next_id_key(prefix)]
    st.session_state[_next_id_key(prefix)] = row_id + 1
    # Rebuild the list immutably rather than mutating it in place.
    st.session_state[_rows_key(prefix)] = st.session_state[_rows_key(prefix)] + [row_id]


def delete_row(prefix, row_id):
    """Remove a row from the section, always leaving at least one row."""
    rows = st.session_state[_rows_key(prefix)]
    if len(rows) > 1:
        st.session_state[_rows_key(prefix)] = [r for r in rows if r != row_id]


def row_ids(prefix):
    """Return the current list of live row ids for the section."""
    return st.session_state[_rows_key(prefix)]


def render_heading_with_info(title, help_text, *, as_subheader=True):
    """Render a section title alongside an ``ℹ️ Info`` disclosure popover."""
    title_col, info_col = st.columns([6, 1])
    if as_subheader:
        title_col.subheader(title)
    else:
        title_col.markdown(f"**{title}**")
    with info_col:
        with st.popover("ℹ️ Info"):
            st.write(help_text)


def render_delete_button(container, prefix, row_id, can_delete):
    """Render a per-row delete button (disabled when only one row remains)."""
    container.button(
        DELETE_BUTTON_LABEL,
        key=f"{prefix}_del_{row_id}",
        help=DELETE_BUTTON_HELP,
        disabled=not can_delete,
        on_click=delete_row,
        args=(prefix, row_id),
    )


def render_add_button(prefix):
    """Render the '+ Add more fields' button for a section."""
    st.button(
        ADD_BUTTON_LABEL,
        key=f"{prefix}_add",
        type="primary",
        on_click=add_row,
        args=(prefix,),
    )
