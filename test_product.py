import pytest
from products import Product

def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-1450, quantity=100)  # Negative price

def test_product_quantity_zero():
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active()

def test_product_purchase():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(3)
    assert total_price == 4350
    assert product.quantity == 97

def test_product_purchase_invalid_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(150)  # Larger quantity than available

