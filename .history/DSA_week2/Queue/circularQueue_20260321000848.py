
# The rear.next should always point to front





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def enque(self,data):
        new_node=Node(data)
        if self.front is None:
            self.front=self.rear=new_node
            self.rear.next=self.front
            
            return
        self.rear.next=new_node
        self.rear=new_node
        self.rear.next=self.front
    def deque(self):
        if self.front is None:
            print("empty")
            return
        self.front=self.front.next
        self.rear.next=self.front