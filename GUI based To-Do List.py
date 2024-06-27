import tkinter as tk
from tkinter import simpledialog, messagebox
import os

TODO_FILE = 'todo_list.txt'

def read_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def write_todos(todos):
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(f"{todo}\n")

def list_todos():
    todos = read_todos()
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo)

def add_todo():
    todo = simpledialog.askstring("New To-Do", "Enter a new to-do item:")
    if todo:
        todos = read_todos()
        todos.append(todo)
        write_todos(todos)
        list_todos()

def update_todo():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        todos = read_todos()
        new_todo = simpledialog.askstring("Update To-Do", "Enter the new to-do item:", initialvalue=todos[idx])
        if new_todo:
            todos[idx] = new_todo
            write_todos(todos)
            list_todos()
    else:
        messagebox.showwarning("Warning", "Select a to-do item to update.")

def delete_todo():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        todos = read_todos()
        todos.pop(idx)
        write_todos(todos)
        list_todos()
    else:
        messagebox.showwarning("Warning", "Select a to-do item to delete.")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=add_todo)
add_button.grid(row=0, column=0, padx=10)

update_button = tk.Button(button_frame, text="Update", command=update_todo)
update_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Delete", command=delete_todo)
delete_button.grid(row=0, column=2, padx=10)

list_todos()

root.mainloop()
