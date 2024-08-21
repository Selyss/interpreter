from abc import ABC, abstractmethod
from typing import List
from tokens import *

class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

class Statement(Node):
    @abstractmethod
    def statement_node(self):
        pass

class Expression(Node):
    @abstractmethod
    def expression_node(self):
        pass

class Program(Node):
    def __init__(self):
        self.statements: List[Statement] = []

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""

class LetStatement(Statement):
    def __init__(self, token: Token, name=None, value=None):
        self.token: Token = token
        self.name = name
        self.value: Expression = value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
class Identifier(Expression):
    def __init__(self, token: Token, value: str):
        self.token: Token = token
        self.value: str = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
