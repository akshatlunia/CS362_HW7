import unittest
import leapyears

class testleapyears(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapyears.leapyears(400), "The year 400 is a 400-leap year")

if __name__ == '__main__':
    unittest.main()
