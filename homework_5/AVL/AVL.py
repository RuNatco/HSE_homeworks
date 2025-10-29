class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if not node:
        return 0
    return node.height


def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(y):
    x = y.left
    temp_right = x.right
    x.right = y
    y.left = temp_right
    update_height(y)
    update_height(x)
    return x


def left_rotate(x):
    y = x.right
    temp_right = y.left
    y.left = x
    x.right = temp_right
    update_height(x)
    update_height(y)
    return y


def insert(node, value):
    if not node:
        return Node(value)
    elif value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    else:
        return node

    update_height(node)

    balance = get_balance(node)

    if balance > 1 and value < node.left.value:
        return right_rotate(node)

    if balance < -1 and value > node.right.value:
        return left_rotate(node)

    if balance > 1 and value > node.left.value:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and value < node.right.value:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def min_value_node(node):
    if node is None or node.left is None:
        return node
    return min_value_node(node.left)


def delete(node, value):
    if not node:
        return node
    elif value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value_node(node.right)
        node.value = temp.value
        node.right = delete(node.right, temp.value)

    update_height(node)

    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def search(node, value):
    if node is None or node.value == value:
        return node

    if value < node.value:
        return search(node.left, value)
    return search(node.right, value)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = insert(self.root, value)

    def delete(self, value):
        self.root = delete(self.root, value)

    def search(self, value):
        return search(self.root, value)
