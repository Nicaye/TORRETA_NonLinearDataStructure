
from collections import deque


# Create the TORRETA Graph
graph = {
    "T₁": ["O", "R₁"],
    "O": ["T₁", "E", "R₂"],
    "R₁": ["T₁", "A"],
    "E": ["O", "A"],
    "A": ["E", "R₁", "R₂"],
    "R₂": ["O", "A", "T₂"],
    "T₂": ["R₂"]
}


# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Depth-First Search (DFS)
def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result


# Display the traversals
print("TORRETA - GRAPH")
print()

print("BFS Traversal:")
print(" → ".join(bfs(graph, "T₁")))

print("\nDFS Traversal:")
print(" → ".join(dfs(graph, "T₁")))
