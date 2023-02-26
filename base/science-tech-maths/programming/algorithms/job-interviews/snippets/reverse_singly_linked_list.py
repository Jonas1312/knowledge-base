class Node:
    def __init__(self, data, next_node: "Node" | "None" = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        if self.next_node:
            return " -> ".join((str(self.data), str(self.next_node)))
        return str(self.data)


def main():
    linked_list = Node(1, Node(2, Node(3)))
    print(linked_list)

    prev_ = None
    curr_ = linked_list
    next_ = curr_.next_node

    while next_:
        next_ = curr_.next_node
        curr_.next_node = prev_
        prev_ = curr_
        curr_ = next_

    # second version:
    # while curr_:
    #     curr_.next_node = prev_
    #     prev_ = curr_
    #     curr_ = next_
    #     if not curr_:
    #         break
    #     next_ = curr_.next_node

    linked_list = prev_
    print(linked_list)


if __name__ == "__main__":
    main()
