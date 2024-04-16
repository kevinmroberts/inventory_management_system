from src.repositories.product_repository import ProductRepository
from src.utils.event_manager import PRODUCT_ADDED, PRODUCT_DELETED, PRODUCT_UPDATED
from src.validators.product_validator import ProductValidator

class ProductService:
    """
    Provides service layer functionalities for product management including fetching,
    adding, and deleting products, with validation and event management.

    Attributes:
        event_manager: The event manager to publish events related to product operations.
    """

    def __init__(self, event_manager):
        """
        Initializes the ProductService with an event manager.

        Parameters:
            event_manager: The event manager to publish product-related events.
        """
        self.event_manager = event_manager

    def fetch_products(self):
        """
        Fetches all products from the database and returns them as a list of Product instances.

        Returns:
            A list of Product instances representing all products in the database. Returns an empty list in case of any error.
        """
        try:
            products = ProductRepository.read_products()
            return products
        except Exception as e:
            print(f"Error fetching products: {e}")
            return []

    def add_product(self, product):
        """
        Validates and adds a new product to the database. Publishes a PRODUCT_ADDED event upon successful addition.

        Parameters:
            product: The Product instance to be added to the database.

        Returns:
            A tuple containing a boolean indicating success or failure, and a message string.
        """
        is_valid, error_message = ProductValidator.validate(product)
        if not is_valid:
            print(f"Validation error: {error_message}")
            return False, error_message

        try:
            ProductRepository.create_product(product)
            self.event_manager.publish(PRODUCT_ADDED)
            return True, "Product added successfully."
        except Exception as e:
            print(f"Error adding product: {e}")
            return False, "Error adding product."
        
    def update_product(self, product):
        is_valid, error_message = ProductValidator.validate(product)
        if not is_valid:
            print(f"Validation error: {error_message}")
            return False, error_message
        
        try:
            ProductRepository.update_product(product)
            self.event_manager.publish(PRODUCT_UPDATED)
            return True, ""
        except Exception as e:
            print(f"Error updating product: {e}.")
            return False, "Error updating product."

    def delete_product(self, product):
        """
        Deletes a product from the database and publishes a PRODUCT_DELETED event upon successful deletion.

        Parameters:
            product: The Product instance to be deleted from the database.

        Returns:
            True if the deletion was successful, False otherwise.
        """
        try:
            ProductRepository.delete_product(product)
            self.event_manager.publish(PRODUCT_DELETED)
            return True
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False

    def get_product_by_id(self, product_id):
        """
        Retrieves a single product by its ID from the database.

        Parameters:
            product_id: The ID of the product to retrieve.

        Returns:
            The Product instance corresponding to the provided ID, or None if not found.
        """
        try:
            product = ProductRepository.get_product_by_id(product_id)
            return product  # Directly return the product or None
        except Exception as e:
            print(f"Error fetching product: {e}")
            return None
