from unittest import TestCase
from unittest_data_provider import data_provider

from .prime_digit_replacements import solve


class TestSolution(TestCase):
    @data_provider(lambda: (
        (6, 13),      # Example 1
        (7, 56003),   # Example 2
        (8, 121313),  # Problem
    ))
    def test_solve(self, prime_family_count: int, expected_smallest_prime: int):
        self.assertEqual(expected_smallest_prime, solve(prime_family_count))
