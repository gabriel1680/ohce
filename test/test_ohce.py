from unittest import TestCase
from unittest.mock import patch, call

from src.ohce import Ohce


class TestOhce(TestCase):

    @patch("src.ohce.Console")
    @patch("src.ohce.Greeter")
    @patch("src.ohce.Interpreter")
    def setUp(self, MockConsole, MockGreeter, MockInterpreter) -> None:
        self.console = MockConsole.return_value
        self.greeter = MockGreeter.return_value
        self.interpreter = MockInterpreter.return_value
        self.sut = Ohce(self.console, self.greeter, self.interpreter)
        return super().setUp()

    def test_greet_and_stop(self):
        self.greeter.greet.return_value = "Buenos dias Pedro!"
        self.console.read_line.return_value = "Stop!"
        self.sut.run("Pedro")
        self.console.println.assert_has_calls([
            call("Buenos dias Pedro!"), call("Adios Pedro")])
        
    def test_greet_and_echo_and_stop(self):
        self.greeter.greet.return_value = "Buenos dias Pedro!"
        self.console.read_line.side_effect = ["hola", "Stop!"]
        self.interpreter.interpret.return_value = ["olah"]
        self.sut.run("Pedro")
        self.console.println.assert_has_calls([
            call("Buenos dias Pedro!"), call("olah"), call("Adios Pedro")])

    def test_greet_and_echo_palindrom__and_stop(self):
        self.greeter.greet.return_value = "Buenos dias Pedro!"
        self.console.read_line.side_effect = ["oto", "Stop!"]
        self.interpreter.interpret.return_value = ["oto", "Bonita palabra"]
        self.sut.run("Pedro")
        self.console.println.assert_has_calls([
            call("Buenos dias Pedro!"), 
            call("oto"), 
            call("Bonita palabra"), 
            call("Adios Pedro")])
