from unittest import TestCase
from parameterized import parameterized

from src.ohce import Greeter

class TestGreeter(TestCase):

    def setUp(self) -> None:
        self.current_hour = 0
        self.get_hour = lambda : self.current_hour
        self.sut = Greeter(self.get_hour)
        return super().setUp()

    @parameterized.expand([6, 7, 8, 9, 10, 11])
    def test_greet_on_the_morning(self, hour):
        self.current_hour = hour
        self.assertEqual(self.sut.greet("John"), "Buenos dias John!")

    @parameterized.expand([12, 13, 14, 15, 16, 17, 18, 19])
    def test_greet_on_the_evening(self, hour):
        self.current_hour = hour
        self.assertEqual(self.sut.greet("John"), "Buenas tardes John!")

    @parameterized.expand([20, 21, 22, 23, 0, 1, 2, 3, 4, 5])
    def test_greet_on_the_night(self, hour):
        self.current_hour = hour
        self.assertEqual(self.sut.greet("John"), "Buenas noches John!")
