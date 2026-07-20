"""GRI 301-1 — Materials used by weight or volume."""

import streamlit as st

from app.components import dynamic_rows

SOURCE_OPTIONS = ["Purchased", "Sourced internally"]
UNIT_OPTIONS = ["Tonnes", "Kilo litres"]

WEIGHT_UNIT = "Tonnes"
VOLUME_UNIT = "Kilo litres"

DISCLOSURE_HELP = (
    "GRI 301-1: Report the total weight or volume of materials used to produce "
    "and package the organization's primary products and services during the "
    "reporting period, broken down by renewable and non-renewable materials. "
    "Use 'Tonnes' for materials measured by weight and 'Kilo litres' for "
    "materials measured by volume."
)


def _render_row_headers():
    header = st.columns([3, 3, 2, 2, 1])
    header[0].markdown("**name (type of raw material used)**")
    header[1].markdown("**Purchased / sourced internally**")
    header[2].markdown("**unit used (Tonnes or Kilo ltrs)**")
    header[3].markdown("**Amount**")
    header[4].markdown("** **")


def _render_row(prefix, row_id, can_delete):
    cols = st.columns([3, 3, 2, 2, 1])

    cols[0].text_input(
        "name",
        key=f"{prefix}_name_{row_id}",
        label_visibility="collapsed",
        placeholder="Type of raw material used",
    )
    cols[1].selectbox(
        "source",
        SOURCE_OPTIONS,
        key=f"{prefix}_source_{row_id}",
        label_visibility="collapsed",
    )
    cols[2].selectbox(
        "unit",
        UNIT_OPTIONS,
        key=f"{prefix}_unit_{row_id}",
        label_visibility="collapsed",
    )
    cols[3].number_input(
        "amount",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_amount_{row_id}",
        label_visibility="collapsed",
    )
    dynamic_rows.render_delete_button(cols[4], prefix, row_id, can_delete)


def _section_totals(prefix):
    total_weight = 0.0
    total_volume = 0.0

    for row_id in dynamic_rows.row_ids(prefix):
        unit = st.session_state.get(f"{prefix}_unit_{row_id}", WEIGHT_UNIT)
        amount = st.session_state.get(f"{prefix}_amount_{row_id}", 0.0) or 0.0

        if unit == WEIGHT_UNIT:
            total_weight += amount
        elif unit == VOLUME_UNIT:
            total_volume += amount

    return total_weight, total_volume


def _render_section(prefix, section_title, weight_label, volume_label):
    dynamic_rows.init_section(prefix)

    with st.container(border=True):
        dynamic_rows.render_heading_with_info(section_title, DISCLOSURE_HELP)

        _render_row_headers()

        rows = dynamic_rows.row_ids(prefix)
        can_delete = len(rows) > 1
        for row_id in rows:
            _render_row(prefix, row_id, can_delete)

        dynamic_rows.render_add_button(prefix)

        total_weight, total_volume = _section_totals(prefix)

        total_col1, total_col2 = st.columns(2)
        total_col1.metric(weight_label, f"{total_weight:g} {WEIGHT_UNIT}")
        total_col2.metric(volume_label, f"{total_volume:g} {VOLUME_UNIT}")


def render():
    st.header("GRI-301-1 (Materials used by weight or volume)")

    _render_section(
        prefix="renewable",
        section_title="Renewable material used",
        weight_label="Total renewable material used by WEIGHT",
        volume_label="Total renewable material used by VOLUME",
    )

    _render_section(
        prefix="non_renewable",
        section_title="Non-renewable material used",
        weight_label="Total non-renewable material used by WEIGHT",
        volume_label="Total non-renewable material used by VOLUME",
    )
