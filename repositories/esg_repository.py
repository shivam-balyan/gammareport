import pandas as pd
from sqlalchemy import text

from core.database import engine
from utils.constants import ESG_TABLE_MAPPING


class ESGRepository:

    @staticmethod
    def fetch_data(
        company_id,
        year,
        esg_type,
        kpi=None
    ):

        all_dataframes = []

        # ==========================================
        # ENVIRONMENT
        # ==========================================

        if esg_type == "ENVIRONMENT":

            selected_tables = ESG_TABLE_MAPPING["ENVIRONMENT"]

            # Specific KPI selected
            if kpi and kpi != "ALL":

                selected_tables = {
                    kpi: ESG_TABLE_MAPPING["ENVIRONMENT"][kpi]
                }

            for kpi_name, table_name in selected_tables.items():

                query = f"""
                SELECT
                    '{kpi_name}' AS kpi_name,
                    fm.name AS master_field_name,
                    fm."group" AS master_field_group,

                    t.id,
                    t.company_id,
                    t.form_id,
                    t.company_unit,
                    t.frequency_type,
                    t.frequency_date,
                    t.frequency_month,
                    t.frequency_year,
                    t.field_id,
                    t.field_group,
                    t.unit_id,
                    t.prev_value,
                    t.target,
                    t.value,
                    t.comment,
                    t.attachment,
                    t.group_name,
                    t.status,
                    t.position,
                    t.approval_status,
                    t.approved_by,
                    t.approved_at,
                    t.created_by,
                    t.updated_by,
                    t.created_at,
                    t.updated_at
                  

                FROM {table_name} t

                LEFT JOIN fields_master fm
                    ON fm.id = t.field_id

                WHERE t.company_id = :company_id
                AND t.frequency_year = :year
                """

                df = pd.read_sql(
                    text(query),
                    engine,
                    params={
                        "company_id": company_id,
                        "year": str(year)
                    }
                )

                all_dataframes.append(df)

        # ==========================================
        # SOCIAL
        # ==========================================

        elif esg_type == "SOCIAL":

            query = """
            SELECT
                'SOCIAL' AS kpi_name,
                fm.name AS master_field_name,
                fm."group" AS master_field_group,

                s.id,
                s.cat_id,
                s.sub_cat_id,
                s.kpi_id,
                s.company_id,
                s.company_unit,
                s.field_id,
                s.field_group,
                s.form_id,
                s.months,
                s.year,
                s.value,
                s.comment,
                s.attachment,
                s.status,
                s.position,
                s.created_by,
                s.updated_by,
                s.created_at,
                s.updated_at,
                s.approval_status,
                s.approved_by,
                s.approved_at

            FROM social s

            LEFT JOIN fields_master fm
                ON fm.id = s.field_id

            WHERE s.company_id = :company_id
            AND s.year = :year
            """

            df = pd.read_sql(
                text(query),
                engine,
                params={
                    "company_id": company_id,
                    "year": year
                }
            )

            all_dataframes.append(df)

        # ==========================================
        # GOVERNANCE
        # ==========================================

        elif esg_type == "GOVERNANCE":

            query = """
            SELECT
                'GOVERNANCE' AS kpi_name,
                fm.name AS master_field_name,
                fm."group" AS master_field_group,

                g.id,
                g.cat_id,
                g.sub_cat_id,
                g.kpi_id,
                g.company_id,
                g.company_unit,
                g.field_id,
                g.field_group,
                g.form_id,
                g.months,
                g.year,
                g.value,
                g.comment,
                g.attachment,
                g.status,
                g.position,
                g.created_by,
                g.updated_by,
                g.created_at,
                g.updated_at,
                g.approval_status,
                g.approved_by,
                g.approved_at

            FROM governance g

            LEFT JOIN fields_master fm
                ON fm.id = g.field_id

            WHERE g.company_id = :company_id
            AND g.year = :year
            """

            df = pd.read_sql(
                text(query),
                engine,
                params={
                    "company_id": company_id,
                    "year": year
                }
            )

            all_dataframes.append(df)

        # ==========================================
        # ALL ESG
        # ==========================================

        elif esg_type == "ALL":

            # SOCIAL + GOVERNANCE

            for category in ["SOCIAL", "GOVERNANCE"]:

                table_name = category.lower()

                query = f"""
                SELECT
                    '{category}' AS kpi_name,
                    fm.name AS master_field_name,
                    fm."group" AS master_field_group,
                    t.*

                FROM {table_name} t

                LEFT JOIN fields_master fm
                    ON fm.id = t.field_id

                WHERE t.company_id = :company_id
                AND t.year = :year
                """

                df = pd.read_sql(
                    text(query),
                    engine,
                    params={
                        "company_id": company_id,
                        "year": year
                    }
                )

                # Remove duplicate columns if any
                df = df.loc[:, ~df.columns.duplicated()]

                all_dataframes.append(df)

            # ENVIRONMENT TABLES

            for kpi_name, table_name in ESG_TABLE_MAPPING["ENVIRONMENT"].items():

                query = f"""
                SELECT
                    '{kpi_name}' AS kpi_name,
                    fm.name AS master_field_name,
                    fm."group" AS master_field_group,
                    t.*

                FROM {table_name} t

                LEFT JOIN fields_master fm
                    ON fm.id = t.field_id

                WHERE t.company_id = :company_id
                AND t.frequency_year = :year
                """

                df = pd.read_sql(
                    text(query),
                    engine,
                    params={
                        "company_id": company_id,
                        "year": str(year)
                    }
                )

                # Remove duplicate columns if any
                df = df.loc[:, ~df.columns.duplicated()]

                all_dataframes.append(df)

    
        if all_dataframes:

            final_df = pd.concat(
                all_dataframes,
                ignore_index=True
            )

            # Final duplicate cleanup
            final_df = final_df.loc[
                :,
                ~final_df.columns.duplicated()
            ]

            return final_df

        return pd.DataFrame()