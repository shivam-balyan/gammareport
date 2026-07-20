"""GRI 301-2 — Recycled input materials used."""

import streamlit as st

from app.components import dynamic_rows

SOLID_UNIT_OPTIONS = ["Tonne", "Kilo joule"]
LIQUID_UNIT_OPTIONS = ["Tonne", "Kilo litres"]

DISCLOSURE_HELP = (
    "GRI 301-2: Report the percentage of recycled input materials used to "
    "manufacture the organization's primary products and services. Recycled "
    "input materials include both pre-consumer and post-consumer recycled "
    "material. The totals below are calculated automatically from the rows "
    "filled in by the user."
)

AUTO_CALC_CAPTION = (
    "These would be automatically calculated from the above fields "
    "filled by user."
)


def _render_row_headers():
    header = st.columns([3, 2, 2, 3, 1])
    header[0].markdown("**Name of material used**")
    header[1].markdown("**Unit**")
    header[2].markdown("**Amount (Material used)**")
    header[3].markdown("**Percentage of recycled material used (in terms of %)**")
    header[4].markdown("** **")


def _render_row(prefix, row_id, unit_options, can_delete):
    cols = st.columns([3, 2, 2, 3, 1])

    cols[0].text_input(
        "name",
        key=f"{prefix}_name_{row_id}",
        label_visibility="collapsed",
        placeholder="Name of material used",
    )
    cols[1].selectbox(
        "unit",
        unit_options,
        key=f"{prefix}_unit_{row_id}",
        label_visibility="collapsed",
    )
    cols[2].number_input(
        "amount",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_amount_{row_id}",
        label_visibility="collapsed",
    )
    cols[3].number_input(
        "pct",
        min_value=0.0,
        max_value=100.0,
        step=1.0,
        key=f"{prefix}_pct_{row_id}",
        label_visibility="collapsed",
    )
    dynamic_rows.render_delete_button(cols[4], prefix, row_id, can_delete)


def _section_totals(prefix):
    total_input = 0.0
    recycled_amount = 0.0

    for row_id in dynamic_rows.row_ids(prefix):
        amount = st.session_state.get(f"{prefix}_amount_{row_id}", 0.0) or 0.0
        pct = st.session_state.get(f"{prefix}_pct_{row_id}", 0.0) or 0.0

        total_input += amount
        recycled_amount += amount * pct / 100.0

    return total_input, recycled_amount


def _render_section(prefix, section_title, unit_options, total_input_label, recycled_label):
    dynamic_rows.init_section(prefix)

    with st.container(border=True):
        dynamic_rows.render_heading_with_info(
            section_title, DISCLOSURE_HELP, as_subheader=False
        )

        _render_row_headers()

        rows = dynamic_rows.row_ids(prefix)
        can_delete = len(rows) > 1
        for row_id in rows:
            _render_row(prefix, row_id, unit_options, can_delete)

        dynamic_rows.render_add_button(prefix)

        total_input, recycled_amount = _section_totals(prefix)

        total_col1, total_col2 = st.columns(2)
        total_col1.metric(total_input_label, f"{total_input:g}")
        total_col2.metric(recycled_label, f"{recycled_amount:g}")
        st.caption(AUTO_CALC_CAPTION)


def render():
    st.header("GRI-301-2 (Recycled input materials used)")
    st.write("Recycled input material used :")

    _render_section(
        prefix="recycled_solid",
        section_title="(FOR SOLID MATERIALS)",
        unit_options=SOLID_UNIT_OPTIONS,
        total_input_label="Total input material used by WEIGHT",
        recycled_label="Amount of recycled material used by WEIGHT",
    )

    _render_section(
        prefix="recycled_liquid",
        section_title="(FOR LIQUID MATERIALS)",
        unit_options=LIQUID_UNIT_OPTIONS,
        total_input_label="Total input material used by VOLUME",
        recycled_label="Amount of recycled material used by VOLUME",
    )
