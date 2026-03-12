from unittest.mock import MagicMock
from unittest.mock import patch
from praktikum.database import Database
from constants import AvailableBuns, AvailableIngredients


class MockDatabaseBun:
    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def __init__(self, mock_bun, mock_ingredient):
        """
        Собираем базу, мокаем создание элементов. Выставляем заглушкам 
        атрибуты, требуемые для работы метода и ассертов.
        """

        mock_black = MagicMock()
        mock_black.name = AvailableBuns.BLACK['name']
        mock_black.price = AvailableBuns.BLACK['price']
        mock_white = MagicMock()
        mock_white.name = AvailableBuns.WHITE['name']
        mock_white.price = AvailableBuns.WHITE['price']
        mock_red = MagicMock()
        mock_red.name = AvailableBuns.RED['name']
        mock_red.price = AvailableBuns.RED['price']
        mock_bun.side_effect = [mock_black, mock_white, mock_red]
        mock_ingredient.return_value = MagicMock()
        self.instance = Database()


class MockDatabaseIngredient:
    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def __init__(self, mock_bun, mock_ingredient):
        """
        Собираем базу, мокаем создание элементов. Выставляем заглушкам
        атрибуты, требуемые для работы метода.
        """
        mock_bun.return_value = MagicMock()
        mock_hot_sauce = MagicMock()
        mock_hot_sauce.name = AvailableIngredients.HOT_SAUCE['name']
        mock_hot_sauce.type = AvailableIngredients.HOT_SAUCE['type']
        mock_hot_sauce.price = AvailableIngredients.HOT_SAUCE['price']
        mock_sour_cream = MagicMock()
        mock_sour_cream.name = AvailableIngredients.SOUR_CREAM['name']
        mock_sour_cream.type = AvailableIngredients.SOUR_CREAM['type']
        mock_sour_cream.price = AvailableIngredients.SOUR_CREAM['price']
        mock_chilly_sauce = MagicMock()
        mock_chilly_sauce.name = AvailableIngredients.CHILLI_SAUCE['name']
        mock_chilly_sauce.type = AvailableIngredients.CHILLI_SAUCE['type']
        mock_chilly_sauce.price = AvailableIngredients.CHILLI_SAUCE['price']
        mock_cutlet = MagicMock()
        mock_cutlet.name = AvailableIngredients.CUTLET['name']
        mock_cutlet.type = AvailableIngredients.CUTLET['type']
        mock_cutlet.price = AvailableIngredients.CUTLET['price']
        mock_dinosaur = MagicMock()
        mock_dinosaur.name = AvailableIngredients.DINOSAUR['name']
        mock_dinosaur.type = AvailableIngredients.DINOSAUR['type']
        mock_dinosaur.price = AvailableIngredients.DINOSAUR['price']
        mock_sausage = MagicMock()
        mock_sausage.name = AvailableIngredients.SAUSAGE['name']
        mock_sausage.type = AvailableIngredients.SAUSAGE['type']
        mock_sausage.price = AvailableIngredients.SAUSAGE['price']
        mock_ingredient.side_effect = [mock_hot_sauce, mock_sour_cream,
                                       mock_chilly_sauce, mock_cutlet, mock_dinosaur, mock_sausage]

        self.instance = Database()
