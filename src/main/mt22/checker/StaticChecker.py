from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
from typing import List, Tuple


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.loop_stack = []
        self.array_dimension_stack = []

    def check(self):
        return self.visit(self.ast, [])
    
    def _inferType(env, name, typ): 
        for scope in env:
            if name in scope and type(scope[name]) is FuncDecl:
                # new_funcDecl = scope[name]
                # new_funcDecl.return_typ
                scope[name].return_type = typ
                return typ
            elif name in scope:
                scope[name] = typ
                return typ
    
    def _add_loop_stack(self):
        self.loop_stack += [1]

    def _pop_loop_stack(self):
        stack_len = len(self.loop_stack)
        self.loop_stack = self.loop_stack[:stack_len - 1]

    def visitIntegerType(self, ast: IntegerType, o): 
        return IntegerType()
    
    def visitFloatType(self, ast: FloatType, o):
        return FloatType()

    def visitStringType(self, ast: StringType, o):
        return StringType()

    def visitBooleanType(self, ast: BooleanType, o):
        return BooleanType()

    # dimensions: List[int], typ: atomicType
    def visitArrayType(self, ast: ArrayType, o):
        return ArrayType(ast.dimensions, ast.typ)

    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()
    
    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    # explist: List[Expr]
    # env
    def visitArrayLit(self, ast: ArrayLit, o): 
        if (not len(ast.explist)):
            return None

        ### GET TYPE
        exp_list = ast.explist
        exp_typ_list = list(map(lambda exp: self.visit(exp, o), exp_list))
        print("exp typ list:\n", exp_typ_list)

        ## Check if it has array type in list
        


        common_typ_list = {type(exp_typ) if type(exp_typ) is not FuncDecl else type(exp_typ.return_type)  for exp_typ in exp_typ_list}
        # print("common_types: ", common_typ_list)
        common_typ = None

        # 1 - Dimension Array: Auto - Int - Float
        if len(common_typ_list) > 3:
            raise IllegalArrayLiteral(ast)
        elif len(common_typ_list) == 3:
            common_typ = FloatType
        elif len(common_typ_list) == 2:
            if AutoType in common_typ_list:
                common_typ_list.remove(AutoType)
                common_typ_it = iter(common_typ_list)
                common_typ= next(common_typ_it)
                # print(common_typ)

                # => Infer all the AutoType in the exp_list
                # print("o before infer: \n", o)
                for exp in exp_typ_list:
                    if type(exp) is FuncDecl and type(exp.return_type) is AutoType:
                        StaticChecker._inferType(o, exp.name, common_typ())
                # print("o after infer: \n", o)

            elif FloatType in common_typ_list and IntegerType in common_typ_list:
                common_typ = FloatType
            else:
                raise IllegalArrayLiteral(ast)
        else:
            common_typ_it = iter(common_typ_list)
            common_typ = next(common_typ_it)

        print("common_type: ", common_typ)

        ### GET DIMENSION
        dimensions = Utils.getArrayDimensions(ast)
        print("dimension:\n", dimensions)        

        return ArrayType(dimensions, common_typ)


    def visitAutoType(self, ast, o):
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()

    # BinExpr: #op: str, #left: Expr, #right: Expr
    def visitBinExpr(self, ast: BinExpr, o): 
        left_typ = self.visit(ast.left, o)
        right_typ = self.visit(ast.right, o)
        op = ast.op
        # print("left_typ: ", type(left_typ))
        # print("right_typ: ", type(right_typ))

        if op in ["+", "-", "*", "/"]: #IntType() or FloatType()
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return IntegerType()
            if type(left_typ) is FloatType and type(right_typ) in [FloatType, IntegerType]:
                return FloatType()
            if type(right_typ) is FloatType and type(left_typ) in [FloatType, IntegerType]:
                return FloatType()
            if type(left_typ) is AutoType and type(right_typ) in [FloatType, IntegerType]:
                StaticChecker._inferType(o, ast.left.name, right_typ) 
                return right_typ
            if type(right_typ) is AutoType and type(left_typ) in [FloatType, IntegerType]:
                StaticChecker._inferType(o, ast.right.name, left_typ)
                return left_typ
            raise TypeMismatchInExpression(ast)
        
        if op in ["%"]:
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return IntegerType()
            if type(left_typ) is AutoType and type(right_typ) is IntegerType:
                StaticChecker._inferType(o, ast.left.name, right_typ)
                return IntegerType()
            if type(right_typ) is AutoType and type(left_typ) is IntegerType:
                StaticChecker._inferType(o, ast.right.name, left_typ)
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["&&", "||"]:
            if type(left_typ) is BooleanType and type(right_typ) is BooleanType:
                return BooleanType()
            if type(left_typ) is AutoType and type(right_typ) is BooleanType:
                StaticChecker._inferType(o, ast.left.name, right_typ)
                return BooleanType()
            if type(right_typ) is AutoType and type(left_typ) is BooleanType:
                StaticChecker._inferType(o, ast.right.name, left_typ)
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["::"]:
            if type(left_typ) is StringType and type(right_typ) is StringType:
                return StringType()
            if type(left_typ) is AutoType and type(right_typ) is StringType:
                StaticChecker._inferType(o, ast.left.name, right_typ)
                return StringType()
            if type(right_typ) is AutoType and type(left_typ) is StringType:
                StaticChecker._inferType(o, ast.right.name, left_typ)
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ["==", "!="]:
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return BooleanType
            if type(left_typ) is BooleanType and type(right_typ) in [BooleanType, IntegerType]:
                return BooleanType()
            if type(right_typ) is BooleanType and type(left_typ) in [BooleanType, IntegerType]:
                return BooleanType()
            if type(left_typ) is AutoType and type(right_typ) in [BooleanType, IntegerType]:
                StaticChecker._inferType(o, ast.left.name, right_typ)
                return BooleanType()
            if type(right_typ) is AutoType and type(left_typ) in [BooleanType, IntegerType]:
                StaticChecker._inferType(o, ast.right.name, left_typ)
                return BooleanType()
            raise TypeMismatchInExpression(ast)

    
        if op in ["<", ">", "<=", ">="]:
            if type(left_typ) is IntegerType and type(right_typ) is IntegerType:
                return BooleanType
            if type(left_typ) is FloatType and type(right_typ) in [FloatType, IntegerType]:
                return BooleanType()
            if type(right_typ) is FloatType and type(left_typ) in [FloatType, IntegerType]:
                return BooleanType()
            if type(left_typ) is AutoType and type(right_typ) in [FloatType, IntegerType]:
                StaticChecker._inferType(o, ast.left.name, right_typ)
                return BooleanType()
            if type(right_typ) is AutoType and type(left_typ) in [FloatType, IntegerType]:
                StaticChecker._inferType(o, ast.right.name, left_typ)
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
            if type(val_typ) is AutoType:
                StaticChecker._inferType(o, ast.val.name, BooleanType())
                return BooleanType()
            raise TypeMismatchInExpression(ast)
                
    # name: str
    def visitId(self, ast: Id, o): 
        for scope in o:
            if ast.name in scope:
                return scope[ast.name]
            
        raise Undeclared( Identifier(), ast.name)

    def visitArrayCell(self, ast, o): pass

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        funcDecl = Utils.getFuncDecl(o)
        return funcDecl.return_typ
        # infer params for proto

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, o): 
        rhs_typ = self.visit(ast.rhs, o)
        lhs_typ = self.visit(ast.lhs, o)

        # in var: AutoType() already infered in decl
        if type(lhs_typ) is FloatType and type(rhs_typ) in [IntegerType, FloatType]:
            return FloatType()
        if type(rhs_typ) is not type(lhs_typ):
            raise TypeMismatchInStatement(ast)
        
        return rhs_typ

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o):
        env = [{}] + o

        for body_line in ast.body:
            self.visit(body_line, env)


    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast: IfStmt, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.tstmt)

        if type(ast.fstmt) is not None:
            self.visit(ast.fstmt)

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast: ForStmt, o):
        StaticChecker._add_loop_stack()

        init_typ = self.visit(ast.init, o)
        if type(init_typ) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        cond_typ = self.visit(ast.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        upd_typ = self.visit(ast.upd, o)
        if type(upd_typ) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, o)

        StaticChecker._pop_loop_stack()

    #cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, o):
        StaticChecker._add_loop_stack()

        cond_typ = self.visit(ast.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.stmt, o)

        StaticChecker._pop_loop_stack()


    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        StaticChecker._add_loop_stack()

        self.visit(ast.stmt, o)

        cond_typ = self.visit(ast.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        StaticChecker._pop_loop_stack()

    def visitBreakStmt(self, ast: BreakStmt, o):
        if len(self.loop_stack) in [0]:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        if len(self.loop_stack) in [0]:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast, o): pass

    # name: str, args: [Expr]    
    def visitCallStmt(self, ast: CallStmt, o):
        funcDecl = Utils.getFuncDecl(o, ast.name)
        return funcDecl.return_type
        # TypeMismatch 


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
            raise Redeclared(Variable(), ast.name)                 
        
        o[0][ast.name] = ast.typ
             
        # checkType Mismatch______________
        if ast.init is not None:
            init_typ = self.visit(ast.init, o) # Type()
            # print(ast.name,": ",type(ast.typ) is AutoType)
            if type(ast.typ) is AutoType:
                StaticChecker._inferType(o, ast.name, init_typ)
                ast.typ = init_typ
            elif not StaticChecker._check_Float_Int_coersion(ast.typ, init_typ):
                raise TypeMismatchInVarDecl(ast)      
        elif type(ast.typ) is AutoType:
            raise Invalid(Variable(), ast.name)


    ### ParamDecl # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        pass 

    ### Func # name: str, return_type: Type, params: List[oDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        pass

    ### Program # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        firstchecker = GlobalFunctionChecker(self.ast)
        o = firstchecker.check()
        # Utils.printEnvironment(o)
        # print("ast: ",o)

        for decl in ast.decls:
            self.visit(decl, o)
        return o





