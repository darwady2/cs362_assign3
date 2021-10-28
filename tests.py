import random
import unittest
from unittest import TestCase


class Test(TestCase):
    def test_credit_card_validator_random_9_digit(self):
        for i in range(0, 1000):
            val = random.randint(10000000, 99999999)
            mystery_func(val)

    def test_credit_card_validator_random_10_digit(self):
        pass



if __name__ == '__main__':
    unittest.main()
