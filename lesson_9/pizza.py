from abc import ABC, abstractmethod


class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self._ingredients = list(ingredients)
        self.base_prices = {"S": 10.0, "M": 15.0, "L": 20.0}

    @property
    def ingredients(self):
        return self._ingredients

    def add_ingredient(self, ingredient):
        if len(self._ingredients) < 10:
            self._ingredients.append(ingredient)
        else:
            print("Очень много начинки! Пицца не пропечется!")

    def calculate_price(self):
        price = self.base_prices.get(self.size, 10.0) + len(self._ingredients) * 1.0
        return float(price)


class MeatPizza(Pizza):
    def calculate_price(self):
        return round(super().calculate_price() * 1.2, 2)


class VeggiePizza(Pizza):
    def calculate_price(self):
        return round(super().calculate_price() * 0.9, 2)


class Order(ABC):
    @abstractmethod
    def prepare(self):
        pass


class PizzaOrder(Order):
    def __init__(self, pizza):
        self.pizza = pizza

    def prepare(self):
        price = self.pizza.calculate_price()
        ingredients_list = ", ".join(self.pizza.ingredients)

        if isinstance(self.pizza, MeatPizza):
            pizza_type = "Мясную"
        elif isinstance(self.pizza, VeggiePizza):
            pizza_type = "Овощную"
        else:
            pizza_type = "Обычную"

        print(f"Готовим {pizza_type} пиццу размера {self.pizza.size} ({ingredients_list}). Цена: {price}$")


class Pizzeria:
    def take_order(self, pizza_type, size, ingredients):
        if pizza_type.lower() == "meat":
            pizza = MeatPizza(size, ingredients)
        elif pizza_type.lower() == "veggie":
            pizza = VeggiePizza(size, ingredients)
        else:
            pizza = Pizza(size, ingredients)

        order = PizzaOrder(pizza)
        order.prepare()




my_pizzeria = Pizzeria()
my_pizzeria.take_order("meat", "L", ["бекон", "пепперони", "сыр"])
my_pizzeria.take_order("veggie", "S", ["сыр", "оливки"])
