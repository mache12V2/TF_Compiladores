# Generated from JuliaSimplificadaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JuliaSimplificadaParser import JuliaSimplificadaParser
else:
    from JuliaSimplificadaParser import JuliaSimplificadaParser

# This class defines a complete listener for a parse tree produced by JuliaSimplificadaParser.
class JuliaSimplificadaParserListener(ParseTreeListener):

    # Enter a parse tree produced by JuliaSimplificadaParser#program.
    def enterProgram(self, ctx:JuliaSimplificadaParser.ProgramContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#program.
    def exitProgram(self, ctx:JuliaSimplificadaParser.ProgramContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#functionDecl.
    def enterFunctionDecl(self, ctx:JuliaSimplificadaParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#functionDecl.
    def exitFunctionDecl(self, ctx:JuliaSimplificadaParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#parameterList.
    def enterParameterList(self, ctx:JuliaSimplificadaParser.ParameterListContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#parameterList.
    def exitParameterList(self, ctx:JuliaSimplificadaParser.ParameterListContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#parameter.
    def enterParameter(self, ctx:JuliaSimplificadaParser.ParameterContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#parameter.
    def exitParameter(self, ctx:JuliaSimplificadaParser.ParameterContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#type.
    def enterType(self, ctx:JuliaSimplificadaParser.TypeContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#type.
    def exitType(self, ctx:JuliaSimplificadaParser.TypeContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#statement.
    def enterStatement(self, ctx:JuliaSimplificadaParser.StatementContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#statement.
    def exitStatement(self, ctx:JuliaSimplificadaParser.StatementContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#assignment.
    def enterAssignment(self, ctx:JuliaSimplificadaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#assignment.
    def exitAssignment(self, ctx:JuliaSimplificadaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#returnStatement.
    def enterReturnStatement(self, ctx:JuliaSimplificadaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#returnStatement.
    def exitReturnStatement(self, ctx:JuliaSimplificadaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#ifStatement.
    def enterIfStatement(self, ctx:JuliaSimplificadaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#ifStatement.
    def exitIfStatement(self, ctx:JuliaSimplificadaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#forLoop.
    def enterForLoop(self, ctx:JuliaSimplificadaParser.ForLoopContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#forLoop.
    def exitForLoop(self, ctx:JuliaSimplificadaParser.ForLoopContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#expressionStatement.
    def enterExpressionStatement(self, ctx:JuliaSimplificadaParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#expressionStatement.
    def exitExpressionStatement(self, ctx:JuliaSimplificadaParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#expression.
    def enterExpression(self, ctx:JuliaSimplificadaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#expression.
    def exitExpression(self, ctx:JuliaSimplificadaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:JuliaSimplificadaParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:JuliaSimplificadaParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:JuliaSimplificadaParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:JuliaSimplificadaParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:JuliaSimplificadaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:JuliaSimplificadaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:JuliaSimplificadaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:JuliaSimplificadaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:JuliaSimplificadaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:JuliaSimplificadaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:JuliaSimplificadaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:JuliaSimplificadaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:JuliaSimplificadaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:JuliaSimplificadaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by JuliaSimplificadaParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:JuliaSimplificadaParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by JuliaSimplificadaParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:JuliaSimplificadaParser.PrimaryExpressionContext):
        pass



del JuliaSimplificadaParser