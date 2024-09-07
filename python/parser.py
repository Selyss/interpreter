from typing import Callable, List
from astt import *
from lexer import *
from tokens import *

prefix_parse_fn = Callable[[], Expression]
infix_parse_fn = Callable[[Expression], Expression]

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer: Lexer = lexer
        self.current_token: Token = None
        self.peek_token: Token = None
        self.errors: List[str] = []

        self.prefix_parse_fns: dict[TokenType, prefix_parse_fn] = {}
        self.infix_parse_fns: dict[TokenType, infix_parse_fn] = {}

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
            return None
    
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
