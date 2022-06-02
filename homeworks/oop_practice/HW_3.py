from abc import ABC, abstractmethod
import random


class Person(ABC):

    def __init__(self, name, age, availability_of_money, having_your_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home

    @abstractmethod
    def provide_info(self):
        pass

    @abstractmethod
    def make_money(self):
        pass

    @abstractmethod
    def buy_house(self):
        pass


class Human(Person):
    def __init__(self, name, age, availability_of_money, having_your_own_home, money):
        super().__init__(name, age, availability_of_money, having_your_own_home)
        self.money = money

    def provide_info(self):
        print(f"Hello my name is {self.name} I am {self.age} years old")

    def make_money(self):
        self.money = random.randint(300, 900)
        if int(self.availability_of_money) <= 200:
            print(f"I'm running out of money will go to work because I want to make {self.money} dollars per month")
        else:
            print(f"I have enough money, I don't need to make money ")

    def buy_house(self):
        if self.having_your_own_home:
            print(f'Hello my name is {self.name}, and I have own house')
        else:
            print(f"I'm homeless, I will buy a house for myself")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def house_info(self):
        print(
            f"This house has  has {self.area}"
            f"square meters and it cost {self.cost} euro")


class Home(House):
    def __init__(self, area, cost, address, rooms, discount):
        super().__init__(area, cost)
        self.address = address
        self.rooms = rooms
        self.discount = discount

    def get_discount(self):
        if int(self.area) <= 40:
            self.cost = self.cost - (self.cost * self.discount)/100
            print(f"As this is a very small house {self.area} square meters, we will drop price "
                  f"with {self.discount} %, so you will pay {self.cost}")
        else:
            print(f'Sorry.This house doesnt have any discount')


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info_about_houses(self, ):
        for house in self.houses:
            house.house_info()

    def give_discount(self):
        if self.discount:
            print(f"I can give you discount ")
        else:
            print(f"No discount for you")

    def steal_money(self, person):
        if random.randint(0, 10) == 0:
            print(f'Hello I"m {self.name} and Im stealing your money !!!')
            person.availability_of_money = 0

        else:
            print(f"I won't steal you money")


taras = Human("Jon", 34, 4555, 5560, True)
taras.provide_info()
taras.make_money()
taras.buy_house()

beach_house = Home(20, 3000, "Miami", 45, 20)
forest_house = Home(20, 100000, "Wood Street", 45, 50)
beach_house.get_discount()
forest_house.get_discount()

frank = Realtor("Frank", [beach_house, forest_house], True)

frank.steal_money(taras)
frank.provide_info_about_houses()
frank.give_discount()
