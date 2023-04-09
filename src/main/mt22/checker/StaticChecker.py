from Visitor import Visitor


class StaticChecker(Visitor):
    def visitIntegerType(self, ctx, param): pass
    def visitFloatType(self, ctx, param): pass
    def visitBooleanType(self, ctx, param): pass
    def visitStringType(self, ctx, param): pass
    def visitArrayType(self, ctx, param): pass
    def visitAutoType(self, ctx, param): pass
    def visitVoidType(self, ctx, param): pass

    def visitBinExpr(self, ctx, param): pass
    def visitUnExpr(self, ctx, param): pass
    def visitId(self, ctx, param): pass
    def visitArrayCell(self, ctx, param): pass
    def visitIntegerLit(self, ctx, param): pass
    def visitFloatLit(self, ctx, param): pass
    def visitStringLit(self, ctx, param): pass
    def visitBooleanLit(self, ctx, param): pass
    def visitArrayLit(self, ctx, param): pass
    def visitFuncCall(self, ctx, param): pass

    def visitAssignStmt(self, ctx, param): pass
    def visitBlockStmt(self, ctx, param): pass
    def visitIfStmt(self, ctx, param): pass
    def visitForStmt(self, ctx, param): pass
    def visitWhileStmt(self, ctx, param): pass
    def visitDoWhileStmt(self, ctx, param): pass
    def visitBreakStmt(self, ctx, param): pass
    def visitContinueStmt(self, ctx, param): pass
    def visitReturnStmt(self, ctx, param): pass
    def visitCallStmt(self, ctx, param): pass

    ### VarDecl # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, param): pass

    ### ParamDecl # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx, param): pass

    ### Func # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, param): pass

    ### Program # decl: List[Decl]
    def visitProgram(self, ctx: Program, o): pass
