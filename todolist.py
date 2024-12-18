import os
import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal
    if not tasks:
        print("No tasks found.")
        return

    print("=== Your Tasks ===")
    for idx, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        due_date = task.get("due_date", "No due date")
        priority = task.get("priority", "Normal")
        print(f"{idx}. {status} {task['task']} | Priority: {priority} | Due: {due_date}")
    print("===================")

# Add a new task
def add_task(tasks):
    task_description = input("Enter the task description: ").strip()
    if not task_description:
        print("Task description cannot be empty.")
        return

    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    if priority not in ["High", "Medium", "Low", ""]:
        print("Invalid priority. Defaulting to 'Normal'.")
        priority = "Normal"

    due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ").strip()
    try:
        if due_date:
            datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Skipping due date.")
        due_date = "No due date"

    tasks.append({
        "task": task_description,
        "completed": False,
        "priority": priority or "Normal",
        "due_date": due_date or "No due date",
    })
    print("Task added successfully!")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Sort tasks by priority or due date
def sort_tasks(tasks):
    print("1. Sort by Priority")
    print("2. Sort by Due Date")
    print("3. Back to Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        tasks.sort(key=lambda x: {"High": 1, "Medium": 2, "Low": 3}.get(x["priority"], 4))
        print("Tasks sorted by priority.")
    elif choice == "2":
        tasks.sort(key=lambda x: x["due_date"] if x["due_date"] != "No due date" else "9999-12-31")
        print("Tasks sorted by due date.")
    elif choice == "3":
        return
    else:
        print("Invalid choice. Returning to menu.")
    input("Press Enter to continue...")

# Main menu
def main_menu():
    tasks = load_tasks()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== To-Do List App ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Sort Tasks")
        print("6. Exit")
        print("======================")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_tasks(tasks)
            input("\nPress Enter to return to the menu...")
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
            input("\nPress Enter to return to the menu...")
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
            input("\nPress Enter to return to the menu...")
        elif choice == "4":
            mark_task_completed(tasks)
            save_tasks(tasks)
            input("\nPress Enter to return to the menu...")
        elif choice == "5":
            sort_tasks(tasks)
            save_tasks(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu...")

# Run the app
if __name__ == "__main__":
    main_menu()
