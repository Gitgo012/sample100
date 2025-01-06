import heapq

class Node:
    def __init__(self, level, weight, profit, bound, items):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.items = items

    def __lt__(self, other):
        return self.bound < other.bound 

def calculate_bound(node, n, W, weights, profits):
    if node.weight >= W:
        return 0 
    bound = node.profit
    total_weight = node.weight
    j = node.level + 1
    while j < n and total_weight + weights[j] <= W:
        total_weight += weights[j]
        bound += profits[j]
        j += 1
    if j < n:
        bound += (W - total_weight) * (profits[j] / weights[j])
    
    return bound

def knapsack_A_star(W, weights, profits):
    n = len(weights)
    initial_node = Node(0, 0, 0, 0, [-1] * n)
    initial_node.bound = calculate_bound(initial_node, n, W, weights, profits)
    priority_queue = [initial_node]
    heapq.heapify(priority_queue)
    best_profit = 0
    best_solution = None

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        
        if current_node.bound > best_profit: 
            for choice in [0, 1]:
                child = Node(
                    current_node.level + 1,
                    current_node.weight + choice * weights[current_node.level] if current_node.level < n else 0,
                    current_node.profit + choice * profits[current_node.level] if current_node.level < n else 0,
                    bound=0,
                    items = current_node.items[:]
                )

                if current_node.level < n:
                    child.items[current_node.level] = choice
                if child.weight <= W and child.profit > best_profit:
                    best_profit = child.profit
                    best_solution = child.items
                child.bound = calculate_bound(child, n, W, weights, profits)
                if child.bound > best_profit:
                    heapq.heappush(priority_queue, child)

    return best_profit, best_solution
weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
W = 5
max_profit, solution = knapsack_A_star(W, weights, profits)
print("Maximum Profit:", max_profit)
print("Solution Vector:", solution)
