parser grammar JuliaSimplificadaParser;

options {
	tokenVocab = JuliaSimplificadaLexer;
}

// Programa
program: statement* EOF;

// Declaración de función
functionDecl:
	FUNCTION IDENTIFIER LPAREN parameterList? RPAREN (
		TYPE_ASSIGN type
	)? statement* END;

// Lista de parámetros
parameterList: parameter (COMMA parameter)*;

// Parámetro
parameter: IDENTIFIER TYPE_ASSIGN type;

// Tipo de dato
type: INT_TYPE | FLOAT_TYPE | STRING_TYPE | BOOL_TYPE;

// Sentencias
statement:
	assignment
	| functionDecl
	| returnStatement
	| ifStatement
	| forLoop
	| expressionStatement;

// Asignación
assignment: IDENTIFIER ASSIGN expression;

// Declaración de retorno
returnStatement: RETURN expression;

// Sentencia `if`
ifStatement: IF expression statement (ELSE statement)?;

// Bucle `for`
forLoop: FOR IDENTIFIER IN expression statement;

// Expresiones
expressionStatement: expression;

expression: logicalOrExpression;

logicalOrExpression:
	logicalAndExpression (OR logicalAndExpression)*;

logicalAndExpression:
	equalityExpression (AND equalityExpression)*;

equalityExpression:
	relationalExpression (
		EQ relationalExpression
		| NEQ relationalExpression
	)*;

relationalExpression:
	additiveExpression (LT | GT | LTE | GTE relationalExpression)?;

additiveExpression:
	multiplicativeExpression (
		PLUS
		| MINUS multiplicativeExpression
	)*;

multiplicativeExpression:
	unaryExpression (MULT | DIV unaryExpression)*;

unaryExpression: NOT unaryExpression | primaryExpression;

primaryExpression:
	IDENTIFIER
	| INT
	| FLOAT
	| BOOL
	| STRING
	| LPAREN expression RPAREN;