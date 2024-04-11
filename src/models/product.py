class Product:
    """
    Represents a product in the inventory system.

    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (float): The price of the product.
        quantity_in_stock (int): The quantity of the product currently in stock.
        id (int, optional): The unique identifier for the product. Defaults to None.
    """

    def __init__(self, name, description, price, quantity_in_stock, id=None):
        """
        Constructs all the necessary attributes for the product object.

        Parameters:
            name (str): The name of the product.
            description (str): A brief description of the product.
            price (float): The price of the product.
            quantity_in_stock (int): The quantity of the product currently in stock.
            id (int, optional): The unique identifier for the product. Defaults to None.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.id = id
