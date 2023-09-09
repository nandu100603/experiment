import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    
    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecarr"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))

if __name__ == '__main__':
    unittest.main()
