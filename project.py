# برنامه مدیریت تسک‌های روزانه

tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found in the list.")

def show_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. Add a task")
        print("2. Remove a task")
        print("3. Show tasks")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
