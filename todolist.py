tasks = []

def show_tasks():
    if not tasks:
        print("\n No tasks available!")
    else:
        print("\n Your To-Do List:")
        index = 1
        for task in tasks:
            print(f"{index}. {task}")
            index += 1
            
def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")
    
def delete_task():
    show_tasks()
    if tasks:
        try:
            del tasks[int(input("\nEnter task number to delete: ")) - 1]
            print("Task deleted!")
        except (ValueError, IndexError):
            print("Enter a valid number to be deleted!")

def main():
    while True:
        print("\nHere is your To Do List")
        print("1. View  Current Tasks ")
        print("2. Add A New Task ")
        print("3. Delete A Completed Task ")
        print("4. Exit ")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Have a productive day!")
            break
        else:
            print("Enter a valid choice.")

main()

            