
# DFS Methods in Binary Tree
# Nicoleit Torreta

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the binary tree using the letters of NICOLEIT TORRETA
letters = list("NICOLEITTORRETA")


def create_tree(letters):
    nodes = [Node(letter) for letter in letters]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]

        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


# DFS Preorder: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# DFS Inorder: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# DFS Postorder: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main Program
root = create_tree(letters)

print("BINARY TREE: NICOLEIT TORRETA")
print("\nDFS PREORDER:")
preorder(root)

print("\n\nDFS INORDER:")
inorder(root)

print("\n\nDFS POSTORDER:")
postorder(root)

print()
