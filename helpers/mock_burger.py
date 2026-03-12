from unittest.mock import MagicMock
from praktikum.burger import Burger


class MockBurger(Burger):
    def __init__(self):
        """
        Собираем объект для чека с параметрами, см. constants.Receipt.RRECEIPT.
        Устанавливаем моки в атрибуты так, чтобы при обращении к ним 
        через методы возвращалось заданное значение.
        """
        super().__init__()
        mock_bun = MagicMock()
        mock_bun.get_name.return_value = "Мок булочка"
        mock_bun.get_price.return_value = 100
        self.bun = mock_bun
        mock_ingredient1 = MagicMock()
        mock_ingredient1.get_name.return_value = "Чесночный"
        mock_ingredient1.get_type.return_value = "соус"
        mock_ingredient1.get_price.return_value = 30
        mock_ingredient2 = MagicMock()
        mock_ingredient2.get_name.return_value = "Провансаль"
        mock_ingredient2.get_type.return_value = "майонез"
        mock_ingredient2.get_price.return_value = 35
        self.ingredients = [mock_ingredient1, mock_ingredient2]
        mock_price = MagicMock()
        mock_price.return_value = 165
        self.price = mock_price
