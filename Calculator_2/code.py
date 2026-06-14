import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Improved Cube Calculator")
window.geometry("320x260")

label = tk.Label(window, text="Enter a number:")
label.pack(pady=5)

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var)
entry.pack(pady=5)

result_label = tk.Label(window, text="Result:")
result_label.pack(pady=5)

def validate_input(value):
    if value.strip() == "":
        messagebox.showerror("Input Error", "Input field is empty.")
        return None
    try:
        number = float(value)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a numeric value.")
        return None
    if number < 0:
        messagebox.showerror("Input Error", "Negative numbers are not allowed.")
        return None
    return number

def calculate_cube(number):
    return number ** 3

def on_calculate_click():
    value = entry_var.get()
    number = validate_input(value)
    if number is None:
        return
    result = calculate_cube(number)
    result_label.config(text="Result: " + str(result), fg="green")

def clear_fields():
    entry_var.set("")
    result_label.config(text="Result:", fg="black")

def check_entry(*args):
    if entry_var.get().strip() != "":
        calculate_button.config(state=tk.NORMAL)
    else:
        calculate_button.config(state=tk.DISABLED)

entry_var.trace_add("write", check_entry)

calculate_button = tk.Button(window, text="Calculate Cube", command=on_calculate_click, state=tk.DISABLED)
calculate_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

window.mainloop()