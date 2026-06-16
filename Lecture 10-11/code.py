import tkinter as tk
from tkinter import messagebox
import os

class StudentRecordApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Student Record System")
        self.window.geometry("380x320")
        
        self.file_path = "students.txt"
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.window, text="Student Name:").pack(pady=2)
        self.entry_name = tk.Entry(self.window, width=30)
        self.entry_name.pack(pady=2)
        
        tk.Label(self.window, text="Age:").pack(pady=2)
        self.entry_age = tk.Entry(self.window, width=30)
        self.entry_age.pack(pady=2)
        
        tk.Label(self.window, text="Course/Major:").pack(pady=2)
        self.entry_course = tk.Entry(self.window, width=30)
        self.entry_course.pack(pady=2)
        
        self.btn_save = tk.Button(self.window, text="Save to File", command=self.save_record, width=15)
        self.btn_save.pack(pady=5)
        
        self.btn_view = tk.Button(self.window, text="View Records", command=self.view_records, width=15)
        self.btn_view.pack(pady=5)
        
        self.btn_clear = tk.Button(self.window, text="Clear Form", command=self.clear_form, width=15)
        self.btn_clear.pack(pady=5)

    def save_record(self):
        name = self.entry_name.get().strip()
        age = self.entry_age.get().strip()
        course = self.entry_course.get().strip()
        
        if not name or not age or not course:
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            age_num = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer!")
            return
            
        with open(self.file_path, "a") as file:
            file.write(f"Name: {name} | Age: {age_num} | Course: {course}\n")
            
        messagebox.showinfo("Success", "Record saved successfully!")
        self.clear_form()
        
    def view_records(self):
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            messagebox.showinfo("Records", "No records found.")
            return
            
        with open(self.file_path, "r") as file:
            records = file.read()
            
        records_window = tk.Toplevel(self.window)
        records_window.title("Saved Student Records")
        records_window.geometry("400x300")
        
        text_area = tk.Text(records_window, wrap="word")
        text_area.insert(tk.END, records)
        text_area.config(state=tk.DISABLED)
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_course.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StudentRecordApp()
    app.run()


