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
        
    def delete_at_head(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=self.head.next
        return temp.data
        
    def insert_at_position(self,p,data):
        new_node=Node(data)
        current=self.head
        for _ in range(p-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
        return
    
    def delete_duplicate(self):
        seen=set()
        current=self.head
        prev=None
        while current:
            if current.data in seen:
                prev.next=current.next
            else:
                seen.add(current.data)
                prev=current
            current=current.next
            
    def middle_insert(self,data):
        new_node=Node(data)
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        if slow:
            new_node.next=slow.next
            slow.next=new_node
            
            
    def       
                
    
        
    def display(self):
        if self.head is None:
            return "underflow"
        current=self.head
        while current:
            
            print(current.data,end=' <-')
            current=current.next
        return
    
    
    
l=LinkedList()

l.insert_at_head(10)
l.insert_at_head(20)
l.insert_at_head(56)
l.insert_at_head(120)
l.insert_at_head(556)
l.insert_at_head(240)
l.insert_at_head(586)
l.insert_at_head(280)
l.display()
# l.delete_at_head()
print("******insert at position****")
l.insert_at_position(2,100)
l.display()
print("**********remove duplications from linkedlist************")
l.delete_duplicate()
l.display()
print("***middle insert******")
l.middle_insert(10000)
l.display()


        