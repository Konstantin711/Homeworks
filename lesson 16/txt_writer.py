from writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, data_to_write):
        with open(self.file_path, 'a') as file:
            file.write(data_to_write + '\n')
