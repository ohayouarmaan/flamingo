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


class BlockExpression:
    def __init__(self, statements):
        self.statements = statements
        self.expr_type = "BLOCK"

    def __repr__(self):
        return f"BLOCK EXPRESSION: {self.statements[len(self.statements) - 1]}"

    def to_string(self):
        return f"BLOCK EXPRESSION: {self.statements[len(self.statements) - 1]}"


class IfExpression:
    def __init__(self, condition, if_block, else_expression):
        self.condition = condition
        self.if_block = if_block
        self.else_expression = else_expression
        self.expr_type = "CONDITIONAL"

    def __repr__(self):
        return f"IF: {self.condition} ELSE: {self.else_expression}"

    def to_string(self):
        return f"IF: {self.condition} ELSE: {self.else_expression}"

class VarDeclarationExpression:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        self.expr_type = "VAR_DECLARATION_EXPRESSION"

    def __repr__(self):
        return f"{self.name} = {self.expr}"

    def to_string(self):
        return f"{self.name} = {self.expr}"


class VarUpdateExpression:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        self.expr_type = "VAR_UPDATE_EXPRESSION"

    def __repr__(self):
        return f"{self.name} = {self.expr}"

    def to_string(self):
        return f"{self.name} = {self.expr}"

class StructInitializationExpression:
    def __init__(self, name, values):
        self.values = values
        self.name = name
        self.expr_type = "STRUCT_INIT_EXPRESSION"

    def __repr__(self):
        return f"{self.name}: {self.values}"

    def to_string(self):
        return f"{self.name}: {self.values}"

class CallExpression:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments
        self.expr_type = "CALL_EXPRESSION"

    def __repr__(self):
        return f"{self.name}({','.join(map(lambda x: x.to_string(), self.arguments))})"
    9

    def to_string(self):
        return f"{self.name}({','.join(map(lambda x: x.to_string(), self.arguments))})"

class Program:
    def __init__(self, tokens):
        self.tokens = tokens

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

class VarUpdateStatement:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        self.statement_type = "VAR_UPDATE_STATEMENT"

    def __repr__(self):
        return f"{self.name} = {self.expr}"

    def to_string(self):
        return f"{self.name} = {self.expr}"


class ExpressionStatement:
    def __init__(self, expr):
        self.expr = expr
        self.statement_type = "EXPRESSION_STATEMENT"

    def __repr__(self):
        return f"{self.expr}"

    def to_string(self):
        return f"{self.expr}"

class ForStatement:
    def __init__(self, initializer, conditional, incrementor, block):
        self.initializer = initializer
        self.conditional = conditional
        self.incrementor = incrementor
        self.statement_type = "FOR_LOOP_STATEMENT"
        self.block = block

    def __repr__(self):
        return f"FOR: {self.conditional}"

    def to_string(self):
        return f"FOR: {self.conditional}"

class FunctionDeclarationStatement:
    def __init__(self, name, arguments, function_block):
        self.arguments = arguments
        self.name = name
        self.function_block = function_block
        self.statement_type = "FUNCTION_DECLARATION_STATEMENT"

    def __repr__(self):
        return f"@{self.name}({','.join(self.arguments)})"

    def to_string(self):
        return f"@{self.name}({','.join(self.arguments)})"

class ReturnStatement:
    def __init__(self, expr):
        self.expr = expr
        self.statement_type = "RETURN_STATEMENT"

    def __repr__(self):
        return f"return {self.expr}"

    def to_string(self):
        return f"return {self.expr}"

class StructItem:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}: {self.value}"

    def to_string(self):
        return f"{self.name}: {self.value}"

