class HashTable:
    def __init__(self,size):
        self.size=size
        self.items=[[] for _ in range(self.size)]
        self.count=0
        
    def myhash(self,key):
        return hash(key)%self.size
        
    def insert(self,key,val):
        index=self.myhash(key)
        for pair in self.items[index]:
            if pair[0]==key:
                pair[1]=val
                return
        self.items[index].append([key,val])
        self.count+=1
        
        if self.count/self.size > 0.7:
            self.rehashing(up=True)
            
    def  delete(self,key):
        index=self.myhash(key)
        for i,pair in enumerate(self.items[index]):
            if pair[0]==key:
                del self.items[index][i]
                self.count-=1
                return
            
        if self.count/self.size <0.3 and self.size >5:
            self.rehashing(up=False)
        
    def rehashing(self,up=None):
        old_items=self.items
        new_size=self.size* 2 if up else max(self.size//2,5)
        self.count=0
        if self.size==new_size:
            return
        self.size=new_size
        self.items=[[] for _ in range(self.size)]
        for bucket in old_items:
            for k,v in bucket:
                self.insert(k,v)
            
                
    def display(self):
        for i,pair in enumerate(self.items):
            print(f"{i} - {pair}")
            
h=HashTable(5)
a={
    "apple":40,
    "banana":50,
    "orange":90,
    "kiwi":45,
    "stone":62
    
}
for k,v in a.items():
    h.insert(k,v)
    
h.display()
h.delete("banana")
h.delete("orange")
h.delete("kiwi")
print("****")
h.display()


