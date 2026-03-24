class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head is not None:
            new_node.next=self.head
            self.head=new_node
            return
        self.head=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end=' ->')
            current=current.next
        print(None)


    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev


ll=LinkedList()
arr=[1,2,8,6]
for i in arr:
    ll.insert_at_head(i)
ll.display()
print("Reversed list")
ll.reverse()
ll.display()

            



