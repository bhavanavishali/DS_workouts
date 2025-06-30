class HashTable:
    
    def __init__(self,size):
        self.size=size
        self.items=[[] for _ in range(self.size)]
        self.count=0
    def my_hash(self,key):
        return hash(key)%self.size
        
    def insert(self,key,val):
        index=self.my_hash(key)
        for pair in self.items[index]:
            if pair[0]==key:
                pair[1]=val
                return
        self.items[index].append([key,val])
        self.count+=1
        if self.count/ self.size >0.7:
            self.rehashing(up=True)
            
    def delete_item(self,key):
        index=self.my_hash(key)
        for  i,pair in enumerate(self.items[index]):
            if pair[0]==key:
                del self.items[index][i]
                self.count-=1
                
                
        if self.count/self.size < 0.3 and self.size >5:
            self.rehashing(up=False)
            
            
    def rehashing(self,up=None):
        old_table=self.items
        new_size=self.size*2 if up else max(5,self.size//2)
        if self.size == new_size:
            return
        self.size=new_size
        self.items=[[] for _ in range(self.size)]
        self.count=0
        for bucket in old_table:
            for k,v in bucket:
                self.insert(k,v)
    
    def display(self):
        for i,pair in enumerate(self.items):
            print(f"{i} :{pair}")
                
                
                
h=HashTable(6)
d={"apple":1,"orange":2,"banana":5}
for k,v in d.items():
    h.insert(k,v)
h.display()
print("**********  second half  ************")
d={"kiwi":1,"cherry":4,"chakka":3}
for k,v in d.items():
    h.insert(k,v)   
h.display()
print("******  delete the item  *****************")
h.delete_item("banana")
h.display()
