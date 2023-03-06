from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def stocks_each_company(list):
        counter_products = Counter(
            [product["nome_da_empresa"] for product in list]
        )
        report = ""
        for company, qty in counter_products.items():
            report += f"- {company}: {qty}\n"
        # print(company, qty)
        return report

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        stocks_company = CompleteReport.stocks_each_company(list)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n {stocks_company}"
        )
