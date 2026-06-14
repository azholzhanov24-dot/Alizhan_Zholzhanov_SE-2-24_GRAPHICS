import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Structured Calculator")
        self.window.geometry("320x260")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.window, text="Enter a number:")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(self.window)
        self.entry.pack(pady=5)
        
        self.result_label = tk.Label(self.window, text="Result:")
        self.result_label.pack(pady=5)
        
        self.calculate_button = tk.Button(self.window, text="Calculate Square", command=self.on_button_click)
        self.calculate_button.pack(pady=5)
        
        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_fields)
        self.clear_button.pack(pady=5)
        
    def validate_input(self, value):
        if value == "":
            messagebox.showerror("Error", "Input field is empty")
            return None
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value")
            return None
            
    def calculate_square(self, number):
        return number ** 2
        
    def on_button_click(self):
        value = self.entry.get()
        number = self.validate_input(value)
        if number is not None:
            result = self.calculate_square(number)
            self.result_label.config(text="Result: " + str(result))
            
    def clear_fields(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Result:")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()