import unittest
import Kata_4 as k4

class Kata_4_test(unittest.TestCase):
    def test_shouldReturnNone_whenInputLT2(self):
        self.assertTrue(k4.too_short("B"))
    
    def test_shouldPrintParis_whenInputaris(self):
        self.assertEqual(k4.search("aris"), "Paris")

    def test_shouldPrintParis_whenInputAris(self):
        self.assertEqual(k4.search("Aris"), "Paris")

if __name__ == "__main__":
    unittest.main()