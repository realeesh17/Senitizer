import unittest
from src.sanitizer import Sanitizer

class TestSanitizer(unittest.TestCase):

    def setUp(self):
        self.sanitizer = Sanitizer()

    def test_sanitize_input(self):
        self.assertEqual(self.sanitizer.sanitize_input("<script>alert('test')</script>"), "alert('test')")
        self.assertEqual(self.sanitizer.sanitize_input("Hello, World!"), "Hello, World!")

    def test_validate_input(self):
        self.assertTrue(self.sanitizer.validate_input("valid_input"))
        self.assertFalse(self.sanitizer.validate_input(""))

if __name__ == '__main__':
    unittest.main()