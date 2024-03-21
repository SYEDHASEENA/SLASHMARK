task_list = []

def display_tasks():
    if not task_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(task_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

def add_task(task_name):
    task = {"task": task_name, "completed": False}
    task_list.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

def mark_completed(task_index):
    if 1 <= task_index <= len(task_list):
        task_list[task_index - 1]["completed"] = True
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

def remove_task(task_index):
    if 1 <= task_index <= len(task_list):
        removed_task = task_list.pop(task_index - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number)
    elif choice == '4':
        display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
