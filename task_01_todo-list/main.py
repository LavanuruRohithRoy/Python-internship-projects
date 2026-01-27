# Task structure
class Task:
    def __init__(self,task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False

# Task management system
class TaskManager:
    def __init__(self):
        self.tasks={}
        self.next_id=1

    # Adding a new task to the list
    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        print("Task added successfully")
    
    # Viewing existing tasks in the list
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return
        for task in self.tasks.values():
            status = "Completed" if task.completed else "Pending"
            print(f"{task.task_id}  {task.description} - Status: {status}")
    
    # Marking a task as completed
    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].completed = True
            print("Task marked as completed")
        else:
            print("Invalid task ID")
    
def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                manager.mark_task_completed(task_id)
            except ValueError:
                print("Please enter a valid number")
        elif choice == "4":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice, please try again")
    
if __name__ == "__main__":
    main()