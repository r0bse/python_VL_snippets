class CsvReader():

    def __init__(self, path: str):
        self.path = path

    def read(self):
        pass
def file_reader(path):

    # TODO check if file exists
    if path.endswith(".csv"):
        return CsvReader(path)
    elif path.endswith(".xml"):
        # TODO
        ...
    else:
        return None

if __name__ == "__main__":
    reader = file_reader("test.csv")

