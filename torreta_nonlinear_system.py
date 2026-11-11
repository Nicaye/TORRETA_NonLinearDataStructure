
from collections import deque

# ==========================================
#       TORRETA - NON-LINEAR DATA STRUCTURE
# ==========================================

# ---------- BINARY TREE ----------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node("T₁")
root.left = Node("O")
root.right = Node("R₁")
root.left.left = Node("R₂")
root.left.right = Node("E")
root.right.left = Node("T₂")
root.right.right = Node("A")


def tree_bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def tree_dfs(root):
    if root is None:
        return []

    result = [root.data]
    result += tree_dfs(root.left)
    result += tree_dfs(root.right)

    return result


def display_tree():
    print("\n" + "=" * 48)
    print("                 BINARY TREE")
    print("=" * 48)
    print("""
                  T₁
                /    \\
               O      R₁
              / \\    / \\
             R₂  E  T₂  A
    """)
    print("-" * 48)
    print("[1] Breadth-First Search (BFS)")
    print("[2] Depth-First Search (DFS)")
    print("[3] Back to Main Menu")
    print("-" * 48)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nBINARY TREE - BFS")
        print("Level-by-level traversal:")
        print(" → ".join(tree_bfs(root)))

    elif choice == "2":
        print("\nBINARY TREE - DFS")
        print("Preorder traversal:")
        print(" → ".join(tree_dfs(root)))

    elif choice == "3":
        return

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")

    input("\nPress ENTER to continue...")


# ---------- GRAPH ----------
graph = {
    "T₁": ["O", "R₁"],
    "O": ["T₁", "E", "R₂"],
    "R₁": ["T₁", "A"],
    "E": ["O", "A"],
    "A": ["E", "R₁", "R₂"],
    "R₂": ["O", "A", "T₂"],
    "T₂": ["R₂"]
}


def graph_bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def graph_dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, result)

    return result


def display_graph():
    print("\n" + "=" * 48)
    print("                    GRAPH")
    print("=" * 48)
    print("""
          T₁ -------- O
           \\          | \\
            \\         |  \\
             R₁       E   R₂
               \\     /   /
                \\   /   /
                  A     T₂
    """)
    print("-" * 48)
    print("Starting Vertex: T₁")
    print("-" * 48)
    print("[1] Breadth-First Search (BFS)")
    print("[2] Depth-First Search (DFS)")
    print("[3] Back to Main Menu")
    print("-" * 48)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nGRAPH - BFS")
        print("Traversal:")
        print(" → ".join(graph_bfs(graph, "T₁")))

    elif choice == "2":
        print("\nGRAPH - DFS")
        print("Traversal:")
        print(" → ".join(graph_dfs(graph, "T₁")))

    elif choice == "3":
        return

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")

    input("\nPress ENTER to continue...")


# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n")
        print("=" * 48)
        print("       TORRETA NON-LINEAR DATA STRUCTURE")
        print("=" * 48)
        print("          Explore and Traverse")
        print("-" * 48)
        print("[1] View Binary Tree")
        print("[2] View Graph")
        print("[3] Exit Program")
        print("=" * 48)

        choice = input("Choose a data structure: ")

        if choice == "1":
            display_tree()

        elif choice == "2":
            display_graph()

        elif choice == "3":
            print("\nThank you for using the TORRETA program!")
            print("Program closed.")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
            input("Press ENTER to try again...")


if __name__ == "__main__":
    main()
