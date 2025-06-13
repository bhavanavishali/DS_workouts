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
        return
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        return 
    
    def insert_at_position(self,data,position):
        new_node=Node(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        for _ in range(position-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node            
        
        
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end=' ->')
            current=current.next
        print(None)   
        
ll=LinkedList()
a=[5,9,7,6,7]
for i in a:
    ll.insert_at_end(i)
ll.display()



ll.insert_at_position(1000,3)
ll.display()