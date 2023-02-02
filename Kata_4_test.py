import unittest
import Kata_4 as k4

class Kata_4_test(unittest.TestCase):
    def test_shouldReturnNone_whenInputLT2(self):
        self.assertTrue(k4.too_short("B"))
    
    def test_shouldReturnValenciaVancouver_whenInputVa(self):
        self.assertTrue(k4.search("Va"), ["Valencia", "Vancouver"])

    def test_shouldPrintParis_whenInputaris(self):
        self.assertEqual(k4.search("aris"), ["Paris"])

    def test_shouldPrintParis_whenInputAris(self):
        self.assertEqual(k4.search("ARIS"), ["Paris"])

    def test_shouldPrintParis_whenInputAris(self):
        self.assertEqual(k4.search("ArIs"), ["Paris"])

    def test_shouldPrintSkopjeBangkokHongKong_whenInputko(self):
        self.assertEqual(k4.search("ko"), ["Skopje", "Bangkok", "Hong Kong"])

    def test_shouldPrintAll_whenInputAsteriks(self):
        self.assertEqual(k4.search("*"), ["Paris", "Budapest", "Skopje", 
            "Rotterdam", "Valencia", "Vancouver", "Amsterdam", "Vienna", 
            "Sydney", "New York City", "London", "Bangkok", "Hong Kong", 
            "Dubai", "Rome", "Istanbul"])

if __name__ == "__main__":
    unittest.main()