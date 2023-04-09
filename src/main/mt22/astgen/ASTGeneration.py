from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.many_decl()))

    #______DECLARATION___________________________________________________________
    # Visit a parse tree produced by MT22Parser#many_decl.
    # many_decl: single_decl many_decl | single_decl;
    def visitMany_decl(self, ctx:MT22Parser.Many_declContext):
        if ctx.many_decl():
            return self.visit(ctx.single_decl()) + self.visit(ctx.many_decl())
        else:
            return self.visit(ctx.single_decl())

    # Visit a parse tree produced by MT22Parser#single_decl.
    # single_decl: var_decl | func_decl ; [VarDecl(), VarDecl(), VarDecl(),...] or FuncDecl()
    def visitSingle_decl(self, ctx:MT22Parser.Single_declContext): 
        return self.visit(ctx.var_decl()) if ctx.var_decl() else [self.visit(ctx.func_decl())]


    # Visit a parse tree produced by MT22Parser#var_decl.
    # var_decl: ID sub_var_decl expr SM_COLON | id_list COLONS var_type SM_COLON;
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        if ctx.COLONS():
            idlist = self.visit(ctx.id_list()) # [a,b,c,d]
            return list(map(lambda x: VarDecl(x, self.visit(ctx.var_type()), None), idlist)) 
        else:
            var_val_list = [ctx.ID().getText()] + self.visit(ctx.sub_var_decl()) + [self.visit(ctx.expr())]
            var_list = var_val_list[:int(len(var_val_list)/2)]
            val_list = var_val_list[-int(len(var_val_list)/2):]
            var_type = var_val_list[int(len(var_val_list)/2)]
            return list(map(lambda var,val: VarDecl(var, var_type, val), var_list, val_list))

    # Visit a parse tree produced by MT22Parser#sub_var_decl.
    # sub_var_decl: COMMA ID sub_var_decl expr COMMA| COLONS var_type ASSIGN;
    def visitSub_var_decl(self, ctx:MT22Parser.Sub_var_declContext):
        if ctx.COLONS():
            return [self.visit(ctx.var_type())]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.sub_var_decl()) + [self.visit(ctx.expr())]

    # Visit a parse tree produced by MT22Parser#id_list.
    # id_list: ID id_li;
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return [ctx.ID().getText()] + self.visit(ctx.id_li())

    # Visit a parse tree produced by MT22Parser#id_li.
    # id_li: COMMA ID id_li | ;
    def visitId_li(self, ctx:MT22Parser.Id_liContext):
        if ctx.COMMA():
            return [ctx.ID().getText()] + self.visit(ctx.id_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#param_decl.
    # param_decl: INHERIT? OUT? ID COLONS var_type;
    def visitParam_decl(self, ctx:MT22Parser.Param_declContext):
        if ctx.INHERIT() and ctx.OUT():
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), True, True)
        elif ctx.INHERIT():
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), inherit = True)
        elif ctx.OUT():
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), out = True)
        else:
            return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()))

    # Visit a parse tree produced by MT22Parser#param_decl_list.
    # param_decl_list: param_decl param_decl_li | ; 
    def visitParam_decl_list(self, ctx:MT22Parser.Param_decl_listContext):
        if ctx.param_decl():
            return [self.visit(ctx.param_decl())] + self.visit(ctx.param_decl_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#param_decl_li.
    # param_decl_li: COMMA param_decl param_decl_li | ;
    def visitParam_decl_li(self, ctx:MT22Parser.Param_decl_liContext):
        if ctx.COMMA():
            return [self.visit(ctx.param_decl())] + self.visit(ctx.param_decl_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#func_decl.
    # func_decl: ID COLONS FUNCTION return_type LRB param_decl_list RRB (INHERIT ID)? blockStatement;
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        if ctx.INHERIT():
            return FuncDecl(ctx.getChild(0).getText(), self.visit(ctx.return_type()), self.visit(ctx.param_decl_list()), ctx.ID(1).getText(), self.visit(ctx.blockStatement()))
        else:
            return FuncDecl(ctx.getChild(0).getText(), self.visit(ctx.return_type()), self.visit(ctx.param_decl_list()), None, self.visit(ctx.blockStatement()))

    # Visit a parse tree produced by MT22Parser#statement.
    # statement: non_SM_statement | sM_statement;
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        if ctx.non_SM_statement():
            return self.visit(ctx.non_SM_statement())
        else:
            return self.visit(ctx.sM_statement())

    # Visit a parse tree produced by MT22Parser#non_SM_statement.
    # non_SM_statement: ifStatement
	# 			      | forStatement
	# 			      | whileStatement
	# 			      | blockStatement;
    def visitNon_SM_statement(self, ctx:MT22Parser.Non_SM_statementContext):
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        else:
            return self.visit(ctx.blockStatement())
        
    # Visit a parse tree produced by MT22Parser#sM_statement.
    # sM_statement: statement_type SM_COLON;
    def visitSM_statement(self, ctx:MT22Parser.SM_statementContext):
        return self.visit(ctx.statement_type())

    # Visit a parse tree produced by MT22Parser#statement_type.
    # statement_type: assignStatement 
	# 		  | doWhileStatement 
	# 		  | breakStatement 
	# 		  | continueStatement 
	# 		  | returnStatement
	# 		  | callStatement;
    def visitStatement_type(self, ctx:MT22Parser.Statement_typeContext):
        if ctx.assignStatement():
            return self.visit(ctx.assignStatement())
        elif ctx.doWhileStatement():
            return self.visit(ctx.doWhileStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        else:
            return self.visit(ctx.callStatement())


    # Visit a parse tree produced by MT22Parser#assignStatement.
    # assignStatement: lhs ASSIGN expr;
    def visitAssignStatement(self, ctx:MT22Parser.AssignStatementContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MT22Parser#lhs.
    # lhs: ID | array_index_expr;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.array_index_expr())

    # Visit a parse tree produced by MT22Parser#ifStatement.
    # ifStatement: IF LRB expr RRB (blockStatement | statement) (ELSE (blockStatement | statement))?;
    def visitIfStatement(self, ctx:MT22Parser.IfStatementContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.getChild(4)), self.visit(ctx.getChild(6)))
        else:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.getChild(4)), None)

    # Visit a parse tree produced by MT22Parser#forStatement.
    # forStatement: FOR LRB assignStatement COMMA condition_expr COMMA update_expr RRB (blockStatement|statement);
    def visitForStatement(self, ctx:MT22Parser.ForStatementContext):
        return ForStmt(self.visit(ctx.assignStatement()), self.visit(ctx.condition_expr()), self.visit(ctx.update_expr()), self.visit(ctx.getChild(8)))

    # Visit a parse tree produced by MT22Parser#condition_expr.
    # condition_expr: expr;
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#update_expr.
    # update_expr: expr;
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#whileStatement.
    # whileStatement: WHILE LRB expr RRB (blockStatement|statement);
    def visitWhileStatement(self, ctx:MT22Parser.WhileStatementContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.getChild(4)))

    # Visit a parse tree produced by MT22Parser#doWhileStatement.
    # doWhileStatement: DO blockStatement WHILE LRB expr RRB;
    def visitDoWhileStatement(self, ctx:MT22Parser.DoWhileStatementContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockStatement()))

    # Visit a parse tree produced by MT22Parser#breakStatement.
    # breakStatement: BREAK;
    def visitBreakStatement(self, ctx:MT22Parser.BreakStatementContext):
        return BreakStmt()

    # Visit a parse tree produced by MT22Parser#continueStatement.
    # continueStatement: CONTINUE;
    def visitContinueStatement(self, ctx:MT22Parser.ContinueStatementContext):
        return ContinueStmt()

    # Visit a parse tree produced by MT22Parser#returnStatement.
    # returnStatement: RETURN (expr)?;
    def visitReturnStatement(self, ctx:MT22Parser.ReturnStatementContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt(None)

    # Visit a parse tree produced by MT22Parser#callStatement.
    # callStatement: function_call;
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        funcObj = self.visit(ctx.function_call())
        return CallStmt(funcObj.name, funcObj.args)

    # Visit a parse tree produced by MT22Parser#blockStatement.
    # blockStatement: LCB many_body_line RCB ;
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return BlockStmt(self.visit(ctx.many_body_line()))

    # Visit a parse tree produced by MT22Parser#many_body_line.
    # many_body_line: many_body_li | ;
    def visitMany_body_line(self, ctx:MT22Parser.Many_body_lineContext):
        if ctx.many_body_li():
            return self.visit(ctx.many_body_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#many_body_li.
    # many_body_li: body_line many_body_li | body_line;
    def visitMany_body_li(self, ctx:MT22Parser.Many_body_liContext):
        if isinstance(self.visit(ctx.body_line()),list):
            if ctx.many_body_li():
                return self.visit(ctx.body_line()) + self.visit(ctx.many_body_li())
            else:
                return self.visit(ctx.body_line())
        else:
            if ctx.many_body_li():
                return [self.visit(ctx.body_line())] + self.visit(ctx.many_body_li())
            else:
                return [self.visit(ctx.body_line())]

    # Visit a parse tree produced by MT22Parser#body_line.
    # body_line: statement | var_decl;  Stmt() or [VarDecl() VarDecl(), VarDecl()]
    def visitBody_line(self, ctx:MT22Parser.Body_lineContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        else:
            return self.visit(ctx.var_decl())

    # Visit a parse tree produced by MT22Parser#var_type.
    # var_type: atomic_type | AUTO | array_decl_type | VOID;
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_decl_type())

    # Visit a parse tree produced by MT22Parser#return_type.
    # return_type: atomic_type | VOID | AUTO | array_decl_type;
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_decl_type())

    # Visit a parse tree produced by MT22Parser#atomic_type.
    # atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()

    # Visit a parse tree produced by MT22Parser#array_decl_type.
    # array_decl_type: ARRAY LSB array_dimension RSB OF atomic_type;
    def visitArray_decl_type(self, ctx:MT22Parser.Array_decl_typeContext):
        return ArrayType(self.visit(ctx.array_dimension()), self.visit(ctx.atomic_type()))

    # Visit a parse tree produced by MT22Parser#array_dimension.
    # array_dimension: INTLIT int_li | ;
    def visitArray_dimension(self, ctx:MT22Parser.Array_dimensionContext):
        if ctx.INTLIT():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.int_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#int_li.
    # int_li: COMMA INTLIT int_li | ; 
    def visitInt_li(self, ctx:MT22Parser.Int_liContext):
        if ctx.INTLIT():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.int_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#arrLIT.
    # arrLIT: LCB expr_list RCB;
    def visitArrLIT(self, ctx:MT22Parser.ArrLITContext):
        return ArrayLit(self.visit(ctx.expr_list()))


    # Visit a parse tree produced by MT22Parser#expr_list.
    # expr_list: expr expr_li | ;    
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_li())
        else:
            return [] 


    # Visit a parse tree produced by MT22Parser#expr_li.
    # expr_li: COMMA expr expr_li | ;
    def visitExpr_li(self, ctx:MT22Parser.Expr_liContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_li())
        else:
            return []

    # Visit a parse tree produced by MT22Parser#relational_equal_OPERATOR.
    # relational_equal_OPERATOR: (EQUAL | NEQ);
    def visitRelational_equal_OPERATOR(self, ctx:MT22Parser.Relational_equal_OPERATORContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by MT22Parser#relational_OPERATOR.
    # relational_OPERATOR: ( LWT | GRT | LEQ | GEQ);
    def visitRelational_OPERATOR(self, ctx:MT22Parser.Relational_OPERATORContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by MT22Parser#logical_OPERATOR.
    # logical_OPERATOR: (AND | OR);
    def visitLogical_OPERATOR(self, ctx:MT22Parser.Logical_OPERATORContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MT22Parser#adding_OPERATOR.
    # adding_OPERATOR: (ADD_OP | MIN_OP);
    def visitAdding_OPERATOR(self, ctx:MT22Parser.Adding_OPERATORContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MT22Parser#multiplying_OPERATOR.
    # multiplying_OPERATOR: (MUL_OP | DIV_OP | MOD_OP);
    def visitMultiplying_OPERATOR(self, ctx:MT22Parser.Multiplying_OPERATORContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MT22Parser#expr.
    # expr: sub_expr1 STRING_CONCAT sub_expr1 | sub_expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.STRING_CONCAT():
            return BinExpr(ctx.STRING_CONCAT().getText(), self.visit(ctx.sub_expr1(0)), self.visit(ctx.sub_expr1(1)))
        else:
            return self.visit(ctx.sub_expr1(0))

    # Visit a parse tree produced by MT22Parser#sub_expr1.
    # sub_expr1: sub_expr2 (relational_equal_OPERATOR | relational_OPERATOR) sub_expr2| sub_expr2;
    def visitSub_expr1(self, ctx:MT22Parser.Sub_expr1Context):
        if ctx.relational_equal_OPERATOR():
            return BinExpr(self.visit(ctx.relational_equal_OPERATOR()), self.visit(ctx.sub_expr2(0)), self.visit(ctx.sub_expr2(1)))
        elif ctx.relational_OPERATOR():
            return BinExpr(self.visit(ctx.relational_OPERATOR()), self.visit(ctx.sub_expr2(0)), self.visit(ctx.sub_expr2(1)))
        else:
            return self.visit(ctx.sub_expr2(0))
    
    # Visit a parse tree produced by MT22Parser#sub_expr2.
    # sub_expr2: sub_expr2 logical_OPERATOR sub_expr3 | sub_expr3;
    def visitSub_expr2(self, ctx:MT22Parser.Sub_expr2Context):
        if ctx.logical_OPERATOR():
            return BinExpr(self.visit(ctx.logical_OPERATOR()), self.visit(ctx.sub_expr2()), self.visit(ctx.sub_expr3()))
        else:
            return self.visit(ctx.sub_expr3())

    # Visit a parse tree produced by MT22Parser#sub_expr3.
    # sub_expr3: sub_expr3 adding_OPERATOR sub_expr4 | sub_expr4;
    def visitSub_expr3(self, ctx:MT22Parser.Sub_expr3Context):
        if ctx.adding_OPERATOR():
            return BinExpr(self.visit(ctx.adding_OPERATOR()), self.visit(ctx.sub_expr3()), self.visit(ctx.sub_expr4()))
        else:
            return self.visit(ctx.sub_expr4())

    # Visit a parse tree produced by MT22Parser#sub_expr4.
    # sub_expr4: sub_expr4 multiplying_OPERATOR sub_expr5 | sub_expr5;
    def visitSub_expr4(self, ctx:MT22Parser.Sub_expr4Context):
        if ctx.multiplying_OPERATOR():
            return BinExpr(self.visit(ctx.multiplying_OPERATOR()), self.visit(ctx.sub_expr4()), self.visit(ctx.sub_expr5()))
        else:
            return self.visit(ctx.sub_expr5())

    # Visit a parse tree produced by MT22Parser#sub_expr5.
    # sub_expr5: NOT sub_expr5 | sub_expr6;
    def visitSub_expr5(self, ctx:MT22Parser.Sub_expr5Context):
        if ctx.NOT():
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.sub_expr5()))
        else:
            return self.visit(ctx.sub_expr6())
        
    # Visit a parse tree produced by MT22Parser#sub_expr6.
    # sub_expr6: MIN_OP sub_expr6 | sub_expr7;
    def visitSub_expr6(self, ctx:MT22Parser.Sub_expr6Context):
        if ctx.MIN_OP():
            return UnExpr(ctx.MIN_OP().getText(), self.visit(ctx.sub_expr6()))
        else:
            return self.visit(ctx.sub_expr7())

    # Visit a parse tree produced by MT22Parser#sub_expr7.
    # sub_expr7: operand | function_call | array_index_expr | (LRB expr RRB);
    def visitSub_expr7(self, ctx:MT22Parser.Sub_expr7Context):
        if ctx.operand():
            return self.visit(ctx.operand())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.array_index_expr():
            return self.visit(ctx.array_index_expr())
        elif ctx.expr():
            return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#function_call.
    # function_call: ID LRB argument_list RRB;
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.argument_list()))

    # Visit a parse tree produced by MT22Parser#argument_list.
    # argument_list: expr argument_li |;
    def visitArgument_list(self, ctx:MT22Parser.Argument_listContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.argument_li())
        else:
            return [] 

    # Visit a parse tree produced by MT22Parser#argument_li.
    # argument_li: COMMA expr argument_li | ;
    def visitArgument_li(self, ctx:MT22Parser.Argument_liContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.argument_li())
        else:
            return [] 

    # Visit a parse tree produced by MT22Parser#operand.
    # operand: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrLIT;
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            float_str = ctx.FLOATLIT().getText()
            float_lit = float("0" + float_str) if float_str[0] == "." else float(float_str)
            return FloatLit(float_lit)
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.arrLIT())
        

    # Visit a parse tree produced by MT22Parser#array_index_expr.
    # array_index_expr: ID LSB index_list RSB;
    def visitArray_index_expr(self, ctx:MT22Parser.Array_index_exprContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.index_list()))

    # Visit a parse tree produced by MT22Parser#index_list.
    # index_list: expr index_li;
    def visitIndex_list(self, ctx:MT22Parser.Index_listContext):
        if ctx.index_li():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_li())

    # Visit a parse tree produced by MT22Parser#index_li.
    # index_li: COMMA expr index_li | ;
    def visitIndex_li(self, ctx:MT22Parser.Index_liContext):
        if ctx.expr():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_li())
        else:
            return []