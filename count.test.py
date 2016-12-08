import unittest
from count import count

class CountTest(unittest.TestCase):
    def test_count(self):
        testInput1 = [1,1,1,3,3]
        testInput2 = [1,1,5,0]
        self.assertEqual(count(testInput1),{1: 3,3: 2})
        self.assertEqual(count(testInput2),{0:1,1:2,5: 1})
        self.assertNotEqual(count(testInput1),{1: 10,3: 2})
        



if __name__ == '__main__':
    unittest.main()