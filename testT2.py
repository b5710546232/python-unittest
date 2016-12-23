import unittest
import t2

class CountTest(unittest.TestCase):
    def test_one_should_be_odd(self):
        testInput = 1
        expect = "Odd"
        self.assertEqual(t2.checknum(testInput),expect)

    def test_one_should_not_even(self):
        testInput = 1
        unExpect = "Even"
        self.assertNotEqual(t2.checknum(testInput),unExpect)

        



if __name__ == '__main__':
    unittest.main()