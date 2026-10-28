tasks = []
def add_task(tasks):
    while True:
        task = input("Enter a task: ").strip()
        tasks.append(task)
        print("Task added")

def show_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty")
    else:
        print("Your tasks:")
        for number, task in enumerate(tasks, start=1):
            print(number, "-", task)

def remove_task(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty")
        return
    else:
        show_tasks(tasks)
        try:
            task_number = int(input("Number of the task you want to remove: "))
            if task_number >= 1 and task_number <= len(tasks):
                tasks.pop(task_number-1)
                print("Task removed")
            else:
                print("Invalid number")
        except ValueError:
            print("Please enter a number")
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks(tasks):
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("No saved tasks yet")

load_tasks(tasks)
while True:
    print("\n====TO-DO LIST====")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        remove_task(tasks)
    elif choice == "3":
        show_tasks(tasks)
    elif choice == "4":
        print("Goodbye")
        save_tasks(tasks)
        break
    else:
        print("Invalid choice. Please enter 1,2,3 or 4")