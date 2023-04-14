# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#many_decl.
    def visitMany_decl(self, ctx:MT22Parser.Many_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#single_decl.
    def visitSingle_decl(self, ctx:MT22Parser.Single_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_var_decl.
    def visitSub_var_decl(self, ctx:MT22Parser.Sub_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_li.
    def visitId_li(self, ctx:MT22Parser.Id_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_decl.
    def visitParam_decl(self, ctx:MT22Parser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_decl_list.
    def visitParam_decl_list(self, ctx:MT22Parser.Param_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_decl_li.
    def visitParam_decl_li(self, ctx:MT22Parser.Param_decl_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_SM_statement.
    def visitNon_SM_statement(self, ctx:MT22Parser.Non_SM_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sM_statement.
    def visitSM_statement(self, ctx:MT22Parser.SM_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_type.
    def visitStatement_type(self, ctx:MT22Parser.Statement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignStatement.
    def visitAssignStatement(self, ctx:MT22Parser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStatement.
    def visitIfStatement(self, ctx:MT22Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStatement.
    def visitForStatement(self, ctx:MT22Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStatement.
    def visitWhileStatement(self, ctx:MT22Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:MT22Parser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStatement.
    def visitBreakStatement(self, ctx:MT22Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStatement.
    def visitContinueStatement(self, ctx:MT22Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStatement.
    def visitReturnStatement(self, ctx:MT22Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#many_body_line.
    def visitMany_body_line(self, ctx:MT22Parser.Many_body_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#many_body_li.
    def visitMany_body_li(self, ctx:MT22Parser.Many_body_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body_line.
    def visitBody_line(self, ctx:MT22Parser.Body_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_decl_type.
    def visitArray_decl_type(self, ctx:MT22Parser.Array_decl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_dimension.
    def visitArray_dimension(self, ctx:MT22Parser.Array_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_li.
    def visitInt_li(self, ctx:MT22Parser.Int_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrLIT.
    def visitArrLIT(self, ctx:MT22Parser.ArrLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_li.
    def visitExpr_li(self, ctx:MT22Parser.Expr_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_equal_OPERATOR.
    def visitRelational_equal_OPERATOR(self, ctx:MT22Parser.Relational_equal_OPERATORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_OPERATOR.
    def visitRelational_OPERATOR(self, ctx:MT22Parser.Relational_OPERATORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_OPERATOR.
    def visitLogical_OPERATOR(self, ctx:MT22Parser.Logical_OPERATORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_OPERATOR.
    def visitAdding_OPERATOR(self, ctx:MT22Parser.Adding_OPERATORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_OPERATOR.
    def visitMultiplying_OPERATOR(self, ctx:MT22Parser.Multiplying_OPERATORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr1.
    def visitSub_expr1(self, ctx:MT22Parser.Sub_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr2.
    def visitSub_expr2(self, ctx:MT22Parser.Sub_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr3.
    def visitSub_expr3(self, ctx:MT22Parser.Sub_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr4.
    def visitSub_expr4(self, ctx:MT22Parser.Sub_expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr5.
    def visitSub_expr5(self, ctx:MT22Parser.Sub_expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr6.
    def visitSub_expr6(self, ctx:MT22Parser.Sub_expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr7.
    def visitSub_expr7(self, ctx:MT22Parser.Sub_expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument_list.
    def visitArgument_list(self, ctx:MT22Parser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument_li.
    def visitArgument_li(self, ctx:MT22Parser.Argument_liContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_index_expr.
    def visitArray_index_expr(self, ctx:MT22Parser.Array_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_list.
    def visitIndex_list(self, ctx:MT22Parser.Index_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_li.
    def visitIndex_li(self, ctx:MT22Parser.Index_liContext):
        return self.visitChildren(ctx)



del MT22Parser