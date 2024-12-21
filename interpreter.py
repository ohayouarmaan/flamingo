import storage

class Interpreter:
    def __init__(self, program):
        self.program = program 
        self.global_storage = storage.GlobalStorage(None)

    def interpret(self):
        for statement in self.program:
            self.eval_statement(statement)

    def eval_statement(self, statement):
        match statement.statement_type:
            case "PRINT_STATEMENT":
                value = self.eval_expr(statement.expr)
                print(value)

            case "VAR_DECLARATION_STATEMENT":
                value = self.eval_expr(statement.expr)
                self.global_storage.add_value(value, statement.name)



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

        elif expr.operator.type == "MINUS":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not isinstance(lhs, float) or not isinstance(rhs, float):
                raise Exception("Expected LHS and RHS of a Subtraction Expression to be a number.")
            return lhs - rhs

        elif expr.operator.type == "MULTIPLY":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not isinstance(lhs, float) or not isinstance(rhs, float):
                raise Exception("Expected LHS and RHS of a Multiply Expression to be a number.")
            return lhs * rhs

        elif expr.operator.type == "DIVIDE":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not isinstance(lhs, float) or not isinstance(rhs, float):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs / rhs

    def visit_unary(self, expr):
        pass

    def visit_literal(self, expr):
        if expr.type == "NUMBER":
            return float(expr.value.lexeme)
        elif expr.type == "STRING":
            return expr.value.lexeme
        elif expr.type == "NIL":
            return None
        elif expr.type == "WORD":
            return self.global_storage.get_value(expr.value.lexeme)

