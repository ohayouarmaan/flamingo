import string

"""
LEFT_BRACKET
RIGHT_BRACKET
KEYWORD
IDENTIFIER
STRINGS
NUMBERS
DELIMITERS
"""

# CONSTANTS
DELIMITERS = [" ", "\t", "\n", ""]
LETTERS = string.ascii_letters + "_"
NUMBERS = [f"{x}" for x in range(0, 10)]

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

    def build_word(self, first_letter: str):
        lexeme = ""
        while first_letter not in DELIMITERS and first_letter in LETTERS:
            lexeme += first_letter
            if self.peek() in DELIMITERS or self.peek() not in LETTERS:
                self.tokens.append(Token("WORD", lexeme))
                break
            first_letter = self.advance()

    def build_numbers(self, first_letter: str):
        lexeme = ""
        while first_letter not in DELIMITERS and first_letter in NUMBERS:
            lexeme += first_letter
            if self.peek() in DELIMITERS or self.peek() not in NUMBERS:
                self.tokens.append(Token("NUMBER", lexeme))
                break
            first_letter = self.advance()


    def lex(self):
        self.tokens = []
        while self.current_index < len(self.source_code) - 1:
            current_character = self.advance()

            ### BRACKETS
            if current_character == "(":
                self.tokens.append(Token("LEFT_BRACKET", current_character))
            elif current_character == ")":
                self.tokens.append(Token("RIGHT_BRACKET", current_character))
            elif current_character == "{":
                self.tokens.append(Token("LEFT_CURLY", current_character))
            elif current_character == "}":
                self.tokens.append(Token("RIGHT_CURLY", current_character))
            elif current_character == "[":
                self.tokens.append(Token("LEFT_SQUARE_BRACE", current_character))
            elif current_character == "]":
                self.tokens.append(Token("RIGHT_SQUARE_BRACE", current_character))

            ### INITIALIZERS
            elif current_character == "@":
                self.tokens.append(Token("FUNCTION_INITIALIZER", current_character))

            ### OPERATORS
            elif current_character == "+":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character == "/":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character == "*":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character == "%":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character in [" ", "\t", "\n"]:
                pass
            elif current_character == "-":
                self.tokens.append(Token("OPERATOR", current_character))
            elif current_character == ">":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("OPERATOR", ">="))
                else:
                    self.tokens.append(Token("OPERATOR", ">"))
            elif current_character == "!":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("OPERATOR", "!="))
                else:
                    self.tokens.append(Token("OPERATOR", "!"))
            elif current_character == "<":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("OPERATOR", "<="))
                else:
                    self.tokens.append(Token("OPERATOR", "<"))

            elif current_character == ",":
                self.tokens.append(Token("DELIMITER", current_character))
            elif current_character == ":":
                self.tokens.append(Token("COLON", current_character))
            elif current_character == ".":
                if self.peek() == ".":
                    self.advance()
                    self.tokens.append(Token("RANGE", ".."))
                else:
                    self.tokens.append(Token("DOT", "."))

            ### Multi character Tokens
            elif current_character in LETTERS:
                self.build_word(current_character)
            elif current_character in NUMBERS:
                self.build_numbers(current_character)


