from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        cls.check_file_extension(cls, file_path, "xml")
        file = ElementTree.parse(file_path).getroot()
        data_dict = []

        for record in file.findall("record"):
            records = {}

            for product in record:
                records[product.tag] = product.text

            data_dict.append(records)

        return data_dict
