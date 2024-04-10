# main_app.py

import tkinter as tk
from tkinter import ttk
from src.gui.add_product import add_product_popup
from src.utils.utils import center_window
from src.utils.singleton import Singleton
from src.utils.event_manager import EventManager, PRODUCT_ADDED
from src.services.product_service import ProductService

class MainApp(Singleton):
    def __init__(self):
        # Ensure only one instance of MainApp is created
        super().__init__()
        
        self.root = tk.Tk()
        self.root.title("Inventory Management System")
        self.event_manager = EventManager()
        self.setup_gui()

        # Subscribe to the product_added event
        self.event_manager.subscribe(PRODUCT_ADDED, self.load_products)

    def setup_gui(self):
        # Set the window's size
        window_width = 800
        window_height = 600

        # Center the window on the screen
        center_window(self.root, window_width, window_height)

        # Set the window's size explicitly
        self.root.geometry(f"{window_width}x{window_height}")

        # Create a frame to hold the left section (inventory table)
        left_frame = ttk.Frame(self.root)
        left_frame.pack(side="left", fill="both", expand=True)

        # Create a frame to hold the right section (action buttons)
        right_frame = ttk.Frame(self.root)
        right_frame.pack(side="right", fill="y")

        # Add widgets to the left frame (inventory table)
        inventory_label = ttk.Label(left_frame, text="Inventory Table")
        inventory_label.pack()

        # Initialize the treeview as an instance attribute
        self.treeview = ttk.Treeview(left_frame, columns=('ID', 'Name', 'Description', 'Price', 'Quantity In Stock'), show='headings')
        self.treeview.pack(side='top', fill='both', expand=True)

        # Define headings
        for col in self.treeview['columns']:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100, anchor='center')

        # Initialize products in the treeview
        self.load_products()

        # Scrollbar
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Add widgets to the right frame (action buttons)
        add_product_button = ttk.Button(right_frame, text="Add Product", command=lambda: add_product_popup(self.root, self.event_manager))
        add_product_button.pack(pady=10)

        remove_product_button = ttk.Button(right_frame, text="Remove Product")
        remove_product_button.pack(pady=10)

        manage_categories_button = ttk.Button(right_frame, text="Manage Categories")
        manage_categories_button.pack(pady=10)

        update_inventory_button = ttk.Button(right_frame, text="Update Inventory")
        update_inventory_button.pack(pady=10)

    def load_products(self, _=None):
        """
        Load products from the database and insert them into the Treeview.
        """
        # Clear the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            
        # Fetch new product data and populate the treeview
        for product in ProductService.fetch_products():
            self.treeview.insert('', 'end', values=product)

    def run(self):
        # Run the main event loop
        self.root.mainloop()