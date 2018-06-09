import unittest

from conic import Conic


class TestConic(unittest.TestCase):
    def test_raise(self):
        with self.assertRaises(ValueError):
            Conic.from_str('1 3 2,')
