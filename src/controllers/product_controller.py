from src.utils.event_manager import PRODUCT_ADDED, PRODUCT_DELETED
from tkinter import messagebox

class ProductController:
    """
    Controls the product management operations within the application.

    This controller handles the interactions between the product service layer and the UI,
    including loading products into the UI, deleting a product, and responding to other product-related events.

    Attributes:
        root (tk.Tk): The root Tkinter window.
        event_manager (EventManager): The event manager for subscribing to and publishing events.
        product_service (ProductService): The service layer for product operations.
        treeview (ttk.Treeview): The Treeview widget for displaying products.
    """

    def __init__(self, root, event_manager, product_service, treeview):
        """
        Initializes the ProductController with the necessary components.

        Parameters:
            root (tk.Tk): The root Tkinter window.
            event_manager (EventManager): The event manager for subscribing and publishing events.
            product_service (ProductService): The service layer for product operations.
            treeview (ttk.Treeview): The Treeview widget for displaying products.
        """
        self.root = root
        self.event_manager = event_manager
        self.product_service = product_service
        self.treeview = treeview

        # Subscribe to product related events
        self.event_manager.subscribe(PRODUCT_ADDED, self.load_products)
        self.event_manager.subscribe(PRODUCT_DELETED, self.load_products)

    def load_products(self, _=None):
        """
        Loads products from the product service into the Treeview widget.

        This method is subscribed to PRODUCT_ADDED and PRODUCT_DELETED events
        to refresh the product list when products are added or deleted.
        """
        self.treeview.delete(*self.treeview.get_children())
        for product in self.product_service.fetch_products():
            self.treeview.insert('', 'end', values=(product.id, product.name, product.description, product.price, product.quantity_in_stock))

    def on_delete_product_button_click(self):
        """
        Handles the deletion of a selected product.

        This method is triggered when the delete product button is clicked.
        It confirms the deletion with the user before proceeding.
        """
        selected_product_id = self.get_selected_product_id()
        if selected_product_id:
            product_to_delete = self.product_service.get_product_by_id(selected_product_id)
            if product_to_delete:
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {product_to_delete.name}?", parent=self.root)
                if confirm:
                    self.product_service.delete_product(product_to_delete)
                    self.load_products()
            else:
                messagebox.showwarning("Error", "Product not found.", parent=self.root)

    def get_selected_product_id(self):
        """
        Retrieves the ID of the currently selected product in the Treeview.

        Returns:
            The ID of the selected product or None if no product is selected.
        """
        selected_items = self.treeview.selection()
        if selected_items:
            selected_item = selected_items[0]
            item = self.treeview.item(selected_item)
            return item['values'][0]
        messagebox.showwarning("Selection Error", "Please select a product first.", parent=self.root)
