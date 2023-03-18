from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    @property
    def is_actual(self):
        return self.__is_actual

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, data_to_write: str):
        self.__txt_writer.write(data_to_write)
        if self.__is_actual:
            self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')

    print(proxy_reader.is_actual)

    proxy_reader.read_file()
    print(proxy_reader.is_actual)

    proxy_reader.write_file('Text to write')
    print(proxy_reader.is_actual)

    proxy_reader.read_file()
    print(proxy_reader.is_actual)

    proxy_reader.write_file('Text to write')
    print(proxy_reader.is_actual)
