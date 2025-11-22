Task Management App:This is a simple command-line application written in Python to manage a list of tasks. You can add, update, delete, and view your daily tasks.                                         Features:Add tasks to the list.Update an existing task by its name.Delete a task by its name.View all tasks currently in the list.Handles input validation for the main menu operation.
Requirements:Python 3 (The script uses basic Python features and should work with any modern version of Python 3).
How to RunSave the Code: Save the provided Python code into a file named task_manager.py.Run from Terminal: Open your terminal or command prompt and execute the script:Bashpython task_manager.py
Usage:When you run the script, the application will first ask you to initialize your task list.1. Initial Task Setup----WELCOME TO THE TASK MANAGEMENT APP----
Enter how many tasks you want to add = 2
Enter task 1 = Buy groceries
Enter task 2 = Finish report
Today's tasks are
['Buy groceries', 'Finish report']
2. Main MenuAfter the initial setup, you will be presented with the main menu where you can perform operations on your task list.Enter 
1-Add
2-Update
3-Delete
4-View
5-Exit/Stop
OperationsOperationInputActionExampleAdd1Adds a new task to the end of the list.Enter task you want to add = Call doctorUpdate2Replaces an existing task with a new one.Enter the task name you want to update = Buy groceries followed by Enter new task = Pay billsDelete3Removes a task from the list by its name.Which task you want to delete = Finish reportView4Prints the complete list of tasks.Total tasks = ['Pay bills', 'Call doctor']Exit5Closes the program.Closing the program....
Code Snippet:The core logic of the application:Pythondef task():
    tasks = []  # Initialize an empty list to store tasks
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    # ... (code for initial task setup)
