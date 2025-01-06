import matplotlib.pyplot as plt
import networkx as nx

variables = ["A", "B", "C", "D"]
domains = {
    "A": [1, 2, 3, 4, 5],
    "B": [2, 3, 4, 5, 6],
    "C": [3, 4, 5, 6, 7],
    "D": [5, 6, 7, 8]
}

N_UC = 3
unary_constraints = [
    ("A", "<", 5),
    ("B", ">", 3),
    ("D", "<", 8)  
]

N_BC = 3
binary_constraints = [
    ("A", "<", "B", "+", 1),
    ("B", ">", "C", "+", 2),
    ("D", ">", "A", "+", 2)  
]

def unary(domains, constraints):
    for var, op, const in constraints:
        if op == "<":
            domains[var] = [val for val in domains[var] if val < const]
        elif op == ">":
            domains[var] = [val for val in domains[var] if val > const]
    return domains

def binary(domains, constraints):
    for var1, op1, var2, ops2, const in constraints:
        new_domain = []
        for val in domains[var1]:
            if op1 == "<" and any(val < (other_val + const) for other_val in domains[var2]):
                new_domain.append(val)
            elif op1 == ">" and any(val > (other_val + const) for other_val in domains[var2]):
                new_domain.append(val)
        domains[var1] = new_domain
    return domains

def draw_graph(variables, constraints, domains, title):
    G = nx.DiGraph()
    for var in variables:
        G.add_node(var, label=f"{var}\n{domains[var]}")

    for var1, _, var2, _, _ in constraints:
        G.add_edge(var1, var2)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels)
    plt.title(title)
    plt.show()

domains = unary(domains, unary_constraints)
draw_graph(variables, binary_constraints, domains, "Constraint Graph (Unary)")

domains = binary(domains, binary_constraints)
draw_graph(variables, binary_constraints, domains, "Constraint Graph (Binary)")
