import unittest
from utils.PrimeGenerator import PrimeGenerator
from unittest_data_provider import data_provider


class PrimeGeneratorTest(unittest.TestCase):
    @data_provider(lambda: (
        (-1,),
        (0,),
        (1,),
    ))
    def test_invalid_value(self, invalid_num: int):
        with self.assertRaises(ValueError):
            PrimeGenerator(invalid_num)

    def test_base_value(self):
        self.assertEqual([2], list(PrimeGenerator(2)))

    def test_second_value(self):
        self.assertEqual([2, 3], list(PrimeGenerator(3)))

    def test_several_values_end_on_prime(self):
        self.assertEqual([2, 3, 5, 7, 11], list(PrimeGenerator(11)))

    def test_several_values_end_on_non_prime(self):
        self.assertEqual([2, 3, 5, 7, 11], list(PrimeGenerator(12)))

    def test_primes_under_100(self):
        primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        self.assertEqual(primes_under_100, list(PrimeGenerator(100)))
