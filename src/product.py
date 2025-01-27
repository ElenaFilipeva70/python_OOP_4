from typing import List


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict, products_list: List["Product"]) -> "Product":
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает
        созданный объект класса Product"""
        for product in products_list:
            if product.name == product_dict["name"]:
                product.quantity += product_dict["quantity"]
                if product_dict["price"] > product.price:
                    product.price = product_dict["price"]
                return product
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            print(f"Цена не была изменена, она осталась {self.__price}")
            return
        else:
            if new_price < self.__price:
                print("Вы действительно хотите изменить цену на меньшую? (y/n)")
                users_choice = str(input().strip().lower())
                if users_choice == "y":
                    self.__price = new_price
                    print(f"Цена изменена на {new_price}")
                else:
                    print(f"Цена не была изменена, она осталась {self.__price}")
                    return
            else:
                self.__price = new_price
                print(f"Цена изменена на {new_price}")
