import unittest
from lexer import *
from parser import *
from token import *

class TestAST(unittest.TestCase):
    def test_string(self):
        program = Program()

        let_stmt = LetStatement(
            token=Token(TokenType.LET, "let"),
            name=Identifier(Token(TokenType.IDENT, "myVar"), "myVar"),
            value=Identifier(Token(TokenType.IDENT, "anotherVar"), "anotherVar")
        )

        program.statements.append(let_stmt)

        self.assertEqual(program.string(), "let myVar = anotherVar;")

if __name__ == "__main__":
    unittest.main()