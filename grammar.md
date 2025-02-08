# Grammar for flamingo

```
expression     → equality | assignment;
assignment     → identifier "=" expression ; 
equality       → comparison ( ( "!=" | "==" ) comparison )* ;
comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           → factor ( ( "-" | "+" ) factor )* ;
factor         → unary ( ( "/" | "*" ) unary )* ;
unary          → ( "!" | "-" ) unary
               | call ;
call           → primary ( "(" arguments? ")" )* ;
primary        → NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" | identifier ;

PROGRAM        -> declaration* EOF ;
declaration    -> functionDeclarationStatement |
                  structDeclarationStatement |
                  statement ;
statement      -> exprStatement |
                  printStatement ;

structDeclarationStatement -> "struct" identifier "{" (field ":" fieldType ",")* "}" ;
functionDeclarationStatement -> "@" identifier "(" (arguments ",")* ")" block ;
printStatement -> "print" expression ";" ;
returnStatement -> "return" expression ";" ;
exprStatement  -> expression ";" ;
ifExpression    -> 'if' expression <block> (else statement)? ;
block          -> '{' (statement ';')* '}'

arguments       -> expression ( "," expression )* ;
```
