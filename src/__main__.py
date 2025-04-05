import sys
from datetime import datetime

from ohce import Ohce, Console, Greeter, Interpreter

def main():
    get_hour = lambda : datetime.now().day
    ohce = Ohce(Console(), Greeter(get_hour), Interpreter())
    ohce.run(sys.argv[1])

if __name__ == "__main__":
    main()
