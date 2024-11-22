# Generated from JuliaSimplificadaParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,182,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,53,8,1,1,
        1,1,1,1,1,3,1,58,8,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,1,2,
        1,2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,88,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,3,8,102,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,12,5,12,117,8,12,10,12,12,12,120,9,12,1,13,1,13,
        1,13,5,13,125,8,13,10,13,12,13,128,9,13,1,14,1,14,1,14,1,14,1,14,
        5,14,135,8,14,10,14,12,14,138,9,14,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,146,8,15,1,16,1,16,1,16,1,16,5,16,152,8,16,10,16,12,16,155,
        9,16,1,17,1,17,1,17,1,17,5,17,161,8,17,10,17,12,17,164,9,17,1,18,
        1,18,1,18,3,18,169,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,3,19,180,8,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,0,1,1,0,10,13,190,0,43,1,0,0,0,2,48,1,0,0,0,
        4,67,1,0,0,0,6,75,1,0,0,0,8,79,1,0,0,0,10,87,1,0,0,0,12,89,1,0,0,
        0,14,93,1,0,0,0,16,96,1,0,0,0,18,103,1,0,0,0,20,109,1,0,0,0,22,111,
        1,0,0,0,24,113,1,0,0,0,26,121,1,0,0,0,28,129,1,0,0,0,30,139,1,0,
        0,0,32,147,1,0,0,0,34,156,1,0,0,0,36,168,1,0,0,0,38,179,1,0,0,0,
        40,42,3,10,5,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,
        0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,
        49,5,1,0,0,49,50,5,40,0,0,50,52,5,31,0,0,51,53,3,4,2,0,52,51,1,0,
        0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,57,5,32,0,0,55,56,5,28,0,0,56,
        58,3,8,4,0,57,55,1,0,0,0,57,58,1,0,0,0,58,62,1,0,0,0,59,61,3,10,
        5,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,
        1,0,0,0,64,62,1,0,0,0,65,66,5,2,0,0,66,3,1,0,0,0,67,72,3,6,3,0,68,
        69,5,30,0,0,69,71,3,6,3,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,
        0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,72,1,0,0,0,75,76,5,40,0,0,76,77,
        5,28,0,0,77,78,3,8,4,0,78,7,1,0,0,0,79,80,7,0,0,0,80,9,1,0,0,0,81,
        88,3,12,6,0,82,88,3,2,1,0,83,88,3,14,7,0,84,88,3,16,8,0,85,88,3,
        18,9,0,86,88,3,20,10,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,
        87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,11,1,0,0,0,89,90,5,
        40,0,0,90,91,5,27,0,0,91,92,3,22,11,0,92,13,1,0,0,0,93,94,5,3,0,
        0,94,95,3,22,11,0,95,15,1,0,0,0,96,97,5,4,0,0,97,98,3,22,11,0,98,
        101,3,10,5,0,99,100,5,5,0,0,100,102,3,10,5,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,17,1,0,0,0,103,104,5,7,0,0,104,105,5,40,0,0,105,
        106,5,8,0,0,106,107,3,22,11,0,107,108,3,10,5,0,108,19,1,0,0,0,109,
        110,3,22,11,0,110,21,1,0,0,0,111,112,3,24,12,0,112,23,1,0,0,0,113,
        118,3,26,13,0,114,115,5,25,0,0,115,117,3,26,13,0,116,114,1,0,0,0,
        117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,25,1,0,0,0,120,
        118,1,0,0,0,121,126,3,28,14,0,122,123,5,24,0,0,123,125,3,28,14,0,
        124,122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,
        127,27,1,0,0,0,128,126,1,0,0,0,129,136,3,30,15,0,130,131,5,18,0,
        0,131,135,3,30,15,0,132,133,5,19,0,0,133,135,3,30,15,0,134,130,1,
        0,0,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,
        0,0,0,137,29,1,0,0,0,138,136,1,0,0,0,139,145,3,32,16,0,140,146,5,
        20,0,0,141,146,5,21,0,0,142,146,5,22,0,0,143,144,5,23,0,0,144,146,
        3,30,15,0,145,140,1,0,0,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,31,1,0,0,0,147,153,3,34,17,0,148,152,
        5,14,0,0,149,150,5,15,0,0,150,152,3,34,17,0,151,148,1,0,0,0,151,
        149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,
        33,1,0,0,0,155,153,1,0,0,0,156,162,3,36,18,0,157,161,5,16,0,0,158,
        159,5,17,0,0,159,161,3,36,18,0,160,157,1,0,0,0,160,158,1,0,0,0,161,
        164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,35,1,0,0,0,164,162,
        1,0,0,0,165,166,5,26,0,0,166,169,3,36,18,0,167,169,3,38,19,0,168,
        165,1,0,0,0,168,167,1,0,0,0,169,37,1,0,0,0,170,180,5,40,0,0,171,
        180,5,37,0,0,172,180,5,38,0,0,173,180,5,36,0,0,174,180,5,39,0,0,
        175,176,5,31,0,0,176,177,3,22,11,0,177,178,5,32,0,0,178,180,1,0,
        0,0,179,170,1,0,0,0,179,171,1,0,0,0,179,172,1,0,0,0,179,173,1,0,
        0,0,179,174,1,0,0,0,179,175,1,0,0,0,180,39,1,0,0,0,18,43,52,57,62,
        72,87,101,118,126,134,136,145,151,153,160,162,168,179
    ]

