class Tokens:
    def __init__(self):
        self.recognized_tokens = {"preach" : self.print_token}

    def print_token(self, args):
        for arg in args:
            if not type(arg) == str:
                raise Exception("oops, argument not of type string!")
            print(arg, end=' ')