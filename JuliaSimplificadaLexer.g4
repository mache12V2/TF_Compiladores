lexer grammar JuliaSimplificadaLexer;

// Palabras clave
FUNCTION   : 'function';
END        : 'end';
RETURN     : 'return';
IF         : 'if';
ELSE       : 'else';
ELSEIF     : 'elseif';
FOR        : 'for';
IN         : 'in';
WHILE      : 'while';
INT_TYPE   : 'Int';
FLOAT_TYPE : 'Float';
STRING_TYPE: 'String';
BOOL_TYPE  : 'Bool';

// Operadores
PLUS     : '+';
MINUS    : '-';
MULT     : '*';
DIV      : '/';
EQ       : '==';
NEQ      : '!=';
LT       : '<';
GT       : '>';
LTE      : '<=';
GTE      : '>=';
AND      : '&&';
OR       : '||';
NOT      : '!';
ASSIGN   : '=';
TYPE_ASSIGN : '::';
COLON    : ':';
COMMA    : ',';
LPAREN   : '(';
RPAREN   : ')';
LBRACKET : '[';
RBRACKET : ']';
SEMI     : ';';

// Literales
BOOL     : 'true' | 'false';
INT      : [0-9]+;
FLOAT    : [0-9]+ '.' [0-9]+;
STRING   : '"' (~["\\] | '\\' .)* '"'
         | '"""' .*? '"""';

// Identificadores
IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios en blanco y comentarios
WS : [ \t\r\n]+ -> skip;
COMMENT : '#' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '#=' .*? '=#' -> skip;
