// Name: Nguyễn Trần Minh Phước
// Student's ID: 2052662

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//___SYNTAX_______________________________________________________

program: many_decl EOF;

many_decl: single_decl many_decl | single_decl;
single_decl: var_decl | func_decl ;

// variable declaration
// var_decl: normal_var_decl;
var_decl: ID sub_var_decl expr SM_COLON | id_list COLONS var_type SM_COLON;
sub_var_decl: COMMA ID sub_var_decl expr COMMA| COLONS var_type ASSIGN;

id_list: ID id_li;
id_li: COMMA ID id_li | ;

// parameter declaration
param_decl: INHERIT? OUT? ID COLONS var_type;
param_decl_list: param_decl param_decl_li | ; // comma-separated list of parameters declaration 
param_decl_li: COMMA param_decl param_decl_li | ;

// function declaration
func_decl: ID COLONS FUNCTION return_type LRB param_decl_list RRB (INHERIT ID)? blockStatement;


// Statement
statement: non_SM_statement | sM_statement;
non_SM_statement: ifStatement
				| forStatement
				| whileStatement
				| blockStatement;

sM_statement: statement_type SM_COLON;
statement_type: assignStatement 
			  | doWhileStatement 
			  | breakStatement 
			  | continueStatement 
			  | returnStatement
			  | callStatement;

	// ASSIGN Statement
assignStatement: lhs ASSIGN expr;

lhs: ID | array_index_expr;

	// IF ELSE statement
ifStatement: IF LRB expr RRB (blockStatement | statement) (ELSE (blockStatement | statement))?;


	// FOR statement
forStatement: FOR LRB assignStatement COMMA condition_expr COMMA update_expr RRB (blockStatement|statement);

condition_expr: expr;
update_expr: expr;

	// WHILE statement
whileStatement: WHILE LRB expr RRB (blockStatement|statement);

	// DO-WHILE statement
doWhileStatement: DO blockStatement WHILE LRB expr RRB;

breakStatement: BREAK;
continueStatement: CONTINUE;
returnStatement: RETURN (expr)?;
callStatement: function_call;

blockStatement: LCB many_body_line RCB ;
many_body_line: many_body_li | ;
many_body_li: body_line many_body_li | body_line;
body_line: statement | var_decl;



// Type of variable
var_type: atomic_type | AUTO | array_decl_type;
return_type: atomic_type | VOID | AUTO | array_decl_type;
atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;
array_decl_type: ARRAY LSB array_dimension RSB OF atomic_type;

array_dimension: INTLIT int_li | ;
int_li: COMMA INTLIT int_li | ; 

// Comma-Separated list of expr
arrLIT: LCB expr_list RCB;

expr_list: expr expr_li | ;
expr_li: COMMA expr expr_li | ;

// Expression
	// operator
relational_equal_OPERATOR: (EQUAL | NEQ);
relational_OPERATOR: ( LWT | GRT | LEQ | GEQ);
logical_OPERATOR: (AND | OR);
adding_OPERATOR: (ADD_OP | MIN_OP);
multiplying_OPERATOR: (MUL_OP | DIV_OP | MOD_OP);

expr: sub_expr1 STRING_CONCAT sub_expr1 | sub_expr1;
sub_expr1: sub_expr2 (relational_equal_OPERATOR | relational_OPERATOR) sub_expr2| sub_expr2;
sub_expr2: sub_expr2 logical_OPERATOR sub_expr3 | sub_expr3;
sub_expr3: sub_expr3 adding_OPERATOR sub_expr4 | sub_expr4;
sub_expr4: sub_expr4 multiplying_OPERATOR sub_expr5 | sub_expr5;
sub_expr5: NOT sub_expr5 | sub_expr6;
sub_expr6: MIN_OP sub_expr6 | sub_expr7;
sub_expr7: operand | function_call | array_index_expr | (LRB expr RRB);

	// expr for function call
function_call: ID LRB argument_list RRB;
argument_list: expr argument_li |;
argument_li: COMMA expr argument_li | ;

operand: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrLIT;

	// expr return ARRAY
array_index_expr: ID LSB index_list RSB;

index_list: expr index_li;
index_li: COMMA expr index_li | ;


//___LEXICAL___________________________________________________________________________
// Comment:
C_COMMENT: '/*' .*? '*/' -> skip; 
CPP_COMMENT: '//' ~[\r\n]* -> skip;

// Literals
INTLIT: ([0] | [1-9]DIGIT*([_]DIGIT+)*) {self.text = self.text.replace('_','')};
fragment DEC_PART: [.]DIGIT*;
fragment EXP_PART: [eE][+-]?DIGIT+; 
FLOATLIT: (INTLIT DEC_PART EXP_PART
		| INTLIT EXP_PART
		| DEC_PART EXP_PART
		| INTLIT DEC_PART) {self.text = self.text.replace('_','')};

BOOLLIT: TRUE | FALSE;

	// string literal and errors: illegal escape and unclosed string 
// STRING_OPEN: ["] -> push_mode(string_mode);

fragment ESCAPE_SEQUENCE: [\\][bfrnt'\\"];
STRINGLIT: (["] ( ESCAPE_SEQUENCE | ~['\\"])*? ["])  {self.text = self.text[1:-1]};

// Keyword
INTEGER: 'integer';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
ARRAY: 'array';
VOID: 'void';
AUTO: 'auto';

FALSE: 'false';
TRUE: 'true';

FOR: 'for';
WHILE: 'while';
DO: 'do';

BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';

RETURN: 'return';
OUT: 'out';
FUNCTION: 'function';
OF: 'of';
INHERIT: 'inherit';

// Separators
LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';

DOT: '.';
COMMA: ',';
SM_COLON: ';';
COLONS: ':';
ASSIGN: '=';

STRING_CONCAT: '::';

// Operator
// SIGN_OP: MIN_OP;
ADD_OP: [+];
MIN_OP: [-];
MUL_OP: [*];
DIV_OP: [/];
MOD_OP: [%];

NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NEQ: '!=';

GRT: '>';
GEQ: '>=';
LWT: '<';
LEQ: '<=';



// Identifier:
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: [_];
fragment DIGIT: [0-9];
ID: (LETTER|UNDERSCORE)(LETTER | UNDERSCORE | DIGIT)*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ILLEGAL_ESCAPE: '"' (~["] | '\\"')* [\\]~[bfnrt'"\\]  {
	string_error = str(self.text)
	raise IllegalEscape(string_error[1:])
};

UNCLOSE_STRING: ["] ( ESCAPE_SEQUENCE | ~['\\"])* (EOF | '\n')  {
	string_error = str(self.text)
	escape = '\n'
	if string_error[-1] == escape:
		raise UncloseString(self.text[1:-2])
	else:
		raise UncloseString(self.text[1:])
};

ERROR_CHAR: .{raise ErrorToken(self.text)};


