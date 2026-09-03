# Program has 4 major components:
# Part A: Tokenizer
# Part B: Parser
# Part C: Evaluator
# Part D: File Processing

def tokenize(expression):
    tokens = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1

        elif char.isdigit():
            number = char
            i += 1

            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            tokens.append(("NUM", number))

        elif char in "+-*/%^":
            tokens.append(("OP", char))
            i += 1

        elif char == "(":
            tokens.append(("LPAREN", "("))
            i += 1

        elif char == ")":
            tokens.append(("RPAREN", ")"))
            i += 1

        else:
            raise ValueError("Invalid character")

    tokens.append(("END", ""))

    return tokens

print(tokenize("3 + 5"))  # Example usage of the tokenizer function

def current_token():
    return tokens[position]

def advance():
    global position
    position += 1

def parse_primary():
    token_type, value = current_token()

    if token_type == "NUM":
        advance()
        return value

    if token_type == "LPAREN":
        advance()

        node = parse_expression()

        if current_token()[0] != "RPAREN":
            raise ValueError("Missing closing parenthesis")

        advance()
        return node

    raise ValueError("Expected number or parenthesis")

tokens = tokenize("5")
position = 0

print(parse_primary())

# Testing pushing git extensions 2.