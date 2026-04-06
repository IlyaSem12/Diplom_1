import pytest
from config import *
from helpers import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.test_burger
class TestDataBase:
    @pytest.mark.parametrize(
    "index, expected_name",
    [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun"),
    ]
    )
    def test_database_success_available_buns_return_name(self, db, index, expected_name):
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize(
        "index, expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
        ]
    )
    def test_database_success_available_buns_return_price(self, db, index, expected_price):
        bun = db.available_buns()[index]
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type",
        [
            (0, INGREDIENT_TYPE_SAUCE),
            (1, INGREDIENT_TYPE_SAUCE),
            (2, INGREDIENT_TYPE_SAUCE),
            (3, INGREDIENT_TYPE_FILLING),
            (4, INGREDIENT_TYPE_FILLING),
            (5, INGREDIENT_TYPE_FILLING),
        ]
    )
    def test_database_success_available_ingredients_return_type(self, db, index, expected_type):
        ingredient = db.available_ingredients()[index]
        assert ingredient.get_type() == expected_type


    @pytest.mark.parametrize(
        "index, expected_name",
        [
            (0, "hot sauce"),
            (1, "sour cream"),
            (2, "chili sauce"),
            (3, "cutlet"),
            (4, "dinosaur"),
            (5, "sausage"),
        ]
    )
    def test_database_success_available_ingredients_return_name(self, db, index, expected_name):
        ingredient = db.available_ingredients()[index]
        assert ingredient.get_name() == expected_name


    @pytest.mark.parametrize(
        "index, expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
            (3, 100),
            (4, 200),
            (5, 300),
        ]
    )
    def test_database_success_available_ingredients_return_price(self, db, index, expected_price):
        ingredient = db.available_ingredients()[index]
        assert ingredient.get_price() == expected_price