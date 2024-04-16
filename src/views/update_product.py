import tkinter as tk
from tkinter import messagebox, ttk
from src.utils.utils import center_window
from src.utils.event_manager import PRODUCT_ADDED
from src.services.product_service import ProductService
from src.models.product import Product

def update_product_popup(root, event_manager, product: Product):
    """
    Creates and displays a popup window for updating a product.

    This function sets up a simple form within a popup window where users can enter details
    for a new product, including its name, description, price, and quantity in stock.
    Once the information is submitted, the product is added to the inventory through the ProductService.

    Parameters:
        root (tk.Tk): The root window to which this popup belongs.
        event_manager: The event manager instance for handling PRODUCT_ADDED events.

    """
    if product is None:
        messagebox.showerror("Error", "No product selected or product not found.", parent=root)
        return
    popup = tk.Toplevel(root)
    popup.title("Update Product")
    popup_width = 300
    popup_height = 200
    center_window(popup, popup_width, popup_height)

    # Labels and entry fields for product details
    name_label = tk.Label(popup, text=f"Name:")
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

    name_entry.insert(0, product.name)
    description_entry.insert(0, product.description)
    price_entry.insert(0, str(product.price))
    quantity_entry.insert(0, str(product.quantity_in_stock))


    product_service = ProductService(event_manager)  # ProductService instance

    def update_product():
        """
        Collects product details from the form, validates them, and adds the product.

        This inner function is triggered when the "Update Product" button is clicked.
        It collects input from the user, validates the price and quantity to ensure they are numbers,
        and then attempts to update the product using the ProductService. Feedback is provided via popup messages.
        """
        name = name_entry.get()
        description = description_entry.get()
        
        try:
            price = float(price_entry.get())
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure price and quantity are valid numbers.", parent=popup)
            return
        
        updated_product = Product(name, description, price, quantity, product.id)
        isCreated, error_message = product_service.update_product(updated_product)
        if isCreated:
            messagebox.showinfo("Success", "Product updated successfully.", parent=popup)
            popup.destroy()  # Close the popup upon successful update
        else:
            messagebox.showerror("Error", error_message, parent=popup)

    update_product_button = tk.Button(popup, text="Update Product", command=update_product)
    update_product_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    popup.mainloop()
