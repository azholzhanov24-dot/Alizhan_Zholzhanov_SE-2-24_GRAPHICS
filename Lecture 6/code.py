import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Information Form")
window.geometry("350x280")

tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Grade:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_grade = tk.Entry(window)
entry_grade.grid(row=2, column=1, padx=10, pady=5)

result_label = tk.Label(window, text="", justify="left", font=("Arial", 10, "bold"))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

def submit_form():
    name = entry_name.get().strip()
    age_raw = entry_age.get().strip()
    grade = entry_grade.get().strip()
    
    if name == "" or age_raw == "" or grade == "":
        messagebox.showerror("Error", "All fields must be filled!")
        return
        
    try:
        age = int(age_raw)
    except ValueError:
        messagebox.showerror("Error", "Age must be a numeric value!")
        return
        
    output = f"Student: {name}\nAge: {age}\nGrade: {grade}"
    result_label.config(text=output)

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    result_label.config(text="")

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_form)
clear_button.grid(row=4, column=1, padx=10, pady=10)

window.mainloop()