class StructDeclarationStatement:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        self.statement_type = "STRUCT_DECLARATION_STATEMENT"

    def __repr__(self):
        return f"{self.name}: {self.values}"

    def to_string(self):
        return f"{self.name}: {self.values}"

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
                case "if":
                    expr = self.expression()
                    if self.match_tokens(["SEMI_COLON"]):
                        pass
                    return ExpressionStatement(expr)
                case "for":
                    self.consume("KEYWORD")
                    initializer = self.expression()
                    self.consume("COMMA")
                    condition = self.expression()
                    self.consume("COMMA")
                    incrementor = self.expression()
                    loop_block = self.expression()
                    return ForStatement(initializer, condition, incrementor, loop_block)
                
                case "return":
                    self.consume("KEYWORD")
                    ret = self.expression()
                    self.consume("SEMI_COLON")
                    r = ReturnStatement(ret)
                    return r

                case "struct":
                    self.consume("KEYWORD")
                    struct_name = self.tokens[self.current_index].lexeme
                    self.consume("WORD")
                    self.consume("LEFT_CURLY")
                    struct_fields = []
                    while not self.match_tokens("RIGHT_CURLY"):
                        name = self.tokens[self.current_index].lexeme
                        self.consume("WORD")
                        self.consume("COLON")
                        field_type = self.tokens[self.current_index].lexeme
                        self.consume("WORD")
                        struct_fields.append(StructItem(name, field_type))
                        if self.tokens[self.current_index].type == "COMMA":
                            self.consume("COMMA")
                        else:
                            if self.match_tokens("RIGHT_CURLY"):
                                break
                            else:
                                raise Exception("Expected a '}' after this.")

                    return StructDeclarationStatement(struct_name, struct_fields)
                
        
        elif self.tokens[self.current_index].type == "FUNCTION_INITIALIZER":
            self.consume("FUNCTION_INITIALIZER")
            function_name = self.tokens[self.current_index].lexeme
            self.consume("WORD")
            self.consume("LEFT_BRACKET")
            arguments = []
            while not self.match_tokens("RIGHT_BRACKET"):
                if self.match_tokens("WORD"):
                    arguments.append(self.tokens[self.current_index - 1].lexeme)

                if self.match_tokens("COMMA"):
                    pass

            block = self.expression()
            return FunctionDeclarationStatement(function_name, arguments, block)

        elif self.tokens[self.current_index].type == "HASH":
            self.consume("HASH")

        elif self.tokens[self.current_index].type == "WORD":
            name = self.tokens[self.current_index].lexeme
            self.consume("WORD")
            if self.match_tokens(["EQ"]):
                expr = self.expression()
                self.consume("SEMI_COLON")
                return VarUpdateStatement(name, expr)
            else:
                self.current_index -= 1
                expr = self.expression()
                self.consume("SEMI_COLON")
                return ExpressionStatement(expr)

        else:
            expr = self.expression()
            self.consume("SEMI_COLON")
            return ExpressionStatement(expr)


    def create_binary_expression(self, precedent_fn, match_tokens):
        lhs = precedent_fn()
        while self.match_tokens(match_tokens):
            operator = self.tokens[self.current_index - 1]
            rhs = precedent_fn()
            lhs = BinaryExpression(lhs, rhs, operator)
        return lhs


    def expression(self):
        if self.match_tokens(["LEFT_CURLY"]):
            statements = []
            while not self.match_tokens(["RIGHT_CURLY"]):
                statements.append(self.statement())
            return BlockExpression(statements)
        elif self.match_tokens(["KEYWORD"]):
            kw = self.tokens[self.current_index - 1]
            if kw.lexeme == "if":
                expr = self.expression()
                block_expr = None
                else_expr = None
                if self.tokens[self.current_index].type == "LEFT_CURLY":
                    block_expr = self.expression()
                    if self.tokens[self.current_index].type == "KEYWORD":
                        if self.tokens[self.current_index].lexeme == "else":
                            self.consume("KEYWORD")
                            else_expr = self.expression()
                return IfExpression(expr, block_expr, else_expr)
            elif kw.lexeme == "var":
                if self.consume("WORD"):
                    name = self.tokens[self.current_index - 1].lexeme
                    self.consume("EQ")
                    expr = self.expression()
                    return VarDeclarationExpression(name, expr)
        elif self.match_tokens(["WORD"]):
            ident = self.tokens[self.current_index - 1].lexeme
            if self.match_tokens(["EQ"]):
                expr = self.expression()
                return VarUpdateExpression(ident, expr)
            self.current_index -= 1
            return self.equality()
        elif self.match_tokens(["HASH"]):
            name = self.tokens[self.current_index].lexeme
            self.consume("WORD")
            self.consume("LEFT_CURLY")
            values = {}
            while not self.match_tokens("RIGHT_CURLY"):
                item_name = self.tokens[self.current_index].lexeme
                self.consume("WORD")
                self.consume("COLON")
                item_value = self.expression()
                values[item_name] = item_value
                if not self.match_tokens("COMMA"):
                    self.consume("RIGHT_CURLY")
                    break
            return StructInitializationExpression(name, values)

        return self.equality()

    def equality(self):
        return self.create_binary_expression(self.comparison, ["NOT_EQ", "EQ_EQ"])

    def comparison(self):
        return self.create_binary_expression(self.term, ["LESSER_EQUAL", "GREATER_EQUAL", "GREATER", "LESSER"])

    def term(self):
        return self.create_binary_expression(self.factor, ["MINUS", "PLUS"])

    def factor(self):
        return self.create_binary_expression(self.unary, ["DIVIDE", "MULTIPLY", "MODULUS"])

    def unary(self):
        if self.match_tokens(["NOT", "MINUS"]):
            operator = self.tokens[self.current_index - 1]
            unary_expr = self.unary()
            return UnaryExpression(operator, unary_expr)
        else:
            return self.call()

    def init_struct(self):
        name = self.tokens[self.current_index].lexeme
        self.consume("WORD")
        self.consume("LEFT_CURLY")
        values = {}
        while not self.match_tokens("RIGHT_CURLY"):
            item_name = self.tokens[self.current_index].lexeme
            self.consume("COLON")
            item_value = self.expression()
            values[item_name] = item_value
            if not self.match_tokens("COMMA"):
                self.consume("RIGHT_CURLY")
                break

    def call(self):
        primary = self.primary()
        while self.match_tokens("LEFT_BRACKET"):
            arguments = []
            while not self.match_tokens("RIGHT_BRACKET"):
                current_argument = self.expression()
                arguments.append(current_argument)
                if self.match_tokens("COMMA"):
                    continue

            primary = CallExpression(primary, arguments)
        return primary

    def primary(self):
        if self.match_tokens("NUMBER"):
            return LiteralExpression("NUMBER", self.tokens[self.current_index - 1])
        elif self.match_tokens("STRING"):
            return LiteralExpression("STRING", self.tokens[self.current_index - 1])
        elif self.match_tokens("NIL"):
            return LiteralExpression("NIL", self.tokens[self.current_index - 1])
        elif self.match_tokens("WORD"):
            return LiteralExpression("WORD", self.tokens[self.current_index - 1])
        elif self.match_tokens("LEFT_BRACKET"):
            expr = self.expression()
            self.consume("RIGHT_BRACKET")
            return expr

