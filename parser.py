import lexer

class BinaryExpression:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        self.expr_type = "BINARY"
    
    def __repr__(self):
        return f"BIN({self.left.to_string()}, {self.operator.to_string()}, {self.right.to_string()})"

    def to_string(self):
        return f"BIN({self.left.to_string()}, {self.operator.to_string()}, {self.right.to_string()})"

class UnaryExpression:
    def __init__(self, operator, value):
        self.operator = operator
        self.value = value
        self.expr_type = "UNARY"

    def __repr__(self):
        return f"UNA({self.operator.to_string()} {self.value.to_string()})"

    def to_string(self):
        return f"UNA({self.operator.to_string()} {self.value.to_string()})"

class LiteralExpression:
    def __init__(self, _type, value):
        self.type = _type
        self.value = value
        self.expr_type = "LITERAL"

    def __repr__(self):
        return f"{self.value.to_string()}"

    def to_string(self):
        return f"{self.value.to_string()}"

class Program:
    def __init__(self, tokens):
        self.tokens = tokens
        pass

class PrintStatement:
    def __init__(self, expr):
        self.expr = expr
        self.statement_type = "PRINT_STATEMENT"

    def __repr__(self):
        return f"PRINT: {self.expr}"

    def to_string(self):
        return f"PRINT: {self.expr}"

class VarDeclarationStatement:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        self.statement_type = "VAR_DECLARATION_STATEMENT"

    def __repr__(self):
        return f"{self.name} = {self.expr}"

    def to_string(self):
        return f"{self.name} = {self.expr}"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def parse(self):
        return self.program()

    def match_tokens(self, tokens):
        if self.tokens[self.current_index].type in tokens:
            self.current_index += 1
            return True
        return False
    
    def consume(self, token):
        if self.tokens[self.current_index].type == token:
            self.current_index += 1
            return True
        raise Exception(f"Error while parsing expected a '{token}' found '{self.tokens[self.current_index]}'")

    def program(self):
        statements = []
        while self.current_index < len(self.tokens) - 1:
            stmt = self.declaration()
            statements.append(stmt)

        return statements

    def declaration(self):
        return self.statement()

    def statement(self):
        if self.tokens[self.current_index].type == "KEYWORD":
            match self.tokens[self.current_index].lexeme:
                case "print":
                    self.current_index += 1
                    expr = self.expression()
                    self.consume("SEMI_COLON")
                    return PrintStatement(expr)
                case "var":
                    self.current_index += 1
                    name = self.tokens[self.current_index].lexeme
                    self.consume("WORD")
                    expr = None
                    if self.match_tokens(["EQ"]):
                        expr = self.expression()
                    self.consume("SEMI_COLON")
                    return VarDeclarationStatement(name, expr)


    def create_binary_expression(self, precedent_fn, match_tokens):
        lhs = precedent_fn()
        while self.match_tokens(match_tokens):
            operator = self.tokens[self.current_index - 1]
            rhs = precedent_fn()
            lhs = BinaryExpression(lhs, rhs, operator)
        return lhs


    def expression(self):
        return self.equality()

    def equality(self):
        return self.create_binary_expression(self.comparison, ["NOT_EQ", "EQ_EQ"])

    def comparison(self):
        return self.create_binary_expression(self.term, ["LESSER_EQUAL", "GREATER_EQUAL", "GREATER", "LESSER"])

    def term(self):
        return self.create_binary_expression(self.factor, ["MINUS", "PLUS"])

    def factor(self):
        return self.create_binary_expression(self.unary, ["DIVIDE", "MULTIPLY"])

    def unary(self):
        if self.match_tokens(["NOT", "MINUS"]):
            unary_expr = self.unary()
            return UnaryExpression(self.tokens[self.current_index - 1], unary_expr)
        else:
            return self.primary()


    def primary(self):
        if self.match_tokens("NUMBER"):
            return LiteralExpression("NUMBER", self.tokens[self.current_index - 1])
        elif self.match_tokens("STRING"):
            return LiteralExpression("STRING", self.tokens[self.current_index - 1])
        elif self.match_tokens("NIL"):
            return LiteralExpression("NIL", self.tokens[self.current_index - 1])
        elif self.match_tokens("WORD"):
            return LiteralExpression("WORD", self.tokens[self.current_index - 1])

