class ProductValidator:
    @staticmethod
    def validate(product):
        if not product.name or not isinstance(product.name, str):
            return False, "Product name is required and must be a string."
        if product.description and not isinstance(product.description, str):
            return False, "Product description must be a string."
        if not isinstance(product.price, (int, float)) or product.price < 0:
            return False, "Product price must be a non-negative number."
        if not isinstance(product.quantity_in_stock, int) or product.quantity_in_stock < 0:
            return False, "Product quantity in stock must be a non-negative integer."
        return True, ""