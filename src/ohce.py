from typing import Callable


class Console:

    def read_line(self) -> str:
        return input()

    def println(self, word: str) -> None:
        print(word)


class Greeter:

    def __init__(self, get_hour: Callable[[], int]) -> None:
        self.get_hour = get_hour

    def greet(self, name: str) -> str:
        hour = self.get_hour()
        if hour >= 6 and hour < 12:
            return f"Buenos dias {name}!"
        if hour >= 12 and hour < 20:
            return f"Buenas tardes {name}!"
        return f"Buenas noches {name}!"


class Interpreter:

    def interpret(self, word: str) -> list[str]:
        reversed = word[::-1]
        if word == reversed:
            return [word, "Bonita palabra!"]
        return [reversed]


class Ohce:
    
    def __init__(self, console: Console, greeter: Greeter, interpreter: Interpreter) -> None:
        self.console = console
        self.greeter = greeter
        self.interpreter = interpreter

    def run(self, name: str) -> None:
        self.console.println(self.greeter.greet(name))
        self.mainLoop()
        self.console.println(f"Adios {name}")

    def mainLoop(self) -> None:
        while (True):
            line = self.console.read_line()
            if (line == "Stop!"):
                break
            else:
                result = self.interpreter.interpret(line)
                for word in result:
                    self.console.println(word)
        
