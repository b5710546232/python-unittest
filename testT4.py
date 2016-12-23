import unittest
import t4

class MyTest(unittest.TestCase):
    def teststamp7(self):
       stamps = t4.stamp7(160)
       self.assertEqual(stamps['stamp_1'],1)
       self.assertEqual(stamps['stamp_3'],1)
    def testmembercheck(self):
        testInput = '1234'
        self.assertTrue(t4.memberCheck(testInput))

        self.assertFalse(t4.memberCheck('1150'))

        



if __name__ == '__main__':
    unittest.main()