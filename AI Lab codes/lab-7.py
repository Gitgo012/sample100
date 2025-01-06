import random
def generate_game_tree(tree_depth, branching_factor_range=(3, 5)):
    """
    Generates a random game tree with the specified depth and branching factor range.
    """
    if tree_depth == 0:
        return random.randint(-5, 5) 
    else:
        num_children = random.randint(*branching_factor_range)
        return [generate_game_tree(tree_depth - 1, branching_factor_range) for _ in range(num_children)]
def minimax(node, depth, is_maximizing_player):
    """
    Implements the Minimax algorithm to find the optimal move.
    """
    if depth == 0 or isinstance(node, int):  
        return node

    if is_maximizing_player:
        best_value = float('-infinity')
        for child in node:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('infinity')
        for child in node:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value
def alpha_beta_pruning(node, depth, alpha, beta, is_maximizing_player):
    """
    Implements the Alpha-Beta Pruning algorithm for efficient decision making.
    """
    if depth == 0 or isinstance(node, int):
        return node

    if is_maximizing_player:
        best_value = float('-infinity')
        for child in node:
            value = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('infinity')
        for child in node:
            value = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value
if __name__ == "__main__":
    tree_depth = 3
    print("Generating Game Tree...")
    game_tree = generate_game_tree(tree_depth)
    print("Game Tree:", game_tree)
    minimax_nodes_visited = 0
    best_value_minimax = minimax(game_tree, tree_depth, is_maximizing_player=True)
    print("\nMinimax Result:", best_value_minimax)
    alpha_beta_nodes_visited = 0
    best_value_alpha_beta = alpha_beta_pruning(game_tree, tree_depth, float('-infinity'), float('infinity'), is_maximizing_player=True)
    print("\nAlpha-Beta Pruning Result:", best_value_alpha_beta)
    assert best_value_minimax == best_value_alpha_beta, "Optimal solutions do not match!"
    print("\nOptimal solutions match. Alpha-Beta Pruning is correct.")

