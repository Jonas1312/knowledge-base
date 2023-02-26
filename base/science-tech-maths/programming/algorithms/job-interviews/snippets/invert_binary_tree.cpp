#include <iostream>
#include <map>
#include <memory>

struct Node {
    int m_data;
    Node *p_left_child;
    Node *p_right_child;

    Node(int value) : m_data(value), p_left_child(nullptr), p_right_child(nullptr) {}

    friend std::ostream &operator<<(std::ostream &out, const Node &node) {
        out << "Node " << node.m_data;
        out << ": [";
        if (node.p_left_child) {
            out << (*node.p_left_child).m_data;
        }
        out << " ; ";
        if (node.p_right_child) {
            out << (*node.p_right_child).m_data;
        }
        out << "]" << std::endl;

        if (node.p_left_child) {
            out << *node.p_left_child;
        }
        if (node.p_right_child) {
            out << *node.p_right_child;
        }
        return out;
    }

   private:
    Node() {}
};

void invert(Node *input_graph_root) {
    if (input_graph_root != nullptr) {
        // swap adresses values
        std::swap(input_graph_root->p_left_child, input_graph_root->p_right_child);
        // left = invert(right)
        invert(input_graph_root->p_left_child);
        // right = invert(left)
        invert(input_graph_root->p_right_child);
    }
}

int main(int argc, char const *argv[]) {
    Node root(1);
    Node node_42(42);
    Node node_43(43);
    Node node_44(44);
    Node node_2(2);

    root.p_left_child = &node_42;
    node_42.p_left_child = &node_43;
    node_43.p_left_child = &node_44;
    root.p_right_child = &node_2;

    std::cout << root << std::endl;

    invert(&root);

    std::cout << root << std::endl;
    return 0;
}
