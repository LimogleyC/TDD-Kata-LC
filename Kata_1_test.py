import unittest
import Kata_1

class(unittest.TestCase):
    def fizz_test(self):
        t1 = fizzbuzz(9)
        self.assertEqual(t1,"fizz")