from collections import defaultdict, deque

# Recursive Depth-First Search (DFS)
def recursive_dfs(graph, visited, node):
    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            recursive_dfs(graph, visited, neighbor)

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Get user input for the graph
graph = defaultdict(list)

num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u, v): ").split())
    graph[u].append(v)
    graph[v].append(u)

start_node = int(input("Enter the starting node: "))

# Perform DFS and BFS
print("DFS traversal: ", end='')
recursive_dfs(graph, set(), start_node)
print()

print("BFS traversal: ", end='')
bfs(graph, start_node)
print()
