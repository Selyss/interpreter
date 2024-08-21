from lexer import *
from tokens import *

PROMPT = ">> "

def start():
    while True:
        print(PROMPT, end="")
        user_input = input()
        lexer = Lexer(user_input)
        while True:
            token = lexer.next_token()
            if token.type == TokenType.EOF:
                break
            print(f"{{Type: {token.type}, Literal: {token.literal}}}")