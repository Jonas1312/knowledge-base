#include <iostream>

// Given a node prev_node, insert a
// new node after the given prev_node

template <typename T>
class Node {
   public:
    T m_data;
    Node* m_next_node;

    Node(T data) : m_data(data), m_next_node(nullptr) {}

    // operator << is not a member function, but needs access to member parameters
    // we define it as friend, even though it's useless here because everything is public...
    friend std::ostream& operator<<(std::ostream& out, const Node& node) {
        if (node.m_next_node) {
            return out << node.m_data << " -> " << *node.m_next_node;
        }
        return out << node.m_data;
    }
};

template <typename T>
void insertAfter(Node<T>* prev_node, T new_data) {
    // 1. Check if the given prev_node is NULL
    if (prev_node == nullptr) {
        std::cout << "the given previous node cannot be NULL";
        return;
    }

    // 2. Allocate new node
    Node* new_node = new Node(new_data);

    // 3. Put in the data
    // new_node->data = new_data;

    // 4. Make next of new node as
    // next of prev_node
    new_node->next = prev_node->next;

    // 5. move the next of prev_node
    // as new_node
    prev_node->next = new_node;

    // other solution
    // new_node->next = std::exchange(prev_node->next, new_node);
}
