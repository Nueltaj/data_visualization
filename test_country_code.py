"""this is a module that tests the country code"""

import unittest
from country_codes import get_country_code as GCC


class TestCountryCode(unittest.TestCase):
    """Test 1: Check if the country code is correct"""

    def test_country_code(self):
        """test the get_country_code"""
        self.assertEqual(GCC("Nigeria"), "ng")
        self.assertEqual(GCC("United States"), "us")
        self.assertIsNone(GCC("eden"))

    def test_invalid_data(self):
        """test the handling of the data"""
        with self.assertRaises(ValueError):
            float("Invalid")


# run test
if __name__ == "__main__":
    unittest.main()
