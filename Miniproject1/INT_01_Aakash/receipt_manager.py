task_N = []
task_P = []
task_D = []
task_S = []

while True:
    print("Welcome to Recipe Maneger")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View Pending Tasks")
    print("5. View Completed Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        priority = input("Enter priority (High/Medium/Low): ")
        due = input("Enter due date: ")
        task_N.append(name)
        task_P.append(priority)
        task_D.append(due)
        task_S.append("Pending")
        print("Task added!")

    elif choice == "2":
        if len(task_N) == 0:
            print("No tasks available.")
        else:
            for i in range(len(task_N)):
                print(i+1, task_N[i], task_P[i], task_D[i], task_S[i])

    elif choice == "3":
        num = int(input("Enter task number: ")) - 1
        if 0 <= num < len(task_S):
            task_S[num] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Pending Tasks:")
        for i in range(len(task_S)):
            if task_S[i] == "Pending":
                print(task_N[i])

    elif choice == "5":
        print("Completed Tasks:")
        for i in range(len(task_S)):
            if task_S[i] == "Completed":
                print(task_N[i])

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
