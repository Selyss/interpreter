from abc import ABC, abstractmethod
from tokens import *

class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass
    
    @abstractmethod
    def string(self) -> str:
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
        self.statements: list[Statement] = []

    def token_literal(self) -> str:
        if self.statements:
            return self.statements[0].token_literal()
        else:
            return ""
        
    def string(self) -> str:
        out = ""
        for statement in self.statements:
            out += statement.string()
        return out

class LetStatement(Statement):
    def __init__(self, token: Token, name=None, value=None):
        self.token: Token = token
        self.name = name
        self.value: Expression = value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
    def string(self) -> str:
        out = f"{self.token_literal()} {self.name.string()} = "
        if self.value is not None:
            out += self.value.string()
        out += ";"
        return out
    
class ReturnStatement(Statement):
    def __init__(self, token: Token, return_value=None):
        self.token: Token = token
        self.return_value: Expression = return_value

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
    def string(self) -> str:
        out = f"{self.token_literal()} "
        if self.return_value is not None:
            out += self.return_value.string()
        out += ";"
        return out

class Identifier(Expression):
    def __init__(self, token: Token, value: str):
        self.token: Token = token
        self.value: str = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
    def string(self) -> str:
        return self.value
    
class ExpressionStatement(Statement):
    def __init__(self, token: Token, expression=None):
        self.token: Token = token
        self.expression: Expression = expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
    
    def string(self) -> str:
        if self.expression is not None:
            return self.expression.string()
        return ""