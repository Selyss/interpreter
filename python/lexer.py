class Lexer:
    def __init__(self, input):
        self.input = input
        self.positon = 0
        self.read_position = 0
        self.ch = ""
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_position]
        self.positon = self.read_position
        self.read_position += 1

        