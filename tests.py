import random
import unittest
from unittest import TestCase
from credit_card_validator import credit_card_validator

# How many runs of each test.
RANGE = 100000


class Test(TestCase):
    def test_random_14_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(1000000000, 9999999999))
            credit_card_validator(val)

    # Triggered Bug 3
    def test_random_15_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(100000000000000, 999999999999999))
            credit_card_validator(val)

    # Triggered Bug 1
    def test_random_16_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(1000000000000000, 9999999999999999))
            credit_card_validator(val)

    def test_random_17_digit(self):
        for i in range(0, RANGE):
            val = str(random.randint(10000000000000000, 99999999999999999))
            credit_card_validator(val)

    def test_valid_cc_range(self):
        # Tests 15 digit CC #s through 16 digit CC #s
        for i in range(0, RANGE):
            val = str(random.randint(340000000000000, 5599999999999999))
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
