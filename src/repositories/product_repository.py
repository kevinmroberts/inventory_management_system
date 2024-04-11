# product_repository.py
from src.repositories.repository_base import RepositoryBase
from src.models.product import Product

class ProductRepository(RepositoryBase):
    """
    A repository class for handling database operations related to products.

    This class provides static methods for CRUD operations on the Product table,
    abstracting away the direct database access.
    """

    @staticmethod
    def create_product(product):
        """
        Inserts a new product into the database.

        Parameters:
            product (Product): The product object to be inserted into the database.

        Returns:
            int: The last inserted ID of the new product.
        """
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Product (name, description, price, quantity_in_stock) VALUES (?, ?, ?, ?)",
                (product.name, product.description, product.price, product.quantity_in_stock)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_product_by_id(product_id):
        """
        Retrieves a product by its ID.

        Parameters:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: An instance of the Product model or None if not found.
        """
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Product(id=row[0], name=row[1], description=row[2], price=row[3], quantity_in_stock=row[4])
            return None

    @staticmethod
    def read_products():
        """
        Fetches all products from the database.

        Returns:
            list[Product]: A list of Product instances representing all products in the database.
        """
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product")
            return [Product(id=row[0], name=row[1], description=row[2], price=row[3], quantity_in_stock=row[4]) for row in cursor.fetchall()]

    @staticmethod
    def update_product(product):
        """
        Updates a product's details in the database.

        Parameters:
            product (Product): The product instance with updated details to be saved to the database.
        """
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            sql = """
            UPDATE Product
            SET name = ?, description = ?, price = ?, quantity_in_stock = ?
            WHERE id = ?
            """
            cursor.execute(sql, (product.name, product.description, product.price, product.quantity_in_stock, product.id))
            conn.commit()

    @staticmethod
    def delete_product(product):
        """
        Deletes a product from the database.

        Parameters:
            product (Product): The product instance to be deleted from the database.
        """
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Product WHERE id = ?", (product.id,))
            conn.commit()
