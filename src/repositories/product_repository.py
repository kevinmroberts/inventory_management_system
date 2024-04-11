# product_repository.py
from src.repositories.repository_base import RepositoryBase
from src.models.product import Product

class ProductRepository(RepositoryBase):

    @staticmethod
    def create_product(product):
        """Insert a new product into the database using the Product model."""
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
        """Retrieves a product by id."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return Product(id=row[0], name=row[1], description=row[2], price=row[3], quantity_in_stock=row[4])
            return None


    @staticmethod
    def read_products():
        """Fetch all products from the database."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product")
            products = [Product(id=row[0], name=row[1], description=row[2], price=row[3], quantity_in_stock=row[4]) for row in cursor.fetchall()]
            return products

    @staticmethod
    def update_product(product):
        """Update a product's details in the database using a Product model."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Prepare the SQL statement with placeholders for values to be updated
            sql = """
            UPDATE Product
            SET name = ?, description = ?, price = ?, quantity_in_stock = ?
            WHERE id = ?
            """
            
            # Prepare the values to update based on the product model
            values = (product.name, product.description, product.price, product.quantity_in_stock, product.id)
            
            # Execute the update statement with the provided values
            cursor.execute(sql, values)
            conn.commit()

    @staticmethod
    def delete_product(product):
        """Delete a product from the database using a Product model."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Product WHERE id = ?", (product.id,))
            conn.commit()
