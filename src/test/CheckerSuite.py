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
        c: auto = 1;
        d: auto = true;
        a: integer = c + d;
        a: float = 1.0;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))