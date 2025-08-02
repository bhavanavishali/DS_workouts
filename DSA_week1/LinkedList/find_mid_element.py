class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head is not None:
            new_node.next=self.head
            self.head=new_node
            return
        self.head=new_node
        return
    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
        print(None)
        
    def middle_element(self,data):
        if self.head is None:
            return
        slow=self.head
        fast=self.head
        print(fast.data)

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if slow:
            new_node=Node(data)
            new_node.next=slow.next
            slow.data=new_node.data
            
            
        return None
            
    
ll=Linkedlist()
arr=[4,5,6,7,8,2]
for i in arr:
    ll.insert_at_head(i)
    
ll.display()

# print("mid element",ll.middle_element())

print("***************")
ll.middle_element(100)
ll.display()