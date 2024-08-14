from tokens import *


class Lexer:
    def __init__(self, input):
        self.input = input
        self.positon = 0
        self.read_position = 0
        self.ch = ""
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0 # NUL (or EOF)
        else:
            self.ch = self.input[self.read_position]
        self.positon = self.read_position
        self.read_position += 1

    def next_token(self):
        if self.ch == "=":
            token = Token(TokenType.ASSIGN, self.ch)
        elif self.ch == "+":
            token = Token(TokenType.PLUS, self.ch)
        elif self.ch == "(":
            token = Token(TokenType.LPAREN, self.ch)
        elif self.ch == ")":
            token = Token(TokenType.RPAREN, self.ch)
        elif self.ch == "{":
            token = Token(TokenType.LBRACE, self.ch)
        elif self.ch == "}":
            token = Token(TokenType.RBRACE, self.ch)
        elif self.ch == ",":
            token = Token(TokenType.COMMA, self.ch)
        elif self.ch == ";":
            token = Token(TokenType.SEMICOLON, self.ch)
        elif self.ch is None:
            token = Token(TokenType.EOF, "")
        else:
            token = None
        
        self.read_char()
        return token

