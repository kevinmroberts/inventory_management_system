from src.repositories.product_repository import ProductRepository
from src.utils.event_manager import PRODUCT_ADDED, PRODUCT_DELETED
from src.validators.product_validator import ProductValidator

class ProductService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    # Function to fetch products from the database
    def fetch_products(self):
        """
        Fetch all products from the database and return them as a list of Product instances.
        """
        try:
            products = ProductRepository.read_products()
            return products  # Directly return the list of Product instances
        except Exception as e:
            print(f"Error fetching products: {e}")
            return []  # Return an empty list in case of an error


    # Function to add product to the database
    def add_product(self, product):
        """Calls the repository function to add a product after validation."""
        is_valid, error_message = ProductValidator.validate(product)
        if not is_valid:
            print(f"Validation error: {error_message}")
            return False, error_message

        try:
            ProductRepository.create_product(product)
            self.event_manager.publish(PRODUCT_ADDED)
            return True, "Product added succesfully."
        except Exception as e:
            print(f"Error adding product: {e}")
            return False, error_message
        
    # Function to delete product from the database
    def delete_product(self, product):
        """Calls the repository function to delete a product."""
        try:
            ProductRepository.delete_product(product)
            self.event_manager.publish(PRODUCT_DELETED)
            return True
        except Exception as e:
            print(f"Error deleting product: {e}")
            return False
    
    # Function to get product by id from the database
    def get_product_by_id(self, product_id):
        """Calls the repository function to get a product by id"""
        return ProductRepository.get_product_by_id(product_id)

        
    


