
def dls(graph, node, goal, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return None

    for child in graph.get(node, []):
        if child not in path:
            result = dls(graph, child, goal,
                         limit - 1, path + [node])

            if result is not None:
                return result

    return None


def ids(graph, initial, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Depth Limit:", depth)

        result = dls(graph, initial, goal, depth, [])

        if result is not None:
            print("Goal Found!")
            print("Solution Path:", " -> ".join(result))
            print("Solution Depth:", len(result) - 1)
            return

    print("Goal not found within maximum depth.")


# Main Program
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    children = input("Enter children (- for none): ")

    if children == "-":
        graph[node] = []
    else:
        graph[node] = children.split()

initial = input("Enter initial state: ")
goal = input("Enter goal state: ")
max_depth = int(input("Enter maximum depth: "))

ids(graph, initial, goal, max_depth)
