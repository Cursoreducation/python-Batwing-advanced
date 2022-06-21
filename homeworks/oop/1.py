class Animals:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def info(self):
        print(f'It is {self.name}')

    def eating(self):
        print(f'It eats {self.eat}')

    def sleeping(self):
        print(f'It sleeps for {self.sleep} hours')


class Dog(Animals):
    def __init__(self, name, eat, sleep, sound):
        super().__init__(name, eat, sleep)
        self.sound = sound

    def make_sound(self):
        print(f'Dog say {self.sound}')


class Cat(Animals):
    def __init__(self, name, eat, sleep, sound):
        super().__init__(name, eat, sleep)
        self.sound = sound

    def make_sound(self):
        print(f'Cat say {self.sound}')


class Horse(Animals):
    def __init__(self, name, eat, sleep, jump):
        super().__init__(name, eat, sleep)
        self.jump = jump

    def jumping(self):
        print(f'Horse jumped {self.jump} meter')


class Seal(Animals):
    def __init__(self, name, eat, sleep, swim):
        super().__init__(name, eat, sleep)
        self.swim = swim

    def swimming(self):
        print(f'Seal swam {self.swim} meters')


dog = Dog("Dog", "dog food", 5, "bark")
cat = Cat("Cat", "fish", 6, "meow")
horse = Horse("Horse", "hay", 8, 1)
seal = Seal("Seal", "fish", 4, 5)

animals = (dog, cat, horse, seal)

for animal in animals:
    animal.info()
    animal.eating()
    animal.sleeping()
    print('-' * 12)

dog.make_sound()
cat.make_sound()
horse.jumping()
seal.swimming()
print('-' * 12)

for animal in animals:
    print(isinstance(animal, Animals))

print('-' * 12)


# 1a.
class Human:
    def __init__(self, eat, sleep, study, work):
        self.eat = eat
        self.sleep = sleep
        self.study = study
        self.work = work

    def eating(self):
        print(f'He want to eat {self.eat}')

    def sleep(self):
        print(f'He must sleep {self.sleep} hours')

    def studying(self):
        print(f'He is studying in {self.study}')

    def working(self):
        print(f'He should work {self.work} hours')


class Centaur(Human, Animals):
    def __init__(self, name, eat, sleep, study, work, weapon):
        Animals.__init__(self, name, eat, sleep)
        Human.__init__(self, eat, sleep, study, work)
        self.weapon = weapon

    def information(self):
        print(f'It is centaur {self.name}')

    def weapon_type(self):
        print(f'{self.name} has {self.weapon} as a weapon')


centaur = Centaur("Dave", "pizza", 8, "university", 5, "bow")

centaur.information()
centaur.eating()
centaur.sleeping()
centaur.studying()
centaur.working()
centaur.weapon_type()
