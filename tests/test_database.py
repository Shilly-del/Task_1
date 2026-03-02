import pytest
from unittest.mock import patch
from praktikum.database import Database
from constants import AvailableBuns, AvailableIngredients


class TestDatabaseBun:

    expected_buns = [AvailableBuns.BLACK,
                     AvailableBuns.WHITE, AvailableBuns.RED]

    @pytest.mark.parametrize('expected_bun', expected_buns)
    def test_available_buns(self, mock_database_bun, expected_bun):

        buns = mock_database_bun.available_buns()

        assert any(bun.name == expected_bun['name'] and bun.price ==
                   expected_bun['price'] for bun in buns)

    expected_ingredients = [AvailableIngredients.HOT_SAUCE, AvailableIngredients.SOUR_CREAM,
                            AvailableIngredients.CHILLI_SAUCE, AvailableIngredients.CUTLET,
                            AvailableIngredients.DINOSAUR, AvailableIngredients.SAUSAGE]

    @pytest.mark.parametrize('expected_ingredient', expected_ingredients)
    def test_available_buns(self, mock_database_ingredient, expected_ingredient):

        ingredients = mock_database_ingredient.available_ingredients()

        assert any(ingredient.name == expected_ingredient['name'] and ingredient.type == expected_ingredient['type'] and ingredient.price ==
                   expected_ingredient['price'] for ingredient in ingredients)
