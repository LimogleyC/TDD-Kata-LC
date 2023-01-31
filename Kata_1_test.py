import unittest
import Kata_1 as k1

class Kata_1_test(unittest.TestCase):
    
    def test_fizz(self):
        # t1 = k1.fizzbuzz(9)
        self.assertEqual(k1.fizzbuzz(9),"fizz")

if __name__ == "__main__":
    unittest.main()