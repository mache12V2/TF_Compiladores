grammar JuliaSimplificadaParser;

options { tokenVocab=JuliaSimplificadaLexer; }

program
    : statement* EOF
    ;

statement
    : assignment
    | functionDecl
    | controlStructure
    | returnStatement
    | expression
    | ';' // Separadores opcionales
    ;

assignment
    : IDENTIFIER ('::' type)? ASSIGN expression
    ;

functionDecl
    : FUNCTION IDENTIFIER LPAREN parameterList? RPAREN statement* END
    ;

parameterList
    : IDENTIFIER ('::' type)? (COMMA IDENTIFIER ('::' type)? )*
    ;

controlStructure
    : ifStatement
    | forLoop
    | whileLoop
    ;

ifStatement
    : IF expression statement* (ELSEIF expression statement*)* (ELSE statement*)? END
    ;

forLoop
    : FOR IDENTIFIER IN expression statement* END
    ;

whileLoop
    : WHILE expression statement* END
    ;

returnStatement
    : RETURN expression?
    ;

expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQ | NEQ) relationalExpression)*
    ;

relationalExpression
    : rangeExpression ((LT | GT | LTE | GTE) rangeExpression)*
    ;

rangeExpression
    : additiveExpression (COLON additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MULT | DIV) unaryExpression)*
    ;

unaryExpression
    : (PLUS | MINUS | NOT)? primaryExpression
    ;

primaryExpression
    : literal
    | IDENTIFIER
    | functionCall
    | LPAREN expression RPAREN
    ;

functionCall
    : IDENTIFIER LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

type
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    ;

literal
    : INT
    | FLOAT
    | STRING
    | BOOL
    ;
