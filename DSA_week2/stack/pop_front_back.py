# To support pop from both ends in O(1), the best structure is a Doubly Linked List.




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=self.tail=new_node
            return
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
        
    def pop_front(self):
        if self.head is None:
            print("empty stack")
            return
        val=self.head.data
        self.head=self.head.next
        self.head.prev=None
        return val
        
    def pop_back(self):
        if self.tail is None:
            print("empty stack")
            return
        val=self.tail.data
        self.tail=self.tail.prev
        self.tail.next=None
        return val
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
            
s=Stack()
arr=[10,20,30,40]
for i in arr:
    s.push(i)
    
s.display()

print("front")
print(s.pop_front())
print("bak")
print(s.pop_back())
s.display()