from praktikum.ingredient import Ingredient
from constants import MyIngredient


class TestIngridient:

    def test_get_name(self, ingredient):
        name = ingredient.get_name()

        assert name == MyIngredient.NAME

    def test_get_price(self, ingredient):
        name = ingredient.get_price()

        assert name == MyIngredient.PRICE

    def test_get_type(self, ingredient):
        name = ingredient.get_type()

        assert name == MyIngredient.TYPE
