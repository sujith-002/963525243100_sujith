import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# -----------------------------
# Load Tasks
# -----------------------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


# -----------------------------
# Save Tasks
# -----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Add Task
# -----------------------------
def add_task(tasks):
    print("\n------ Add New Task ------")

    title = input("Enter task title: ")
    description = input("Enter description: ")
    reminder = input("Enter reminder date (DD-MM-YYYY): ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "description": description,
        "reminder": reminder,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!\n")


# -----------------------------
# View Tasks
# -----------------------------
def view_tasks(tasks):

    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\n========== TASK LIST ==========")

    for index, task in enumerate(tasks, start=1):

        print(f"\nTask No : {index}")
        print("Title       :", task["title"])
        print("Description :", task["description"])
        print("Reminder    :", task["reminder"])
        print("Priority    :", task["priority"])
        print("Status      :", task["status"])

    print()


# -----------------------------
# Search Task
# -----------------------------
def search_task(tasks):

    keyword = input("Enter task title to search: ").lower()

    found = False

    for task in tasks:

        if keyword in task["title"].lower():

            print("\nTask Found")
            print("------------------------")
            print("Title :", task["title"])
            print("Description :", task["description"])
            print("Reminder :", task["reminder"])
            print("Priority :", task["priority"])
            print("Status :", task["status"])

            found = True

    if not found:
        print("Task not found.")


# -----------------------------
# Update Task
# -----------------------------
def update_task(tasks):

    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:

        number = int(input("Enter task number to update: "))

        if number < 1 or number > len(tasks):
            print("Invalid number.")
            return

        task = tasks[number - 1]

        task["title"] = input("New title: ")
        task["description"] = input("New description: ")
        task["reminder"] = input("New reminder date: ")
        task["priority"] = input("New priority: ")

        save_tasks(tasks)

        print("Task updated successfully.")

    except:
        print("Invalid input.")


# -----------------------------
# Complete Task
# -----------------------------
def complete_task(tasks):

    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:

        number = int(input("Enter task number completed: "))

        tasks[number - 1]["status"] = "Completed"

        save_tasks(tasks)

        print("Task marked as completed.")

    except:
        print("Invalid input.")


# -----------------------------
# Delete Task
# -----------------------------
def delete_task(tasks):

    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:

        number = int(input("Enter task number to delete: "))

        deleted = tasks.pop(number - 1)

        save_tasks(tasks)

        print("Deleted:", deleted["title"])

    except:
        print("Invalid input.")


# -----------------------------
# Check Today's Reminders
# -----------------------------
def today_reminders(tasks):

    today = datetime.now().strftime("%d-%m-%Y")

    print("\nToday's Reminders")

    print("-----------------------")

    found = False

    for task in tasks:

        if task["reminder"] == today and task["status"] == "Pending":

            print("Task :", task["title"])
            print("Priority :", task["priority"])
            print()

            found = True

    if not found:
        print("No reminders for today.\n")


# -----------------------------
# Count Tasks
# -----------------------------
def task_summary(tasks):

    total = len(tasks)

    completed = 0
    pending = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1
        else:
            pending += 1

    print("\n------ Summary ------")

    print("Total Tasks :", total)
    print("Completed   :", completed)
    print("Pending     :", pending)
    print()


# -----------------------------
# Main Menu
# -----------------------------
def main():

    tasks = load_tasks()

    while True:

        print("==============================================")
        print(" PERSONAL TASK & REMINDER MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Update Task")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Today's Reminders")
        print("8. Task Summary")
        print("9. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            search_task(tasks)

        elif choice == "4":
            update_task(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            delete_task(tasks)

        elif choice == "7":
            today_reminders(tasks)

        elif choice == "8":
            task_summary(tasks)

        elif choice == "9":

            print("\nThank you for using the system.")
            print("Program Closed Successfully.")

            break

        else:

            print("Invalid choice. Please try again.\n")


# -----------------------------
# Program Starts Here
# -----------------------------
if __name__ == "__main__":
    main()