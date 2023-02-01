import unittest
import Kata_1 as k1

class Kata_1_test(unittest.TestCase):
    
    def test_shouldPrintFizz_whenDivisible3(self):
        self.assertEqual(k1.fizzbuzz(3),"fizz")
        self.assertNotEqual(k1.fizzbuzz(0),"fizz")
        self.assertNotEqual(k1.fizzbuzz(5),"fizz")

    def test_shouldPrintBuzz_whenDivisible5(self):
        self.assertEqual(k1.fizzbuzz(5),"buzz")
        self.assertNotEqual(k1.fizzbuzz(0),"buzz")
        self.assertNotEqual(k1.fizzbuzz(3),"buzz")

    def test_shouldPrintFizzBuzz_whenDivisible3or5(self):
        self.assertEqual(k1.fizzbuzz(15), "fizzbuzz")
        self.assertNotEqual(k1.fizzbuzz(3),"fizzbuzz")
        self.assertNotEqual(k1.fizzbuzz(5),"fizzbuzz")


if __name__ == "__main__":
    unittest.main()