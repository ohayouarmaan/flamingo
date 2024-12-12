class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        print(self.eval_expr(self.ast))

    def eval_expr(self, expr):
        match expr.expr_type:
            case "BINARY":
                return self.visit_binary(expr)

            case "UNARY":
                return self.visit_unary(expr)

            case "LITERAL":
                return self.visit_literal(expr)

    def visit_binary(self, expr):
        if expr.operator.type == "PLUS":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            return lhs + rhs

        elif expr.operator.type == "MULTIPLY":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            return lhs * rhs

        elif expr.operator.type == "DIVIDE":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            return lhs / rhs

    def visit_unary(self, expr):
        pass

    def visit_literal(self, expr):
        if expr.type == "NUMBER":
            return float(expr.value.lexeme)

