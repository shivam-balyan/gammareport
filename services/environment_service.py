from utils.sanitizers import sanitize_text


class EnvironmentService:

    @staticmethod
    def save_gri_301_3(
        company_id,
        year,
        methodology,
        file
    ):

        methodology = sanitize_text(
            methodology
        )

        data = {
            "company_id": company_id,
            "year": year,
            "methodology": methodology
        }

        return data