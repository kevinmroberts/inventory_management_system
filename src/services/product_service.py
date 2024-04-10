import sqlite3
from src.repositories.product_repository import ProductRepository
from src.utils.event_manager import PRODUCT_ADDED

class ProductService:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def fetch_products():
        """
        Fetch all products from the database and return them as a list of tuples.
        Each tuple represents a product with (id, name, description, price, quantity).
        """
        try:
            products = ProductRepository.read_products()
        except Exception as e:
            print(f"Error fetching products: {e}")
            products = []  # Return an empty list if there's an error
            
        return products

    # Function to add product to the database
    def add_product(self, name, description, price, quantity):
        ProductRepository.create_product(name, description, price, quantity)
        self.event_manager.publish(PRODUCT_ADDED)

