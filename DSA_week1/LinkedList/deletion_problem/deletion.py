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
    
    
    
    #   def delete_position(self,position):
    #     if position==0:
    #         self.head=self.head.next
    #         return
    #     current=self.head
    #     count=0
    #     while current and current.next:
    #         if count==position-1:
    #             current.next=current.next.next
    #             return
    #         current=current.next
    #         count+=1
    #     print("Not found")
    #     return
    
    def delete_at_position(self,position):
        if position==0:
            self.head=self.head.next
            return
        current=self.head
        count=0
        while current and current.next:
            if count== position-1:
                current.next=current.next.next
                return
            current=current.next
            count+=1
        return 
    
    # def delete_at_value(self,data):
    #     if self.head.data==data:
    #         self.head=self.head.next
    #         return
    #     current=self.head
    #     while current and current.next:
    #         if current.next.data==data:
    #             current.next=current.next.next
    #             return
    #         current=current.next
    #     return
    
    def delete_dup(self):
        dup=[]
        current=self.head
        prev=None
        while current:
            if current.data not in dup:
                dup.append(current.data)
                prev=current
            else:
                prev.next=current.next
            
            current=current.next
        
        return
            
           
    
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end=' ->')
            current=current.next
        print(None)   
        
ll=LinkedList()
a=[5,9,4,6,4,7,5,4,7]
for i in a:
    ll.insert_at_head(i)
ll.display()

# ll.delete_at_position(3)
# ll.display()

# ll.delete_at_value(4)
# ll.display()


ll.delete_dup()
ll.display()



# New 

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class Linkedlist:
#     def __init__(self):
#         self.head=None
        
#     def insert_at_head(self,data):
#         new_node=Node(data)
#         if  self.head is not None:
#             new_node.next=self.head
#             self.head=new_node
#             return
#         self.head=new_node
#         return
    
#     def delete_at_head(self):
#         current=self.head
#         if self.head is not None:
#             self.head=current.next
#             return
#         print("head is empty ")
#         return 
        
        
#     def delete_at_position(self,position):
#         if position==0:
#             self.head=self.head.next
#             return
#         current=self.head
#         for _  in range(position-1):
#             if current is None or current.next is None:
#                 return
#             current=current.next
#         current.next=current.next.next
#         return
            
#     def delete_at_value(self,value):
#         # if self.head is None:
#         #     return

#         # # If head contains the value
#         # if self.head.data == value:
#         #     self.head = self.head.next
#         #     return
    
#         # current = self.head
#         # while current.next:
#         #     if current.next.data == value:
#         #         current.next = current.next.next
#         #         return
#         #     current = current.next
            
#         if self.head.data==value:
#             self.head=self.head.next
#             return
#         current=self.head
#         while current.next:
#             if current.next.data==value:
#                 current.next=current.next.next
#                 return
#             current=current.next
            
        
            
                
#     # def delete_at_value(data):
#     #     if self.head.data==data:
#     #         self.head=self.head.next
            
            
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end='->')
#             current=current.next
#         print(None)
        
# ll=Linkedlist()
# arr=[4,6,88,3]
# for i in arr:
#     ll.insert_at_head(i)
# ll.display()
# # print("delete at head")
# # ll.delete_at_head()
# # ll.display()
# # print("dellete at position")
# # ll.delete_at_position(2)
# # ll.display()

# print("****************")
# print("dellete from value")
# ll.delete_at_value(4)
# ll.display()