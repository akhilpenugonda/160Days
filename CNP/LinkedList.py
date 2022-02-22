class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(13)
b = Node(15)
a.next = b
print(a.next.data)