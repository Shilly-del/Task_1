import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from constants import *
from unittest.mock import MagicMock
from helpers.mock_burger import *
from helpers.mock_database import *


@pytest.fixture
def bun():  # булочка
    bun = Bun(MyBun.NAME, MyBun.PRICE)
    yield bun


@pytest.fixture
def burger():  # пустой бургер
    burger = Burger()
    yield burger


@pytest.fixture
def my_burger():  # бургер с ингридиентами
    burger = Burger()
    mock_ingredient_1 = MagicMock()
    mock_ingredient_2 = MagicMock()
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    yield burger


@pytest.fixture
def mock_burger():
    """
    передаем в тест собранный объект для чека с параметрами, 
    см. helpers.mocker и constants.Receipt.RECEIPT
    """
    burger = MockBurger()
    yield burger


@pytest.fixture
def ingredient():  # ингредиент. Чесночный соус по 15.
    ingredient = Ingredient(
        MyIngredient.TYPE, MyIngredient.NAME, MyIngredient.PRICE)
    yield ingredient


@pytest.fixture
def mock_database_bun(scope="class"):
    """
    передаем в тест собранную датабазу
    """
    database = MockDatabaseBun()
    mock = database.instance
    yield mock


@pytest.fixture
def mock_database_ingredient(scope="class"):
    """
    создаем датабазу, мокаем вызовы Bun.
    """
    database = MockDatabaseIngredient()
    mock = database.instance
    yield mock
