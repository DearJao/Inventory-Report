from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        cls.check_file_extension(cls, file_path, "csv")
        with open(file_path, "r") as file:
            file_reader = DictReader(file, delimiter=",")
            data_dict = []
            for row in file_reader:
                data_dict.append(row)
            return data_dict
