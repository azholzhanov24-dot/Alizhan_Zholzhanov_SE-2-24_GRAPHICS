# Python GUI & Interface Design Assignments

This repository contains a complete collection of practical assignments and laboratory works for the **GRAPHICS** (Graphical User Interfaces) course completed during the academic semester.

## Student Information
* **Name:** Alizhan Zholzhanov
* **Group:** SE 2-24
* **Institution:** APEC PetroTechnic Higher College
* **Instructor:** Senior Lecturer Rakhym K.D.

---

## Repository Structure

The repository is organized chronologically, tracking the progression from basic UI design concepts to advanced multi-component applications and object-oriented programming (OOP) structures in Python.

### 📁 Task 1: UI/UX Concept Design
* **Topic:** Introduction to GUI vs CLI & Layout Architecture.
* **Description:** A purely visual wireframe and layout design for a *To-Do List / Notes* mobile application. Focuses on element hierarchy, spacing, text fields, and clear button positioning.

### 📁 Task 3: Basic GUI Application
* **Topic:** Introduction to Tkinter & Event Handling.
* **Description:** A core square calculator application implementing basic user interactions. Features an error-handling popup via `messagebox` for empty inputs and a "Clear" button bonus task.

### 📁 Task 4: Input Validation & UX Enhancements
* **Topic:** Advanced Validation & State Control.
* **Description:** An improved cube calculator featuring a three-tier input validation system (empty checks, numeric-only constraints, and negative number prevention). Includes dynamic state management where the action button is disabled until valid data is entered.

### 📁 Task 5: Structured GUI Application (OOP)
* **Topic:** Object-Oriented Programming in Tkinter.
* **Description:** Full refactoring of previous calculator projects into a clean, scalable Class structure. Eliminates unsafe global variables and isolates UI creation, data validation, and calculation logic into separate class methods.

### 📁 Task 6: Grid Layout & Multi-Input Forms
* **Topic:** Grid Geometry Manager & Registration Forms.
* **Description:** A comprehensive "Student Information Form" gathering multi-type data (Name, Age, Grade). Utilizes `.grid()` placement for precise form alignment, features multi-field data validation, and outputs formatted textual profiles.

### 📁 Task 7: Option Selection with Radiobuttons
* **Topic:** Grouped Conditional Elements.
* **Description:** An application utilizing `Radiobutton` widgets bound to a shared `tk.IntVar()`. It allows users to input a number and select a specific mathematical operation (Square, Cube, or Multiply by 10) via toggles.

### 📁 Task 8: Multi-Option Selection with Checkbuttons
* **Topic:** Independent Boolean Variables.
* **Description:** A service billing selection form using `Checkbutton` controls. Users can select multiple independent premium add-ons simultaneously, with a background loop dynamically calculating the aggregated final cost.

### 📁 Task 9: Dynamic Data Lists with Listbox
* **Topic:** Interactive Item Collections.
* **Description:** A dynamic Task Manager implementation using the `Listbox` widget. Supports real-time entry insertion with trimming validation, selective item removal using current item selections (`.curselection()`), and complete list clearing.
