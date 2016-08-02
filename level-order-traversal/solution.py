class Node:
    def __init__(self, data = "", children = []):
        self.data = data
        self.children = children

def level_order_traversal(root):
    queue = [root]
    while len(queue) > 0:
        cur = queue.pop(0)
        for node in cur.children:
            queue.append(node)
        print cur.data

b = Node("b", [Node("d")])
c = Node("c", [Node("e"), Node("f")])
root = Node("a", [b,c])
level_order_traversal(root)
