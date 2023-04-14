from Visitor import Visitor
from StaticError import *
from AST import *

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])
    
    def _inferType(env, name, typ): 
        for scope in env:
            if name in scope:
                scope[name] = typ
                return typ

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
        right_typ = self.visit(ast.right, o)
        left_typ = self.visit(ast.left, o)
        op = ast.op

        if op in ["+", "-", "*", "/"]: #IntType() or FloatType()
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return IntegerType()
            elif type(left_typ) is FloatType:
                if type(right_typ) is not IntegerType and type(right_typ) is not FloatType:
                    raise TypeMismatchInExpression(ast)
                return FloatType()
            elif type(right_typ) is FloatType:
                if type(left_typ) is not IntegerType and type(left_typ) is not FloatType:
                    raise TypeMismatchInExpression(ast)
                return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["%"]:
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["&&", "||"]:
            if type(left_typ) is BooleanType and type(right_typ) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["::"]:
            if type(left_typ) is StringType and type(right_typ) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["==", "!="]:
            # bool == bool / bool == int
            if type(left_typ) is BooleanType:
                if type(right_typ) is IntegerType or type(right_typ) is BooleanType:
                    return BooleanType()
                raise TypeMismatchInExpression(ast)

            # bool == bool / int == bool
            if type(right_typ) is BooleanType:
                if type(left_typ) is IntegerType or type(left_typ) is BooleanType:
                    return BooleanType()                
                raise TypeMismatchInExpression(ast)
            
            # int == int
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return BooleanType()

            raise TypeMismatchInExpression(ast)
    
        if op in ["<", ">", "<=", ">="]:
            # int > int / int > float
            if type(left_typ) is IntegerType:
                if type(right_typ) is IntegerType or type(right_typ) is FloatType:
                    return BooleanType()
                raise TypeMismatchInExpression(ast)
            
            # int < int / float < int
            if type(right_typ) is IntegerType:
                if type(left_typ) is IntegerType or type(left_typ) is FloatType:
                    return BooleanType()
                raise TypeMismatchInExpression(ast)
            
            # float < float
            if type(left_typ) is FloatType and type(right_typ) is FloatType:
                return BooleanType()
            
            raise TypeMismatchInExpression(ast)

    # op: str,  val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        val_typ = self.visit(ast.val, o) #Type()
        op = ast.op

        if op in ["-"]:
            if type(val_typ) is IntegerType:
                return IntegerType
            if type(val_typ) is FloatType:
                return FloatType
            raise TypeMismatchInExpression(ast)
        
        if op in ["!"]:
            if type(val_typ) is BooleanType:
                return BooleanType
            raise TypeMismatchInExpression(ast)
                

    def visitId(self, ast: Id, o): 
        pass

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

    def _check_Float_Int_coersion(var_type, init_type):
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
            # print(ast.name,": ",type(ast.typ) is AutoType)
            if type(ast.typ) is AutoType:
                print("before: ",ast.name,": ", ast.typ)
                # StaticChecker._inferType(o, ast.name, init_typ)
                ast.typ = init_typ
                print("after: ", ast.name,": ", ast.typ)
            elif not StaticChecker._check_Float_Int_coersion(ast.typ, init_typ):
                raise TypeMismatchInVarDecl(ast)      
        elif type(ast.typ) is AutoType:
            raise Invalid(Variable(), ast.name)

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

