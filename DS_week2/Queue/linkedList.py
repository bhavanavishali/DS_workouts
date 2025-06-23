class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front =self.rear =new_node
            return
        self.rear.next=new_node
        self.rear =new_node

    def dequeue(self):
        if self.front is None:
            self.rear=None
            return 
        tem=self.front
        self.front=tem.next
        return tem.data


    def peek(self):
        return self.front.data if self.front else "Queue is empty"
    

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
x=q.dequeue()
print("delete element",x)
x=q.dequeue()
print("delete element",x)




