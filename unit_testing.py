import unittest

# 1. The function we want to test
def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b

# 2. The Testing Class
class TestMathOperations(unittest.TestCase):
    
    def test_divide_success(self):
        # Testing a correct division
        self.assertEqual(divide_numbers(10, 2), 5.0)
        self.assertEqual(divide_numbers(-9, 3), -3.0)
        
    def test_divide_by_zero(self):
        # Testing error handling
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()
