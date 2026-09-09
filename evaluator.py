# Program has 4 major components:
# Part A: Tokenizer
# Part B: Parser
# Part C: Evaluator
# Part D: File Processing

import os

tokens = []
position = 0


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
            decimal_seen = False

            while i < len(expression):
                if expression[i].isdigit():
                    number += expression[i]
                    i += 1

                elif expression[i] == "." and not decimal_seen:
                    decimal_seen = True
                    number += "."
                    i += 1

                else:
                    break

            if number.endswith("."):
                raise ValueError("Invalid number")

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
            raise ValueError("Missing ')'")

        advance()
        return node

    raise ValueError("Expected number or parenthesis")


def parse_power():
    left = parse_primary()

    token_type, value = current_token()

    if token_type == "OP" and value == "^":
        advance()
        right = parse_power()
        return ("^", left, right)

    return left


def parse_unary():
    token_type, value = current_token()

    if token_type == "OP" and value == "-":
        advance()
        return ("neg", parse_unary())

    if token_type == "OP" and value == "+":
        raise ValueError("Unary plus not supported")

    return parse_power()


def starts_factor(token_type):
    return token_type in ("NUM", "LPAREN")


def parse_term():
    left = parse_unary()

    while True:
        token_type, value = current_token()

        if token_type == "OP" and value in ("*", "/", "%"):
            advance()
            right = parse_unary()
            left = (value, left, right)

        elif starts_factor(token_type):
            if (
                isinstance(left, str)
                and token_type == "NUM"
            ):
                raise ValueError(
                    "Adjacent numbers are not implicit multiplication"
                )

            right = parse_unary()
            left = ("*", left, right)

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


def format_number(value):
    value = float(value)

    if value.is_integer():
        return str(int(value))

    return f"{value:.4f}".rstrip("0").rstrip(".")


def tree_to_string(node):
    if isinstance(node, str):
        return format_number(float(node))

    if node[0] == "neg":
        return f"(neg {tree_to_string(node[1])})"

    return (
        f"({node[0]} "
        f"{tree_to_string(node[1])} "
        f"{tree_to_string(node[2])})"
    )


def format_tokens(token_list):
    parts = []

    for token_type, value in token_list:
        if token_type == "END":
            parts.append("[END]")
        else:
            parts.append(f"[{token_type}:{value}]")

    return " ".join(parts)


def format_result(value):
    if value == "ERROR":
        return "ERROR"

    if float(value).is_integer():
        return str(int(value))

    return f"{value:.4f}"


def process_expression(expression):
    global tokens
    global position

    try:
        tokens = tokenize(expression)
        position = 0

        tree = parse_expression()

        if current_token()[0] != "END":
            raise ValueError("Unexpected token")

        result = evaluate(tree)

        return {
            "input": expression,
            "tree": tree_to_string(tree),
            "tokens": format_tokens(tokens),
            "result": result
        }

    except Exception:
        return {
            "input": expression,
            "tree": "ERROR",
            "tokens": "ERROR",
            "result": "ERROR"
        }


def write_output(input_path, results):
    output_path = os.path.join(
        os.path.dirname(input_path),
        "output.txt"
    )

    with open(output_path, "w") as outfile:
        for item in results:

            outfile.write(
                f"Input: {item['input']}\n"
            )

            outfile.write(
                f"Tree: {item['tree']}\n"
            )

            outfile.write(
                f"Tokens: {item['tokens']}\n"
            )

            outfile.write(
                f"Result: {format_result(item['result'])}\n\n"
            )


def evaluate_file(input_path: str) -> listresults = []

    with open(input_path, "r") as infile:
        expressions = [
            line.rstrip("\n")
            for line in infile
        ]

    for expression in expressions:
        results.append(
            process_expression(expression)
        )

    write_output(input_path, results)

    return results


if __name__ == "__main__":
    evaluate_file("input.txt")