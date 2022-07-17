from abc import ABC, abstractmethod
import random

class Person(ABC):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home

    def print_info_person(self):
        print(f"Some person: {self.name, self.age, self.availability_of_money, self.having_your_own_home}")

    @abstractmethod
    def make_money(self):
        raise NotImplementedError("Method is not implemented")
    @abstractmethod
    def buy_a_house(self):
        raise NotImplementedError("Method is not implemented")

class New_Person(Person):
    def __init__(self, name, age, availability_of_money, having_your_own_home, place_of_work, ability_of_buy_a_house):
        super().__init__(name, age, availability_of_money, having_your_own_home)
        self.ability_of_buy_a_house = ability_of_buy_a_house
        self.place_of_work = place_of_work

    def make_money(self):
        return print(f' {self.name} has a job. {self.name} works as -> {self.place_of_work}\n')

    def buy_a_house(self):
        return self.ability_of_buy_a_house

    def print_deatail_info_person(self):
        print(f" Some info about person: {self.name}\n age: {self.age}\n availability_of_money: {self.availability_of_money}\n having_your_own_home: {self.having_your_own_home}\n")

class House(ABC):

    def __init__(self, area, cost, age, type_of_buildings, address):
        self.address = address
        self.type_of_buildings = type_of_buildings
        self.area = area
        self.cost = cost
        self.age = age

    def info_about_house(self):
        return print(f'Area of buildings -> {self.area}, Price -> {self.cost} y.o., Type of Buildings -> {self.type_of_buildings}, Address -> {self.address}')

    @abstractmethod
    def detail_information(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def print_info_about_rooms(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def print_info_about_remonts(self):
        raise NotImplementedError("This method is not realized")

    def __repr__(self):
        return self.address


class NewHouse(House):

    def __init__(self, area, cost, age, type_of_buildings, address, remonts, rooms):
        super().__init__(area, cost, age, type_of_buildings, address)
        self.remonts = remonts
        self.rooms = rooms

    def detail_information(self):
        return f'Address -> {self.address}\nRooms -> {self.rooms}\nArea of buildings -> {self.area}\nPrice -> {self.cost} y.o.\nType of Buildings -> {self.type_of_buildings}\nRemonts -> {self.remonts}'

    def print_info_about_rooms(self):
        print(f'This house has {self.rooms} rooms')
        pass

    def print_info_about_remonts(self):
        if self.remonts == True:
            print("This building has remont")
        else:
            print("This building hasn't remont")


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses, persons):
        self.persons = persons
        self.name = name
        self.houses = houses

    def who_can_reach_a_discount(self):
        print("List of all person who can reach a discount and can not! List below  \n-----------------------")
        for i in range(len(self.persons)):
            discount = self.houses[0].cost * 0.1
            if self.persons[i].having_your_own_home == False:
                print(f'{self.persons[i].name}, Your discount is -> {discount} and you should pay -> {self.houses[i].cost - discount}')
            else:
                print(f'{self.persons[i].name}, sorry! You do not have a discount because you have your own house!\nIt is a business :(\nYou should pay -> {self.houses[i].cost}')


    def give_info_about_houses(self):
        print(f'There are all buildings _> {self.houses}')

    def detail_information_about_all_houses(self):
        for i in range(len(self.houses)):
            print('-------------------------\n',"House", i+1)
            print(self.houses[i].detail_information())
        print('-------------------------------')

    # steal money with chance 10%
    def steal_money(self):
        list1 = [1,2,3,4,5,6,7,8,9,10]
        if random.choice(list1) == 1:
            for i in range(len(self.persons)):
                print(f'Yeeessss, {self.persons[i].name} i have stolen yuor deposit and moved another place')
        else:
            pass



person1 = New_Person('George', 23, True, True, "waiter", True)
person1.print_deatail_info_person()
person1.make_money()

person2 = New_Person('Anjelina', 24, True, False, "actress", True)
person2.print_deatail_info_person()
person2.make_money()


house1 = NewHouse(40, 1000000, 15, "tsegla", "address1", True, 2)
house2 = NewHouse(50, 1100000, 13, "blocks", "address2", False, 3)
house3 = NewHouse(60, 1200000, 12, "blocks", "address3", False, 2)
house4 = NewHouse(70, 1300000, 16, "tsegla", "address4", True, 4)

house4.print_info_about_remonts()
house4.info_about_house()
house4.print_info_about_rooms()

newRealtor = Realtor("yura", [house1, house2, house3, house4], [person1, person2])
newRealtor.give_info_about_houses()
newRealtor.detail_information_about_all_houses()
newRealtor.who_can_reach_a_discount()
newRealtor.steal_money()


