import uuid
import random


def generate_name_bun():
    '''Функция генерации имени булочки'''
    return f"test_bun_{uuid.uuid4().hex[:8]}"

def generate_price_bun():
    '''Функция генерации цены булочки'''
    return round(random.uniform(1, 1000), 2)