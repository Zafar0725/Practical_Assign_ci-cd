import json
import sys
 
TASKS_FILE = 'tasks.json'
 
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
 
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
 
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")
 
def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
 
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed}")
    except IndexError:
        print("Invalid task number.")
 
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add/list/delete [task/index]")
    else:
        cmd = sys.argv[1]
        if cmd == "add" and len(sys.argv) > 2:
            add_task(" ".join(sys.argv[2:]))
        elif cmd == "list":
            list_tasks()
        elif cmd == "delete" and len(sys.argv) > 2:
            delete_task(int(sys.argv[2]))
        else:
            print("Invalid command or missing arguments.")