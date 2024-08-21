import sys
from lexer import Lexer
from token import TokenType

PROMPT = ">> "

def start():
    while True:
        print(PROMPT, end="")
        input = sys.stdin.readline()
        lexer = Lexer(input)
        while True:
            token = lexer.next_token()
            if token.type == TokenType.EOF:
                break
            print(f"{{Type: {token.type}, Literal: {token.literal}}}")