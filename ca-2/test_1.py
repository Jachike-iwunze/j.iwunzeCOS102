import tkinter as tk
from tkinter import messagebox

#  function to define the menu items and prices
menu_items = {
    "RICE/PASTA": {
        "Jollof Rice": 350,
        "Coconut Fried Rice": 350,
        "Jollof Spaghetti": 350
    },
    "PROTEIN": {
        "Sweet Chilli chicken": 1100,
        "Grilled chicken wings": 400,
        "Fried beef": 400,
        "Fried fish": 500,
        "Boiled egg": 200,
        "Sauteed sausage": 200 
    },
    "SIDE DISHES": {
        "Savoury Beans": 350,
        "Roasted sweet potatoes": 300,
        "Fried Plantains": 150,
        "Mixed vegetable salad": 150,
        "Boiled yam": 150
    },
    "SOUPS & SWALLOWS": {
        "Eba": 100,
        "Pound0 Yam": 100,
        "Semo": 100,
        "Atamah soup": 450,
        "Egusi soup": 480
    },
    "BEVERAGES": {
        "Water": 200,
        "Glass drink (35cl)": 150,
        "PET drink (35cl)": 300,
        "PET drink (50cl)": 350,
        "Glass/canned malt": 500,
        "Fresh Yo": 600,
        "Pineapple juice": 350,
        "Mango juice": 350,
        "Zobo drink": 350
    },
}

def calculate_order():
    total_cost = 0

    # Retrieve user's name
    name = customer_name.get().strip()

    # check if user name is valid
    if not name:
        messagebox.showerror("Error", "Please input your name.")
        return

    # Calculate total cost based on users selected items and quantities
    for category, items in menu_items.items():
        for item, price in items.items():
            quantity_str = item_quantities[(category, item)].get()

            # Validate the quantities input
            if quantity_str.isdigit():
                quantity = int(quantity_str)
                if quantity >= 0:
                    total_cost += price * quantity
                else:
                    messagebox.showerror("Input Error", f"Invalid quantity entered for {item}: Quantity must be non-negative.")
            else:
                messagebox.showerror("Input Error", f"Invalid quantity entered for {item}: Quantity must be a valid integer.")

    # Determine discount based on total cost
    if total_cost < 1000:
        discount = 0
    elif total_cost < 2500:
        discount = 0.1
    elif total_cost < 5000:
        discount = 0.15
    else:
        discount = 0.25

    # Calculate discounted amount
    discount_amount = total_cost * (1 - discount)

    # Display order summary
    display_order_summary(total_cost, discount, discount_amount,name)

def display_order_summary(total_cost, discount, discount_amount,name):
    
    # Create a new window for displaying order summary
    summary_window = tk.Toplevel()
    summary_window.title("Order Summary")

    # Display order details in the new window
    tk.Label(summary_window, text = f"Customer Name: {name}").pack(pady=10)
    tk.Label(summary_window, text=f"Total Cost: ₦{total_cost}").pack(pady=10)
    tk.Label(summary_window, text=f"Discount: {discount * 100}%").pack(pady=10)
    tk.Label(summary_window, text=f"Discounted Amount: ₦{discount_amount}").pack(pady=10)

# Create the main GUI window
root = tk.Tk()
root.title("PAU Cafeteria Order System")

# Create a Canvas widget with a vertical scrollbar
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold menu items
frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Display the menu items inside the frame
item_quantities = {}
row_num = 0

for category, items in menu_items.items():
    category_label = tk.Label(frame, text=category, font=("Times New Roman", 12, "bold"), bg="white")
    category_label.grid(row=row_num, column=0, columnspan=2, pady=(10, 5), sticky="w")
    row_num += 1

    for item, price in items.items():
        
        # Display menu item label
        item_label = tk.Label(frame, text=f"{item} - ₦{price}", bg="white")
        item_label.grid(row=row_num, column=0, sticky="w", padx=10)

        # Entry widget for quantity input
        quantity_entry = tk.Entry(frame, width=5)
        quantity_entry.grid(row=row_num, column=1, sticky="w", padx=10)
        quantity_entry.insert(tk.END, "0")  # Initialize quantity entry with default value
        item_quantities[(category, item)] = quantity_entry

        row_num += 1

# Update scroll bar to enable scrolling 
frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Label and Entry widget for customer name
tk.Label(root, text="Enter Your Name:").pack(pady=10)
customer_name = tk.Entry(root)
customer_name.pack(pady=10)

# Button to calculate the total cost
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_order)
calculate_button.pack(pady=10)

# Run the main event loop
root.mainloop()
