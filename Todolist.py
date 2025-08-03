def todo_list():
    tasks = []

    while True:
        task = input("Enter a task (or 'quit' to stop): ")
        if task.lower() == 'quit':
            break
        tasks.append(task)

    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


todo_list()


#OUTPUT

Enter a task (or 'quit' to stop): Reading
Enter a task (or 'quit' to stop): learning
Enter a task (or 'quit' to stop): studying
Enter a task (or 'quit' to stop): quit
Your To-Do List:
1. Reading
2. learning
3. studying
PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> 
