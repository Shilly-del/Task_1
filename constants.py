class MyBun:
    NAME = "Моя булочка"
    PRICE = 50


class MyBurger:
    INGRIDIENTS = []


class Receipt:
    RECEIPT = """(==== Мок булочка ====)
= соус Чесночный =
= майонез Провансаль =
(==== Мок булочка ====)

Price: 265"""


class MyIngredient:
    NAME = 'Чесночный'
    PRICE = 15
    TYPE = "SAUCE"


class AvailableBuns:
    BLACK = {'name': "sweet bun", 'price': 100}
    WHITE = {'name': "sugar bun", 'price': 200}
    RED = {'name': "poppy seed bun", 'price': 300}


class AvailableIngredients:
    HOT_SAUCE = {'name': "hot sauce", 'type': 'SAUCE', 'price': 100}
    SOUR_CREAM = {'name': "sour cream", 'type': 'SAUCE', 'price': 200}
    CHILLI_SAUCE = {'name': "chili sauce", 'type': 'SAUCE', 'price': 300}
    CUTLET = {'name': "cutlet", 'type': 'FILLING', 'price': 100}
    DINOSAUR = {'name': "dinosaur", 'type': 'FILLING', 'price': 200}
    # что такое динозавр??!
    SAUSAGE = {'name': "sausage", 'type': 'FILLING', 'price': 300}
