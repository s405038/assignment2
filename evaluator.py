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

def parse_unary():
    token_type, value = current_token()

    if token_type == "OP" and value == "-":
        advance()
        operand = parse_unary()
        return ("neg", operand)

    if token_type == "OP" and value == "+":
        raise ValueError("Unary plus not supported")

    return parse_primary()

tokens = tokenize("-5")
position = 0

print(parse_unary())

def parse_power():
    left = parse_unary()
    
    token_type, value = current_token()

    if token_type == "OP" and value == "^":
        advance()

        right = parse_power()

        return ("^", left, right)

    return left

def parse_term():
    left = parse_power()

    while True:
        token_type, value = current_token()

        if token_type == "OP" and value in ("*", "/", "%"):
            advance()
            right = parse_power()
            left = (value, left, right)
        else:
            break

    return left


def parse_expression():
    left = parse_term()

    while True:
        token_type, value = current_token()

        if token_type == "OP" and value in ("+", "-"):
            advance()
            right = parse_term()
            left = (value, left, right)
        else:
            break

    return left


tokens = tokenize("2 + 3 * 4")
position = 0

tree = parse_expression()

print(tree)

def evaluate(node):
    if isinstance(node, str):
        return float(node)

    if node[0] == "neg":
        return -evaluate(node[1])

    op = node[0]

    left = evaluate(node[1])
    right = evaluate(node[2])

    if op == "+":
        return left + right

    if op == "-":
        return left - right

    if op == "*":
        return left * right

    if op == "/":
        if right == 0:
            raise ValueError("Division by zero")
        return left / right

    if op == "%":
        if right == 0:
            raise ValueError("Modulo by zero")
        return left % right

    if op == "^":
        return left ** right

raise ValueError("Unknown operator")

tokens = tokenize("2 + 3 * 4")
position = 0

tree = parse_expression()

print(tree)
print(evaluate(tree))

def tree_to_string(node):
    if isinstance(node, str):
        return node

    if node[0] == "neg":
        return f"(neg {tree_to_string(node[1])})"

    return (
        f"({node[0]} "
        f"{tree_to_string(node[1])} "
        f"{tree_to_string(node[2])})"

)

tokens = tokenize("2 + 3 * 4")
position = 0

tree = parse_expression()

print(tree_to_string(tree))

def format_result(value):
    if value == int(value):
        return str(int(value))
    
    return str(round(value, 4))