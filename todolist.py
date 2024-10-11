tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})

def mark_complete():
    display_tasks()
    num = int(input("Task number to complete: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]['completed'] = True

def delete_task():
    display_tasks()
    num = int(input("Task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        tasks.pop(num)

def main():
    while True:
        print("\n1. View tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Exit")
        choice = input("Choose: ")
        if choice == '1': display_tasks()
        elif choice == '2': add_task()
        elif choice == '3': mark_complete()
        elif choice == '4': delete_task()
        elif choice == '5': break

main()
