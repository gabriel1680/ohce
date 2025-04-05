from unittest import TestCase

from src.ohce import Interpreter


class TestInterpreter(TestCase):

    def setUp(self) -> None:
        self.sut =  Interpreter()
        return super().setUp()

    def test_revert_a_word(self):
        self.assertEqual(["aloh"], self.sut.interpret("hola"))

    def test_palindrome(self):
        self.assertEqual(["oto", "Bonita palabra!"], self.sut.interpret("oto"))
