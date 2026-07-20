"""GRI 302-2 — Energy Consumption Outside of the Organization."""

import streamlit as st

from app.components import dynamic_rows

# Conversion factors to Joules.
ELECTRICITY_UNIT_TO_JOULES = {
    "KWH": 3.6e6,
    "MWH": 3.6e9,
    "GWH": 3.6e12,
}
ENERGY_UNIT_TO_JOULES = {
    "Joules": 1.0,
    "Mega Joules": 1e6,
    "Giga Joules": 1e9,
}

DEFAULT_ELECTRICITY_UNIT = "KWH"
DEFAULT_ENERGY_UNIT = "Joules"

OTHER_ENERGY_PREFIX = "energy_other"

DISCLOSURE_HELP = (
    "GRI 302-2: Report energy consumed outside of the organization, expressed "
    "in joules or multiples. Electricity is entered in KWH (by default) and "
    "converted to its joule equivalent automatically. Total energy consumption "
    "= electricity (joule equivalent) + other fuel energy (joule equivalent)."
)


def _electricity_joules():
    amount = st.session_state.get("elec_amount", 0.0) or 0.0
    unit = st.session_state.get("elec_unit", DEFAULT_ELECTRICITY_UNIT)
    factor = ELECTRICITY_UNIT_TO_JOULES.get(unit, ELECTRICITY_UNIT_TO_JOULES[DEFAULT_ELECTRICITY_UNIT])
    return amount * factor


def _render_electricity_row():
    st.markdown("**Energy consumption in form electricity**")

    cols = st.columns(3)
    cols[0].number_input(
        "Amount (in terms of numbers)",
        min_value=0.0,
        step=1.0,
        key="elec_amount",
    )
    cols[1].selectbox(
        "Unit (KWH by default)",
        list(ELECTRICITY_UNIT_TO_JOULES.keys()),
        key="elec_unit",
    )
    cols[2].metric(
        "Its Joule equivalent (converted by code)",
        f"{_electricity_joules():,.0f} J",
    )


def _render_other_row_headers():
    header = st.columns([3, 2, 3, 1])
    header[0].markdown("**Type of fuel used**")
    header[1].markdown("**Amount (in terms of numbers)**")
    header[2].markdown("**Unit (Joules/Mega Joules/Giga Joules)**")
    header[3].markdown("** **")


def _render_other_row(prefix, row_id, can_delete):
    cols = st.columns([3, 2, 3, 1])

    cols[0].text_input(
        "fuel",
        key=f"{prefix}_fuel_{row_id}",
        label_visibility="collapsed",
        placeholder="Type of fuel used",
    )
    cols[1].number_input(
        "amount",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_amount_{row_id}",
        label_visibility="collapsed",
    )
    cols[2].selectbox(
        "unit",
        list(ENERGY_UNIT_TO_JOULES.keys()),
        key=f"{prefix}_unit_{row_id}",
        label_visibility="collapsed",
    )
    dynamic_rows.render_delete_button(cols[3], prefix, row_id, can_delete)


def _other_energy_joules(prefix):
    total = 0.0

    for row_id in dynamic_rows.row_ids(prefix):
        amount = st.session_state.get(f"{prefix}_amount_{row_id}", 0.0) or 0.0
        unit = st.session_state.get(f"{prefix}_unit_{row_id}", DEFAULT_ENERGY_UNIT)
        total += amount * ENERGY_UNIT_TO_JOULES.get(unit, 1.0)

    return total


def render():
    st.header("GRI 302-2 (Energy Consumption Outside of the Organization)")

    prefix = OTHER_ENERGY_PREFIX
    dynamic_rows.init_section(prefix)

    with st.container(border=True):
        dynamic_rows.render_heading_with_info(
            "A. Energy Consumption Outside of the Organization",
            DISCLOSURE_HELP,
        )

        _render_electricity_row()

        st.write(
            "Energy consumption excluding Electricity "
            "(unit would be in joules or its multiples only)"
        )

        _render_other_row_headers()

        rows = dynamic_rows.row_ids(prefix)
        can_delete = len(rows) > 1
        for row_id in rows:
            _render_other_row(prefix, row_id, can_delete)

        dynamic_rows.render_add_button(prefix)

        total_joules = _electricity_joules() + _other_energy_joules(prefix)
        st.metric(
            "Total energy consumption = Electricity (Joule equivalent) "
            "+ Other (Joule equivalent)",
            f"{total_joules:,.0f} J",
        )
