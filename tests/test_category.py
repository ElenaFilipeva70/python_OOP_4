from src.category import Category
from src.product import Product


def test_category(first_category: Category, second_category: Category) -> None:
    """Тестируем инициализацию объекта класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций"
    )
    assert len(first_category.products_in_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_products_property(first_category: Category) -> None:
    """Тестируем геттер, который возвращает строку со всеми продуктами в приватном атрибуте products"""
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product(first_category: Category) -> None:
    """Тестируем метод для добавления продукта в атрибут products"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    assert len(first_category.products_in_list) == 3
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 4


def test_category_str(second_category: Category) -> None:
    """Тестируем строковое отображение товаров в категории"""
    assert str(second_category) == "Телевизоры, количество продуктов: 7 шт."
