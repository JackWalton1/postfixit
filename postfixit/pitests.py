# Name:         Jack Walton
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021

import unittest

import postfixit

class TestIsOperator(unittest.TestCase):

    def test_is_operator_1(self):
        self.assertTrue(postfixit.is_operator("*"))

    def test_is_operator_2(self):
        self.assertTrue(postfixit.is_operator("+"))

    def test_is_operator_3(self):
        self.assertTrue(postfixit.is_operator("/"))

    def test_is_operator_4(self):
        self.assertTrue(postfixit.is_operator("-"))

    def test_is_operator_5(self):
        self.assertFalse(postfixit.is_operator("4"))



class TestIsNumber(unittest.TestCase):

    def test_is_number_1(self):
        self.assertTrue(postfixit.is_number("-1"))

    def test_is_number_2(self):
        self.assertTrue(postfixit.is_number("4.000"))

    def test_is_number_3(self):
        self.assertTrue(postfixit.is_number("88"))

    def test_is_number_4(self):
        self.assertFalse(postfixit.is_number("-"))

    def test_is_number_5(self):
        self.assertTrue(postfixit.is_number("+1"))


class TestPrec(unittest.TestCase):

    def test_prec_1(self):
        self.assertEqual(postfixit.prec("("), 0)
        val1 = postfixit.prec("(")
        val2 = postfixit.prec(")")
        self.assertTrue(val1 == val2)

    def test_prec_2(self):
        self.assertEqual(postfixit.prec("+"), 1)
        val1 = postfixit.prec("+")
        val2 = postfixit.prec("-")
        self.assertTrue(val1 == val2)

    def test_prec_3(self):
        self.assertEqual(postfixit.prec("*"), 2)
        val1 = postfixit.prec("*")
        val2 = postfixit.prec("/")
        self.assertTrue(val1 == val2)

    def test_prec_4(self):
        self.assertEqual(postfixit.prec("^"), 3)

    def test_prec_5(self):
        self.assertEqual(postfixit.prec("3"), 0)



class TestBuildPostfix(unittest.TestCase):

    def test_build_postfix_1(self):
        infix = "8 / 4 ^ 3"
        postfix = "8 4 3 ^ /"
        self.assertEqual(postfixit.build_postfix(infix), postfix) 

    def test_build_postfix_2(self):
        infix = "( -1 + 2 ) * 3 - ( 4.1 - 5 ) * ( 6 + 7 )"
        postfix = "-1 2 + 3 * 4.1 5 - 6 7 + * -"
        self.assertEqual(postfixit.build_postfix(infix), postfix)

    def test_build_postfix_3(self):
        infix = "( ( ( 1 + 2 ) * 3 ) - ( ( 4 - 5 ) * ( 6 + 7 ) ) )"
        postfix = "1 2 + 3 * 4 5 - 6 7 + * -"
        self.assertEqual(postfixit.build_postfix(infix), postfix)    

    def test_build_postfix_4(self):
        infix = "( ( 1 + 2 ) * 3 ) ^ 2"
        postfix = "1 2 + 3 * 2 ^"
        self.assertEqual(postfixit.build_postfix(infix), postfix)    

    def test_build_postfix_5(self):
        infix = "( ( ( 3 * 6 ) * ( 2 - 4 ) ) + 7 )"
        postfix = "3 6 * 2 4 - * 7 +"
        self.assertEqual(postfixit.build_postfix(infix), postfix)   

 

class TestSolvePostfix(unittest.TestCase):

    def test_solve_postfix_1(self):
        postfix = "8 4 3 ^ /"
        self.assertEqual(postfixit.solve_postfix(postfix), "0.125")

    def test_solve_postfix_2(self):
        postfix = "-1 2 + 3 * 4.1 5 - 6 7 + * -"
        self.assertEqual(postfixit.solve_postfix(postfix), "14.700")    

    def test_solve_postfix_3(self):
        postfix = "3 6 * 2 4 - * 7 +"
        self.assertEqual(postfixit.solve_postfix(postfix), "-29.000")

    def test_solve_postfix_4(self):
        postfix = "1 2 + 3 * 2 ^"
        self.assertEqual(postfixit.solve_postfix(postfix), "81.000")

    def test_solve_postfix_5(self):
        postfix = "1 2 + 5 3 - *"
        self.assertEqual(postfixit.solve_postfix(postfix), "6.000")  



if __name__ == "__main__":
    unittest.main()
 