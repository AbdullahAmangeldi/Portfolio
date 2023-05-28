todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added successfully.")

def remove_task():
    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found.")

def view_tasks():
    if todo_list:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Todo List is empty.")

def main():
    while True:
        print("\n==== Todo List Menu ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
