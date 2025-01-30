from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0
    products_list: list = []

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)
        Category.products_list.extend(products)


    def __str__(self):
        quantity_sum = 0
        for product in self.__products:
            quantity_sum += product.quantity
        return f"{self.name}, количество продуктов: {quantity_sum} шт."


    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в атрибут products"""
        self.__products.append(product)
        Category.product_count += 1
        Category.products_list.append(product)

    @property
    def products(self) -> str:
        """Геттер возвращает строку со всеми продуктами в приватном атрибуте products"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self) -> list:
        """Геттер, который возвращает приватный атрибут products в виде списка"""
        return self.__products
