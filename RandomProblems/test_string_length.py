import unittest
import string_length

class BaseTest(unittest.TestCase):

    def test_string_length(self):
        self.assertEqual(string_length.recursive_str_len('paul'), 4)
        self.assertEqual(string_length.recursive_str_len('paulotieno'), 10)
        self.assertEqual(string_length.recursive_str_len(''), 0)
        self.assertEqual(string_length.recursive_str_len('p'), 1)

if __name__ == "__main__":
    unittest.main()