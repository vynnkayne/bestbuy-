from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        """
        Initialize a Promotion object.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the promotion to the given product and quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        pass


class PercentageDiscount(Promotion):
    """Class representing a percentage discount promotion."""

    def __init__(self, name, discount_percentage):
        """
        Initialize a PercentageDiscount object.

        Args:
            name (str): The name of the promotion.
            discount_percentage (float): The percentage discount to apply.
        """
        super().__init__(name)
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount promotion to the product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        original_price = product.price * quantity
        discount_amount = original_price * (self.discount_percentage / 100)
        discounted_price = original_price - discount_amount
        return discounted_price


class SecondItemHalfPrice(Promotion):
    """Class representing the second item at half price promotion."""

    def __init__(self, name):
        """
        Initialize a SecondItemHalfPrice object.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the second item at half price promotion to the product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        full_price_items = quantity - quantity // 2
        discounted_price = full_price_items * product.price + (quantity // 2) * (product.price / 2)
        return discounted_price


class Buy2Get1Free(Promotion):
    """Class representing the buy 2, get 1 free promotion."""

    def __init__(self, name):
        """
        Initialize a Buy2Get1Free object.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the buy 2, get 1 free promotion to the product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        full_price_items = quantity - quantity // 3
        discounted_price = full_price_items * product.price
        return discounted_price


class Product:
    def __init__(self, name, price, quantity):
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
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")

        if quantity <= 0:
            raise ValueError("Invalid quantity: Quantity must be positive.")

        if quantity > self.quantity:
            raise ValueError("Invalid quantity: Not enough stock available.")

        total_price = self.price * quantity

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None

