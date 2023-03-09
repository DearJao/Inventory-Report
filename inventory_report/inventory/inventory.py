from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import DictReader
from json import loads
from xml.etree import ElementTree


class Inventory:
    @classmethod
    def get_xml_file_data(cls, file_path):
        file = ElementTree.parse(file_path).getroot()
        data_dict = []

        for record in file.findall("record"):
            records = {}

            for product in record:
                records[product.tag] = product.text

            data_dict.append(records)

        return data_dict

    @classmethod
    def get_csv_file_data(cls, file_path):
        with open(file_path, "r") as file:
            file_reader = DictReader(file, delimiter=",")
            data_dict = []
            for row in file_reader:
                data_dict.append(row)
            return data_dict

    @classmethod
    def get_json_file_data(cls, file_path):
        with open(file_path, "r") as file:
            file_reader = file.read()
            data_dict = loads(file_reader)
            return data_dict

    @classmethod
    def get_file_by_type(cls, file_path):
        extension = file_path.split(".")[-1]
        if extension == "csv":
            return cls.get_csv_file_data(file_path)
        elif extension == "json":
            return cls.get_json_file_data(file_path)
        elif extension == "xml":
            return cls.get_xml_file_data(file_path)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def import_data(cls, file_path, report_type):
        data_dict = cls.get_file_by_type(file_path)
        if report_type == "simples":
            return SimpleReport.generate(data_dict)
        elif report_type == "completo":
            return CompleteReport.generate(data_dict)
        else:
            raise ValueError("Formato inválido")
