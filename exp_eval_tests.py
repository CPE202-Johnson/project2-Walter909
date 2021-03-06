# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 4 e')

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 4 + 2 / +')

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 4 + 2')

    def test_postfix_eval_simple(self):
        self.assertEqual(postfix_eval("3 5 +"), 8)
        self.assertEqual(postfix_eval("3 2 -"), 1)
        self.assertEqual(postfix_eval("3 5 *"), 15)
        self.assertEqual(postfix_eval("3 1 /"), 3.0)
        self.assertEqual(postfix_eval("3 2 **"), 9)
        self.assertEqual(postfix_eval('2 1 <<'), 4)
        self.assertEqual(postfix_eval('2 1 >>'), 1)
        self.assertEqual(postfix_eval(''), '')

    def test_postfix_eval_simple_negative(self):
        self.assertEqual(postfix_eval("-3 5 +"), 2)
        self.assertEqual(postfix_eval("-3 2 -"), -5)
        self.assertEqual(postfix_eval("-3 5 *"), -15)
        self.assertEqual(postfix_eval("-3 1 /"), -3.0)
        self.assertEqual(postfix_eval("-3 3 **"), -27)
        self.assertEqual(postfix_eval('-2 1 <<'), -4)
        self.assertEqual(postfix_eval('-2 1 >>'), -1)

    def test_postfix_eval_floats(self):
        self.assertEqual(postfix_eval("3.0 5.0 +"), 8.0)
        self.assertEqual(postfix_eval("3.0 2.0 -"), 1.0)
        self.assertEqual(postfix_eval("3.0 5.0 *"), 15.0)
        self.assertEqual(postfix_eval("3.0 2.0 **"), 9.0)
        self.assertEqual(postfix_eval("3.0 1.0 /"), 3.0)


    def test_postfix_eval__negative_floats(self):
        self.assertEqual(postfix_eval("-3.0 5.0 +"), 2.0)
        self.assertEqual(postfix_eval("-3.0 2.0 -"), -5.0)
        self.assertEqual(postfix_eval("3.0 -5.0 *"), -15.0)
        self.assertEqual(postfix_eval("-3.0 3.0 **"), -27.0)
        self.assertEqual(postfix_eval("3.0 -1.0 /"), -3.0)

    def test_postfix_eval_invalid_bitshift(self):
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 1.0 <<')
        with self.assertRaises(PostfixFormatException):
            postfix_eval('3 1.0 >>')

    def test_postfix_eval_divide_by_zero(self):
        with self.assertRaises(ValueError):
            postfix_eval('3 0 /')
        with self.assertRaises(ValueError):
            postfix_eval('3 3 - 0 /')

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix('+ << 3 4 >> 5 6'), '3 4 << 5 6 >> +')
        self.assertEqual(prefix_to_postfix('** -1 2'), '-1 2 **')
        self.assertEqual(prefix_to_postfix(''), '')

    def test_loop_break(self):
        with self.assertRaises(IndexError):
            prefix_to_postfix('e')

if __name__ == "__main__":
    unittest.main()
