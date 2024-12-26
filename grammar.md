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
declaration    -> statement ;
statement      -> exprStatement |
                  printStatement ;
printStatement -> KW:"print" expression ";" ;
exprStatement  -> expression ";" ;
ifExpression    -> 'if' expression <block> (else statement)? ;
block          -> '{' (statement ';')* '}'

arguments       -> expression ( "," expression )* ;
```
