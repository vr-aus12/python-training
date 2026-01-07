tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    
    for i, task in enumerate(tasks):
        status = "[DONE]" if task["done"] else "[TODO]"
        print(f"{i+1}. {status} {task['name']}")

if __name__ == '__main__':
    add_task("Learn Python")
    add_task("Build Project")
    view_tasks()

# Expected Output:
# Task 'Learn Python' added.
# Task 'Build Project' added.
# 1. [TODO] Learn Python
# 2. [TODO] Build Project
