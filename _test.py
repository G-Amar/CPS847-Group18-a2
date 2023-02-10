"""
Test helper functions
"""

import unittest
from func import square

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test_square(self):
        """
        Test increments
        """
        self.assertEqual(square(0), 0)
        self.assertEqual(square(6), 36)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(-1), 1)

if __name__ == '__main__':
    unittest.main()
