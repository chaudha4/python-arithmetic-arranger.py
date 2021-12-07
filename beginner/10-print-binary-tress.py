class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.data}"




root = Node(23)
node20 = Node(20)
node30 = Node(30)

root.left = node20
root.right = node30


def printtree(root) -> None:
    if (root == None):
        return
    
    print(f"Data is {root}")

    if (root.left != None):
        printtree(root.left)

    if (root.right != None):
        printtree(root.right)


printtree(root)