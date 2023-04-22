import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_simple_decl_401(self):
    #     input = """
    #     a: integer = 1;
    #     a: float = 1.0;"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_simple_decl_402(self):
    #     input = """
    #     d: auto = 2.0;
    #     a: integer = c + d;
    #     a: float = 1.0;"""
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_simple_decl_403(self):
    #     input = """
    #     c: auto = 1.0;
    #     d: auto = true;
        
    #     a: integer = c + d;
        
    #     main: function void(){}
    #     b: float = 1.0;"""
    #     expect = "Type mismatch in expression: BinExpr(+, Id(c), Id(d))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_simple_decl_404(self):
    #     input = """
    #     c: auto;
    #     d: auto = true;
    #     a: integer = c + d;
    #     a: float = 1.0;"""
    #     expect = "Invalid Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_simple_decl_405(self):
    #     input = """
    #     a: auto = a + 1;
    #     f: string = a;
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(f, StringType, Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    def test_simple_decl_406(self):
        input = """
        main: function auto(){}
        a: function auto(anArg: auto){}
        b: boolean = true;
        arr: array [4] of float = {{1,2,3}, {2,a, main}};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(f, StringType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_simple_decl_407(self):
    #     input = """
    #     foo: function auto(a: integer, b: auto){
        
    #     }
    #     main: function void(){}
    #     goo: function integer(inherit c: float, d: boolean) inherit boo{}
    #     """
    #     expect = "Undeclared"
    #     self.assertTrue(TestChecker.test(input, expect, 407))