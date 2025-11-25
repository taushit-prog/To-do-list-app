def view_tasks(task_list):
    """Displays all tasks with numbers using a standard loop."""
    if not task_list:
        print("\nYour task list is empty!")
    else:
        print("\n---- YOUR TASKS ----")
        # Concept: len() gives the total count. range() generates numbers 0, 1, 2...
        for i in range(len(task_list)):
            # We use [i] to access the item at that specific position
            # We add 1 to i because Python lists start at 0, but humans count from 1
            print(f"{i + 1}. {task_list[i]}")
        print("--------------------")

def add_task(task_list):
    """Adds a new task to the list."""
    task_name = input("Enter the task you want to add: ").strip() 
    if task_name:
        task_list.append(task_name)
        print(f"Task '{task_name}' successfully added.")
    else:
        print("Cannot add an empty task.")

def update_task(task_list):
    """Updates an existing task."""
    view_tasks(task_list) 
    if not task_list:
        return

    name_to_update = input("Enter the exact name of the task to update: ").strip()
    
    if name_to_update in task_list:
        new_task = input("Enter the new task name: ").strip()
        if new_task:
            index = task_list.index(name_to_update)
            task_list[index] = new_task
            print(f"Updated '{name_to_update}' to '{new_task}'.")
        else:
            print("Update failed. New task name cannot be empty.")
    else:
        print("Task not found.")

def delete_task(task_list):
    """Deletes a task from the list."""
    view_tasks(task_list)
    if not task_list:
        return

    name_to_delete = input("Enter the exact name of the task to delete: ").strip()
    
    if name_to_delete in task_list:
        task_list.remove(name_to_delete)
        print(f"Task '{name_to_delete}' has been deleted.")
    else:
        print("Task not found.")

def main():
    tasks = [] 
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")

    try:
        total_task = int(input("How many initial tasks do you want to add? "))
        for i in range(total_task):
            task_name = input(f"Enter task {i + 1}: ").strip()
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
                add_task(tasks)
            elif operation == 2:
                update_task(tasks)
            elif operation == 3:
                delete_task(tasks)
            elif operation == 4:
                view_tasks(tasks)
            elif operation == 5:
                print("Closing the program... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
        
        except ValueError:
            print("Invalid Input. Please enter a number.")

if __name__ == "__main__":
    main()
