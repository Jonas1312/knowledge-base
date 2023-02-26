def is_symmetric(left_node, right_node):
    if left_node.value != right_node.value:
        return False
    check_out = is_symmetric(left_node.left_node, right_node.right_node)
    check_in = is_symmetric(left_node.right_node, right_node.left_node)
    return check_out and check_in
