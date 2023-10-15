import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")
        

root = tk.Tk()
root.title("To-Do List")


listbox = tk.Listbox(root, width=50, height=10,bd=1)
listbox.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
 
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)


root.mainloop()