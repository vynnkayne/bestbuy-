class Product:
    """A class representing a product."""

    def __init__(self, name, price, quantity):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        if not name:
            raise ValueError("Invalid name: Name cannot be empty.")
        if price < 0:
            raise ValueError("Invalid price: Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Invalid quantity: Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Get the quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        """
        Check if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """
        Generate a string representation of the product.

        Returns:
            str: The string representation of the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buy a specific quantity of the product and calculate the total price.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.
        """
        if not self.active:
            raise Exception("Product is not active.")

        if quantity <= 0:
            raise ValueError("Invalid quantity: Quantity must be positive.")

        if quantity > self.quantity:
            raise ValueError("Invalid quantity: Not enough stock available.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
