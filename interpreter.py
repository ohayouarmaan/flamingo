import storage

class Interpreter:
    def __init__(self, program):
        self.program = program 
        self.global_storage = storage.Storage(None)
        self.current_storage = self.global_storage

    def interpret(self):
        for statement in self.program:
            self.eval_statement(statement)

    def eval_statement(self, statement):
        match statement.statement_type:
            case "PRINT_STATEMENT":
                value = self.eval_expr(statement.expr)
                print(value)
                return None

            case "VAR_DECLARATION_STATEMENT":
                value = self.eval_expr(statement.expr)
                self.current_storage.add_value(value, statement.name)
                return None

            case "VAR_UPDATE_STATEMENT":
                value = self.eval_expr(statement.expr)
                self.current_storage.update_value(value, statement.name)
                return None

            case "EXPRESSION_STATEMENT":
                value = self.eval_expr(statement.expr)
                return value

    def eval_expr(self, expr):
        match expr.expr_type:
            case "BINARY":
                return self.visit_binary(expr)

            case "UNARY":
                return self.visit_unary(expr)

            case "LITERAL":
                return self.visit_literal(expr)

            case "BLOCK":
                return self.visit_block(expr)

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
            return self.current_storage.get_value(expr.value.lexeme)

    def visit_block(self, expr):
        last_statement = None
        block_storage = storage.Storage(self.current_storage)
        self.current_storage = block_storage
        for stmt in expr.statements:
            last_statement = self.eval_statement(stmt)
        self.current_storage = self.current_storage.parent
        return last_statement
