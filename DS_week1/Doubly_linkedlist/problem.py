class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class D_linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head is not None:
            self.head.prev=new_node
            new_node.next=self.head
            
        self.head=new_node
        
    def delete_at_head(self):
        if self.head is None:
            print("empty")
            return
        self.head=self.head.next
        self.head.prev=None
        return
    def middle_element(self):
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if slow:
            return slow.data
        return None
        
        
        
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end='<->')
            current=current.next
        print(None)

ll=D_linkedlist()
arr=[4,8,9,3,54]
for i in arr:
    ll.insert_at_head(i)
    
ll.display()
# print("delelte at head")
# ll.delete_at_head()
# ll.display()

print("middle element",ll.middle_element())


# new


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class D_linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head is not None:
            new_node.next=self.head
            self.head.prev=new_node
            
        self.head=new_node
        
        
    def delete_at_position(self,position):
        if position==0:
            self.head=self.head.next
            self.head.prev=None
            return
        current=self.head
        
        for _ in range(position-1):
            if current is None:
                return print(" found")  # position out of range
            current=current.next
        current.next=current.next.next
        
        return 
    def middle_element(self):
        
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if slow:
            return slow.data
            
            
            
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end='<->')
            current=current.next
        print(None)
        
ll=D_linkedlist()
arr=[4,5,6]
for i in arr:
    ll.insert_at_head(i)
ll.display()
print("delete at Position")
ll.delete_at_position(2)
ll.display()
print("mid element",ll.middle_element())
