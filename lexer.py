"""
LEFT_BRACKET
RIGHT_BRACKET
KEYWORD
IDENTIFIER
STRINGS
"""

class Token:
    def __init__(self, _type, lexeme):
        self.type = _type
        self.lexeme = lexeme

    def __repr__(self):
        return f"{self.lexeme}"

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.current_index = -1

    def advance(self):
        if self.current_index < len(self.source_code) - 1:
            self.current_index += 1
        return self.source_code[self.current_index]

    def peek(self):
        if self.current_index < len(self.source_code) - 1:
            return self.source_code[self.current_index + 1]

    def lex(self):
        self.tokens = []
        while self.current_index < len(self.source_code) - 1:
            current_character = self.advance()
            if current_character == "(":
                self.tokens.append(Token("LEFT_BRACKET", current_character))
            elif current_character == ")":
                self.tokens.append(Token("RIGHT_BRACKET", current_character))
            elif current_character == "{":
                self.tokens.append(Token("LEFT_CURLY", current_character))
            elif current_character == "}":
                self.tokens.append(Token("RIGHT_CURLY", current_character))
            elif current_character == "+":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character in [" ", "\t", "\n"]:
                pass
            elif current_character == "-":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character == ">":
                if self.peek() == "=":
                    self.tokens.append(Token("OPERATOR", ">="))
            elif current_character == "<":
                if self.peek() == "=":
                    self.tokens.append(Token("OPERATOR", "<="))



