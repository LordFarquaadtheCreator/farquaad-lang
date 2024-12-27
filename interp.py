class Interp:
    def __init__(self, file_path):
        self.path = file_path
        self.contents = None
        self.get_file(file_path)

    '''
    opens and loads all file `path` contents to self.contents
    '''
    def get_file(self, path: str) -> None:
        import os
        try:
            file = open(path, "r")
            self.contents = file.read()
            file.close()
        except Exception as e:
            print("Ruh roh raggy, smth went wrong!", e)
            exit(1)

if __name__ == "__main__":
    i = Interp("test.skibidi")
    