import unittest
import leapyears

class testleapyears(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapyears.leapyears(400), "The year 400 is not a leap year")

if __name__ == '__main__':
    unittest.main()
