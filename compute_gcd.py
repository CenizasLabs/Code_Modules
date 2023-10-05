import unittest

# REQUIREMENTS
import math

#GLOBAL VARIABLES

#SETUP INSTRUCTIONS

# FUNCTIONS
def compute_gcd(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute GCD.")
    
    gcd_result = numbers[0]
    
    for i in range(1, len(numbers)):
        gcd_result = math.gcd(gcd_result, numbers[i])
    
    return gcd_result

# TEST CASES
class TestComputeGCD(unittest.TestCase):

    def test_gcd_of_positive_numbers(self):
        numbers = [12, 18, 24]
        result = compute_gcd(numbers)
        self.assertEqual(result, 6)

    def test_gcd_of_negative_numbers(self):
        numbers = [-12, -18, -24]
        result = compute_gcd(numbers)
        self.assertEqual(result, 6)

    def test_gcd_of_mixed_numbers(self):
        numbers = [-12, 18, 24]
        result = compute_gcd(numbers)
        self.assertEqual(result, 6)

    def test_gcd_of_same_numbers(self):
        numbers = [42, 42, 42]
        result = compute_gcd(numbers)
        self.assertEqual(result, 42)

    def test_gcd_of_two_numbers(self):
        numbers = [9, 27]
        result = compute_gcd(numbers)
        self.assertEqual(result, 9)

    def test_gcd_of_two_prime_numbers(self):
        numbers = [13, 17]
        result = compute_gcd(numbers)
        self.assertEqual(result, 1)

    def test_gcd_of_empty_list(self):
        with self.assertRaises(ValueError):
            compute_gcd([])

    def test_gcd_of_single_number(self):
        with self.assertRaises(ValueError):
            compute_gcd([42])

if __name__ == '__main__':
    unittest.main()