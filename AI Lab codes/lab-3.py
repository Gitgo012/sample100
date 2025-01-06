from collections import deque

def valid_transitions(state):
    farmer, goat, wolf, cabbage = state
    if farmer != goat and wolf == goat:
        return False
    if farmer != goat and goat == cabbage:
        return False
    return True

def get_neighbours(state):
    farmer, goat, wolf, cabbage = state
    possible_transitions = []

    moves = [
        (1 - farmer, goat, wolf, cabbage), 
        (1 - farmer, 1 - goat, wolf, cabbage) if farmer == goat else None, 
        (1 - farmer, goat, wolf, 1 - cabbage) if farmer == cabbage else None,  
        (1 - farmer, goat, 1 - wolf, cabbage) if farmer == wolf else None 
    ]

    for move in moves:
        if move and valid_transitions(move):
            possible_transitions.append(move)

    return possible_transitions

def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited_node = set([initial])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path + [current_state]

        for next_state in get_neighbours(current_state):
            if next_state not in visited_node:
                visited_node.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None

initial_state = (0, 0, 0, 0)  
goal_state = (1, 1, 1, 1)  

solution = bfs(initial_state, goal_state)
if solution:
    print("Found solution, the steps are as follows:")
    for step in solution:
        print(step)
else:
    print("No solution found")
