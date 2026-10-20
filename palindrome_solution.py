# Given an integer x, return True if x is a palindrome, and False otherwise.
#
# Example 1:
#   Input: x = 121
#   Output: True
#   Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
#   Input: x = -121
#   Output: False
#   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#   Input: x = 10
#   Output: False
#   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints: -2exp(31) <= x <= 2exp(31) - 1

import unittest

I32_MAX = 2**31 - 1
I32_MIN = -(2**31)


def is_palindrome(x: int) -> bool:
    # TODO
    return False


#
# Test Cases
#
class Tests(unittest.TestCase):

    # The three examples from the problem statement.

    def test_example_1_positive_palindrome(self):
        self.assertTrue(is_palindrome(121))

    def test_example_2_negative_is_never_a_palindrome(self):
        self.assertFalse(is_palindrome(-121))

    def test_example_3_trailing_zero_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome(10))

    # Single digits, including zero, are palindromes.

    def test_zero_is_a_palindrome(self):
        self.assertTrue(is_palindrome(0))

    def test_all_single_digits_are_palindromes(self):
        for x in range(0, 10):
            self.assertTrue(is_palindrome(x), f"{x} should be a palindrome")

    # Every negative value is rejected by the sign, including -0 cases
    # such as -10 whose absolute value also ends in zero.

    def test_negative_single_digit_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome(-1))

    def test_negative_with_trailing_zero_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome(-10))

    # Even and odd digit counts take different paths in a half-reversal
    # implementation, so both are covered.

    def test_even_digit_count_palindrome(self):
        self.assertTrue(is_palindrome(1221))

    def test_odd_digit_count_palindrome(self):
        self.assertTrue(is_palindrome(12321))

    def test_even_digit_count_non_palindrome(self):
        self.assertFalse(is_palindrome(1231))

    def test_odd_digit_count_non_palindrome(self):
        self.assertFalse(is_palindrome(12345))

    # Interior zeros must be preserved by the reversal.

    def test_interior_zeros_palindrome(self):
        self.assertTrue(is_palindrome(1_000_000_001))

    def test_interior_zeros_non_palindrome(self):
        self.assertFalse(is_palindrome(1_000_000_000))

    def test_near_miss_differing_only_in_the_middle(self):
        self.assertFalse(is_palindrome(123_456_789))
        # These two differ only near the middle digit.
        self.assertTrue(is_palindrome(1_002_001))
        self.assertFalse(is_palindrome(1_002_011))

    # Boundary values of i32. Reversing the full value of a large input
    # overflows i32, so these detect an implementation that reverses into
    # an i32 without a checked or widening operation.

    def test_i32_max_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome(I32_MAX))  # 2147483647

    def test_i32_min_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome(I32_MIN))  # -2147483648, negation also overflows

    def test_largest_palindrome_within_i32(self):
        self.assertTrue(is_palindrome(2_147_447_412))

    def test_reversal_of_input_overflows_i32(self):
        # 1534236469 reversed is 9646324351, which exceeds i32::MAX.
        self.assertFalse(is_palindrome(1_534_236_469))


if __name__ == "__main__":
    unittest.main()
