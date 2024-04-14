import tkinter as tk
from tkinter import messagebox
import csv

# Function to read employee data from CSV file
def read_employee_data():
    file_path = 'GIG-logistics.csv'  # Specify the path to the CSV file
    employees = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            full_name = f"{row['SURNAME']}, {row['FIRST NAME']}"
            department = row['DEPARTMENT'].strip()
            employees[full_name.upper()] = department  # Store names in uppercase for case-insensitive matching
    return employees

# Function to handle employee verification
def check_employee():
    name = entry_name.get().strip()
    department = entry_department.get().strip()
    
    if name == '' or department == '':
        messagebox.showerror("Error", "Please enter both name and department.")
        return

    full_name = name.upper()
    if full_name in employees:
        if employees[full_name] == department:
            # Employee exists in the specified department
            messagebox.showinfo("Welcome", f"Welcome {full_name}!")
            # Find other members in the same department
            dept_members = [emp for emp, dept in employees.items() if dept == department and emp != full_name]
            if dept_members:
                messagebox.showinfo("Department Members", f"Other members in {department}: {', '.join(dept_members)}")
            else:
                messagebox.showinfo("Department Members", f"No other members in {department}")
        else:
            messagebox.showerror("Error", f"{full_name} is not in the {department} department.")
    else:
        messagebox.showerror("Error", f"{full_name} is not an employee.")

# Main GUI setup
root = tk.Tk()
root.title("Employee Verification")

# Read employee data from CSV
employees = read_employee_data()

# Name Label and Entry
label_name = tk.Label(root, text="Enter Name (Surname, First Name):")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Department Label and Entry
label_department = tk.Label(root, text="Enter Department:")
label_department.pack()
entry_department = tk.Entry(root)
entry_department.pack()

# Check Button
check_button = tk.Button(root, text="Check", command=check_employee)
check_button.pack()

# Run the main event loop
root.mainloop()
