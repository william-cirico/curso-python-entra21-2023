import pytest

from product import Product

def test_product_creation():
    product = Product("Produto 01", 100, 10)
    
    assert product.in_stock == 10
    
def test_buy_product():
    product = Product("Produto 01", 100, 10)
    
    product.buy_product(5)
    
    assert product.in_stock == 15
    
def test_sell_product():
    product = Product("Produto 01", 100, 10)
    
    product.sell_product(5)
    
    assert product.in_stock == 5
    
def test_sell_product_without_stock(capfd):
    product = Product("Produto 01", 100, 10)
    
    product.sell_product(11)
    
    out, _ = capfd.readouterr()
    
    assert out == "Não há estoque para realizar a operação.\n"
    
def test_get_total_value():
    product = Product("Produto 01", 100, 10)
    
    assert product.get_total_value() == 1000