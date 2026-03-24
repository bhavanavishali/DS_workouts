class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        # Step 1: remove duplicate if exists
        prev = None
        current = self.top

        while current:
            if current.data == data:
                # remove the node
                if prev is None:
                    self.top = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next

        # Step 2: push new node to top
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next