# test_fibonacci.py

import unittest
from fibonacci import generate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_negative_terms(self):
        result = generate_fibonacci(-5)
        self.assertEqual(result, "Please enter a positive integer")
    
    def test_zero_terms(self):
        result = generate_fibonacci(0)
        self.assertEqual(result, "Please enter a positive integer")
    
    def test_one_term(self):
        result = generate_fibonacci(1)
        self.assertEqual(result, [0])
    
    def test_multiple_terms(self):
        result = generate_fibonacci(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])
    
    def test_large_number_of_terms(self):
        result = generate_fibonacci(10)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == "_main_":
    unittest.main()
