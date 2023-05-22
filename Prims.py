from collections import defaultdict

# Function to find the vertex with the minimum key value
def min_key(vertices, key, visited):
    min_key = float('inf')
    min_vertex = None

    for vertex in vertices:
        if key[vertex] < min_key and not visited[vertex]:
            min_key = key[vertex]
            min_vertex = vertex

    return min_vertex

# Function to print the minimum spanning tree
def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")

# Greedy Search Algorithm for Prim's Minimum Spanning Tree
def prim_mst(graph):
    num_vertices = len(graph)
    key = [float('inf')] * num_vertices  # Key values used to pick minimum weight edge
    parent = [None] * num_vertices  # Array to store constructed MST
    visited = [False] * num_vertices  # Array to track visited vertices

    # Start with the first vertex as the root
    key[0] = 0
    parent[0] = -1

    for _ in range(num_vertices - 1):
        u = min_key(range(num_vertices), key, visited)
        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph)

# Get user input for the graph
num_vertices = int(input("Enter the number of vertices: "))
graph = defaultdict(dict)

for i in range(num_vertices):
    for j in range(num_vertices):
        weight = int(input(f"Enter the weight between vertex {i} and {j}: "))
        graph[i][j] = weight
        graph[j][i] = weight

# Run Prim's Minimum Spanning Tree algorithm
prim_mst(graph)
