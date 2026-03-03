from constants import *
from praktikum.burger import Burger
from unittest.mock import MagicMock
from unittest.mock import patch


class TestBurger:
    def test_set_buns(self, burger):
        mock_bun = MagicMock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingridient = MagicMock()
        burger.add_ingredient(mock_ingridient)

        assert mock_ingridient in burger.ingredients

    def test_add_other_ingridient(self, my_burger):
        mock_ingridient = MagicMock()
        count = len(my_burger.ingredients)
        my_burger.add_ingredient(mock_ingridient)
        total_count = len(my_burger.ingredients)

        assert mock_ingridient in my_burger.ingredients
        assert total_count == count + 1

    def test_remove_ingredient(self, my_burger):
        count = len(my_burger.ingredients)
        my_burger.remove_ingredient(count - 1)
        total_count = len(my_burger.ingredients)

        assert total_count == count - 1

    def test_move_ingredient(self, my_burger):
        element = my_burger.ingredients[-1]
        element_index = len(my_burger.ingredients) - 1
        new_index = 0
        my_burger.move_ingredient(element_index, new_index)
        element_index = my_burger.ingredients.index(element)

        assert element_index == new_index

    def test_get_price(self, burger):
        '''
        Мокаем вызовы цены булочки и цен ингридиентов, устанавливаем их как атрибуты,
        запускаем метод, проверяем, что цена посчиталась правильно.
        В бургере булочка за 120 и 2 ингредиента 50 и 25. Итого 315.
        '''
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 120
        burger.bun = mock_bun
        mock_ingredient1 = MagicMock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = MagicMock()
        mock_ingredient2.get_price.return_value = 25
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        price = burger.get_price()
        assert price == 315

    def test_get_receipt(self, mock_burger):
        """
        Объект собирается в helpers.mock_burger. На методы внутри проверяемого метода 
        устанавливются моки с заданными значениями.
        """

        receipt = mock_burger.get_receipt()

        assert receipt == Receipt.RECEIPT
