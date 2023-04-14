import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_simple_decl_401(self):
        input = """
        a: integer = 1;
        a: float = 1.0;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_simple_decl_402(self):
        input = """
        d: auto = 2.0;
        a: integer = c + d;
        a: float = 1.0;"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_simple_decl_403(self):
        input = """
        c: auto = 1.0;
        d: auto = true;
        a: integer = c + d;
        a: float = 1.0;"""
        expect = "Type mismatch in expression: BinExpr(+, Id(c), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_simple_decl_404(self):
        input = """
        c: auto;
        d: auto = true;
        a: integer = c + d;
        a: float = 1.0;"""
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_simple_decl_405(self):
        input = """
        main: function void(){
            a: integer;
            for (a = 1, a < 12, a+1){
                b = 2;
            }
            break;
        }
        """
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 405))

