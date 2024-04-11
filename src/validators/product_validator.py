class ProductValidator:
    """
    A utility class for validating Product instances against predefined rules
    to ensure data integrity before performing database operations.
    """

    @staticmethod
    def validate(product):
        """
        Validates a Product instance against various integrity and format rules.

        Validation rules include:
        - The product name must be provided and must be a string.
        - The product description, if provided, must be a string.
        - The product price must be a non-negative number (int or float).
        - The product quantity in stock must be a non-negative integer.

        Parameters:
            product (Product): The Product instance to validate.

        Returns:
            tuple: A tuple containing a boolean and a message string.
                   The boolean is True if the product passes all validation checks,
                   and False otherwise. The message string contains the reason for
                   validation failure or an empty string if validation is successful.
        """
        if not product.name or not isinstance(product.name, str):
            return False, "Product name is required and must be a string."
        
        if product.description and not isinstance(product.description, str):
            return False, "Product description must be a string."
        
        if not isinstance(product.price, (int, float)) or product.price < 0:
            return False, "Product price must be a non-negative number."
        
        if not isinstance(product.quantity_in_stock, int) or product.quantity_in_stock < 0:
            return False, "Product quantity in stock must be a non-negative integer."
        
        return True, ""
