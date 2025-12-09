from collections import deque

todo_queue = deque()
completed_stack = []

def add_task(task):
    todo_queue.append(task)
    print("Task added successfully")

def complete_task():
    if todo_queue:
        task = todo_queue.popleft()
        completed_stack.append(task)
        print("Completed:", task)
    else:
        print("No pending tasks")

def undo_task():
    if completed_stack:
        task = completed_stack.pop()
        todo_queue.appendleft(task)
        print("Undo successful:", task)
    else:
        print("No completed tasks to undo")

def show_tasks():
    print("\nPending Tasks:")
    for task in todo_queue:
        print("-", task)
    print("\nCompleted Tasks:")
    for task in completed_stack:
        print("-", task)

while True:
    print("\n1.Add Task 2.Complete Task 3.Undo 4.Show Tasks 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        complete_task()
    elif choice == 3:
        undo_task()
    elif choice == 4:
        show_tasks()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
