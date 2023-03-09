from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, file):
        raise NotImplementedError

    @abstractmethod
    def file_extension(cls, file_path, extension):
        check_extension = file_path.split(".")[-1]
        if check_extension != extension:
            raise ValueError("Extenção de arquivo inválido")
