from Visitor import Visitor
from StaticError import *
from AST import *

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    def visitIntegerType(self, ast: IntegerType, o): 
        return IntegerType()
    
    def visitFloatType(self, ast: FloatType, o):
        return FloatType()

    def visitStringType(self, ast: StringType, o):
        return StringType()

    def visitBooleanType(self, ast: BooleanType, o):
        return BooleanType()

    def visitArrayType(self, ast, o):
        pass

    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()
    
    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    # explist: List[Expr]
    def visitArrayLit(self, ast: ArrayLit, o):
        
        for expr in ast.explist:
            exp_type =  self.visit()

    def visitAutoType(self, ast, o):
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()

    # BinExpr: #op: str, #left: Expr, #right: Expr
    def visitBinExpr(self, ast: BinExpr, o):
        right_typ = self.visit(ast.right)
        left_typ = self.visit(ast.left)
        op = ast.op

        if op in ["+", "-", "*", "/"]:
            # if type(right_typ) is :


    def visitUnExpr(self, ast, o): pass
    def visitId(self, ast, o): pass
    def visitArrayCell(self, ast, o): pass
    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast, o): pass
    def visitBlockStmt(self, ast, o): pass
    def visitIfStmt(self, ast, o): pass
    def visitForStmt(self, ast, o): pass
    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass

    def _check_typeMismatch(var_type, init_type):
        if type(var_type) is FloatType and type(init_type) is IntegerType:
            return True
        elif type(var_type) is not type(init_type): 
            return False
        return True

    ### VarDecl # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        # check duplicated name___________
        if ast.name in o[0]:
            print("visitVarDecl scope: ", o[0])
            raise Redeclared(Variable(), ast.name)

        # checkType is Void_______________
        if type(ast.typ) is VoidType:
            raise TypeMismatchInVarDecl(ast)                    
             
        # checkType Mismatch______________
        if ast.init is not None:
            init_typ = self.visit(ast.init, o) # Type()
            if not StaticChecker._check_typeMismatch(ast.typ, init_typ):
                raise TypeMismatchInVarDecl(ast)                    

        o[0][ast.name] = ast.typ


    ### ParamDecl # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        pass 

    ### Func # name: str, return_type: Type, params: List[oDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o): pass

    ### Program # decla: List[Decl]
    def visitProgram(self, ast: Program, o):
        o = [{}]
        for decl in ast.decls:
            self.visit(decl, o)
        return []

