# Define rules as functions
def de_morgan_and(expr):
    return expr.replace("(A . B)'", "A' + B'").replace("(A1 . A2 . A3 ... An)'", "A1' + A2' + ... + An'")

def de_morgan_or(expr):
    return expr.replace("(A + B)'", "A' . B'").replace("(A1 + A2 + ... + An)'", "A1' . A2' . ... . An'")

def transposition(expr):
    return expr.replace("A.B + A'.C", "(A + C) . (A' + B)")

def duality(expr):
    return expr.replace("A.(B+C)", "A+(B.C)").replace("A+(B.C)", "(A+B).(A+C)")

def simplify_rules(expr):
    rules = [
        ("A.0", "0"),
        ("A + 1", "1"),
        ("A.1", "A"),
        ("A + 0", "A"),
        ("A + A", "A"),
        ("A.A", "A"),
        ("A + A'", "1"),
        ("A.A'", "0"),
        ("((A)')'", "A"),
        ("A + B", "B + A"),
        ("A.B", "B.A"),
        ("A+(B+C)", "(A+B)+C"),
        ("A.(B.C)", "(A.B).C"),
        ("A.(B+C)", "(A.B)+(A.C)"),
        ("A.(A+B)", "A"),
        ("A + A.B", "A"),
        ("A + A'.B", "A + B"),
        ("A.(A' + B)", "A.B")
    ]
    for rule, result in rules:
        expr = expr.replace(rule, result)
    return expr

# Define a function to step through simplifications
def simplify_expression(expr):
    prev_expr = ""
    while prev_expr != expr:  # Keep simplifying until no further simplifications are made
        prev_expr = expr
        expr = de_morgan_and(expr)
        expr = de_morgan_or(expr)
        expr = transposition(expr)
        expr = duality(expr)
        expr = simplify_rules(expr)
        print(f"Simplified to: {expr}")
    return expr

# Starting expression
expression = "A.B + B.C' + A.C"

# Simplify step by step
simplified_expression = simplify_expression(expression)
print(f"Final Simplified Expression: {simplified_expression}")

# Compare with RHS
rhs = "A.C + B.C'"
if simplified_expression == rhs:
    print("The expression has been successfully proven!")
else:
    print("The expression could not be proven.")
