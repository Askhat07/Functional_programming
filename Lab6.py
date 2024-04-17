import tkinter as tk
from rx.subject import Subject

class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_added = Subject()
        self.task_removed = Subject()

    def add_task(self, task):
        self.tasks.append(task)
        self.task_added.on_next(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.task_removed.on_next(task)

def main():
    todo_list = TodoList()

    def print_tasks():
        tasks_label.config(text="Tasks: " + ", ".join(todo_list.tasks))

    def add_task():
        task = entry.get()
        if task:
            todo_list.add_task(task)
            entry.delete(0, tk.END)

    def remove_task():
        task = entry.get()
        if task:
            todo_list.remove_task(task)
            entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Todo List")

    entry = tk.Entry(root)
    entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack()

    remove_button = tk.Button(root, text="Remove Task", command=remove_task)
    remove_button.pack()

    tasks_label = tk.Label(root, text="Tasks:")
    tasks_label.pack()

    todo_list.task_added.subscribe(lambda task: print_tasks())
    todo_list.task_removed.subscribe(lambda task: print_tasks())

    root.mainloop()

if __name__ == "__main__":
    main()