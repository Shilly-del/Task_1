from praktikum.bun import Bun
from constants import MyBun


class TestBun:
    def test_get_name(self, bun):
        name = bun.get_name()

        assert name == MyBun.NAME

    def test_get_price(self, bun):
        name = bun.get_price()

        assert name == MyBun.PRICE
