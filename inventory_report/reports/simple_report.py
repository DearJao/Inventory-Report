from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def earliest_manufacturing_date(list):
        data = [
            date.fromisoformat(product["data_de_fabricacao"])
            for product in list
        ]
        result = min(data)
        return result

    @staticmethod
    def closest_expiration_date(list):
        now = date.today()

        data = [
            date.fromisoformat(product["data_de_validade"]) for product in list
        ]

        closest_date = [product for product in data if product >= now]
        # print(closest_date)
        # print(min(closest_date))

        return min(closest_date)

    @staticmethod
    def company_with_most_products(list):
        company_produces_most = Counter(
            product["nome_da_empresa"] for product in list
        )

        return company_produces_most.most_common()[0][0]

    @staticmethod
    def generate(list):
        oldest_fabrication_date = SimpleReport.earliest_manufacturing_date(
            list
        )
        closest_expiration_date = SimpleReport.closest_expiration_date(list)
        company_most_products = SimpleReport.company_with_most_products(list)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_most_products}"
        )
