import pandas as pd
from core.database import engine

class CompanyRepository:

    @staticmethod
    def get_companies():

        query = """
        SELECT id, company_name
        FROM companies 
        WHERE role = 'company'
        ORDER BY company_name
        """

        return pd.read_sql(query, engine)