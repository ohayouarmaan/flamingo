import lexer
import parser
import interpreter

l = None

with open("./test.fl", "r") as f:
    content = f.read()
    l = lexer.Lexer(content)


l.lex()
p = parser.Parser(l.tokens)

e = p.parse()
# print(e)
inter = interpreter.Interpreter(e)

inter.interpret()
