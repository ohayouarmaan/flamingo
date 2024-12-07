import lexer

l = None
with open("./test.fl", "r") as f:
    l = lexer.Lexer(f.read())

l.lex()
print(l.tokens)
