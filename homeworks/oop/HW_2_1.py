import random
from abc import ABC


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def description(self):
        print(f"Here is animal {self.name}, {self.age} years old")


class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def dog_sound(self):
        print(f"The {self.age} years old dog {self.name} is eating {self.food}  and saying Wof!")


class Cow(Animal):
    def __init__(self, name, age, color, leg_number):
        super().__init__(name, age)
        self.color = color
        self.leg_number = leg_number

    def cow_sound(self):
        print(f"{self.name} {self.color} cow -  making sound Moo! Moo! Moo!")

    def getLeg(self):
        if self.leg_number != 4:
            print(f"Holy Cow! A cow with {self.leg_number} legs!")
        else:
            print(f"This is normal {self.leg_number} leg cow")


class Bear(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def bear_sound(self):
        print(f" {self.color} bear is sleeping")

    def beer_color(self):
        print(f'Color of beer is {self.color}')


class Reindeer(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def reindeer_run(self):
        print(f" {self.size} reindeer {self.name}  is running through the forest")


Dog1 = Dog("Tomas", 24, "meat")
Dog1.description()
Dog1.dog_sound()
Dog1.eat()
Dog1.sleep()
print("Is Dog1 an Animal:", isinstance(Dog1, Animal))

Cow1 = Cow("Milka", 10, "brown", 4)
Cow1.cow_sound()
Cow1.description()
Cow1.getLeg()
Cow1.description()
print("Is Cow1 an Animal:", isinstance(Cow1, Animal))

Bear1 = Bear("Jack", 31, "Brown")
Bear1.description()
Bear1.eat()
Bear1.sleep()
print("Is Bear1 an Animal:", isinstance(Bear1, Animal))

Deer = Reindeer("Suzy", 32, "small")
Deer.description()
Deer.eat()
Deer.reindeer_run()
print("Is Bear1 an Animal:", isinstance(Deer, Animal))


class Human:
    def __init__(self, name, eat, study, work, sleep):
        self.name = name
        self.eat = eat
        self.study = study
        self.work = work
        self.sleep = sleep

    def human_description(self):
        print(f" Hello this I am {self.name}")

    def eating(self):
        print(f"{self.name} is eating {self.eat}")

    def sleeping(self):
        print(f"{self.name} is going to sleep")

    def studying(self):
        if self.sleep:
            print(f"I'm sleeping")
        else:
            print(f"{self.name} is studying {self.study}")


Boy = Human("John", "Meal", "dance", "jump", False)

Boy.studying()


class Centaur(Animal, Human):
    def __init__(self, name, age, eat, sleep, study, work, legs):
        Animal.__init__(self, name, age)
        Human.__init__(self, name, eat, study, work, sleep)
        self.legs = legs

    def run(self):
        if not self.sleep:
            print(f"{self.name} is sleeping")
        else:
            print(f"{self.name} centaur is running through the forest")

    def human_check(self):
        if self.legs != 2:
            print(f'This is {self.name}  he has {self.legs} legs and he is {self.age} years old and he is centaur who '
                  f'is {self.study}')
        else:
            print(f"OMG! {self.name} is human and it is eating {self.eat}")


centaur = Centaur("Flint", 23, "Meat", random.choice([True, False]), "dancing", "working as accountant",
                  random.randint(0, 4))
centaur.eating()
centaur.studying()
centaur.sleeping()
centaur.human_check()
centaur.description()
