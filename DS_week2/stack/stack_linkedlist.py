class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack Underflow"
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.data if self.top else "Stack is empty"

# Test
s = LinkedStack()
s.push(1)
s.push(2)
print(s.pop())  # 2
print(s.peek())  # 1
