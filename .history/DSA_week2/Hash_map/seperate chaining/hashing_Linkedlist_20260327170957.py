class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
    

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,key,val):
        temp=self.head

        while temp:
            if temp.key==key:
                temp.val=val
                return
            temp=temp.next

        new_node=Node(key,val)
        new_node.next=self.head
        self.head=new_node
        
    def delete(self,key):
        temp=self.head
        prev=None

        while temp:
            if temp.key==key:
                if prev:
                    prev.next=temp.next
                else:
                    self.head=temp.next
                return

            prev=temp
            temp=temp.next
            
    def search(self,key):
        temp=self.head

        while temp:
            if temp.key==key:
                return temp.val
                
            temp=temp.next
            
        return None
        
    def display(self):
        temp=self.head

        while temp:
            print(f"{temp.key}-{temp.val}",end=" -> ")
            temp=temp.next
            
        print()
    

class HashTable:
    def __init__(self,size):
        self.size=size
        self.items=[LinkedList() for _ in range(self.size)]
        
    def myhash(self,key):
        return hash(key)%self.size
        
    def put(self,key,val):
        index=self.myhash(key)
        self.items[index].insert(key,val)
        
    def delete(self,key):
        index=self.myhash(key)
        self.items[index].delete(key)
        
    def get(self,key):
        index=self.myhash(key)
        return self.items[index].search(key)
        
    def display(self):
        for i in range(self.size):
            print(f"{i}:",end=" ")
            self.items[i].display()


d={
    "apple":5,
    "banana":4,
    "kiwi":3
}

h=HashTable(5)

for key,val in d.items():
    h.put(key,val)

h.display()