from tokens import *


class Lexer:
    def __init__(self, input):
        self.input = input
        self.positon = 0
        self.read_position = 0
        self.ch = ""
        self.read_char()
    
    def is_letter(self, ch):
        return "a" <= ch and ch <= "z" or "A" <= ch and ch <= "Z" or ch == "_"
    
    def skip_whitespace(self):
        while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
            self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0 # NUL (or EOF)
        else:
            self.ch = self.input[self.read_position]
        self.positon = self.read_position
        self.read_position += 1

    def read_number(self):
        position = self.positon
        while self.ch.isdigit():
            self.read_char()
        return self.input[position:self.position]

    def next_token(self):
        self.skip_whitespace()
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
        elif self.ch == 0:
            token = Token(TokenType.EOF, "")
        else:
            if self.is_letter(self.ch):
                literal = self.read_identifier()
                token_type = lookup_ident(literal)
                token = Token(token_type, literal)
                return token

            elif self.ch.isdigit():
                token_type = TokenType.INT
                literal = self.read_number()
                token = Token(token_type, literal)
                return token

            else:
                token = Token(TokenType.ILLEGAL, self.ch)
        
        self.read_char()
        return token
    
    def read_identifier(self):
        position = self.positon
        while self.is_letter(self.ch):
            self.read_char()
        return self.input[position:self.positon]


