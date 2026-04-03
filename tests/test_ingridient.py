#./tests/test_ingridient.py
import pytest
from config import *
from helpers import *
from praktikum.bun import Bun


@pytest.mark.test_ingredient
class TestIngridient:

    def test_ingridient_success_get_name_return_correct_name(self, create_ingridient):
        '''Тест проверяет возвращает ли класс "Ingredient" корректное имя ингредиента'''
        ingridient = create_ingridient
        received_name = ingridient.get_name()
        assert received_name == INGRIDIENT_NAME, f'Получили не верное имя; Ожидалось: {INGRIDIENT_NAME}; Получили: {received_name}'
    
    def test_ingridient_success_get_price_return_correct_price(self, create_ingridient):
        '''Тест проверяет возвращает ли класс "Ingredient" корректную цену ингредиента'''
        ingridient = create_ingridient
        received_price = ingridient.get_price()
        assert received_price == INGRIDIENT_PRICE, f'Получили не верную цену; Ожидалось: {INGRIDIENT_PRICE}; Получили: {received_price}'

    def test_ingridient_success_get_type_return_correct_type(self, create_ingridient):
        '''Тест проверяет возвращает ли класс "Ingredient" корректный тип ингредиента'''
        ingridient = create_ingridient
        received_price = ingridient.get_type()
        assert received_price == INGRIDIENT_TYPE, f'Получили не верную цену; Ожидалось: {INGRIDIENT_TYPE}; Получили: {received_price}'

    def test_ingridient_success_get_name_return_type_str(self, create_ingridient):
        """Тест проверяет, что get_name() возвращает строку"""
        ingridient = create_ingridient
        received_name = ingridient.get_name()
        assert isinstance(received_name, str), f"Ожидался тип str, получили {type(received_name)}"

    def test_ingridient_success_get_price_return_type_float(self, create_ingridient):
        """Тест проверяет, что get_price() возвращает число"""
        ingridient = create_ingridient
        received_price = ingridient.get_price()
        assert isinstance(received_price, (int, float)), f"Ожидался тип float или int, получили {type(received_price)}"

    def test_ingridient_success_get_type_return_type_str(self, create_ingridient):
        """Тест проверяет, что get_type() возвращает строку"""
        ingridient = create_ingridient
        received_type = ingridient.get_type()
        assert isinstance(received_type, str), f"Ожидался тип str, получили {type(received_type)}"