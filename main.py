import os
import datetime

# Define the file path for storing tasks
tasks_file = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            for line in file:
                task = line.strip().split(",")
                task_desc, priority, due_date, completed = task
                tasks.append({
                    "task_desc": task_desc,
                    "priority": priority,
                    "due_date": due_date,
                    "completed": completed == "True"
                })
    return tasks

def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        for task in tasks:
            file.write(f"{task['task_desc']},{task['priority']},{task['due_date']},{task['completed']}\n")

def add_task(tasks):
    task_desc = input("Enter the task description: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "task_desc": task_desc,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. [{status}] {task['task_desc']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
