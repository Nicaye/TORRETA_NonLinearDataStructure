
from collections import deque


# Create a Node class for the Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the TORRETA Binary Tree
root = Node("T₁")

root.left = Node("O")
root.right = Node("R₁")

root.left.left = Node("R₂")
root.left.right = Node("E")

root.right.left = Node("T₂")
root.right.right = Node("A")


# Breadth-First Search (BFS)
def bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS Traversal:")
    while queue:
        current = queue.popleft()
        print(current.data, end=" → ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Depth-First Search (DFS - Preorder)
def dfs(root):
    if root is None:
        return

    print(root.data, end=" → ")

    dfs(root.left)
    dfs(root.right)


# Display the traversals
print("TORRETA - BINARY TREE")
print()

bfs(root)

print("\n")
print("DFS Traversal:")
dfs(root)

print("\n")
