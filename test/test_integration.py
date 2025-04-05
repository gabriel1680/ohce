from unittest import TestCase
from unittest.mock import patch, call

from src.ohce import Ohce, Greeter, Interpreter


class TestIntegration(TestCase):

    @patch("src.ohce.Console")
    def setUp(self, MockConsole):
        self.console = MockConsole.return_value
        self.greeter = Greeter(lambda : 6)
        self.interpreter = Interpreter()
        self.sut = Ohce(self.console, self.greeter, self.interpreter)
    
    def test_integration(self):
        self.console.read_line.side_effect = ["hola", "oto", "Stop!"]
        self.sut.run("Pedro")
        expected = [call("Buenos dias Pedro!"), call("aloh"), call("oto"), call("Bonita palabra!"), call("Adios Pedro")]
        self.console.println.assert_has_calls(expected)

