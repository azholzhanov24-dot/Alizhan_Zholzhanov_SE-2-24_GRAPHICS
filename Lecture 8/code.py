import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Service Selection")
window.geometry("350x280")

label_title = tk.Label(window, text="Select additional options:", font=("Arial", 11, "bold"))
label_title.pack(pady=10)

chk_var1 = tk.BooleanVar()
chk_var2 = tk.BooleanVar()
chk_var3 = tk.BooleanVar()

check1 = tk.Checkbutton(window, text="Include Premium Support ($50)", variable=chk_var1)
check1.pack(anchor="w", padx=40, pady=5)

check2 = tk.Checkbutton(window, text="Include Fast Delivery ($20)", variable=chk_var2)
check2.pack(anchor="w", padx=40, pady=5)

check3 = tk.Checkbutton(window, text="Include Extended Warranty ($30)", variable=chk_var3)
check3.pack(anchor="w", padx=40, pady=5)

result_label = tk.Label(window, text="Total Cost: $0", font=("Arial", 10, "bold"), fg="blue")
result_label.pack(pady=15)

def calculate_total():
    total = 0
    selected_options = []
    
    if chk_var1.get():
        total += 50
        selected_options.append("Support")
    if chk_var2.get():
        total += 20
        selected_options.append("Delivery")
    if chk_var3.get():
        total += 30
        selected_options.append("Warranty")
        
    if total == 0:
        result_label.config(text="Total Cost: $0 (No options selected)")
    else:
        result_label.config(text=f"Total Cost: ${total} ({', '.join(selected_options)})")

def reset_selection():
    chk_var1.set(False)
    chk_var2.set(False)
    chk_var3.set(False)
    result_label.config(text="Total Cost: $0")

btn_total = tk.Button(window, text="Calculate Total", command=calculate_total)
btn_total.pack(pady=5)

btn_reset = tk.Button(window, text="Reset", command=reset_selection)
btn_reset.pack(pady=5)

window.mainloop()