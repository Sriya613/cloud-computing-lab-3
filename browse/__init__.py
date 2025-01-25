from products import dao
from typing import List, Dict, Any


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: Dict[str, Any]) -> "Product":
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products_data = dao.list_products()
    return [Product.load(product) for product in products_data]

def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found")
    return Product.load(product_data)

def add_product(product: Dict[str, Any]):
    required_keys = {"id", "name", "description", "cost", "qty"}
    if not required_keys.issubset(product.keys()):
        raise ValueError(f"prod data is missing one or more required keys: {required_keys}") 
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    if not dao.get_product(prooduct_id):
        raise ValueError(f"Prod with ID {product_id} does not exist")

    dao.update_qty(product_id, qty)
