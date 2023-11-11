"""TASK MANAGER - able to add and remove tasks, as well as mark them as complete, and display all the tasks added."""

# Stack: TaskManager
class TaskManager:
    # Constructor
    def __init__(self, max_size):
        # List: For containing all the added tasks
        self.task_manager = []
        # Variable: For pointer
        self.top = -1
        # Variable: For limiting the number of tasks added
        self.max_size = max_size

    # Function: To know if stack is full
    def is_full(self):
        return self.top == self.max_size - 1

    # Function: To know if stack is empty
    def is_empty(self):
        return self.top == -1

    # Function: To add new tasks
    def add_task(self, new_task):
        # If stack is not full, append the task
        # If stack is full, print a status message
        if not self.is_full():
            if new_task not in self.task_manager:
                self.top += 1
                self.task_manager.append(new_task)
                print(f"Status: Task '{new_task[0]}' added successfully.")
            else:
                print(f"Status: '{new_task[0]}' is already in Task Manager.")
        else:
            if new_task in self.task_manager:
                print(f"Status: '{new_task[0]}' is already in Task Manager.")
            print("Status: Maximum tasks reached. Remove an existing task first before adding another one.")

    # Function: To remove tasks
    def remove_task(self):
        # If stack is not empty, pop the top element, move the pointer down, and print a status message
        # If stack is empty, print a status message
        if not self.is_empty():
            removed_task = self.task_manager.pop()
            self.top -= 1
            print(f"Task '{removed_task[0]}' removed.")
        else:
            print("Status: No tasks to remove.")

    # Function: To mark tasks as complete
    def complete_task(self, title):
        # Iterate the stack using for loop, then find the same title from the stack
        # If "title" is found within the stack, change the value of task[2] to "Completed", and print a status message,
        # then use return so that the succeeding codes will not be printed anymore
        # If "title" is NOT found within the stack, the iteration stops, and prints a status message
        for task in self.task_manager:
            if task[0] == title:
                task[2] = "Completed"
                print(f"Status: Task '{task[0]}' marked as completed.")
                return
        print(f"Status: Task '{title}' not found.")

    # Function: Display the Task Manager
    def display_tasks(self):
        # Print the first part of the task manager.
        # If stack is empty, print the last part of the task manager, and print a status message
        # If stack is not empty, iterate through the stack, and print the elements one by one using .format()
        print("======================================================================")
        print("")
        print("======================================================================")
        print("|| {0:^64} ||".format("TASK MANAGER"))
        print("======================================================================")
        print("|| {:^15} | {:^28} | {:^15} ||".format("TITLE", "DESCRIPTION", "STATUS"))
        print("==------------------------------------------------------------------==")
        if self.is_empty():
            print("|| {:^15} | {:^28} | {:^15} ||".format("", "", ""))
            print("======================================================================")
            print("Status: No tasks to display.")
        else:
            for task in self.task_manager:
                print("|| {:^15} | {:^28} | {:^15} ||".format(task[0], task[1], task[2]))
            print("======================================================================")
        print("")

    # Function: To stop the code
    def exit_manager(self):
        print("Exiting. Thank you for using the Task Manager!")
        exit()

# Function
def main():
    max_size = int(input("Enter the maximum number of tasks: "))
    task_manager = TaskManager(max_size)

    while True:
        print("""======================================================================
OPTIONS
[1] Add Task                            [4] Display Tasks
[2] Remove Task                         [0] Exit
[3] Mark Task as Completed
======================================================================""")

        choice = input("Enter the number of the option that you want to execute: ")

        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            status = "Not Completed"
            new_task = [title, description, status]
            task_manager.add_task(new_task)
        elif choice == "2":
            task_manager.remove_task()
        elif choice == "3":
            title = input("Enter the title of the mask to be marked as complete: ")
            task_manager.complete_task(title)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "0":
            task_manager.exit_manager()
        else:
            print("Invalid choice.")


# Function Call: Run the main() function
main()
