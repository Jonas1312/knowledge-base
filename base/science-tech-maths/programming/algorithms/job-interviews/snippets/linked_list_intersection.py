# two singly linked list with different length
# they intersect (have a common node)
# find the intersection node
# has to be done in O(1) space so we can't use hashtables
# no cycles

# ANSWER
# once they intersect, the lists have the same elements, since the common node has only one following node...
# we start by getting the length of each node (we might have it or we just iterate until we hit the end node)
# we put both pointers back at the beginning
# then we take the biggest list pointer and we move it forward by |A-B| nodes
# then we move each pointer forward successively until they point to the same node
# if the lists were doubly linked, we could just move backward from the end common node


class Node:
    def __init__(self, value, next_node: "Node" | "None" = None) -> None:
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        if self.next_node is None:
            return str(self.value)
        return " -> ".join((str(self.value), str(self.next_node)))

    def __len__(self) -> int:
        if self.next_node is None:
            return 1
        return 1 + len(self.next_node)


def find_intersection(list_a: Node, list_b: Node) -> Node:
    len_list_a = len(list_a)
    len_list_b = len(list_b)

    pointer_a = list_a
    pointer_b = list_b

    if len_list_a > len_list_b:
        for _ in range(len_list_a - len_list_b):
            pointer_a = pointer_a.next_node
    elif len_list_a < len_list_b:
        for _ in range(len_list_b - len_list_a):
            pointer_b = pointer_b.next_node

    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next_node
        pointer_b = pointer_b.next_node

        if pointer_a is None or pointer_b is None:
            raise ValueError

    return pointer_a


def main():
    common_tail = Node(42, Node(43, Node(44)))
    list_a = Node(1, Node(3, Node(5, common_tail)))
    list_b = Node(2, Node(4, Node(6, common_tail)))

    print(common_tail)
    print(list_a)
    print(list_b)

    print(find_intersection(list_a, list_b))


if __name__ == "__main__":
    main()
