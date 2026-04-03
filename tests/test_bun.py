#./tests/test_bun.py
import pytest
from config import *
from helpers import *


@pytest.mark.test_bun
class TestBun:

    def test_bun_get_name_success_return_correct_name(self, create_bun):
        '''Тест проверяет возвращает ли класс "Bun" корректное имя булочки'''
        bun = create_bun
        received_name = bun.get_name()
        assert received_name == NAME_BUN, f'Получили не верное имя; Ожидалось: {NAME_BUN}; Получили: {received_name}'
    
    def test_bun_get_price_success_return_correct_price(self, create_bun):
        '''Тест проверяет возвращает ли класс "Bun" корректную цену булочки'''
        bun = create_bun
        received_price = bun.get_price()
        assert received_price == PRICE_BUN, f'Получили не верную цену; Ожидалось: {PRICE_BUN}; Получили: {received_price}'

    def test_bun_success_get_name_return_type_str(self, create_bun):
        """Тест проверяет, что get_name() возвращает строку"""
        bun = create_bun
        received_name = bun.get_name()
        assert isinstance(received_name, str), f"Ожидался тип str, получили {type(received_name)}"

    def test_bun_success_get_price_return_type_float(self, create_bun):
        """Тест проверяет, что get_price() возвращает число"""
        bun = create_bun
        received_price = bun.get_price()
        assert isinstance(received_price, (int, float)), f"Ожидался тип float или int, получили {type(received_price)}"
