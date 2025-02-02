from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.category import Category
from src.product import Product


def test_product_init(product: Product) -> None:
    """Тестируем инициализацию объекта класса Product"""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_new_product_different(first_category: Category) -> None:
    """Тестируем метод, который принимает на вход параметры отличного от других наименований товара и возвращает
    созданный объект класса Product"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S32 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 5,
        },
        first_category.products_list,
    )
    assert new_product.name == "Samsung Galaxy S32 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180010.0
    assert new_product.quantity == 5


def test_product_new_product_identical(first_category: Category) -> None:
    """Тестируем метод, который принимает на вход параметры схожего по наименованию товара и возвращает
    измененный объект класса Product"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180010.0,
            "quantity": 5,
        },
        first_category.products_list,
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180010.0
    assert new_product.quantity == 10


def test_product_price_setter_invalid(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если новая цена равна или ниже нуля"""
    product.price = -800
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert f"Цена не была изменена, она осталась {product.price}" in captured.out
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert f"Цена не была изменена, она осталась {product.price}"


def test_product_price_setter_yes(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если цена товара понижается при
    согласии понизить цену"""
    new_price = 800
    with patch("builtins.input", side_effect=["Y"]):
        product.price = new_price
        captured = capsys.readouterr()
        assert "Вы действительно хотите изменить цену на меньшую? (y/n)" in captured.out
        assert f"Цена изменена на {new_price}" in captured.out
        assert product.price == 800


def test_product_price_setter_no(capsys: CaptureFixture[str], product: Product) -> None:
    """Тестируем поведение сеттера для приватного атрибута price в случае если цена товара понижается при
    несогласии понизить цену"""
    new_price = 800
    with patch("builtins.input", side_effect=["N"]):
        product.price = new_price
        captured = capsys.readouterr()
        assert "Вы действительно хотите изменить цену на меньшую? (y/n)" in captured.out
        assert f"Цена не была изменена, она осталась {product.price}" in captured.out
        assert product.price == 180000.0


def test_product_str(product: Product) -> None:
    """Тестируем строковое отображение продукта"""
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product: Product, other_product: Product) -> None:
    """Тестируем метод получения полной стоимости всех выбранных товаров на складе"""
    assert product + other_product == 2580000
