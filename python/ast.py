from abc import ABC, abstractmethod

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