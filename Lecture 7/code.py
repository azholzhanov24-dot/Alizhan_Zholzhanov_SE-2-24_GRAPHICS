import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Operations with Radiobuttons")
window.geometry("350x300")

label = tk.Label(window, text="Enter a number:")
label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

operation_var = tk.IntVar()
operation_var.set(1)

radio_square = tk.Radiobutton(window, text="Calculate Square", variable=operation_var, value=1)
radio_square.pack(anchor="w", padx=50, pady=2)

radio_cube = tk.Radiobutton(window, text="Calculate Cube", variable=operation_var, value=2)
radio_cube.pack(anchor="w", padx=50, pady=2)

radio_multiply = tk.Radiobutton(window, text="Multiply by 10", variable=operation_var, value=3)
radio_multiply.pack(anchor="w", padx=50, pady=2)

result_label = tk.Label(window, text="Result:", font=("Arial", 10, "bold"))
result_label.pack(pady=15)

def process_operation():
    value = entry.get().strip()
    
    if value == "":
        messagebox.showerror("Error", "Please enter a number")
        return
        
    try:
        number = float(value)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Enter a numeric value.")
        return

    choice = operation_var.get()
    if choice == 1:
        result = number ** 2
    elif choice == 2:
        result = number ** 3
    elif choice == 3:
        result = number * 10
        
    result_label.config(text="Result: " + str(result))

def clear_all():
    entry.delete(0, tk.END)
    operation_var.set(1)
    result_label.config(text="Result:")

btn_calc = tk.Button(window, text="Execute", command=process_operation)
btn_calc.pack(pady=5)

btn_clear = tk.Button(window, text="Clear", command=clear_all)
btn_clear.pack(pady=5)

window.mainloop()