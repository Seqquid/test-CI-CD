import unittest
from lab1 import Lab


class TestRegisterNewInstructor(unittest.TestCase):

    def setUp(self):
        self.sorter = Lab()


    def test_sorted_list(self):
        self.assertEqual(self.sorter.selection_sort([1, 2, 3]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(self.sorter.selection_sort([3, 1, 2]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(self.sorter.selection_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(self.sorter.selection_sort([5]), [5])

    def test_repeated_elements(self):
        self.assertEqual(self.sorter.selection_sort([5, 2, 5, 1]), [1, 2, 5, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(self.sorter.selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_floats_and_integers(self):
        self.assertEqual(self.sorter.selection_sort([2.5, 1.2, 3, 1.5]), [1.2, 1.5, 2.5, 3])

    def test_identical_elements(self):
        self.assertEqual(self.sorter.selection_sort([3, 3, 3, 3]), [3, 3, 3, 3])

class TestRegisterNewInstructor2(unittest.TestCase):

    def setUp(self):
        self.word = Lab()

    def test_negative_word(self):
        with self.assertRaises(ValueError):
            self.word.is_palindrome("")

    def test_word1(self):
        self.assertTrue(self.word.is_palindrome(" "))

    def  test_word2(self):
        self.assertFalse(self.word.is_palindrome("123"))

    def test_word3(self):
        self.assertTrue(self.word.is_palindrome("131"))

    def test_word4(self):
        self.assertTrue(self.word.is_palindrome("aaaa"))

    def test_word5(self):
        self.assertTrue(self.word.is_palindrome("a"))

class TestRegisterNewInstructor3(unittest.TestCase):

        def setUp(self):
            self.factorial_calculator =Lab()


        def test_factorial_of_zero(self):
            self.assertEqual(self.factorial_calculator.fac(0), 1)

        def test_factorial_of_one(self):
            self.assertEqual(self.factorial_calculator.fac(1), 1)

        def test_factorial_of_two(self):
            self.assertEqual(self.factorial_calculator.fac(2), 2)

        def test_factorial_of_three(self):
            self.assertEqual(self.factorial_calculator.fac(3), 6)

        def test_factorial_of_four(self):
            self.assertEqual(self.factorial_calculator.fac(4), 24)

        def test_factorial_of_five(self):
            self.assertEqual(self.factorial_calculator.fac(5), 120)

        def test_factorial_of_negative(self):
            with self.assertRaises(ValueError):
                self.factorial_calculator.fac(-1)

        def test_large_factorial(self):
            self.assertEqual(self.factorial_calculator.fac(10), 3628800)



class TestFibonacciFunction(unittest.TestCase):

    def setUp(self):
        self.fibonacci_calculator = Lab()

    def test_negative_fib(self):
        with self.assertRaises(ValueError):
            self.fibonacci_calculator.fibonachi(-1)

    def test_negative_fib2(self):
        with self.assertRaises(ValueError):
            self.fibonacci_calculator.fibonachi(0)

    def test_fibonacci_of_one(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(1), 1)

    def test_fibonacci_of_two(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(2), 1)

    def test_fibonacci_of_three(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(3), 2)

    def test_fibonacci_of_four(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(4), 3)

    def test_fibonacci_of_five(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(5), 5)

    def test_fibonacci_of_six(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(6), 8)

    def test_fibonacci_of_seven(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(7), 13)

    def test_fibonacci_of_eight(self):
        self.assertEqual(self.fibonacci_calculator.fibonachi(8), 21)


class TestStringSearchFunction(unittest.TestCase):

    def setUp(self):
        self.string_searcher = Lab()

    def test_substring_present(self):
        self.assertTrue(self.string_searcher.string_search("1", "2123345345"))

    def test_substring_not_present(self):
        self.assertTrue(self.string_searcher.string_search("TEst", "TESTTEst"))

    def test_empty_substring(self):
        self.assertTrue(self.string_searcher.string_search("test", "11test11"))

    def test_full_string_equal(self):
        self.assertTrue(self.string_searcher.string_search("", ""))

    def test_substring_at_end(self):
        self.assertTrue(self.string_searcher.string_search("test", "testtest"))

    def test_substring_at_false(self):
        self.assertFalse(self.string_searcher.string_search("b", "avxccvx"))

class TestSimpleIntFunction(unittest.TestCase):

    def setUp(self):
        self.number_checker = Lab()

    def test_negative(self):
        with self.assertRaises(ValueError):
            self.number_checker.simple_int(0)

    def test_prime_number(self):
        self.assertTrue(self.number_checker.simple_int(5))

    def test_one(self):
        self.assertTrue(self.number_checker.simple_int(3))

    def test_two(self):
        self.assertTrue(self.number_checker.simple_int(-5))

    def test_three(self):
        self.assertTrue(self.number_checker.simple_int(-3))

    def test_large_prime(self):
        self.assertTrue(self.number_checker.simple_int(-29))

    def test_false(self):
        self.assertFalse(self.number_checker.simple_int(20))



class TestReverse32(unittest.TestCase):
    def setUp(self):
        self.utils = Lab()


    def test_zero(self):
        self.assertEqual(self.utils.reverse_32(0), 0)

    def test_large_numbers(self):
        self.assertEqual(self.utils.reverse_32(1534236469), 0)
        self.assertEqual(self.utils.reverse_32(-2147483648), 0)

    def test_numbers_with_trailing_zeros(self):
        self.assertEqual(self.utils.reverse_32(120), 21)
        self.assertEqual(self.utils.reverse_32(-120), -21)


class TestIntegerToRoman(unittest.TestCase):
    def setUp(self):
        self.converter = Lab()

    def test__negative_rim(self):
        with self.assertRaises(ValueError):
            self.converter.integer_to_roman(0)

    def test__negative_rim2(self):
        with self.assertRaises(ValueError):
            self.converter.integer_to_roman(-1)

    def test_single_digits(self):
        self.assertEqual(self.converter.integer_to_roman(1), 'I')
        self.assertEqual(self.converter.integer_to_roman(2), 'II')
        self.assertEqual(self.converter.integer_to_roman(3), 'III')
        self.assertEqual(self.converter.integer_to_roman(4), 'IV')
        self.assertEqual(self.converter.integer_to_roman(5), 'V')
        self.assertEqual(self.converter.integer_to_roman(6), 'VI')
        self.assertEqual(self.converter.integer_to_roman(7), 'VII')
        self.assertEqual(self.converter.integer_to_roman(8), 'VIII')
        self.assertEqual(self.converter.integer_to_roman(9), 'IX')

    def test_tens(self):
        self.assertEqual(self.converter.integer_to_roman(10), 'X')
        self.assertEqual(self.converter.integer_to_roman(20), 'XX')
        self.assertEqual(self.converter.integer_to_roman(30), 'XXX')
        self.assertEqual(self.converter.integer_to_roman(40), 'XL')
        self.assertEqual(self.converter.integer_to_roman(50), 'L')

    def test_hundreds(self):
        self.assertEqual(self.converter.integer_to_roman(100), 'C')
        self.assertEqual(self.converter.integer_to_roman(200), 'CC')
        self.assertEqual(self.converter.integer_to_roman(300), 'CCC')
        self.assertEqual(self.converter.integer_to_roman(400), 'CD')
        self.assertEqual(self.converter.integer_to_roman(500), 'D')

    def test_combined_values(self):
        self.assertEqual(self.converter.integer_to_roman(1994), 'MCMXCIV')
        self.assertEqual(self.converter.integer_to_roman(2023), 'MMXXIII')
        self.assertEqual(self.converter.integer_to_roman(58), 'LVIII')
        self.assertEqual(self.converter.integer_to_roman(49), 'XLIX')

    def test_boundary_values(self):
        self.assertEqual(self.converter.integer_to_roman(3000), 'MMM')
        self.assertEqual(self.converter.integer_to_roman(1), 'I')
        self.assertEqual(self.converter.integer_to_roman(3999), 'MMMCMXCIX')
        self.assertEqual(self.converter.integer_to_roman(4001), 'MMMMI')

# 0, -5, 4001`
