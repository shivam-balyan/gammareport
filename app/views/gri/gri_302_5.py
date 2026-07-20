"""GRI 302-5 — Reductions in energy requirements of products and services."""

import streamlit as st

from app.components import dynamic_rows

UNIT_OPTIONS = ["KWh", "MWh", "GWh", "MJ", "GJ", "TJ"]
BASE_YEAR_OPTIONS = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

YES = "Yes"
NO = "No"
APPLICABLE_OPTIONS = [YES, NO]

METHOD_BASELINE = "Baseline"
METHOD_BASE_YEAR = "Base Year"
METHOD_OPTIONS = [METHOD_BASELINE, METHOD_BASE_YEAR]

BASELINE_PREFIX = "red_baseline"
BASE_YEAR_PREFIX = "red_baseyear"

APPLICABLE_QUESTION = (
    "Did reductions in energy requirements of products and services occur "
    "during the reporting year?"
)
METHOD_QUESTION = "Comparison methodology"

DISCLOSURE_HELP = (
    "GRI 302-5: Report reductions in the energy requirements of products and "
    "services achieved during the reporting period. Reductions can be compared "
    "against either a baseline or a base year. Multiple products/services are "
    "supported — add a row for each. Reduction % and Energy Saved are "
    "calculated automatically from the amounts you enter."
)

NO_DISCLOSURE_MSG = (
    "No disclosure is required for GRI 302-5 for this reporting year."
)

AUTO_CALC_CAPTION = (
    "Reduction % and Energy Saved are automatically calculated from the "
    "fields above."
)


def _reduction_pct(base_amount, current_amount):
    """Reduction % = (base - current) / base × 100; 0.0 when base is 0.

    An increase in consumption is not a reduction, so a negative result is
    floored to 0.
    """
    if not base_amount:
        return 0.0
    return max(round((base_amount - current_amount) / base_amount * 100.0, 2), 0.0)


def _energy_saved(base_amount, current_amount):
    """Energy saved in the entered unit = base - current, floored to 0.

    Consuming more than the baseline is not a saving, so it reads as 0 rather
    than a negative value.
    """
    return max(base_amount - current_amount, 0.0)


def _render_calc_cells(pct_col, saved_col, base_amount, current_amount):
    """Render the read-only Reduction % and Energy Saved cells for a row."""
    reduction = _reduction_pct(base_amount, current_amount)
    saved = _energy_saved(base_amount, current_amount)
    pct_col.markdown(f"{reduction:g}%")
    saved_col.markdown(f"{saved:g}")
    return reduction, saved


# ==========================================
# BASELINE
# ==========================================

def _render_baseline_row_headers():
    header = st.columns([3, 2, 2, 2, 2, 2, 1])
    header[0].markdown("**Product / service name**")
    header[1].markdown("**Baseline energy consumption**")
    header[2].markdown("**Current energy consumption**")
    header[3].markdown("**Unit**")
    header[4].markdown("**Reduction %**")
    header[5].markdown("**Energy saved**")
    header[6].markdown("** **")


def _render_baseline_row(prefix, row_id, can_delete):
    cols = st.columns([3, 2, 2, 2, 2, 2, 1])

    cols[0].text_input(
        "name",
        key=f"{prefix}_name_{row_id}",
        label_visibility="collapsed",
        placeholder="Product / service name",
    )
    base_amount = cols[1].number_input(
        "baseline",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_base_amt_{row_id}",
        label_visibility="collapsed",
    )
    current_amount = cols[2].number_input(
        "current",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_current_amt_{row_id}",
        label_visibility="collapsed",
    )
    cols[3].selectbox(
        "unit",
        UNIT_OPTIONS,
        key=f"{prefix}_unit_{row_id}",
        label_visibility="collapsed",
    )
    _render_calc_cells(cols[4], cols[5], base_amount, current_amount)
    dynamic_rows.render_delete_button(cols[6], prefix, row_id, can_delete)

    return base_amount, current_amount


# ==========================================
# BASE YEAR
# ==========================================

