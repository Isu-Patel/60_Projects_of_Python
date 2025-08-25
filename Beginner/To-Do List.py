todos = []

while True:
    print("\n1. Add task\n2. View Tasks\n3. Remove Tasks\n4. Exit")
    choice = input("Choose Option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print("Task added!")
    elif choice == "2":
        if todos:
            for i, task in enumerate(todos, 1):
                print(f"{i}.{task}")
        else:
            print("No tasks!")
    elif choice == "3":
        if todos:
            for i, task in enumerate(todos, 1):
                print(f"{i}.{task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                todos.pop(index)
                print("Task removed!")
            except:
                print("Invalid number!")
        else:
            print("No tasks to remove!")
    elif choice == "4":
        break

    else: 
        print("Invalid Choice!")