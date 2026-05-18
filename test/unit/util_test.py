import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    # --- CONVERT TO NUMBER TESTS ---
    def test_convert_to_number_integer(self):
        self.assertEqual(2, util.convert_to_number("2"))
        self.assertEqual(-10, util.convert_to_number("-10"))
        self.assertEqual(0, util.convert_to_number("0"))

    def test_convert_to_number_float(self):
        self.assertEqual(2.5, util.convert_to_number("2.5"))
        self.assertEqual(-0.01, util.convert_to_number("-0.01"))

    def test_convert_to_number_fails_with_invalid_string(self):
        self.assertRaises(TypeError, util.convert_to_number, "abc")
        self.assertRaises(TypeError, util.convert_to_number, "2.5.5")

    def test_convert_to_number_fails_with_invalid_types(self):
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    # --- VALIDATE PERMISSIONS TESTS ---
    def test_validate_permissions_success_for_authorized_user(self):
        self.assertTrue(util.validate_permissions("2 * 2", "user1"))
        self.assertTrue(util.validate_permissions("add", "user1"))

    def test_validate_permissions_fails_for_unauthorized_user(self):
        self.assertFalse(util.validate_permissions("2 * 2", "user2"))
        self.assertFalse(util.validate_permissions("substract", "admin"))
        self.assertFalse(util.validate_permissions("power", None))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
