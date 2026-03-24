def revers_stack(stack):
    temp=[]
    while stack:
        temp.append(stack.pop())
    return temp

stack=[4,5,6,3,10]
print("reverse",revers_stack(stack))


# method 2 using recursion


stack = [1, 2, 3, 4]

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    if stack:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        
    def pop(self):
        if self.top is None:
            return None
        
        value=self.top.data
        self.top=self.top.next
        return value
        
    def is_empty(self):
        return self.top is None
        
    def display(self):
        current=self.top
        while current:
            print(f"|{current.data}|")
            current=current.next


def reverse_stack(stack):

    new_stack = Stack()

    while not stack.is_empty():
        value = stack.pop()
        new_stack.push(value)

    return new_stack


s=Stack()

arr=[4,8,3,5]

for i in arr:
    s.push(i)

print("Original Stack")
s.display()

s = reverse_stack(s)

print("Reversed Stack")
s.display()