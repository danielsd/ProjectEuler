from unittest import TestCase
from unittest_data_provider import data_provider

from .combinatoric_selections import solve, binomial_coefficient


class TestSolution(TestCase):
    @data_provider(lambda: (
        (5, 3, 10),
        (23, 10, 1144066),
    ))
    def test_binomial_coefficient(self, n: int, r: int, expected: int):
        self.assertEqual(expected, binomial_coefficient(n, r))

    @data_provider(lambda: (
        (4075,),
    ))
    def test_solve(self, expected: int):
        self.assertEqual(expected, solve())
