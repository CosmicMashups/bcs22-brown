import time


# Class: Node for Linked List
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Class: Stack in LinkedList
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)

        if self.top is None:
            self.top = new
            self.top.next = None

        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack underflow.")
            return

        elif self.top.next is None:
            popped = self.top.data
            self.top = None
            return popped

        else:
            temp = self.top
            popped = temp
            self.top = temp.next
            temp = None
            return popped

    def getList(self):
        if self.top is None:
            print("Stack underflow.")

        else:
            reversedList = []
            temp = self.top
            while temp:
                reversedList.append(temp.data)
                temp = temp.next
            return reversedList


# Function: Palindrome Checker
def checker(palInput):
    print("Running palindrome checker...")
    time.sleep(1)
    print("Checking the input if it is a palindrome...")
    time.sleep(1)

    palindrome = palInput.lower()
    cleanList = []
    reverseStack = Stack()

    for character in palindrome:
        if character.isalpha():
            cleanList.append(character)
            reverseStack.push(character)

    reverseList = reverseStack.getList()
    clean = "".join(cleanList)
    reverse = "".join(reverseList)

    print(f"""==================================================
              PALINDROME CHECKER
    Input: {palInput}
    Cleaned: {clean}
    Reversed: {reverse}
    """)

    if clean == reverse:
        print("Result: It is a palindrome.")
    else:
        print("Result: It is not a palindrome.")

    print("==================================================")


# Codes: Outside Class and Function
print("""==================================================
Welcome to Palindrome Checker
A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
==================================================""")

while True:
    palindrome = input("Enter your input: ")
    checker(palindrome)

    time.sleep(1)
    option = input("Do you still want to use the checker (Yes or No): ")

    if option.lower() == "yes":
        continue
    elif option.lower() == "no":
        print("Thank you for using the Palindrome Checker!")
        break
    else:
        print("Invalid option. Thank you for using the Palindrome Checker!")
        break
