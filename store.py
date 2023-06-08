from typing import List
from products import Product

class Store:
    """A class representing a store."""

    def __init__(self, products: List[Product]):
        """
        Initialize a Store object.

        Args:
            products (List[Product]): The list of products in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Add a product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of products in the store.

        Returns:
            int: The total quantity of products.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Get a list of all active products in the store.

        Returns:
            List[Product]: The list of active products.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Place an order for the given shopping list and calculate the total price.

        Args:
            shopping_list (List[tuple]): The shopping list containing tuples of (product, quantity).

        Returns:
            float: The total price of the order.
        """
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)
        return total_price