class JuliaSimplificadaParser ( Parser ):

    grammarFileName = "JuliaSimplificadaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'end'", "'return'", "'if'", 
                     "'else'", "'elseif'", "'for'", "'in'", "'while'", "'Int'", 
                     "'Float'", "'String'", "'Bool'", "'+'", "'-'", "'*'", 
                     "'/'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'&&'", "'||'", "'!'", "'='", "'::'", "':'", "','", 
                     "'('", "')'", "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "END", "RETURN", "IF", "ELSE", 
                      "ELSEIF", "FOR", "IN", "WHILE", "INT_TYPE", "FLOAT_TYPE", 
                      "STRING_TYPE", "BOOL_TYPE", "PLUS", "MINUS", "MULT", 
                      "DIV", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "AND", 
                      "OR", "NOT", "ASSIGN", "TYPE_ASSIGN", "COLON", "COMMA", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "SEMI", 
                      "BOOL", "INT", "FLOAT", "STRING", "IDENTIFIER", "WS", 
                      "COMMENT", "MULTILINE_COMMENT" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_parameterList = 2
    RULE_parameter = 3
    RULE_type = 4
    RULE_statement = 5
    RULE_assignment = 6
    RULE_returnStatement = 7
    RULE_ifStatement = 8
    RULE_forLoop = 9
    RULE_expressionStatement = 10
    RULE_expression = 11
    RULE_logicalOrExpression = 12
    RULE_logicalAndExpression = 13
    RULE_equalityExpression = 14
    RULE_relationalExpression = 15
    RULE_additiveExpression = 16
    RULE_multiplicativeExpression = 17
    RULE_unaryExpression = 18
    RULE_primaryExpression = 19

    ruleNames =  [ "program", "functionDecl", "parameterList", "parameter", 
                   "type", "statement", "assignment", "returnStatement", 
                   "ifStatement", "forLoop", "expressionStatement", "expression", 
                   "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
                   "relationalExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression" ]

    EOF = Token.EOF
    FUNCTION=1
    END=2
    RETURN=3
    IF=4
    ELSE=5
    ELSEIF=6
    FOR=7
    IN=8
    WHILE=9
    INT_TYPE=10
    FLOAT_TYPE=11
    STRING_TYPE=12
    BOOL_TYPE=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    EQ=18
    NEQ=19
    LT=20
    GT=21
    LTE=22
    GTE=23
    AND=24
    OR=25
    NOT=26
    ASSIGN=27
    TYPE_ASSIGN=28
    COLON=29
    COMMA=30
    LPAREN=31
    RPAREN=32
    LBRACKET=33
    RBRACKET=34
    SEMI=35
    BOOL=36
    INT=37
    FLOAT=38
    STRING=39
    IDENTIFIER=40
    WS=41
    COMMENT=42
    MULTILINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JuliaSimplificadaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.StatementContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.StatementContext,i)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = JuliaSimplificadaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2132518371482) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(JuliaSimplificadaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(JuliaSimplificadaParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(JuliaSimplificadaParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(JuliaSimplificadaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(JuliaSimplificadaParser.RPAREN, 0)

        def END(self):
            return self.getToken(JuliaSimplificadaParser.END, 0)

        def parameterList(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ParameterListContext,0)


        def TYPE_ASSIGN(self):
            return self.getToken(JuliaSimplificadaParser.TYPE_ASSIGN, 0)

        def type_(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.TypeContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.StatementContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.StatementContext,i)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = JuliaSimplificadaParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(JuliaSimplificadaParser.FUNCTION)
            self.state = 49
            self.match(JuliaSimplificadaParser.IDENTIFIER)
            self.state = 50
            self.match(JuliaSimplificadaParser.LPAREN)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 51
                self.parameterList()


            self.state = 54
            self.match(JuliaSimplificadaParser.RPAREN)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 55
                self.match(JuliaSimplificadaParser.TYPE_ASSIGN)
                self.state = 56
                self.type_()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2132518371482) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(JuliaSimplificadaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.COMMA)
            else:
                return self.getToken(JuliaSimplificadaParser.COMMA, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = JuliaSimplificadaParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.parameter()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 68
                self.match(JuliaSimplificadaParser.COMMA)
                self.state = 69
                self.parameter()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JuliaSimplificadaParser.IDENTIFIER, 0)

        def TYPE_ASSIGN(self):
            return self.getToken(JuliaSimplificadaParser.TYPE_ASSIGN, 0)

        def type_(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.TypeContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = JuliaSimplificadaParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(JuliaSimplificadaParser.IDENTIFIER)
            self.state = 76
            self.match(JuliaSimplificadaParser.TYPE_ASSIGN)
            self.state = 77
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(JuliaSimplificadaParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(JuliaSimplificadaParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(JuliaSimplificadaParser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(JuliaSimplificadaParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = JuliaSimplificadaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.AssignmentContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.FunctionDeclContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ReturnStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.IfStatementContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ForLoopContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = JuliaSimplificadaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.functionDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.forLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.expressionStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JuliaSimplificadaParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(JuliaSimplificadaParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = JuliaSimplificadaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(JuliaSimplificadaParser.IDENTIFIER)
            self.state = 90
            self.match(JuliaSimplificadaParser.ASSIGN)
            self.state = 91
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(JuliaSimplificadaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = JuliaSimplificadaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(JuliaSimplificadaParser.RETURN)
            self.state = 94
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(JuliaSimplificadaParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.StatementContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(JuliaSimplificadaParser.ELSE, 0)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = JuliaSimplificadaParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(JuliaSimplificadaParser.IF)
            self.state = 97
            self.expression()
            self.state = 98
            self.statement()
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(JuliaSimplificadaParser.ELSE)
                self.state = 100
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(JuliaSimplificadaParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(JuliaSimplificadaParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(JuliaSimplificadaParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.StatementContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = JuliaSimplificadaParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(JuliaSimplificadaParser.FOR)
            self.state = 104
            self.match(JuliaSimplificadaParser.IDENTIFIER)
            self.state = 105
            self.match(JuliaSimplificadaParser.IN)
            self.state = 106
            self.expression()
            self.state = 107
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = JuliaSimplificadaParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = JuliaSimplificadaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.OR)
            else:
                return self.getToken(JuliaSimplificadaParser.OR, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)




    def logicalOrExpression(self):

        localctx = JuliaSimplificadaParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.logicalAndExpression()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 114
                self.match(JuliaSimplificadaParser.OR)
                self.state = 115
                self.logicalAndExpression()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.AND)
            else:
                return self.getToken(JuliaSimplificadaParser.AND, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)




    def logicalAndExpression(self):

        localctx = JuliaSimplificadaParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.equalityExpression()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 122
                self.match(JuliaSimplificadaParser.AND)
                self.state = 123
                self.equalityExpression()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.RelationalExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.EQ)
            else:
                return self.getToken(JuliaSimplificadaParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.NEQ)
            else:
                return self.getToken(JuliaSimplificadaParser.NEQ, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)




    def equalityExpression(self):

        localctx = JuliaSimplificadaParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.relationalExpression()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 130
                    self.match(JuliaSimplificadaParser.EQ)
                    self.state = 131
                    self.relationalExpression()
                    pass
                elif token in [19]:
                    self.state = 132
                    self.match(JuliaSimplificadaParser.NEQ)
                    self.state = 133
                    self.relationalExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.AdditiveExpressionContext,0)


        def LT(self):
            return self.getToken(JuliaSimplificadaParser.LT, 0)

        def GT(self):
            return self.getToken(JuliaSimplificadaParser.GT, 0)

        def LTE(self):
            return self.getToken(JuliaSimplificadaParser.LTE, 0)

        def GTE(self):
            return self.getToken(JuliaSimplificadaParser.GTE, 0)

        def relationalExpression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.RelationalExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)




    def relationalExpression(self):

        localctx = JuliaSimplificadaParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relationalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.additiveExpression()
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 140
                self.match(JuliaSimplificadaParser.LT)
                pass
            elif token in [21]:
                self.state = 141
                self.match(JuliaSimplificadaParser.GT)
                pass
            elif token in [22]:
                self.state = 142
                self.match(JuliaSimplificadaParser.LTE)
                pass
            elif token in [23]:
                self.state = 143
                self.match(JuliaSimplificadaParser.GTE)
                self.state = 144
                self.relationalExpression()
                pass
            elif token in [-1, 1, 2, 3, 4, 5, 7, 18, 19, 24, 25, 26, 31, 32, 36, 37, 38, 39, 40]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.PLUS)
            else:
                return self.getToken(JuliaSimplificadaParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.MINUS)
            else:
                return self.getToken(JuliaSimplificadaParser.MINUS, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)




    def additiveExpression(self):

        localctx = JuliaSimplificadaParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.multiplicativeExpression()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 148
                    self.match(JuliaSimplificadaParser.PLUS)
                    pass
                elif token in [15]:
                    self.state = 149
                    self.match(JuliaSimplificadaParser.MINUS)
                    self.state = 150
                    self.multiplicativeExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuliaSimplificadaParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(JuliaSimplificadaParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.MULT)
            else:
                return self.getToken(JuliaSimplificadaParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(JuliaSimplificadaParser.DIV)
            else:
                return self.getToken(JuliaSimplificadaParser.DIV, i)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)




    def multiplicativeExpression(self):

        localctx = JuliaSimplificadaParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.unaryExpression()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 160
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 157
                    self.match(JuliaSimplificadaParser.MULT)
                    pass
                elif token in [17]:
                    self.state = 158
                    self.match(JuliaSimplificadaParser.DIV)
                    self.state = 159
                    self.unaryExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(JuliaSimplificadaParser.NOT, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.UnaryExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = JuliaSimplificadaParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryExpression)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(JuliaSimplificadaParser.NOT)
                self.state = 166
                self.unaryExpression()
                pass
            elif token in [31, 36, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JuliaSimplificadaParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(JuliaSimplificadaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(JuliaSimplificadaParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(JuliaSimplificadaParser.BOOL, 0)

        def STRING(self):
            return self.getToken(JuliaSimplificadaParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(JuliaSimplificadaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(JuliaSimplificadaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(JuliaSimplificadaParser.RPAREN, 0)

        def getRuleIndex(self):
            return JuliaSimplificadaParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = JuliaSimplificadaParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primaryExpression)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(JuliaSimplificadaParser.IDENTIFIER)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(JuliaSimplificadaParser.INT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(JuliaSimplificadaParser.FLOAT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 173
                self.match(JuliaSimplificadaParser.BOOL)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 174
                self.match(JuliaSimplificadaParser.STRING)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 6)
                self.state = 175
                self.match(JuliaSimplificadaParser.LPAREN)
                self.state = 176
                self.expression()
                self.state = 177
                self.match(JuliaSimplificadaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





