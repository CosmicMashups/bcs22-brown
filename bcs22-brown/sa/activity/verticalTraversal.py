"""
VERTICAL TRAVERSAL ALGORITHM
    BROWN, Yuri M. - BCS22
    231211 - Final Laboratory Examination

DESCRIPTION:
    This algorithm provides the vertical traversal of a binary tree from both directions.
    It prints the traversal from the rightmost to the leftmost level, as well as the leftmost to the rightmost level.

COMPLEXITY:
    Time Complexity: O(n log(n))
    Space Complexity: O(n)
"""

# Class: Node [O(1)]
class Node:
    # Constructor: Node
    def __init__(self, data):
        # Variable: Data of the node
        self.data = data
        # Variable: Pointer to the left of the node
        self.left = None
        # Variable: Pointer to the right of the node
        self.right = None

# Function: Get Vertical Order [O(n)]
def vertical_traversal(root_node, distance, tree):
    # If-Else: If there is no root node yet, do not execute the rest of the function.
    if root_node is None:
        return

    # If-Else: Store the data of the current node in 'tree'
    if distance in tree:
        tree[distance].append(root_node.data)
    else:
        tree[distance] = [root_node.data]

    # Recursive Function Call: Store nodes in the left subtree
    vertical_traversal(root_node.left, distance - 1, tree)

    # Recursive Function Call: Store nodes in the right subtree
    vertical_traversal(root_node.right, distance + 1, tree)

# Function: Print Vertical Traversal [O(n log(n))]
def display_traversal(root_node):
    # Dictionary: To store the vertical traversal in the correct level order traversal of the tree
    tree = {}

    # Variable: To store the horizontal distance of each node
    distance = 0

    # Function Call: Store the vertical order in the map using the function vertical_traversal()
    vertical_traversal(root_node, distance, tree)

    # List: To store the vertical order of the tree in array form
    traversed_array = []

    # Variable: To store the vertical order from leftmost to rightmost level
    left_to_right = ""

    # Variable: To store the vertical order from rightmost to leftmost level
    right_to_left = ""

    # Loop: Traverse the tree and append each node at every horizontal distance
    for node in sorted(tree.keys()):
        traversed_array.append(tree[node])

    # Loop: Convert the created array into string that can be printed
    for row in traversed_array:
        for column in row:
            left_to_right = left_to_right + str(column) + " "
            right_to_left = str(column) + " " + right_to_left

    # Print the vertical order traversal
    print("VERTICAL ORDER TRAVERSAL:")
    print("Left to Right:", left_to_right)
    print("Right to Left:", right_to_left)


# Nodes: Tree [O(1)]
root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.left.right = Node(5)
root_node.right.left = Node(6)
root_node.right.right = Node(7)
root_node.right.left.right = Node(8)
root_node.right.right.right = Node(9)

# Print: Given Tree and Vertical Traversal [O(1)]
print("=" * 10, "FINAL LABORATORY EXAMINATION", "=" * 10)
print("""BINARY TREE:
            1
        /       \\
       2         3
     /   \\     /   \\
    4     5   6     7
               \\     \\
                8     9
""")

# Function Call: Print the traversal
display_traversal(root_node)

"""
Reflection:
    I had not previously encountered the method of determining the vertical traversal of a binary tree until I engaged
    in this particular activity. It became apparent to me that this task combined various concepts covered throughout
    the semester: the initial discussion on mapping during our first session, the principles of lists and arrays, the
    intricacies of nodes within linked lists, and the comprehensive understanding of trees. In reflection, I have come
    to acknowledge that the completion of this code might have proven challenging if attempted within the confines of a
    laboratory session lasting only a few hours. This realization underscores the importance of consistently practicing
    coding, as it serves to reinforce one's understanding of the concepts associated with each data structure discussed
    throughout the semester. It is essential to engage in coding regularly rather than relying solely on specific
    activities to ensure a comprehensive retention of these foundational concepts.
"""
