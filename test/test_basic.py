"""
test basics
"""

import unittest
from .context import core

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @classmethod
    def dummy_test(cls):
        """
        dummy_test, used as class method as there is no reference
        to self in the class
        """
        assert True

if __name__ == '__main__':
    unittest.main()
