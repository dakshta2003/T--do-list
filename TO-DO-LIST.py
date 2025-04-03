tasks = []
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Done\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif choice == "3":
        index = int(input("Enter task number to mark done: ")) - 1
        tasks.pop(index)
    elif choice == "4":
        break
