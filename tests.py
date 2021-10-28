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
        for i in range(0, RANGE):
            val = str(random.randint(1000000000, 9999999999))
            credit_card_validator(val)

    # Triggered Bug 3
    def test_credit_card_validator_random_15_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(100000000000000, 999999999999999))
            credit_card_validator(val)

    # Triggered Bug 1
    def test_credit_card_validator_random_16_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(1000000000000000, 9999999999999999))
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
