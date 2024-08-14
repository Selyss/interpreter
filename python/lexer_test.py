import unittest
from .token import TokenType
class TestLexer(unittest.TestCase):
    def test_next_token(self):
        input = "=+(){},;"
        tests = [
            (TokenType.ASSIGN, "="),
            (TokenType.PLUS, "+"),
            (TokenType.LPAREN, "("),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.RBRACE, "}"),
            (TokenType.COMMA, ","),
            (TokenType.SEMICOLON, ";"),
            (TokenType.EOF, ""),
        ]
        
        lexer = Lexer(input)

        for i, (expected_type, expected_literal) in enumerate(tests):
            token = lexer.next_token()
            self.assertEqual(token.type, expected_type, f"tests[{i}] - tokentype wrong. expected={expected_type}, got={token.type}")
            self.assertEqual(token.literal, expected_literal, f"tests[{i}] - literal wrong. expected={expected_literal}, got={token.literal}")

if __name__ == "__main__":
    unittest.main()