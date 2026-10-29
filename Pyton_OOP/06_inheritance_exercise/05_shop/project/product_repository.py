from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name: str) -> None:
        searched_product = self.find(product_name)
        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self) -> str:
        return '\n'.join([
            f"{product.name}: {product.quantity}"
            for product in self.products])
