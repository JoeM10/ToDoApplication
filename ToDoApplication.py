def viewTasks(taskList):
    if taskList == []:
        print("\nYou currently have no tasks!")
    else:
        print("\nHere are your current tasks:")
        for task in range(len(taskList)):
            print(f"{task+1}. {taskList[task]}")

def addTask(taskList) -> str | None:
    try:
        addedTask = str(input("Task to add: ").strip())
        if addedTask == "":
            raise ValueError("Input cannot be empty. Please type a task.")
        else:
            taskList.append(addedTask)
            print(f"\n{addedTask} has been added to your task list.")

    except ValueError as error:
        print(error)

def removeTask(taskList):
    if taskList == []:
        print("\nYou currently have no tasks to remove!")
    else:
        print("\nHere are your current tasks:")
        for task in range(len(taskList)):
            print(f"{task+1}. {taskList[task]}")
        try:
            taskToRemove = input("\nTask number to remove: ").strip()
            if not taskToRemove.isdigit():
                raise ValueError("\nInvalid input. Please enter a number from the list.")
            taskToRemove = int(taskToRemove)
            if 1 <= taskToRemove <= len(taskList):
                removedTask = taskList.pop(taskToRemove - 1)
                print(f"\n{removedTask} has been removed from your task list.")
            else:
                raise ValueError("\nInvalid task number.")
        except ValueError as error:
            print(error)

def choices():
    while True:
        try:
            choice = input("\nWhat would you like to do?\n1.) View Tasks\n2.) Add Task\n3.) Remove Task\n4.) Exit\nChoice: ").strip()
            if choice not in ["1", "2", "3", "4"]:
                raise ValueError("\nInvalid choice. Please select a number between 1 and 4.")
            
            elif choice == "1":
                viewTasks(taskList)
            
            elif choice == "2":
                addTask(taskList)
            
            elif choice == "3":
                removeTask(taskList)
            
            elif choice == "4":
                print("\nExiting the To Do App. Goodbye!")
                return False

        except ValueError as error:
            print(error)


def main():
    print("\nWelcome to the To Do App!")
    choices()

taskList = []


if __name__ == "__main__":
    main()