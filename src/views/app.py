import tkinter as tk
from tkinter import ttk
from src.views.add_product import add_product_popup
from src.utils.utils import center_window
from src.utils.singleton import Singleton
from src.utils.event_manager import EventManager, PRODUCT_ADDED, PRODUCT_DELETED
from src.services.product_service import ProductService
from src.controllers.product_controller import ProductController

class App(Singleton):
    """Singleton class representing the main application for Inventory Management System."""

    def __init__(self):
        """
        Initializes the App instance.

        Sets up the Tkinter root window, event manager, product service, and GUI components.
        """
        if not hasattr(self, 'initialized') or not self.initialized:
            self.root = tk.Tk()
            self.root.title("Inventory Management System")
            self.event_manager = EventManager()
            self.product_service = ProductService(self.event_manager)
            self.setup_basic_gui()
            self.product_controller = ProductController(self.root, self.event_manager, self.product_service, self.treeview)
            

            self.setup_product_related_gui()

            self.initialized = True

    def setup_basic_gui(self):
        """
        Sets up the basic GUI components of the application.

        This includes the main window, the treeview for displaying products, and the left frame with scrollbar.
        """
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
        """
        Sets up the GUI components related to product management.

        This includes buttons for adding and removing products, and any other product-related GUI components.
        """
        right_frame = ttk.Frame(self.root)
        right_frame.pack(side="right", fill="y")

        add_product_button = ttk.Button(right_frame, text="Add Product", command=lambda: add_product_popup(self.root, self.event_manager))
        add_product_button.pack(pady=10)

        remove_product_button = ttk.Button(right_frame, text="Remove Product", command=self.product_controller.on_delete_product_button_click)
        remove_product_button.pack(pady=10)

        # Add any other product-related GUI components here


    def run(self):
        """Runs the main event loop of the application."""
        self.root.mainloop()
