"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture()
def item_from_csv():
    return Item.instantiate_from_csv()

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000.0
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.price == 20000

def test_instantiate_from_csv(item_from_csv):
    assert len(Item.all) == 5