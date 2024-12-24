import lexer
import parser
import interpreter

l = None

with open("./test.fl", "r") as f:
    l = lexer.Lexer(f.read())

l.lex()
print(l.tokens)
p = parser.Parser(l.tokens)

e = p.parse()
inter = interpreter.Interpreter(e)

inter.interpret()