##########################################################################
#_______________________FIRST CHECK______________________________________
##########################################################################
class GlobalFunctionChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        return self.visit(self.ast, [])

    def visitIntegerType(self, ast, param): pass
    def visitFloatType(self, ast, param): pass
    def visitBooleanType(self, ast, param): pass
    def visitStringType(self, ast, param): pass
    def visitArrayType(self, ast, param): pass
    def visitAutoType(self, ast, param): pass
    def visitVoidType(self, ast, param): pass


# ______________EXPR_____________________________
    def visitBinExpr(self, ast, param): pass
    def visitUnExpr(self, ast, param): pass
    def visitId(self, ast, param): pass
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): pass
    def visitFloatLit(self, ast, param): pass
    def visitStringLit(self, ast, param): pass
    def visitBooleanLit(self, ast, param): pass
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass

# ______________STATEMENT_____________________________
    def visitAssignStmt(self, ast, param): pass
    def visitBlockStmt(self, ast, param): pass
    def visitIfStmt(self, ast, param): pass
    def visitForStmt(self, ast, param): pass
    def visitWhileStmt(self, ast, param): pass
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, param): pass
    def visitCallStmt(self, ast, param): pass

# ______________DECLARATION_____________________________
    def visitVarDecl(self, ast, param): pass

    # 
    def visitParamDecl(self, ast: ParamDecl, o): pass 

    # name: str, return_type: Type, param: List[ParamDecl], inherit: str or None, body: BlockStatement
    def visitFuncDecl(self, ast: FuncDecl, o): 
        o[0][ast.name] = ast


    def visitProgram(self, ast: Program, o):
        o = [{
            "readInteger": FuncDecl("readInteger", IntegerType(),[],None, BlockStmt([])),
            "printInteger": FuncDecl("printInteger", VoidType(), [ParamDecl("anArg",IntegerType(),False)], None, BlockStmt([])),
            "readFloat": FuncDecl("readFloat", FloatType(), [], None, BlockStmt([])),
            "writeFloat": FuncDecl("writeFloat", VoidType(), [ParamDecl("anArg", FloatType(),False)], None, BlockStmt([])),
            "readBoolean": FuncDecl("readBoolean", BooleanType(), [], None, BlockStmt([])),
            "printBoolean": FuncDecl("printBoolean", VoidType(), [ParamDecl("anArg", BooleanType(),False)], None, BlockStmt([])),
            "readString": FuncDecl("readString", BooleanType(), [], None, BlockStmt([])),
            "printString": FuncDecl("printString", VoidType(), [ParamDecl("anArg", StringType(),False)], None, BlockStmt([])),
            "preventDefault": FuncDecl("preventDefault", VoidType(), [], None, BlockStmt([]))
        }]

        for decl in ast.decls:
            self.visit(decl, o)
        return o
    


#_______________________Utils_________________________________
class Utils:
    def printEnvironment(env):
        print("env list start__")
        for scope in env:
            for decl in scope:
                print(decl, ": " ,scope[decl])
        print("env list end__")

    def getFuncDecl(env, name):
        for scope in env:
            if name in scope and type(env[name]) is FuncDecl:
                return env[name]
            if name in scope and type(env[name]) is not FuncDecl:
                raise Invalid(Function(), name)
        raise Undeclared(Function(), name)


    def getArrayDimensions(ast):
        if type(ast) is not ArrayLit:
            return []
        
        # print("0:\n",ast.explist[0])
        first_exp_dims = Utils.getArrayDimensions(ast.explist[0])
        for exp in ast.explist[1:]:
            if Utils.getArrayDimensions(exp) != first_exp_dims:
                raise IllegalArrayLiteral(ast)
        
        dimensions = [len(ast.explist)] + first_exp_dims
        # print("utils:\n", dimensions)
        return dimensions