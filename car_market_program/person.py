# We will have a Person superclass. 2 classes will inherit from Person: Buyer and Seller classes.
# Person will have a name, surname, and city attributes.

class Person:
    def __init__(self, name, surname, city):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(city, str):
            self.name = name
            self.surname = surname
            self.city = city

        else:
            raise ValueError('invalid value: please input true value')


# x = Person('suren', 'papikyan', 'yerevan')
#
# print(x.name)
