from car import Car
from seller import Seller


class CarMarket:

    @staticmethod
    def add_car(car: Car, seller: Seller):
        i = 1
        seller.car_park = {i: {'seller': seller,
                               'car': car}}
        i += 1

    def remove_car(self):
        pass

    def set_discount(self):
        pass

    def get_sold_car_history(self):
        pass

    def return_car(self):
        pass

    def get_seller_available_cars(self):
        pass

    def get_car_available_discount(self):
        pass


if __name__ == '__main__':
    seller_1 = Seller('poxos', 'petrosyan', 'yerevan')
    car_1 = Car('BMW', '528', '10000', '2007')
    x = CarMarket
    p = x.add_car(car_1, seller_1)
    print(p)
