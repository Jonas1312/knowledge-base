# BFS uses the Queue data structure
# depth-first algorithms use the Stack data structure.


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, child_node: "Node") -> "Node":
        assert isinstance(child_node, Node)
        self.children.append(child_node)
        # print(f"node {self.value}: {self.children}")
        return self


# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(d) where d is the max depth.
def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)


# Time complexity: O(n) where n is the number of nodes.
# Space complexity: O(b) where b is maximum breadth.
def bfs(node):
    # print(node.value)
    for child in node.children:
        print(child.value)
    for child in node.children:
        bfs(child)


def main():
    root = Node(value=1)
    root.add_child(Node(42).add_child(Node(43).add_child(Node(44))))
    root.add_child(Node(2))
    print("depth:")
    dfs(root)
    print("breadth:")
    bfs(root)


if __name__ == "__main__":
    main()
