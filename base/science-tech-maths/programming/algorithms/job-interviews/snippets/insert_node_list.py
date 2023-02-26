class Node:
    def __init__(self, value, next_node: "Node" | None = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        if self.next_node is None:
            return str(self.value)
        return " -> ".join((str(self.value), str(self.next_node)))


def insert_node_singly(linked_list: Node, node_to_insert: Node, position: int):
    node_before = linked_list

    for _ in range(1, position):
        node_before = node_before.next_node

    node_before.next_node, node_to_insert.next_node = node_to_insert, node_before.next_node


def insert_node_doubly(linked_list: Node, node_to_insert: Node, position: int):
    node_before = linked_list

    for _ in range(1, position):
        node_before = node_before.next_node

    node_after = node_before.next_node

    node_before.next_node, node_after.prev_node, node_to_insert.prev_node, node_to_insert.next_node = (
        node_to_insert,
        node_to_insert,
        node_before,
        node_after,
    )


def main():
    linked_list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(linked_list)

    insert_node_singly(linked_list, Node(42), position=2)
    print(linked_list)


if __name__ == "__main__":
    main()
