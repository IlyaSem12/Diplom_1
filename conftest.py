import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from config import *

@pytest.fixture
def create_bun():
    """Фикстура для создания объекта класса 'Bun'"""
    return Bun(NAME_BUN, PRICE_BUN)

@pytest.fixture
def create_ingridient():
    """Фикстура для создания объекта класса 'Ingredient'"""
    return Ingredient(INGRIDIENT_TYPE,INGRIDIENT_NAME,INGRIDIENT_PRICE)

@pytest.fixture
def burger():
    """Фикстура для создания объекта класса 'Burger'"""
    return Burger()

@pytest.fixture
def db():
    """Фикстура для создания объекта класса 'Database'"""
    return Database()

@pytest.fixture
def bun_mock():
    """Фикстура для создания мока 'Bun'"""
    bun = Mock()
    bun.get_name.return_value = NAME_BUN
    bun.get_price.return_value = PRICE_BUN
    return bun

@pytest.fixture
def ingredient_mock():
    """Фикстура для создания мока 'Ingredient'"""
    ingredient = Mock()
    ingredient.get_name.return_value = INGRIDIENT_NAME
    ingredient.get_price.return_value = INGRIDIENT_PRICE
    ingredient.get_type.return_value = INGRIDIENT_TYPE
    return ingredient


