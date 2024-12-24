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
KEYWORDS = ["print", "for", "while", "if", "else", "var"]

class Token:
    def __init__(self, _type, lexeme):
        self.type = _type
        self.lexeme = lexeme

    def __repr__(self):
        return f"{self.lexeme}"

    def to_string(self):
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
                if lexeme in KEYWORDS:
                    self.tokens.append(Token("KEYWORD", lexeme))
                else:
                    if lexeme == "nil":
                        self.tokens.append(Token("NIL", lexeme))
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

    def build_string(self):
        lexeme = ""
        current_character = self.advance()
        while current_character != "\"":
            lexeme += current_character
            current_character = self.advance()

        self.tokens.append(Token("STRING", lexeme))

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
                self.tokens.append(Token("PLUS", current_character))
            elif current_character == "/":
                self.tokens.append(Token("DIVIDE", current_character))
            elif current_character == "*":
                self.tokens.append(Token("MULTIPLY", current_character))
            elif current_character == "%":
                self.tokens.append(Token("MODULUS", current_character))
            elif current_character in [" ", "\t", "\n"]:
                pass
            elif current_character == "-":
                self.tokens.append(Token("MINUS", current_character))
            elif current_character == ">":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("GREATER_EQUAL", ">="))
                else:
                    self.tokens.append(Token("GREATER", ">"))
            elif current_character == "!":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("NOT_EQ", "!="))
                else:
                    self.tokens.append(Token("NOT", "!"))
            elif current_character == "=":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("EQ_EQ", "=="))
                else:
                    self.tokens.append(Token("EQ", "="))
            elif current_character == "<":
                if self.peek() == "=":
                    self.advance()
                    self.tokens.append(Token("LESSER_EQUAL", "<="))
                else:
                    self.tokens.append(Token("LESSER", "<"))

            elif current_character == ",":
                self.tokens.append(Token("COMMA", current_character))
            elif current_character == ":":
                self.tokens.append(Token("COLON", current_character))
            elif current_character == ";":
                self.tokens.append(Token("SEMI_COLON", current_character))
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
            elif current_character == "\"":
                self.build_string()


