class Product:
    def __init__(self, name, description, price, quantity_in_stock, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.id = id
