import unittest
import FizzBuzz

class testFizzBuzz(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(FizzBuzz.FizzBuzz(), 100)

if __name__ == '__main__':
    unittest.main()
