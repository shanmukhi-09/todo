import tkinter as tk
from tkinter import messagebox

# Function to add a task
def enter_task():
    task = entry_task.get()
    if task:
        listbox_task.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete selected task
def delete_task():
    try:
        selected_task = listbox_task.curselection()[0]
        listbox_task.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark task as completed
def mark_completed():
    try:
        selected_task = listbox_task.curselection()[0]
        task_text = listbox_task.get(selected_task)
        listbox_task.delete(selected_task)
        listbox_task.insert(tk.END, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create main window
window = tk.Tk()
window.title("My To-Do List Application")

# Create frame for tasks
frame_task = tk.Frame(window)
frame_task.pack()

# Create listbox for tasks
listbox_task = tk.Listbox(frame_task, bg="black", fg="white", height=15, width=50, font=("Helvetica", 12))
listbox_task.pack(side=tk.LEFT)

# Create scrollbar
scrollbar_task = tk.Scrollbar(frame_task)
scrollbar_task.pack(side=tk.RIGHT, fill=tk.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Entry box for new task
entry_task = tk.Entry(window, width=50)
entry_task.pack(pady=5)

# Buttons
entry_button = tk.Button(window, text="Add Task", width=50, command=enter_task)
entry_button.pack(pady=3)

delete_button = tk.Button(window, text="Delete Selected Task", width=50, command=delete_task)
delete_button.pack(pady=3)

mark_button = tk.Button(window, text="Mark as Completed", width=50, command=mark_completed)
mark_button.pack(pady=3)

# Run the main loop
window.mainloop()