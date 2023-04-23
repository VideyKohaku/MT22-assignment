import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    """Test program"""
    def test_program_1(self):
        input=""""""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_program_2(self):
        input="""foo: function void()
        {
            
        }
        """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_program_3(self):
        input="""a:integer;"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_program_4(self):
        input="""a: float;
                 foo: function void() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_program_5(self):
        input="""a: float;
                 main: function integer() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,405))

    """Test variable declaration"""

    def test_vardecl_1(self):
        input="""
            a: float;
            b: integer;
            a: string;
            """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl_2(self):
        input="""
            c: string;
            d: string;
            a: string = c::d;
            e: boolean = 2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(e, BooleanType, IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl_3(self):
        input="""
            a: auto;
            """
        expect="Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_vardecl_4(self):
        input="""
            a: integer = 1.2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_vardecl_5(self):
        input="""
            a: float = 2;
            b: integer = 2;
            b: string;
            """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_vardecl_6(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = a + b;
            d: integer = c;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_vardecl_7(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b};
            d: array [2] of float = {"a","b"};
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], FloatType), ArrayLit([StringLit(a), StringLit(b)]))"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_vardecl_8(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b,"d"};
            """
        expect="Illegal array literal: ArrayLit([Id(a), Id(b), StringLit(d)])"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_vardecl_9(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {{a,b},{a,b}};
            d: array [2] of integer = c[0];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], IntegerType), ArrayCell(c, [IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_vardecl_10(self):
        input="""
            a: integer;
            b: array [2,2] of float;
            c: auto = b[2];
            d: integer = c[1];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, ArrayCell(c, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_vardecl_11(self):
        input="""
            a: integer;
            b: array [2,2] of float;
            c: auto = b[2];
            d: integer = c[1];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, ArrayCell(c, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,416))

    """Test function declaration"""
    # def test_funcdecl_1(self):
    #     input="""
    #         a: function integer(b: integer, c:integer) inherit d {}
    #         main: function void()
    #         {
            
    #         }
    #         """
    #     expect="Undeclared Function: d"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_funcdecl_2(self):
    #     input="""
    #         a: integer;
    #         a: function integer(b: integer, c:integer){}
    #         main: function void()
    #         {
            
    #         }
    #         """
    #     expect="Redeclared Function: a"
    #     self.assertTrue(TestChecker.test(input,expect,417))
    
    # def test_funcdecl_3(self):
    #     input="""
    #         a: integer;
    #         b: function integer(c: integer, d:integer) inherit a{}
    #         main: function void()
    #         {
            
    #         }
    #         """
    #     expect="Undeclared Function: a"
    #     self.assertTrue(TestChecker.test(input,expect,418))
    
    # def test_funcdecl_4(self):
    #     input="""
    #         bar : function void (out n : integer, a:float) inherit foo{}
    #         foo : function auto (inherit n: float, n: integer){} 
    #         """
    #     expect="Redeclared Parameter: n"
    #     self.assertTrue(TestChecker.test(input,expect,419))

    # def test_funcdecl_5(self):
    #     input="""
    #         bar : function void (out n : integer, a:float) inherit foo{} 
    #         foo : function auto (inherit n: float){} 
    #         """
    #     expect="Invalid Parameter: n"
    #     self.assertTrue(TestChecker.test(input,expect,420))


    # def test_funcdecl_6(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{} 
    #         foo : function auto (inherit n: float){} 
    #         """
    #     expect="Invalid statement in function: bar"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_funcdecl_7(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{} 
    #         foo : function auto (){} 
    #         """
    #     expect="No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_funcdecl_8(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             super();
    #         } 
    #         foo : function auto (){} 
    #         """
    #     expect="No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_funcdecl_9(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             super();
    #         } 
    #         foo : function auto (){} 
    #         """
    #     expect="No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test_funcdecl_10(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             preventDefault();
    #         } 
    #         foo : function auto (){} 
    #         """
    #     expect="No entry point"
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test_funcdecl_11(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             preventDefault(a);
    #         } 
    #         foo : function auto (){} 
    #         """
    #     expect="Type mismatch in statement: CallStmt(preventDefault, Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,426))

    # def test_funcdecl_12(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             super(a);
    #         } 
    #         foo : function auto (){} 
    #         """
    #     expect="Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test_funcdecl_13(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             super(a,a);
    #         } 
    #         foo : function auto (a: float, b: integer){} 
    #         """
    #     expect="Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_funcdecl_14(self):
    #     input="""
    #         bar : function void (a:float) inherit foo{
    #             super(a,a,a);
    #         } 
    #         foo : function auto (a: float, b: integer){} 
    #         """
    #     expect="Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test_funcdecl_15(self):
    #     input="""
    #         foo: function integer (a: integer, b: auto) inherit bar 
    #         {
    #             preventDefault();
    #             if (a==1)
    #             {
    #                 b: integer;
    #                 b = 1 + foo(1,2);
    #                 foo(1,2)
    #             }
    #             b=1.3;
    #         }

    #         """
    #     expect="Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test_funcdecl_16(self):
    #     input="""
    #         bar: integer;
    #         foo: function integer (a: integer, b: auto) inherit bar 
    #         {
    #             preventDefault();
    #             if (a==1)
    #             {
    #                 b: integer;
    #             }
    #         }
    #         bar: function integer(inherit c: integer)
    #         {
            
    #         }
    #         """
    #     expect="Redeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input,expect,431))

    # def test_funcdecl_17(self):
    #     input="""
    #         bar: integer;
    #         foo: function integer (a: integer, b: auto) inherit bar 
    #         {
    #             preventDefault();
    #             if (a==1)
    #             {
    #                 b: integer;
    #             }
    #         }
    #         """
    #     expect="Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input,expect,432))

    # def test_funcdecl_18(self):
    #     input="""
    #         foo: function integer (a: integer, b: auto)
    #         {
    #             preventDefault();
    #             if (a==1)
    #             {
    #                 b: integer;
    #             }
    #         }
    #         """
    #     expect="Invalid statement in function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,433))

    # def test_funcdecl_19(self):
    #     input="""
    #         foo: function integer (a: integer, b: auto)
    #         {
    #             super();
    #             if (a==1)
    #             {
    #                 b: integer;
    #             }
    #         }
    #         """
    #     expect="Invalid statement in function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # def test_funcdecl_20(self):
    #     input="""
    #         bar: function integer(n: integer, n: integer) {}
    #         foo: function integer (a: integer, b: auto) inherit bar
    #         {
    #             super(1,2);
    #         }
    #         """
    #     expect="Redeclared Parameter: n"
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # """Test statement"""
    # def test_stmt_1(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             if (b==1)
    #             {
                
    #             }
    #             else
    #             {
    #                 if (a<2.0)
    #                 {
                    
    #                 }
    #             }
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,436))
    
    # def test_stmt_2(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             if (a==1)
    #             {
                
    #             }
    #             else
    #             {
    #                 if (a<2.0)
    #                 {
                    
    #                 }
    #             }
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def test_stmt_3(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             if ((a==1) && (b=="a"))
    #             {
                
    #             }
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def test_stmt_4(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             if ((b<2.0) && (b==a))
    #             {
                
    #             }
    #             else
    #             {
    #                 if (b==1)
    #                 {
                    
    #                 }
    #             }
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(==, Id(b), Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,439))

    # def test_stmt_5(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             if ((1!=true) && (b==a))
    #             {
                
    #             }
    #             else
    #             {
    #                 if (b<2)
    #                 {
                    
    #                 }
    #             }
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(b), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,440))
    
    # def test_stmt_6(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             b = 1 + a;
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,441))
    
    # def test_stmt_7(self):
    #     input="""
    #         foo: function integer (a: boolean, b: auto)
    #         {
    #             b = a;
    #             a = b + 1;
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,442))

    # def test_stmt_8(self):
    #     input="""
    #         foo: function integer (a: integer, b: auto)
    #         {
    #             b = "1"::a;
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
    #     self.assertTrue(TestChecker.test(input,expect,443))
        
    # def test_stmt_9(self):
    #     input="""
    #         foo: function integer (a: string, b: auto)
    #         {
    #             b = a + "1";
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(==, Id(b), Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def test_stmt_10(self):
    #     input="""
    #         foo: function integer (a: auto, b: auto)
    #         {
    #             c: integer = a;
    #             b = a + 1.0;
    #             printInteger(a);
    #         }
    #         """
    #     expect="Type mismatch in expression: BinExpr(<, Id(b), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,445))
