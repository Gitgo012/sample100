def parse_rule(rule):

    if "IF" in rule and "THEN" in rule:
        parts = rule.split(" THEN ")
        condition = parts[0].replace("IF ", "").strip()
        consequent = parts[1].strip()
        return condition, consequent
    return None, None


def evaluate_condition(condition, facts):

    condition = condition.replace("AND", "and").replace("OR", "or").replace("NOT", "not")
    for fact, value in facts.items():
        condition = condition.replace(fact, str(value))
    try:
        return eval(condition)
    except:
        return False


def modus_tollens(rules, goal, facts):

    additional_goals = set()
    for rule in rules:
        condition, consequent = parse_rule(rule)
        if consequent == goal:
            if evaluate_condition(condition, facts):
                print(f"Goal {goal} is satisfied using rule: {rule}")
                return True
            else:
                additional_goals.add(condition)
    
    if not additional_goals:
        print(f"Goal {goal} cannot be satisfied.")
        return False

    print(f"New goals to satisfy: {additional_goals}")
    for new_goal in additional_goals:
        sub_goal_vars = [var for var in facts.keys() if var in new_goal]
        for var in sub_goal_vars:
            if facts[var]:
                print(f"Sub-goal {var} satisfied.")
                return True
        print(f"Sub-goal {new_goal} cannot be directly satisfied. Further evaluation needed.")
    return False



variables = ['A', 'B', 'C', 'D']
rules = [
    "IF A AND B THEN C",
    "IF C OR NOT D THEN B",
    "IF A AND NOT C THEN D",
    "IF D THEN A",
    "IF B AND C THEN D"
]
facts = {"A": True, "B": False, "C": False, "D": True}
goal = "C"


if modus_tollens(rules, goal, facts):
    print("Inference complete- Goal is satisfied.")
else:
    print("Inference complete- Goal cannot be satisfied.")
