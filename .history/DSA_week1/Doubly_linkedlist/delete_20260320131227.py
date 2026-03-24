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
            return
        self.head=self.head.next
        self.head.prev=None
        
    def delete_at_end(self):
        if self.head is None:
            print("empty")
            return
        current=self.head
        while current.next.next:
            current=current.next
        current.next=None
        
    def sort_d(self):
        temp1=self.head
        while temp1:
            temp2=temp1.next
            while temp2:
                if temp1.data > temp2.data:
                    temp1.data,temp2.data =temp2.data,temp1.data
                temp2=temp2.next
            temp1=temp1.next
            

                
        

        
        
            
    
   

    
    
    def display(self):
        current=self.head
        
        while current:
            print(f"{current.data}",end='<->')
            current=current.next
            
        return
    
dl=D_linkedlist()
a=[200,450,10,20,30,40]
for i in a:
    dl.insert_at_head(i)
    
dl.display()
print("insert at position")
dl.insert_at_position(3,500)
dl.display()

print("*****")
dl.sort_d()
dl.display()