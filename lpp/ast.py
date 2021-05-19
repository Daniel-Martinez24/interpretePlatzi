from abc import (
	ABC,
	abstractmethod
)

from lpp.token import Token

class ASTnode(ABC):
	"""docstring for ASTnode"""
	@abstractmethod
	def token_literal(self) -> str:
		pass

	@abstractmethod
	def __str__(self) -> None:
		pass

class Statement(ASTnode):
	"""docstring for Statement"""
	def __init__(self, token: Token):
		self.token = Token
		
	def token_literal():
		return self.token_literal

class Expression(ASTnode):
	"""docstring for Expression"""
	def __init__(self, token: Token):
		self.token = Token
		
	def token_literal():
		return self.token_literal


		