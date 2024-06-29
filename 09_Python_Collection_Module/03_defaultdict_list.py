from collections import defaultdict

# List of edges (node1, node2)
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
    (4, 5)
]

# defaultdict with list as the default factory
graph = defaultdict(list)

# Building the adjacency list
for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)  # For undirected graphs

# Printing the adjacency list
for node, neighbors in graph.items():
    print(f'{node}: {neighbors}')
