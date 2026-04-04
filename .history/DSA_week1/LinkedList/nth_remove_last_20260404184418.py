class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


    def remove_n_from_end(self, n):

        fast = self.head
        slow = self.head

        
        for i in range(n):
            fast = fast.next

        
        if fast is None:
            self.head = self.head.next
            return

        
        while fast.next:
            fast = fast.next
            slow = slow.next

        
        slow.next = slow.next.next


    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# ----------------------

l = LinkedList()

arr = [1,2,3,4,5,5,3,600,4,1,4,5]

for i in arr:
    l.insert_at_end(i)

print("Original List")
l.display()

print("After deleting N th node from end")

l.remove_n_from_end(5)

l.display()