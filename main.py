import lexer
import parser
import sys
import interpreter

l = None

if len(sys.argv) < 2:
    print("""
    Usage: python3 main.py <file_name>
    """)
    sys.exit(1)

def parse_file_location(file_path):
    content = file_path.split("/")
    if len(content) == 1:
        return "./"
    else:
        if len(content[:-1]) == 1:
            return "./" + "".join(content[:-1])
        return "/".join(content[:-1])

with open(sys.argv[1], "r") as f:
    content = f.read()
    l = lexer.Lexer(content)
    
    l.lex()
    p = parser.Parser(l.tokens)
    e = p.parse()
    inter = interpreter.Interpreter(e, None, parse_file_location(sys.argv[1]))

    inter.interpret()

