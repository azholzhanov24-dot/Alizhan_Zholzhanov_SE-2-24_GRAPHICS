import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Square Calculator")
window.geometry("300x200")

label = tk.Label(window, text="Enter a number:")
label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

result_label = tk.Label(window, text="Result:")
result_label.pack(pady=5)

def calculate_square():
    value = entry.get()
    
    if value == "":
        messagebox.showerror("Error", "Input field is empty")
        return

    try:
        number = float(value)
        result = number ** 2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter a numeric value")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

calculate_button = tk.Button(window, text="Calculate Square", command=calculate_square)
calculate_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

window.mainloop()