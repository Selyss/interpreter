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
        self.check_parser_errors(parser)
        
        self.assertIsNotNone(program, "parse_program() returned None")
        self.assertEqual(len(program.statements), 3, f"program.statements does not contain 3 statements. got={len(program.statements)}")

        tests = [
            {"expected_identifier": "x"},
            {"expected_identifier": "y"},
            {"expected_identifier": "foobar"},
        ]

        for i, test in enumerate(tests):
            stmt = program.statements[i]
            if not self.let_statement_test(stmt, test["expected_identifier"]):
                return

    def check_parser_errors(self, parser: Parser):
        errors = parser.errors
        if len(errors) == 0:
            return
        
        print(f"parser has {len(errors)} errors")
        for error in errors:
            print(f"parser error: {error}")
        self.fail()

    def let_statement_test(self, stmt: Statement, name: str) -> bool:
        if stmt.token_literal() != "let":
            print(f"stmt.token_literal() != 'let', got={stmt.token_literal()}")
            return False
        
        if not isinstance(stmt, LetStatement):
            print(f"stmt not LetStatement. got={type(stmt)}")
            return False

        if stmt.name.value != name:
            print(f"stmt.name.value != {name}. got={stmt.name.value}")
            return False

        if stmt.name.token_literal() != name:
            print(f"stmt.name.token_literal() != {name}. got={stmt.name.token_literal()}")
            return False

        return True
    
    def return_statement_test(self, stmt: Statement) -> bool:
        if stmt.token_literal() != "return":
            print(f"stmt.token_literal() != 'return'. got={stmt.token_literal()}")
            return False
        
        if not isinstance(stmt, ReturnStatement):
            print(f"stmt not ReturnStatement. got={type(stmt)}")
            return False

        return True

    def test_return_statements(self):
        input_code = """
                return 5;
                return 10;
                return 993322;
                """
        lexer = Lexer(input_code)
        parser = Parser(lexer)
        program = parser.parse_program()
        self.check_parser_errors(parser)
        
        self.assertIsNotNone(program, "parse_program() returned None")
        self.assertEqual(len(program.statements), 3, f"program.statements does not contain 3 statements. got={len(program.statements)}")

        for stmt in program.statements:
            if not self.return_statement_test(stmt):
                return


if __name__ == "__main__":
    unittest.main()
