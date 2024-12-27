class Interp:
    def __init__(self, file_path):
        self.path = file_path
        self.contents = None
        self.get_file(file_path)
        self.parse()

    '''
    opens and loads all file `path` contents to self.contents
    '''
    def get_file(self, path: str) -> None:
        # check if file exits
        file = open(path, "r")
        self.contents = file.read().split('\n')
        file.close()

    '''
    parse through each line by line to find tokens and execute the stuff within
    '''
    def parse(self) -> None:
        from tokens import Tokens
        t = Tokens()
        recognized_tokens = t.recognized_tokens

        for line in self.contents:
            line = line.split(" ")
            
            if line[0] in recognized_tokens:
                func = recognized_tokens[line[0]]
                func(line[1:])
            else:
                raise Exception("Token not recognized", line[0])