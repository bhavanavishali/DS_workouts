class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
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
        
    def delete_even(self):

        current = self.head
        prev = None

        while current and current.next:

            if current.next.data % 2 == 0:

                if prev is None:
                    self.head = current.next
                    current = self.head
                else:
                    prev.next = current.next
                    current = current.next

            else:
                prev = current
                current = current.next
        
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
            
 
        
l=Linkedlist()
a=[10,23,3,40]
for i in a:
    l.insert_at_end(i)
l.display()

print("*********")
l.delete_even()
l.display()
