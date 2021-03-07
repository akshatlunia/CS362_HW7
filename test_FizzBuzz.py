import unittest
import FizzBuzz

class testFizzBuzz(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(FizzBuzz.FizzBuzz(), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
