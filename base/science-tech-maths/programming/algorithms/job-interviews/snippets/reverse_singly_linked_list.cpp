#include <iostream>
#include <memory>

template <typename T>
class Node {
   public:
    T m_data;
    Node* p_next_node;

    Node(T data) : m_data(data), p_next_node(nullptr) {}

    // operator << is not a member function, but needs access to member parameters
    // we define it as friend, even though it's useless here because everything is public...
    friend std::ostream& operator<<(std::ostream& out, const Node& node) {
        if (node.p_next_node) {
            return out << node.m_data << " -> " << *node.p_next_node;
        }
        return out << node.m_data;
    }
};

int main() {
    Node node_1(1);
    Node node_2(2);
    Node node_3(3);
    Node node_4(4);

    node_1.p_next_node = &node_2;
    node_2.p_next_node = &node_3;
    node_3.p_next_node = &node_4;

    std::cout << node_1 << std::endl;

    // reverse list
    decltype(node_1)* prev = nullptr;  //    Inspects the declared type of an entity.
    auto* head = &node_1;
    // int z = std::exchange(x, y);
    // x is assigned the value of y,
    // z is assigned the value that x had initially.
    // 1st call: prev is assigned head, returns prev
    // 2nd call: head->p_next_node is assigned prev, the current node has been linked to the previous one
    // head is set to head->p_next_node (next node in the list to revert)
    while (head != nullptr) {
        head = std::exchange(head->p_next_node, std::exchange(prev, head));
    }

    std::cout << node_4 << std::endl;

    return 0;
}
