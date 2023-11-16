"""
Palindrome Checker
This program checks if the user-input is a palindrome or not. A palindrome is a word, sentence, verse, or even number
that reads the same backward or forward. That means if a sentence is rid of spaces, punctuations, and capitalization,
the original arrangement of the characters and its reversed arrangement should be of the same value.
"""

# Import Time: For animation purposes
import time

# Class: Node for Linked List
class Node:
    # Constructor
    def __init__(self, x):
        # Variable: For data
        self.data = x
        # Variable: For next node
        self.next = None

# Class: Stack in LinkedList
class Stack:
    # Constructor
    def __init__(self):
        # Variable: For pointer
        self.top = None

    # Function: Push - To add data inside the Stack
    def push(self, x):
        new = Node(x)

        if self.top is None:
            self.top = new
            self.top.next = None

        else:
            new.next = self.top
            self.top = new

    # Function: Pop - To delete data inside the Stack
    def pop(self):
        # If Stack is empty, print a status message.
        if self.top is None:
            print("Stack underflow.")
            return

        # If Stack is not empty and the current node HAS NO succeeding node, pop the node where the current pointer
        # is located.
        elif self.top.next is None:
            popped = self.top.data
            self.top = None
            return popped

        # If Stack is not empty and the current node HAS A succeeding node, pop the node where the current pointer
        # is located.
        else:
            temp = self.top
            popped = temp.data
            self.top = temp.next
            temp = None
            return popped

# Function: Palindrome Checker
def checker(pal_input):
    # Print: To check if the function is running
    print("Checking the input if it is a palindrome...")
    time.sleep(1)

    # Variable: To convert the input to lowercase
    palindrome = pal_input.lower()
    # List: To store the characters of the input in original arrangement
    clean_list = []
    # Stack() Instance: To store the characters of the input in a reversed arrangement
    reverse_stack = Stack()

    # For Loop: For each character in the variable "palindrome"
    for character in palindrome:
        # If the character is an alphabet or a number
        if character.isalnum():
            # Append the character to list "clean_list"
            clean_list.append(character)
            # Then, push the character to the stack "reverse_stack"
            reverse_stack.push(character)
        # Else, continue with the loop

    # After appending and pushing all the alphabet and numeric characters...

    # List: To store the contents of the Stack (the input) in reversed order
    reverse_list = []

    # For Loop: Traverse each character in the number of times of the length of the cleaned input
    for character in range(len(clean_list)):
        # Variable: To store the popped data of the Stack
        popped = reverse_stack.pop()
        # Append the popped data inside the list "reverse_list"
        reverse_list.append(popped)

    # Variable: Convert the list "clean_list" into string
    clean = "".join(clean_list)
    # Variable: Convert the list "reverse_list" into string
    reverse = "".join(reverse_list)

    # Print: Display the original input, the cleaned input, and the reversed cleaned input of the user
    print(f"""==================================================
              PALINDROME CHECKER
    Input: {pal_input}
    Cleaned: {clean}
    Reversed: {reverse}
    """)

    # If-Else: Check if the input in original and reversed arrangement are the same.
    # If: The input in original and reversed arrangement ARE the same.
    if clean == reverse:
        print("Result: It is a palindrome.")
    # Else: The input in original and reversed arrangement ARE NOT the same.
    else:
        print("Result: It is not a palindrome.")

    print("==================================================")


# CODES: OUTSIDE THE CLASS AND FUNCTION
# Print: Introductory display
print("Initializing palindrome checker...")
time.sleep(1)
# Print: Introduces the user to what is a palindrome
print("""==================================================
Welcome to Palindrome Checker
A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
==================================================""")

# While Loop: To enable the user to check multiple times if the input is a palindrome or not.
while True:
    # Input: Lets the user input the word, phrase, or sentence to check if it is a palindrome or not.
    palInput = input("Enter your input: ")
    # Function Call: Pass the input of the user to the function "checker()".
    checker(palInput)

    # After executing the checker() function, the code asks if the user wants to check another input or not.
    time.sleep(1)
    option = input("Do you still want to use the checker (Yes or No): ")

    # If-Else: Checks if the user still wants to check another input or not.
    # If: If the user inputs "yes", he will be asked again for another input.
    if option.lower() == "yes":
        continue

    # ElIf: If the user inputs "no", the loop is broken by "break", and the code ends and stops.
    elif option.lower() == "no":
        print("Thank you for using the Palindrome Checker!")
        time.sleep(1)
        print("Closing the palindrome checker...")
        break

    # Else: If the user inputs an invalid option, the loop is broken by "break", and the code ends and stops.
    else:
        print("Invalid option. Thank you for using the Palindrome Checker!")
        break

"""
Reflection:
    I learned that you can use Stack in Linked List to reverse the arrangement of data. By pushing each data into the Stack and
    then popping them off afterwards in a different, the order in which the elements are popped off will be the reverse of the order
    in which they were pushed. I didn't realize how you can use the Stack in such a way before I managed to finish this program.
    
    I realized how crucial it is for you to have a full grasp of how a data structure like Stack and Linked List works so that you can use it
    efficiently and more appropriately. Without this knowledge, you may leave yourself lost within the program that you made yourself. It feels easier
    to code once you know how each line of code works and use by commenting its significance in the code.
"""
