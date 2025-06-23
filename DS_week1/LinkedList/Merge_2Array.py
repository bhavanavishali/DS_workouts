class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next


ll1 = Linkedlist()
ll2 = Linkedlist()

print("Array 1")
arr1 = [4, 2, 1]  
for i in arr1:
    ll1.insert_at_head(i)
ll1.display()

print("Array 2")
arr2 = [8, 7, 6]  
for j in arr2:
    ll2.insert_at_head(j)
ll2.display()

# Merge the two sorted lists
merged_head = merge_sorted_lists(ll1.head, ll2.head)

# Display merged list
print("Merged Sorted List")
merged_list = Linkedlist()
merged_list.head = merged_head
merged_list.display()
       
        