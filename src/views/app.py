# app.py

import tkinter as tk
from tkinter import ttk
from src.views.add_product import add_product_popup
from src.utils.utils import center_window
from src.utils.singleton import Singleton
from src.utils.event_manager import EventManager, PRODUCT_ADDED, PRODUCT_DELETED
from src.services.product_service import ProductService
from src.controllers.product_controller import ProductController


class App(Singleton):
    def __init__(self):
        super().__init__()
        
        self.root = tk.Tk()
        self.root.title("Inventory Management System")
        self.event_manager = EventManager()
        self.product_service = ProductService(self.event_manager)
        
        # Initialize GUI components first without the parts that depend on product_controller
        self.setup_basic_gui()

        # Initialize ProductController here, before calling the parts of setup_gui that use it
        self.product_controller = ProductController(self.root, self.event_manager, self.product_service, self.treeview)

        # Now that product_controller is set up, complete the rest of the GUI setup
        self.setup_product_related_gui()

        # Load products into the treeview
        self.product_controller.load_products()

    def setup_basic_gui(self):
        # Set the window's size and other initial GUI setup here, up until before adding product-related widgets
        window_width = 800
        window_height = 600
        center_window(self.root, window_width, window_height)
        self.root.geometry(f"{window_width}x{window_height}")

        left_frame = ttk.Frame(self.root)
        left_frame.pack(side="left", fill="both", expand=True)

        self.treeview = ttk.Treeview(left_frame, columns=('ID', 'Name', 'Description', 'Price', 'Quantity In Stock'), show='headings')
        self.treeview.pack(side='top', fill='both', expand=True)

        for col in self.treeview['columns']:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100, anchor='center')

        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def setup_product_related_gui(self):
        # Continue the GUI setup that involves product-related widgets and actions
        right_frame = ttk.Frame(self.root)
        right_frame.pack(side="right", fill="y")

        add_product_button = ttk.Button(right_frame, text="Add Product", command=lambda: add_product_popup(self.root, self.event_manager))
        add_product_button.pack(pady=10)

        remove_product_button = ttk.Button(right_frame, text="Remove Product", command=self.product_controller.on_delete_product_button_click)
        remove_product_button.pack(pady=10)

        # Add any other product-related GUI components here


    def run(self):
        # Run the main event loop
        self.root.mainloop()