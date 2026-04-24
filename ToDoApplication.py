
def addTask() -> str | None:
    try:
        addedTask = str(input("Task to add: "))
        if addedTask.strip() == "":
            raise ValueError("Input cannot be empty. Please type a task.")
        else:
            return addedTask

    except ValueError as error:
        print(error)

def viewTasks(tasklist):
    if tasklist == "":
        print("You currently have no tasks!")
    else:
        print("Here are your current tasks:")
        for task in range(len(tasklist)):
            print(f"{task+1}. {tasklist[task]}")

def choices():
    print("\nWhat would you like to do?")
    try:
        choice = int(input("1.) View Tasks\n2.) Add Task\n3.) Remove Task\nChoice: "))
        if choice < 1 or choice > 3:
            raise ValueError("Invalid choice. Please select a number between 1 and 3.")
        return choice
    except ValueError as error:
        print(error)
        return choices()

def main():
    print("Welcome to the To Do App!\n")


choices()