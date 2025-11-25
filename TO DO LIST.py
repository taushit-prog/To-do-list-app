# --- GLOBAL VARIABLE ---
tasks = [] 

def view_tasks():
    """Displays all tasks using explicit length checks."""
    # REPLACED: if not tasks:
    if len(tasks) == 0:
        print("\nYour task list is empty!")
    else:
        print("\n---- YOUR TASKS ----")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print("--------------------")

def add_task():
    """Adds a task to the global list."""
    task_name = input("Enter the task you want to add: ").strip()
    
    # Check length to ensure it's not empty
    if len(task_name) > 0:
        tasks.append(task_name)
        print(f"Task '{task_name}' successfully added.")
    else:
        print("Cannot add an empty task.")

def update_task():
    """Updates a task in the global list."""
    view_tasks()
    
    # REPLACED: if not tasks:
    if len(tasks) == 0:
        return

    name_to_update = input("Enter the exact name of the task to update: ").strip()
    
    if name_to_update in tasks:
        new_task = input("Enter the new task name: ").strip()
        
        if len(new_task) > 0:
            index = tasks.index(name_to_update)
            tasks[index] = new_task
            print(f"Updated '{name_to_update}' to '{new_task}'.")
        else:
            print("Update failed. New task name cannot be empty.")
    else:
        print("Task not found.")

def delete_task():
    """Deletes a task from the global list."""
    view_tasks()
    
    # REPLACED: if not tasks:
    if len(tasks) == 0:
        return

    name_to_delete = input("Enter the exact name of the task to delete: ").strip()
    
    if name_to_delete in tasks:
        tasks.remove(name_to_delete)
        print(f"Task '{name_to_delete}' has been deleted.")
    else:
        print("Task not found.")

def main():
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")

    try:
        total_task = int(input("How many initial tasks do you want to add? "))
        for i in range(total_task):
            task_name = input(f"Enter task {i + 1}: ").strip()
            # Explicit check to ensure valid data
            if len(task_name) > 0:
                tasks.append(task_name)
    except ValueError:
        print("Invalid input. Starting with an empty list.")

    while True:
        print("\n--- MENU ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        try:
            operation = int(input("Choose an operation (1-5): "))

            if operation == 1:
                add_task()
            elif operation == 2:
                update_task()
            elif operation == 3:
                delete_task()
            elif operation == 4:
                view_tasks()
            elif operation == 5:
                print("Closing the program... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
        
        except ValueError:
            print("Invalid Input. Please enter a number.")

if __name__ == "__main__":
    main()
