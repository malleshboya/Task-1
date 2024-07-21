def display_todo_list(todo_list):
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("To-Do list:")
        for i in range(len(todo_list)):
            task = todo_list[i]
            status = "Done" if task["completed"] else "Not done"
            print(f"{i + 1}. {task['task']} ({status})")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' is added to your to-do list.")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print(f"Task {task_number} has been marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(todo_list):
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
        return

    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to remove: "))
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' is removed from your to-do list.")
    else:
        print("Invalid task number.")

todo_list = []
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_todo_list(todo_list)
    elif choice == "2":
        add_task(todo_list)
    elif choice == "3":
        mark_task_completed(todo_list)
    elif choice == "4":
        remove_task(todo_list)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
