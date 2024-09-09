from typing import Callable, List
from enum import Enum, IntEnum
from astt import *
from lexer import *
from tokens import *

prefix_parse_fn = Callable[[], Expression]
infix_parse_fn = Callable[[Expression], Expression]

class Precedence(IntEnum):
    LOWEST = 1
    EQUALS = 2
    LESSGREATER = 3
    SUM = 4
    PRODUCT = 5
    PREFIX = 6
    CALL = 7


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer: Lexer = lexer
        self.current_token: Token = None
        self.peek_token: Token = None
        self.errors: List[str] = []

        self.prefix_parse_fns: dict[TokenType, prefix_parse_fn] = {}
        self.infix_parse_fns: dict[TokenType, infix_parse_fn] = {}

        self.register_prefix(TokenType.IDENT, self.parse_identifier)
        self.register_prefix(TokenType.INT, self.parse_integer_literal)

        # Call this twice to initialize current_token and peek_token
        self.next_token()
        self.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()
    
    def parse_program(self):
        program = Program()
        while self.current_token.type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt is not None:
                program.statements.append(stmt)
            self.next_token()
        
        return program
    
    def register_prefix(self, token_type: TokenType, fn: prefix_parse_fn):
        self.prefix_parse_fns[token_type] = fn

    def register_infix(self, token_type: TokenType, fn: infix_parse_fn):
        self.infix_parse_fns[token_type] = fn
    
    def parse_statement(self):
        if self.current_token.type == TokenType.LET:
            return self.parse_let_statement()
        elif self.current_token.type == TokenType.RETURN:
            return self.parse_return_statement()
        else:
            return self.parse_expression_statement()
    
    def parse_let_statement(self):
        stmt = LetStatement(token=self.current_token)

        if not self.expect_peek(TokenType.IDENT):
            return None
        
        stmt.name = Identifier(token=self.current_token, value=self.current_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None
        
        # TODO: We're skipping the expressions until we encounter a semicolon
        while not self.current_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt
    
    def parse_return_statement(self):
        stmt = ReturnStatement(token=self.current_token)

        self.next_token()

        while not self.current_token_is(TokenType.SEMICOLON):
            self.next_token()
        
        return stmt
        
    def parse_expression_statement(self):
        stmt = ExpressionStatement(token=self.current_token)
        stmt.expression = self.parse_expression(Precedence.LOWEST)

        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()
        
        return stmt
    
    def current_token_is(self, token_type: TokenType) -> bool:
        return self.current_token.type == token_type
    
    def peek_token_is(self, token_type: TokenType) -> bool:
        return self.peek_token.type == token_type
    
    def expect_peek(self, token_type: TokenType) -> bool:
        if self.peek_token_is(token_type):
            self.next_token()
            return True
        else:
            self.peek_error(token_type)
            return False
        
    def errors(self):
        return self.errors
    
    def peek_error(self, token_type: TokenType):
        self.errors.append(f"expected next token to be {token_type}, got {self.peek_token.type} instead")

    def parse_expression(self, precedence: Precedence) -> Expression:
        prefix = self.prefix_parse_fns.get(self.current_token.type)
        if prefix is None:
            return None
        
        left_exp = prefix()
        return left_exp

    def parse_identifier(self) -> Expression:
        return Identifier(token=self.current_token, value=self.current_token.literal)
    
    def parse_integer_literal(self) -> Expression:
        return IntegerLiteral(token=self.current_token, value=int(self.current_token.literal))
    