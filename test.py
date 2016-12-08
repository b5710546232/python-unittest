import unittest

def cube(n):
    return n**3

class MyTest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(cube(5),125)



if __name__ == '__main__':
    unittest.main()()