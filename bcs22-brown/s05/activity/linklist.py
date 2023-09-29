"""
Linked List
- is basically a data structure for storing collection of data or items

class Box{
    int data;
    Box next
}

head.data
- the data of the head

head
- represents the first box

Box next
- reflects to the next box that is connected to a particular box

[6|->]  ->  [3|->]  ->  [ |]
self.head  head.next head.next.next
head	   previous    current

head.next = current.next
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                # 1st Loop: head.next = current.next
                current = current.next
                # 2nd Loop: current.next.next = current.next
            current.next = new_node

    def sort(self):
        current = self.head
        while current.next:
            current = current.next
            if current == current.next:
                return
            elif current > current.next:
                current.next = current
                current = current.next
            elif current < current.next:
                current = current.next
                current.next = current

    def display(self):
        current = self.head
        while current:
            aHead = self.head.next.data # 3
            bHead = self.head.next.next.data # 4

            if current.data == 3:
                print(bHead, end = " -> ")
                current = current.next
                continue
            elif current.data == 4:
                print(aHead, end = " -> ")
                current = current.next
                continue

            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Input Values
input_values = [6, 3, 4, 2, 1]
# input_values.sort(reverse=True)

my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

# Display the Linked List
my_linked_list.display()
