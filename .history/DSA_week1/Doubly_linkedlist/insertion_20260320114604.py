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
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current and current.next:
            current=current.next
        new_node.prev=current
        current.next=new_node
        
    def insert_at_position(self, pos, data):

        new_node = Node(data)
    
        # insert at head
        if pos == 1:
            new_node.next = self.head
            
            self.head.prev = new_node
            self.head = new_node
            return
    
        current = self.head
        count = 1
    
        # move to previous node
        while count < pos-1 and current:
            current = current.next
            count += 1
    
        if current is None:
            print("Position out of range")
            return
    
        # next_node = current.next
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
    
   

    
    
    def display(self):
        current=self.head
        
        while current:
            print(f"{current.data}",end='<->')
            current=current.next
            
        return
    
dl=D_linkedlist()
a=[10,20,30,40]
for i in a:
    dl.insert_at_end(i)
    
dl.display()
print("insert at position")
dl.insert_at_position(3,500)
dl.display()