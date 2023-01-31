import unittest
import Kata_1 as k1

class Kata_1_test(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEqual(k1.fizzbuzz(3),"fizz")
        self.assertEqual(k1.fizzbuzz(9),"fizz")
        self.assertNotEqual(k1.fizzbuzz(0),"fizz")
        self.assertNotEqual(k1.fizzbuzz(5),"fizz")

    def test_buzz(self):
        self.assertEqual(k1.fizzbuzz(5),"buzz")
        self.assertNotEqual(k1.fizzbuzz(0),"buzz")
        self.assertNotEqual(k1.fizzbuzz(3),"buzz")

    def test_fizzbuzz(self):
        self.assertEqual(k1.fizzbuzz(15), "fizzbuzz")
        self.assertNotEqual(k1.fizzbuzz(3),"fizzbuzz")
        self.assertNotEqual(k1.fizzbuzz(5),"fizzbuzz")


if __name__ == "__main__":
    unittest.main()