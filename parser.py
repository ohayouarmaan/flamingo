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

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def parse(self):
        return self.expression()

    def match_tokens(self, tokens):
        if self.tokens[self.current_index].type in tokens:
            self.current_index += 1
            return True
        return False

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

