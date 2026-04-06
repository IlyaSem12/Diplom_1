import pytest
from unittest.mock import Mock
from config import *
from helpers import *


@pytest.mark.test_burger
class TestBurger:

    def test_burger_success_set_buns_sets_bun_correctly(self, burger, bun_mock):
        '''Тест проверяет корректно ли класс "Burger" добавляет булочку'''
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock , f'Получили не верное значение; Ожидалось: {bun_mock}; Получили: {burger.bun}'
    
    def test_burger_success_add_ingredient_adds_ingredient_to_list(self, burger, ingredient_mock):
        '''Тест проверяет корректно ли класс "Burger" добавляет ингридиенты'''
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[-1] == ingredient_mock, f'Получили не верное значение; Ожидалось: {ingredient_mock}; Получили: {burger.ingredients[-1]}'

    def test_burger_success_ingredient_removes_ingredient_by_index(self, burger, ingredient_mock):
        '''Тест проверяет корректно ли класс "Burger" удаляет ингридиенты'''
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients, "Добавленный ингредиент всё еще в списке"
    
    def test_burger_success_move_ingredient_moves_ingredient_to_new_position(self, burger):
        '''Тест проверяет корректно ли класс "Burger" изменяет индекс ингридиентов'''
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        expected_order = [ingredient2, ingredient3, ingredient1]
        assert burger.ingredients == expected_order, f'Ожидался порядок {expected_order}, но получили {burger.ingredients}'

    def test_burger_success_get_price_returns_correct_total_price(self, burger, bun_mock, ingredient_mock):
        '''Тест проверяет корректно ли класс "Burger" расчитывает цену бургера'''
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        actual_price = burger.get_price()
        expected_price = ingredient_mock.get_price() + bun_mock.get_price() * 2
        assert actual_price == expected_price, f"Ожидалось {expected_price}, но получили {actual_price}"

    def test_burger_success_get_price_returns_correct_type_float(self, burger, bun_mock, ingredient_mock):
        '''Тест проверяет, что get_price() класса "Burger" возвращает тип число'''
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        actual_price = burger.get_price()
        assert isinstance(actual_price, float), f"Ожидался тип float, получили {type(actual_price)}"

    def test_burger_success_get_receipt_returns_correct_receipt(self, burger, bun_mock,ingredient_mock):
        '''Тест проверяет корректно ли класс "Burger" возвращает рецепт бургера'''
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        actual_receipt = burger.get_receipt()
        expected_receipt = RECEPT_BURGER 
        assert actual_receipt == expected_receipt

    def test_burger_success_get_receipt_returns_correct_type_float(self, burger, bun_mock,ingredient_mock):
        '''Тест проверяет, что get_receipt() класса "Burger" возвращает тип строка'''
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock,)
        actual_receipt = burger.get_receipt()
        assert isinstance(actual_receipt, str), f"Ожидался тип str, получили {type(actual_receipt)}"



