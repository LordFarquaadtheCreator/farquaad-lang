class Tokens:
    def __init__(self):
        self.recognized_tokens = {
            "preach" : self.print_token,
            "ts" : self.make_variable
            }

    def print_token(self, args):
        for arg in args:
            if not type(arg) == str:
                raise Exception("oops, argument not of type string!")

            if arg in self.recognized_tokens:
                arg = self.recognized_tokens[arg]

            print(arg, end=' ')
        print('\n')
    
    def make_variable(self, args):
        if len(args) != 2:
            raise Exception("ts can only have two arguments")
        
        var = args[0]
        val = args[1]

        self.recognized_tokens[var] = val
