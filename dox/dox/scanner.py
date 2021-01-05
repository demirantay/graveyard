"""
Scanner
-------

This module contains all of the code that creates the scanner part of the
compiler.  ...

Feature list ...

Starting point function: ... its usage and its referenced other functions ...

(document all of the above later on)

"""

# these global vars will be moved to main
line_count = 0


class Token:
    """
    This is a data strucutre that holds a node about the tokens. A taken is a
    series of characters that ends with a blank space in a source code file.
    """
    def __init__(self, lexeme=None, type=None):
        self.lexeme = lexeme  # examples: `varName`, `(`, `;`, `+`, `int`
        self.type = type      # examples: keyword, identifier, operator

    def __str__(self):
        return "lexme: " + str(self.lexeme) + " | type: " + str(self.type)

    def get_lexeme(self):
        return self.lexeme

    def get_type(self):
        return self.type


class Scanner:
    """
        the below code will be integrated into this class
    """
    def __init__(self):
        pass

    def tokenize(self):
        pass


# Algorithms of the Scanner (Lexical Analysis)

def scanner():
    tokens_chars = []
    tokens = []
    line_count = 0

    # open the source code file
    file = open("example.txt", "rt")

    # traverse all of the lines and scan tokens
    for char in file.read():
        print(char)

        tokens_chars.append(char)

        if char == "\n":
            tokens.append(Token("\\n", "operator"))
        elif char == "+":
            tokens.append(Token("+", "operator"))
        elif char == "1":
            tokens.append(Token(1, "identifier"))
        elif char == "2":
            tokens.append(Token(2, "identifier"))

    for token in tokens:
        print(token)

    print("tokens chars: ", tokens_chars)

    # update the line code



scanner()
