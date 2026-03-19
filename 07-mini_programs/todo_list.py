def display_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "⬜"
        print(f"{i}. {status} {task['name']}")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == '1':
            task_name = input("Enter task: ")
            tasks.append({'name': task_name, 'done': False})
            print("Task added!")
        
        elif choice == '2':
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                idx = int(input("Enter task number: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]['done'] = True
                    print("Task marked as done!")
        
        elif choice == '4':
            display_tasks(tasks)
            if tasks:
                idx = int(input("Enter task number: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    print("Task deleted!")
        
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()