import unittest
from unittest.mock import patch
from utils.utils import is_int, try_get_int_value


class TestMainFunctions(unittest.TestCase):
    def test_is_int(self):
        self.assertTrue(is_int("5"))
        self.assertTrue(is_int("-3"))
        self.assertTrue(is_int("0"))
        self.assertFalse(is_int("10.0"))
        self.assertFalse(is_int("str"))
        self.assertFalse(is_int("4t"))

    @patch("builtins.print")
    def test_valid_int_input(self, mock_print):
        test_cases = [("3", 3), ("-3", -3), ("0", 0)]

        for input_value, expected_output in test_cases:
            with patch("builtins.input", return_value=input_value):
                result = try_get_int_value()
                self.assertEqual(result, expected_output)
                mock_print.assert_not_called()

    @patch("builtins.print")
    def test_invalid_int_input(self, mock_print):
        test_cases = ["abc", "test", "", "10-"]
        for input_value in test_cases:
            with patch("builtins.input", return_value=input_value):
                result = try_get_int_value()
                self.assertIsNone(result)
                mock_print.assert_called()


if __name__ == "__main__":
    unittest.main()
