from statistics import mean

class Coffee:
    def __init__(self, name):
        self._name = None  # Initialize _name attribute
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name is None:
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
            else:
                raise ValueError("Name must be a string with at least 3 characters.")
        else:
            raise AttributeError("Name is immutable and cannot be changed.")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return mean([order.price for order in self.orders()])


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string with 1 to 15 characters.")

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Argument must be a Coffee instance.")
        coffee_all_orders = [order for order in Order.all if order.coffee is coffee]
        if coffee_all_orders:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be a Customer instance.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be a Coffee instance.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not hasattr(self, '_price'):  # Ensure price can only be set once
            if isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
                self._price = price
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0.")
        else:
            raise AttributeError("Price can only be set once.")
