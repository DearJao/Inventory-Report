from inventory_report.importer.importer import Importer
from json import loads


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        cls.check_file_extension(cls, file_path, "json")
        with open(file_path, "r") as file:
            file_reader = file.read()
            data_dict = loads(file_reader)
            return data_dict
