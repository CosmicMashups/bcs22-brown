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

    def display(self):
        current = self.head
        while current:
            aTemp = self.head.next.data         # 3
            bTemp = self.head.next.next.data    # 4

            if current.data == self.head.next.data:
                print(bTemp, end = " -> ")
                current = current.next
                continue
            elif current.data == self.head.next.next.data:
                print(aTemp, end = " -> ")
                current = current.next
                continue

            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Input Values
input_values = [6, 3, 4, 2, 1]

# List to Linked List
my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

# Display the Linked List
my_linked_list.display()
