# product_repository.py
from src.repositories.repository_base import RepositoryBase

class ProductRepository(RepositoryBase):

    @staticmethod
    def create_product(name, description, price, quantity_in_stock):
        """Insert a new product into the database."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Product (name, description, price, quantity_in_stock) VALUES (?, ?, ?, ?)",
                (name, description, price, quantity_in_stock)
            )
            conn.commit()

    @staticmethod
    def read_products():
        """Fetch all products from the database."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, description, price, quantity_in_stock FROM Product")
            return cursor.fetchall()

    @staticmethod
    def update_product(product_id, name=None, description=None, price=None, quantity_in_stock=None):
        """Update a product's details in the database."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            update_values = []
            if name:
                update_values.append(("name", name))
            if description:
                update_values.append(("description", description))
            if price:
                update_values.append(("price", price))
            if quantity_in_stock:
                update_values.append(("quantity_in_stock", quantity_in_stock))

            set_clause = ", ".join([f"{field} = ?" for field, _ in update_values])

            cursor.execute(
                f"UPDATE Product SET {set_clause} WHERE id = ?",
                [value for _, value in update_values] + [product_id]
            )
            conn.commit()

    @staticmethod
    def delete_product(product_id):
        """Delete a product from the database."""
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Product WHERE id = ?", (product_id,))
            conn.commit()