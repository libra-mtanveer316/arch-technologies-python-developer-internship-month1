
tasks = []          # currently pending tasks
completed_count = 0  # how many tasks have been completed and removed so far
 
def show_menu():
    print("\n----- To-Do List -----")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task (removes it from the list)")
    print("4. Exit")
 
def add_task():
    task_name = input("Enter the task: ").strip()
    if task_name == "":
        print("Task can't be empty, try again.")
        return
    tasks.append(task_name)
    print(f"Added: {task_name}")
 
def show_progress_bar():
    total_ever = completed_count + len(tasks)
    if total_ever == 0:
        return
    percent = int((completed_count / total_ever) * 100)
    bar_length = 20
    filled = int(bar_length * completed_count / total_ever)
    bar = "#" * filled + "-" * (bar_length - filled)
    print(f"Progress: [{bar}] {percent}% ({completed_count}/{total_ever} completed)")
 
def view_tasks():
    if not tasks and completed_count == 0:
        print("Your list is empty. Add something to get started.")
        return
    if not tasks:
        print("\nNo pending tasks right now, nice work!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    show_progress_bar()
 
def complete_task():
    global completed_count
    if not tasks:
        print("Nothing to complete, your list is empty.")
        return
    view_tasks()
    try:
        choice = int(input("\nWhich task number is done? "))
        finished = tasks.pop(choice - 1)
        completed_count += 1
        print(f"Nice, '{finished}' is done and removed from your list.")
        show_progress_bar()
    except (ValueError, IndexError):
        print("That's not a valid task number.")
 
def main():
    print("Welcome to your To-Do List app!")
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Alright, closing the app. Have a productive day!")
            break
        else:
            print("Please choose a number between 1 and 4.")
 
if __name__ == "__main__":
    main()
