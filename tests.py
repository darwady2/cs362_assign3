import random
import unittest
from unittest import TestCase
from credit_card_validator import credit_card_validator

# How many runs of each test.
RANGE = 1000


class Test(TestCase):
    def test_credit_card_validator_random_9_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(100000000, 999999999))
            credit_card_validator(val)

    def test_credit_card_validator_random_10_digit(self):
        pass


if __name__ == '__main__':
    unittest.main()
