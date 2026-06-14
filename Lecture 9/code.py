import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Task Manager Listbox")
window.geometry("400x350")

label = tk.Label(window, text="Enter a new item:")
label.pack(pady=5)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

listbox = tk.Listbox(window, width=35, height=8)
listbox.pack(pady=10)

initial_items = ["Buy groceries", "Read a lecture note", "Clean the room"]
for item in initial_items:
    listbox.insert(tk.END, item)

def add_item():
    text = entry.get().strip()
    if text == "":
        messagebox.showerror("Error", "Cannot add an empty item!")
        return
    listbox.insert(tk.END, text)
    entry.delete(0, tk.END)

def remove_item():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select an item to delete!")

def clear_all():
    listbox.delete(0, tk.END)

btn_add = tk.Button(window, text="Add Item", command=add_item, width=15)
btn_add.pack(pady=2)

btn_remove = tk.Button(window, text="Delete Selected", command=remove_item, width=15)
btn_remove.pack(pady=2)

btn_clear = tk.Button(window, text="Clear All", command=clear_all, width=15)
btn_clear.pack(pady=2)

window.mainloop()