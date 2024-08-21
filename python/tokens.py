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
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"
    EQ = "=="
    NOT_EQ = "!="

class Token:
    def __init__(self, type_, literal):
        self.type = type_
        self.literal = literal


keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN,
}

def lookup_ident(ident):
    return keywords.get(ident, TokenType.IDENT)