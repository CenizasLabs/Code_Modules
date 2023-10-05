import unittest

# REQUIREMENTS
import math

#GLOBAL VARIABLES

#SETUP INSTRUCTIONS

# FUNCTIONS
def compute_lcm(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute LCM.")
    
    lcm_result = numbers[0]
    
    for i in range(1, len(numbers)):
        lcm_result = math.lcm(lcm_result, numbers[i])
    
    return lcm_result

# TEST CASES
class TestComputeLCM(unittest.TestCase):

    def test_compute_lcm_two_numbers(self):
        numbers = [12, 18]
        result = compute_lcm(numbers)
        self.assertEqual(result, 36)

    def test_compute_lcm_three_numbers(self):
        numbers = [12, 18, 24]
        result = compute_lcm(numbers)
        self.assertEqual(result, 72)

    def test_compute_lcm_more_than_three_numbers(self):
        numbers = [4, 6, 8, 10, 12]
        result = compute_lcm(numbers)
        self.assertEqual(result, 120)

    def test_compute_lcm_negative_numbers(self):
        numbers = [-6, -9, -15]
        result = compute_lcm(numbers)
        self.assertEqual(result, 90)

    def test_compute_lcm_with_zero(self):
        numbers = [0, 5, 10]
        result = compute_lcm(numbers)
        self.assertEqual(result, 0)

    def test_compute_lcm_single_number(self):
        numbers = [42]
        with self.assertRaises(ValueError):
            compute_lcm(numbers)

    def test_compute_lcm_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            compute_lcm(numbers)

if __name__ == '__main__':
    unittest.main()