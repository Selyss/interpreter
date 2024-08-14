class TokenType:
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"
    IDENT = "IDENT"
    INT = "INT"
    ASSIGN = "="
    PLUS = "+"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    FUNCTION = "FUNCTION"
    LET = "LET"

class Token:
    def __init__(self, type_, literal):
        self.type = type_
        self.literal = literal


keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
}

def lookup_ident(ident):
    return keywords.get(ident, TokenType.IDENT)