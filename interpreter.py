import storage
import os
from callable import Callable
from parser import SetExpression, Parser
from lexer import Lexer
from standard.time import Time
from standard.user_defined import UserDefined, ReturnException
from standard_types.struct import StructItem, StructType
from standard_types.modules import FlamingoModuleItem, FlamingoModuleType

class Interpreter:
    def __init__(self, program, _storage, cwd="."):
        self.program = program 
        if _storage:
            self.global_storage = _storage
        else:
            self.global_storage = storage.Storage(None)
            self.global_storage.add_value(Time(), "time")
        self.current_storage = self.global_storage
        self.cwd = cwd

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
                if isinstance(statement.name, SetExpression):
                    self.visit_set_expression(statement.name, statement.expr)
                else:
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

            case "FUNCTION_DECLARATION_STATEMENT":
                self.current_storage.add_value(UserDefined(statement.arguments, statement.function_block), statement.name)
                return None
            case "RETURN_STATEMENT":
                raise ReturnException(self.eval_expr(statement.expr))

            case "STRUCT_DECLARATION_STATEMENT":
                self.global_storage.add_value(statement.values, statement.name)
                return None
            case "IMPORT_STATEMENT":
                with open(os.path.join(self.cwd, self.eval_expr(statement.path)), "r") as f:
                    content = f.read()
                    l = Lexer(content)
                    l.lex()
                    p = Parser(l.tokens)
                    e = p.parse()
                    new_module_storage = storage.Storage(None)
                    i = Interpreter(e, new_module_storage)
                    i.interpret()

                    module_key_values = []

                    for _, (key, value) in enumerate(new_module_storage.storage.items()):
                        module_key_values.append(FlamingoModuleItem(key, value))

                    self.current_storage.add_value(FlamingoModuleType(module_key_values), statement.module_name.lexeme)



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

            case "CALL_EXPRESSION":
                return self.visit_call_expression(expr)
            
            case "STRUCT_INIT_EXPRESSION":
                return self.visit_struct_init_expression(expr)

            case "GET_EXPRESSION":
                return self.visit_get_expression(expr)

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
            return lhs == rhs

        elif expr.operator.type == "NOT_EQ":
            lhs = self.eval_expr(expr.left)
            rhs = self.eval_expr(expr.right)
            return lhs != rhs


    def visit_unary(self, expr):
        if expr.operator.lexeme == "!":
            return not self.eval_expr(expr.value)
        elif expr.operator.lexeme == "-":
            return -self.eval_expr(expr.value)

    
    def visit_set_expression(self, name, obj):
        for val in self.eval_expr(name.obj).values:
            if val.name == name.name:
                val.set(self.eval_expr(obj))

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
            value = self.current_storage.get_value(expr.value.lexeme)
            if isinstance(value, Callable):
                return value
            else:
                return value

    def visit_block(self, expr):
        last_statement = None
        block_storage = storage.Storage(self.current_storage)
        self.current_storage = block_storage
        for stmt in expr.statements:
            try:
                last_statement = self.eval_statement(stmt)
            except ReturnException as e:
                raise e
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

    def visit_call_expression(self, expr):
        value = self.eval_expr(expr.name)
        if len(expr.arguments) != value.arity:
            raise Exception(f"Expected {value.arity} arguments got {len(expr.arguments)}. in the {expr.name} function")

        arguments = []
        for arg in expr.arguments:
            arguments.append(self.eval_expr(arg))

        return value.call(self, arguments)
    
    def visit_struct_init_expression(self, expr):
        struct_def = self.global_storage.get_value(expr.name)
        values = []
        for def_val in struct_def:
            values.append(StructItem(def_val.name, self.eval_expr(expr.values[def_val.name])))

        return StructType(values)

    
    def visit_get_expression(self, expr):
        t = self.eval_expr(expr.obj).values
        for e in t:
            if e.name == expr.name:
                return e.value


