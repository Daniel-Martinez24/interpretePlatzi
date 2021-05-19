from unittest import TestCase

from lpp.lexer import Lexer
from lpp.parser import Parse

class ParserTest(TestCase):
	"""Test para parser"""
	def test_parse_program(self) -> None:
		source: str = 'variable x = 5;'
		lexer: Lexer = Lexer(source)
		parser: Parse = Parser(lexer)


		program: Program = parser.parse_program()

		self.assertIsNotNone(program)
		self.assertIsInstance(program, Program)