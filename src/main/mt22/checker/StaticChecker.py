from Visitor import Visitor
from StaticError import *
from AST import *

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.loop_stack = []

    def check(self):
        return self.visit(self.ast, [])
    
    def _inferType(env, name, typ): 
        for scope in env:
            if name in scope:
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

    # dimensions: List[int], typ: atomicTyp
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
        left_typ = self.visit(ast.left, o)
        right_typ = self.visit(ast.right, o)
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
                
    # name: str
    def visitId(self, ast: Id, o): 
        for scope in o:
            if ast.name in scope:
                return scope[ast.name]
            
        raise Undeclared( Identifier(), ast.name)

    def visitArrayCell(self, ast, o): pass
    def visitFuncCall(self, ast, o): pass

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

        cond_typ = self.visit(ast.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt)

        StaticChecker._pop_loop_stack()

    def visitBreakStmt(self, ast: BreakStmt, o):
        if len(self.loop_stack) in [0]:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        if len(self.loop_stack) in [0]:
            raise MustInLoop(ast)

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
            # print("visitVarDecl scope: ", o[0])
            raise Redeclared(Variable(), ast.name)                 
             
        # checkType Mismatch______________
        if ast.init is not None:
            init_typ = self.visit(ast.init, o) # Type()
            # print(ast.name,": ",type(ast.typ) is AutoType)
            if type(ast.typ) is AutoType:
                # StaticChecker._inferType(o, ast.name, init_typ)
                ast.typ = init_typ
            elif not StaticChecker._check_Float_Int_coersion(ast.typ, init_typ):
                raise TypeMismatchInVarDecl(ast)      
        elif type(ast.typ) is AutoType:
            raise Invalid(Variable(), ast.name)

        o[0][ast.name] = ast.typ


    ### ParamDecl # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        pass 

    ### Func # name: str, return_type: Type, params: List[oDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, o):
        pass

    ### Program # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        o = [{}]
        for decl in ast.decls:
            self.visit(decl, o)
        return []

