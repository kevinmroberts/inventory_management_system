import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.services.product_service import create_product
from src.services.database_service import connect_to_database
from src.utils.utils import center_window
from src.utils.event_manager import PRODUCT_ADDED

def add_product_popup(root, event_manager):
    popup = tk.Toplevel(root)
    popup.title("Add Product")
    popup_width = 300
    popup_height = 200
    center_window(popup, popup_width, popup_height)

    # Create labels and entry fields for product details
    name_label = tk.Label(popup, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(popup)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    description_label = tk.Label(popup, text="Description:")
    description_label.grid(row=1, column=0, padx=5, pady=5)
    description_entry = tk.Entry(popup)
    description_entry.grid(row=1, column=1, padx=5, pady=5)

    price_label = tk.Label(popup, text="Price:")
    price_label.grid(row=2, column=0, padx=5, pady=5)
    price_entry = tk.Entry(popup)
    price_entry.grid(row=2, column=1, padx=5, pady=5)

    quantity_label = tk.Label(popup, text="Quantity:")
    quantity_label.grid(row=3, column=0, padx=5, pady=5)
    quantity_entry = tk.Entry(popup)
    quantity_entry.grid(row=3, column=1, padx=5, pady=5)

    # Function to add product to the database
    def add_product():
        # Get product details from the entry fields
        name = name_entry.get()
        description = description_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        create_product(name, description, price, quantity)
        messagebox.showinfo("Success", "Product added successfully.")
        event_manager.publish(PRODUCT_ADDED) # Publish the product_added event
        popup.destroy() # Close the popup

    # Create the "Add Product" button
    add_product_button = tk.Button(popup, text="Add Product", command=add_product)
    add_product_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


    # Run the main event loop for the popup window
    popup.mainloop()
