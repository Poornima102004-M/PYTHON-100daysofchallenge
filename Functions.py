# Define a global list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed(index):
    if index >= 1 and index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(index):
    if index >= 1 and index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main function to run the program
def main():
    print("Welcome to the Todo List Manager!")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter the task index to mark as completed: "))
            mark_completed(index)
        elif choice == '4':
            index = int(input("Enter the task index to delete: "))
            delete_task(index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
