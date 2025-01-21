import unittest
from test_module import add, subtract

class TestMyModule(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 8), -3)

if __name__ == '__main__':
    unittest.main()