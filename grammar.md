# Grammar for flamingo

```
expression     → equality | assignment;
assignment     → (call ".")? identifier "=" expression ; 
equality       → comparison ( ( "!=" | "==" ) comparison )* ;
comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           → factor ( ( "-" | "+" ) factor )* ;
factor         → unary ( ( "/" | "*" ) unary )* ;
unary          → ( "!" | "-" ) unary
               | call ;
call           → primary ( "(" arguments? ")" | "." identifier )* ;
primary        → NUMBER | STRING | "true" | "false" | "nil"
               | "(" expression ")" | identifier ;

PROGRAM        → declaration* EOF ;
declaration    → functionDeclarationStatement |
                  structDeclarationStatement |
                  statement ;
statement      → exprStatement |
                  printStatement |
                  structDeclarationStatement |
                  structInitStatement |
                  functionDeclarationStatement |
                  returnStatement |
                  importStatement;

structDeclarationStatement   → "struct" identifier "{" (field ":" fieldType ",")* "}" ;
functionDeclarationStatement → "@" identifier "(" (arguments ",")* ")" block ;
printStatement               → "print" expression ";" ;
returnStatement              → "return" expression ";" ;
exprStatement                → expression ";" ;
importStatement              → "%%" "import" path "as" MODULE_NAME
structInitStatement          → "#" structName "{" (field ":" value ",")* "}" ;

ifExpression                 → 'if' expression <block> (else statement)? ;
forStatement                 → "for" expression "," expression "," expression BlockStatement ;
block                        → '{' (statement ';')* '}' ;
arguments                    → expression ( "," expression )* ;
```
