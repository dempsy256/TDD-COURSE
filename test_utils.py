import unittest
import json
from datetime import datetime

# Assuming utils.py is in the same directory
from utils import (
    sum_numbers,
    create_user,
    filter_adults,
    find_in_list,
    parse_json,
    approximate_division
)

class TestUtilityModule(unittest.TestCase):

    # 1. EXACT EQUALITY (Jest: toBe, toEqual, toStrictEqual)
    def test_exact_equality_pass(self):
        """Mirrors Jest: toBe, toEqual, toStrictEqual (Passing)"""
        # toBe -> assertEqual / assertIs
        self.assertEqual(sum_numbers(2, 2), 4)
        self.assertIs(sum_numbers(2, 2), 4)

        # toEqual / toStrictEqual -> assertDictEqual, assertListEqual
        user = create_user("Alice", 30)

        # Remove 'created_at' for exact dictionary matching, as time is non-deterministic
        del user["created_at"]
        expected_user = {"name": "Alice", "age": 30}
        self.assertDictEqual(user, expected_user)

        self.assertListEqual(filter_adults([{"age": 15}, {"age": 20}]), [{"age": 20}])

    @unittest.expectedFailure
    def test_exact_equality_fail(self):
        """Mirrors Jest: toBe, toEqual (Failing intentionally)"""
        # Fails because 2+2 != 5
        self.assertEqual(sum_numbers(2, 2), 5)

    # 2. NEGATION (Jest: .not)
    def test_negation_pass(self):
        """Mirrors Jest: .not.toBe, .not.toEqual (Passing)"""
        self.assertNotEqual(sum_numbers(1, 1), 3)
        self.assertIsNot(None, 0)
        self.assertNotIn("z", "apple")

    @unittest.expectedFailure
    def test_negation_fail(self):
        """Mirrors Jest: .not.toBe (Failing intentionally)"""
        # Fails because 2+2 IS 4, so assertNotEqual fails
        self.assertNotEqual(sum_numbers(2, 2), 4)

    # 3. TRUTHINESS (Jest: toBeNull, toBeDefined, toBeTruthy, toBeFalsy)
    def test_truthiness_pass(self):
        """Mirrors Jest: toBeTruthy, toBeFalsy, toBeNull (Passing)"""

        # toBeTruthy / toBeFalsy
        self.assertTrue(find_in_list([1, 2, 3], 2))
        self.assertFalse(find_in_list([1, 2, 3], 4))

        # toBeNull -> assertIsNone
        self.assertIsNone(None)
        
        # toBeDefined / not.toBeNull -> assertIsNotNone
        self.assertIsNotNone(create_user("Bob", 25))

    @unittest.expectedFailure
    def test_truthiness_fail(self):
        """Mirrors Jest: toBeTruthy (Failing intentionally)"""
        # Fails because 4 is NOT in the list
        self.assertTrue(find_in_list([1, 2, 3], 4))

    # 4. NUMBER MATCHERS (Jest: toBeGreaterThan, toBeCloseTo, etc.)
    def test_number_matchers_pass(self):
        """Mirrors Jest: toBeGreaterThan, toBeLessThanOrEqual, toBeCloseTo (Passing)"""
        self.assertGreater(sum_numbers(2, 3), 4)
        self.assertLessEqual(approximate_division(10, 2), 5)

        # toBeCloseTo -> assertAlmostEqual (Great for floating point issues)
        self.assertAlmostEqual(approximate_division(0.3, 0.1), 3.0, places=5)

    @unittest.expectedFailure
    def test_number_matchers_fail(self):
        """Mirrors Jest: toBeGreaterThan (Failing intentionally)"""
        # Fails because 2+3 is not greater than 5
        self.assertGreater(sum_numbers(2, 3), 5)

    # 5. STRING MATCHERS (Jest: toMatch)
    def test_string_matchers_pass(self):
        """Mirrors Jest: toMatch (Passing)"""
        self.assertRegex("Hello World", r"World")
        self.assertNotRegex("Hello World", r"Python")

    @unittest.expectedFailure
    def test_string_matchers_fail(self):
        """Mirrors Jest: toMatch (Failing intentionally)"""
        # Fails because "Python" is not in "Hello World"
        self.assertRegex("Hello World", r"Python")

    # 6. ARRAYS / ITERABLES (Jest: toContain)
    def test_array_matchers_pass(self):
        """Mirrors Jest: toContain (Passing)"""
        users = ["Alice", "Bob", "Charlie"]
        self.assertIn("Alice", users)
        self.assertNotIn("David", users)

    @unittest.expectedFailure
    def test_array_matchers_fail(self):
        """Mirrors Jest: toContain (Failing intentionally)"""
        users = ["Alice", "Bob", "Charlie"]
        # Fails because "David" is not in users
        self.assertIn("David", users)

    # 7. EXCEPTIONS (Jest: toThrow)
    def test_exceptions_pass(self):
        """Mirrors Jest: toThrow (Passing)"""
        # Basic toThrow equivalent
        with self.assertRaises(ValueError):
            parse_json(None)

        # toThrow(Error message) equivalent
        with self.assertRaisesRegex(ValueError, "No JSON string provided"):
            parse_json("")

    @unittest.expectedFailure
    def test_exceptions_fail(self):
        """Mirrors Jest: toThrow (Failing intentionally)"""
        # Fails because it DOES NOT raise an error; the string is valid JSON
        with self.assertRaises(ValueError):
            parse_json('{"key": "value"}')

if __name__ == "__main__":
    # Running unittest.main() will execute all tests
    unittest.main()