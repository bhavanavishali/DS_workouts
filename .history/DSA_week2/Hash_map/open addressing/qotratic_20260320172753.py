class QuadraticProbingHash:
    def __init__(self,size):
        self.size=size
        self.items=[None]*self.size
        self.count=0
        
    def myhash(self,key):
        return hash(key)%self.size

        
    def insert(self,key):
        index=self.myhash(key)
        print(index)
        i=0
        while self.items[(index+i*i)%self.size] is not None:
            i+=1
            
        new_index=(index+i*i)%self.size
        self.items[new_index]=key
        self.count+=1
        
        if self.count/self.size >0.7:
            self.rehashing()
            
    def rehashing(self):
        
        old_items=self.items
        new_size=self.size*2
        self.size=new_size
        self.items=[None]*self.size
        self.count=0
        for item in old_items:
            if item is not None:
                self.insert(item)
    def display(self):
        print(self.items)
        
lb=LinearProbing(10)
a=[10,5,61,40]
for i in a:
    lb.insert(i)
lb.display()   