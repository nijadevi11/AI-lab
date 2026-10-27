import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)     # 0 = blank


# Manhattan Distance
def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            current_row = i // 3
            current_col = i % 3

            goal_pos = tile - 1
            goal_row = goal_pos // 3
            goal_col = goal_pos % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate successor states
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


# A* Algorithm
def a_star(start):

    # (f, g, state, path)
    frontier = []

    g = 0
    h = manhattan(start)
    f = g + h

    heapq.heappush(frontier, (f, g, start, []))

    explored = set()

    while frontier:

        f, g, state, path = heapq.heappop(frontier)

        if state == GOAL:
            return path

        if state in explored:
            continue

        explored.add(state)

        for child, move in get_neighbors(state):

            if child not in explored:

                new_g = g + 1
                new_f = new_g + manhattan(child)

                heapq.heappush(
                    frontier,
                    (new_f, new_g, child, path + [(move, child)])
                )

    return None


# Display board
def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# ---------------- INPUT ----------------

print("8-Puzzle using A*")

print("Enter the puzzle board")
print("Use _ for blank space")

start = []

for i in range(3):
    row = input("Enter row " + str(i + 1) + ": ").split()

    for value in row:
        if value == '_':
            start.append(0)
        else:
            start.append(int(value))

start = tuple(start)

print("\nInitial State:")
display(start)


# ---------------- SOLVE ----------------

solution = a_star(start)


if solution is not None:

    print("Solution Found")

    for number, (move, state) in enumerate(solution, 1):

        print("Move", number, ":", move)
        display(state)

    print("Goal State Reached")
    print("Solution Cost =", len(solution))

else:
    print("No solution found")
