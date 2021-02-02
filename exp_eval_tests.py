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

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

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



if __name__ == "__main__":
    unittest.main()
