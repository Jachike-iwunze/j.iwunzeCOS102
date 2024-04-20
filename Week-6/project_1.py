import tkinter as tk
from tkinter import messagebox

# Function to calculate delivery charge
def calculate_charge():
    location = location_var.get()
    weight = weight_var.get()
    
    if location == "Ibeju-Lekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "Epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        messagebox.showerror("Error", "Invalid location")
        return
    
    messagebox.showinfo("Delivery Charge", f"You need to pay: N{charge}")

# Create main window
root = tk.Tk()
root.title("Simi Services Delivery Calculator")

# Location dropdown
tk.Label(root, text="Location:").pack()
location_var = tk.StringVar()
location_var.set("Ibeju-Lekki")  # Default location
location_option = tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe")
location_option.pack(pady=10)

# Weight entry
tk.Label(root, text="Package Weight (kg):").pack()
weight_var = tk.IntVar()
weight_entry = tk.Entry(root, textvariable=weight_var)
weight_entry.pack(pady=10)

# Button to calculate charge
calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.pack(pady=20)

# Run the main loop
root.mainloop()
