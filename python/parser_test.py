import unittest
from astt import *
from lexer import *
from parser import *


class TestParser(unittest.TestCase):
    def test_let_statements(self):
        input_code = """
                let x = 5;
                let y = 10;
                let foobar = 838383;
                """
        lexer = Lexer(input_code)
        parser = Parser(lexer)
        program = parser.parse_program()
        
        self.assertIsNotNone(program, "parse_program() returned None")
        self.assertEqual(len(program.statements), 3, f"program.statements does not contain 3 statements. got={len(program.statements)}")

        tests = [
            {"expected_identifier": "x"},
            {"expected_identifier": "y"},
            {"expected_identifier": "foobar"},
        ]

        for i, test in enumerate(tests):
            stmt = program.statements[i]
            self.assertTrue(self.test_let_statement(stmt, test["expected_identifier"]))

    def test_let_statement(self, stmt, name):
        self.assertEqual(stmt.token_literal(), "let")
        self.assertIsInstance(stmt, LetStatement, f"stmt not LetStatement. got={type(stmt)}")
        self.assertEqual(stmt.name.value, name)
        self.assertEqual(stmt.name.token_literal(), name)
        return True
    
if __name__ == "__main__":
    unittest.main()
