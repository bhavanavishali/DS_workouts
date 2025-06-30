class Node:
    def __init__(self,key,data):
        self.data=data
        self.key=key
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,key,val):
        temp=self.head
        while temp:
            if temp.key==key:
                temp.data=val
                return
            temp=temp.next
        
        new_node=Node(key,val)
        new_node.next=self.head
        self.head=new_node
    
    def search(self,key):
        temp=self.head
        while temp:
            if temp.key==key:
                return temp.data
            temp=temp.next
        return None
    
    def delete(self,key):
        temp=self.head
        prev=None
        while temp:
            if temp.key==key:
                if prev:
                    prev.next=temp.next
                else:
                    self.head=temp.next
            prev=temp
            temp=temp.next
        return False
class HashTable:
    def __init__(self,size):
        self.size=size
        self.items=[LinkedList() for _ in range(self.size)]
    
    def my_hash(self,key):
        return hash(key)%self.size
    
    def put(self,key,val):
        index=self.my_hash(key)
        return self.items[index].insert(key,val)
    
    def get(self,key):
        index=self.my_hash(key)
        return self.items[index].search(key)
    def delete(self,key):
        index=self.my_hash(key)
        return self.items[index].delete(key)


ht = HashTable(10)

ht.put("apple", 10)
ht.put("banana", 20)
ht.put("grape", 30)
ht.put("elppa", 40)  # Might cause a collision with "apple"

print(ht.get("banana"))  # Output: 20
print(ht.get("apple"))   # Output: 10

ht.delete("banana")
print(ht.get("banana"))  # Output: None