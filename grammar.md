# Grammar for mark

```
expression     → equality | assignment;
assignment     → identifier "=" expression ; 
equality       → comparison ( ( "!=" | "==" ) comparison )* ;
comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           → factor ( ( "-" | "+" ) factor )* ; // factor -> unary -> primary -> number + factor -> ...
factor         → unary ( ( "/" | "*" ) unary )* ;
unary          → ( "!" | "-" ) unary
               | primary ;
primary        → NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" ;

PROGRAM        -> declaration* EOF ;
declaration    -> statement ;
statement      -> exprStatement |
                  printStatement ;
printStatement -> KW:"print" expression ";" ;
exprStatement  -> expression ";" ;
ifExpression    -> 'if' expression <block> (else statement)? ;
block          -> '{' (statement ';')* '}'
```
