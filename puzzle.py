from collections import deque

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def find_empty(state):
    return state.index(0)

def is_goal_state(state):
    return state == goal_state

def get_neighbors(state):
    empty_pos = find_empty(state)
    row, col = empty_pos // 3, empty_pos % 3
    neighbors = []
    
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = state.copy()
            new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
            neighbors.append(new_state)
    
    return neighbors

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(list(current))
        current = came_from.get(current)
    path.reverse()
    return path

def bfs(start_state):
    queue = deque([start_state])
    came_from = {tuple(start_state): None}
    
    while queue:
        current_state = queue.popleft()

        if is_goal_state(current_state):
            return reconstruct_path(came_from, tuple(current_state))

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in came_from:
                came_from[neighbor_tuple] = tuple(current_state)
                queue.append(neighbor)
    
    return None

def display_state(state):
    for i in range(3):
        print(state[i*3:i*3+3])
    print()

def solve_8_puzzle(start_state):
    print("Initial State:")
    display_state(start_state)
    
    solution_path = bfs(start_state)

    if solution_path:
        print(f"Solution found in {len(solution_path)-1} moves!")
        print("\nSolution Path:")
        for i, step in enumerate(solution_path):
            print(f"Step {i}:")
            display_state(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    start_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    solve_8_puzzle(start_state)
