import unittest
import count_consonants


class BaseTest(unittest.TestCase):
    def test_count_consonants(self):
        self.assertEqual(count_consonants.count_consonants('PaulOtieno'), 4)
        self.assertEqual(count_consonants.count_consonants('Johnywalker'), 8)
        self.assertEqual(count_consonants.count_consonants('XYZ'), 3)

    def test_count_consonants_recursive(self):
        self.assertEqual(count_consonants.count_consonants_recursive('PaulOtieno'), 4)
        self.assertEqual(count_consonants.count_consonants_recursive('Johnywalker'), 8)
        self.assertEqual(count_consonants.count_consonants_recursive('XYZ'), 3)


if __name__ == "__main__":
    unittest.main()