def _render_base_year_row_headers():
    header = st.columns([3, 2, 2, 2, 2, 2, 2, 1])
    header[0].markdown("**Product / service name**")
    header[1].markdown("**Base year**")
    header[2].markdown("**Base year amount**")
    header[3].markdown("**Current year amount**")
    header[4].markdown("**Unit**")
    header[5].markdown("**Reduction %**")
    header[6].markdown("**Energy saved**")
    header[7].markdown("** **")


def _render_base_year_row(prefix, row_id, can_delete):
    cols = st.columns([3, 2, 2, 2, 2, 2, 2, 1])

    cols[0].text_input(
        "name",
        key=f"{prefix}_name_{row_id}",
        label_visibility="collapsed",
        placeholder="Product / service name",
    )
    cols[1].selectbox(
        "year",
        BASE_YEAR_OPTIONS,
        key=f"{prefix}_year_{row_id}",
        label_visibility="collapsed",
    )
    base_amount = cols[2].number_input(
        "base_amount",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_base_amt_{row_id}",
        label_visibility="collapsed",
    )
    current_amount = cols[3].number_input(
        "current_amount",
        min_value=0.0,
        step=1.0,
        key=f"{prefix}_current_amt_{row_id}",
        label_visibility="collapsed",
    )
    cols[4].selectbox(
        "unit",
        UNIT_OPTIONS,
        key=f"{prefix}_unit_{row_id}",
        label_visibility="collapsed",
    )
    _render_calc_cells(cols[5], cols[6], base_amount, current_amount)
    dynamic_rows.render_delete_button(cols[7], prefix, row_id, can_delete)

    return base_amount, current_amount


# ==========================================
# SHARED SECTION RENDER
# ==========================================

def _render_summary(rows_data, base_total_label):
    """Render the four live summary metrics from the per-row (base, current)."""
    total_base = sum(base for base, _ in rows_data)
    total_current = sum(current for _, current in rows_data)
    total_saved = sum(_energy_saved(base, current) for base, current in rows_data)

    reductions = [
        _reduction_pct(base, current)
        for base, current in rows_data
        if base
    ]
    avg_reduction = sum(reductions) / len(reductions) if reductions else 0.0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(base_total_label, f"{total_base:g}")
    col2.metric("Total current consumption", f"{total_current:g}")
    col3.metric("Total energy saved", f"{total_saved:g}")
    col4.metric("Average reduction %", f"{avg_reduction:g}%")


def _render_section(prefix, section_title, base_total_label, render_headers, render_row):
    dynamic_rows.init_section(prefix)

    with st.container(border=True):
        dynamic_rows.render_heading_with_info(
            section_title, DISCLOSURE_HELP, as_subheader=False
        )

        render_headers()

        rows = dynamic_rows.row_ids(prefix)
        can_delete = len(rows) > 1
        rows_data = [render_row(prefix, row_id, can_delete) for row_id in rows]

        dynamic_rows.render_add_button(prefix)

        _render_summary(rows_data, base_total_label)
        st.caption(AUTO_CALC_CAPTION)


def render():
    st.header(
        "GRI 302-5 (Reductions in energy requirements of products and services)"
    )

    applicable = st.selectbox(APPLICABLE_QUESTION, APPLICABLE_OPTIONS, key="red_applicable")

    if applicable == NO:
        st.info(NO_DISCLOSURE_MSG)
        return

    method = st.selectbox(METHOD_QUESTION, METHOD_OPTIONS, key="red_method")

    if method == METHOD_BASELINE:
        _render_section(
            prefix=BASELINE_PREFIX,
            section_title="Baseline comparison",
            base_total_label="Total baseline consumption",
            render_headers=_render_baseline_row_headers,
            render_row=_render_baseline_row,
        )
    else:
        _render_section(
            prefix=BASE_YEAR_PREFIX,
            section_title="Base year comparison",
            base_total_label="Total base year consumption",
            render_headers=_render_base_year_row_headers,
            render_row=_render_base_year_row,
        )
