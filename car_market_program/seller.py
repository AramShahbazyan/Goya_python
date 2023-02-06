from person import Person


class Seller(Person):
    sold_cars = {}
    money = 0
    car_park = {}

    # for i in range(100):
    #     car_park = {}

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)

    def sell(self):
        pass

    def return_car(self):
        pass

    def change_money(self):
        pass

    def get_available_cars(self):
        pass

    def check_discount(self):
        pass

    def add_sold_car(self):
        pass


