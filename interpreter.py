import storage

class Interpreter:
    def __init__(self, program):
        self.program = program 
        self.global_storage = storage.Storage(None)
        self.current_storage = self.global_storage

    def interpret(self):
        for i in range(len(self.program)):
            self.eval_statement(self.program[i])

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

            case "FOR_LOOP_STATEMENT":
                block_storage = storage.Storage(self.current_storage)
                self.current_storage = block_storage
                value = self.eval_expr(statement.initializer)
                while self.eval_expr(statement.conditional):
                    self.eval_expr(statement.block)
                    self.eval_expr(statement.incrementor)
                self.current_storage = self.current_storage.parent
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

            case "CONDITIONAL":
                return self.visit_conditional(expr)

            case "VAR_UPDATE_EXPRESSION":
                return self.visit_var_update(expr)

            case "VAR_DECLARATION_EXPRESSION":
                return self.visit_var_declaration(expr)

    def visit_binary(self, expr):
        if expr.operator.type == "PLUS":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if isinstance(lhs, str) or isinstance(rhs, str):
                return str(lhs) + str(rhs)
            return lhs + rhs

        elif expr.operator.type == "MINUS":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Subtraction Expression to be a number.")
            return lhs - rhs

        elif expr.operator.type == "MULTIPLY":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Multiply Expression to be a number.")
            return lhs * rhs

        elif expr.operator.type == "DIVIDE":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs / rhs

        elif expr.operator.type == "GREATER_EQUAL":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs >= rhs

        elif expr.operator.type == "LESSER_EQUAL":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs <= rhs

        elif expr.operator.type == "GREATER":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs > rhs

        elif expr.operator.type == "MODULUS":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs % rhs

        elif expr.operator.type == "LESSER":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs < rhs

        elif expr.operator.type == "EQ_EQ":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            if not (isinstance(lhs, float) or isinstance(lhs, int)) or not (isinstance(rhs, float) or isinstance(rhs, int)):
                raise Exception("Expected LHS and RHS of a Divide Expression to be a number.")
            return lhs == rhs

        elif expr.operator.type == "NOT_EQ":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            return lhs != rhs


    def visit_unary(self, expr):
        pass

    def visit_literal(self, expr):
        if expr.type == "NUMBER":
            try:
                return int(expr.value.lexeme)
            except ValueError:
                return float(expr.value.lexeme)
            except:
                raise Exception("Expected a Number")
            
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

    def visit_conditional(self, expr):
        condition = expr.condition
        if_block = expr.if_block
        result = None
        if self.eval_expr(condition):
            result = self.eval_expr(if_block)
        else:
            if expr.else_expression:
                result = self.eval_expr(expr.else_expression)
        return result
    
    def visit_var_declaration(self, expr):
        value = self.eval_expr(expr.expr)
        self.current_storage.add_value(value, expr.name)
        return None

    def visit_var_update(self, expr):
        value = self.eval_expr(expr.expr)
        self.current_storage.update_value(value, expr.name)
        return value

