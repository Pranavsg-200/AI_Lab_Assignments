from heapq import heappop, heappush

# Game state class
class GameState:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic
        self.g = 0

    def __lt__(self, other):
        return (self.heuristic + self.g) < (other.heuristic + other.g)

# Heuristic function: Manhattan Distance
def manhattan_distance(state, goal_state):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i][j]

            if tile == 0:
                continue

            goal_pos = find_tile_position(goal_state, tile)
            distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])

    return distance

# Helper function: Find tile position in the game state
def find_tile_position(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)

# Generate next possible states
def generate_next_states(state):
    next_states = []
    zero_pos = find_tile_position(state, 0)

    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        dx, dy = move
        new_pos = (zero_pos[0] + dx, zero_pos[1] + dy)

        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_state = [list(row) for row in state]
            new_state[zero_pos[0]][zero_pos[1]] = state[new_pos[0]][new_pos[1]]
            new_state[new_pos[0]][new_pos[1]] = 0
            next_states.append(new_state)

    return next_states

# A* search algorithm
def astar_search(initial_state, goal_state, heuristic_func):
    open_list = []
    closed_list = set()

    start_node = GameState(initial_state, heuristic_func(initial_state, goal_state))
    start_node.g = 0
    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)

        if current_node.state == goal_state:
            return current_node.state

        closed_list.add(tuple(map(tuple, current_node.state)))

        # Generate next possible states
        next_states = generate_next_states(current_node.state)

        for next_state in next_states:
            if tuple(map(tuple, next_state)) in closed_list:
                continue

            g_score = current_node.g + 1
            h_score = heuristic_func(next_state, goal_state)
            next_node = GameState(next_state, h_score)
            next_node.g = g_score

            heappush(open_list, next_node)

    return None

# Get user input for the initial and goal states
print("Enter the initial state (3x3 matrix):")
initial_state = [list(map(int, input().split())) for _ in range(3)]

print("Enter the goal state (3x3 matrix):")
goal_state = [list(map(int, input().split())) for _ in range(3)]

# Run A* search
result = astar_search(initial_state, goal_state, manhattan_distance)

# Print the result
if result:
    print("Goal state reached:")
    for row in result:
        print(*row)
else:
    print("Goal state not found.")
