from abc import abstractclassmethod, ABC
# =================== 1 =============================
class Animal:

    def __init__(self, name, typeOfEat, hoursOfsleep):
        self.name = name
        self.typeOfEat = typeOfEat
        self.hoursOfsleep = hoursOfsleep
    def get_name_of_Animal(self):
        print(self.name)
    def eat(self):
        print("Type of food -> ", self.typeOfEat)
    def sleep(self):
        print("Amount hours of sleep -> ",self.hoursOfsleep)

class Dog(Animal):
    def __init__(self, name, typeOfEat, hoursOfsleep):
        super().__init__(name, typeOfEat, hoursOfsleep)
    def execution_of_the_command_voice(self):
        print('Gav-Gav')
    def execution_of_the_command_glory_Ukraine(self):
        print('Gav-Gav-Gav-Gav-Gav-Gav-Gav-Gav')

brovchik = Dog("Brovchik", "bones", "14")
brovchik.execution_of_the_command_voice()
brovchik.execution_of_the_command_glory_Ukraine()
brovchik.eat()
brovchik.sleep()
print(issubclass(Dog, Animal))
class Cat(Animal):
    def __init__(self, name, typeOfEat, hoursOfsleep):
        super().__init__(name, typeOfEat, hoursOfsleep)

    def voice_to_eat(self):
        print('Meeeaaaaav')
    def voice_to_go_out(self):
        print('Meeeaaaaav-Meeeaaaaav-Meeeaaaaav')

mrCat = Cat("MrCat", "fish", 15)
mrCat.voice_to_eat()
mrCat.voice_to_go_out()
mrCat.eat()
mrCat.sleep()
print(issubclass(Cat, Animal))

class Frog(Animal):
    def __init__(self, name, typeOfEat, hoursOfsleep):
        super().__init__(name, typeOfEat, hoursOfsleep)

    def voice_of_frog(self):
        print('kva-kva')
mrFrog = Frog("MrFrog", "insects", 7)
mrFrog.voice_of_frog()
mrFrog.eat()
mrFrog.sleep()
print(issubclass(Frog, Animal))

class Dinosaur(Animal):
    def __init__(self, name, typeOfEat, hoursOfsleep):
        super().__init__(name, typeOfEat, hoursOfsleep)

    def danger(self):
        print('hrhrhr')

    def extremely_danger(self):
        print('hrhrhr-hrhrhr-hrhrhr')

rex = Dinosaur("Rex", "human", 10)
rex.danger()
rex.extremely_danger()
rex.sleep()
rex.eat()
print(issubclass(Dinosaur, Animal))

class Duck(Animal):
    def __init__(self, name, typeOfEat, hoursOfsleep):
        super().__init__(name, typeOfEat, hoursOfsleep)

    def voice_of_duck(self):
        print('krya-krya')

msDuck = Duck("MsDuck", "bones", 9)
msDuck.voice_of_duck()
print(issubclass(Duck, Animal))

# ===================================================

# ========================================== 1a ============================================================

class Human():
    def __init__(self, last_name, age, passport_id, insurance_id ):
        self.last_name = last_name
        self.age = age
        self.passport_id = passport_id
        self.insurance_id = insurance_id

    def get_info_about_Human(self):
        print(f"last_name -> {self.last_name} \nage -> {self.age} years \npassport_id -> {self.passport_id} "
              f"\ninsurance_id -> {self.insurance_id}")

class Centaur(Animal, Human):
    def __init__(self, name, hoursOfsleep, typeOfEat, last_name, age, passport_id, insurance_id, country):
        Animal.__init__(self, name, hoursOfsleep, typeOfEat)
        Human.__init__(self, last_name, age, passport_id, insurance_id)
        self.coutry = country

    def get_all_nfo_about_Centaur(self):
        print(f"name -> {self.name}\nlast_name -> {self.last_name} \nage -> {self.age} years "
              f"\npassport_id -> {self.passport_id} \ninsurance_id -> {self.insurance_id} "
              f"\ncountry -> {self.coutry}")

mrCentaur = Centaur("Mr Centaur", "all food", 12, "Boss", 45, 123456789, 5589634427, "Palestyna")
mrCentaur.get_all_nfo_about_Centaur()
mrCentaur.get_name_of_Animal()
mrCentaur.get_info_about_Human()
mrCentaur.sleep()
mrCentaur.eat()
# ==========================================================================================================

# =========================================== 2 ============================================================
# ==================================== a(Composition) ======================================================
class Person:
    def __init__(self, name):
        self.name = name
        clock1 = Arm("8:32")
        clock2 = Arm("9:32")
        clock3 = Arm("10:32")
        clock4 = Arm("11:32")
        clock5 = Arm("12:32")
        self.clocks = [clock1.clock, clock2.clock, clock3.clock, clock4.clock, clock5.clock]

class Arm:
    def __init__(self, clock):
        self.clock = clock

arm = Person("Adolf")
print(f'{arm.name} has to wake up in {arm.clocks}')

# ==========================================================================================================
# ==================================== b(Aggregation) ======================================================
class CellPhone:
    def __init__(self, phone_number, screens):
        self.phone_number = phone_number
        self.screens = screens

class Screen:
    def __init__(self, listOfScreens):
        self.listOfScreens = listOfScreens

screen1 = Screen("Screen 1")
screen2 = Screen("Screen 2")
screen3 = Screen("Screen 3")
screen4 = Screen("Screen 4")
screen5 = Screen("Screen 5")
screens = [screen1.listOfScreens, screen2.listOfScreens, screen3.listOfScreens, screen4.listOfScreens, screen5.listOfScreens]
mrScreen = CellPhone(380630000000, screens )
print(f'Your phone number is -> {mrScreen.phone_number} and your cellphone has these screens -> {mrScreen.screens}')

# ==========================================================================================================
# =========================================== 3 ============================================================

class DictMixin:
    def to_dict(self):
        return self._traverse_to_dict(self.__dict__ )

    def _traverse_to_dict(self, attributes):
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_to_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_to_dict(value.__dict__ )
        else:
            return value

class Profile(DictMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


a = Profile("yura", "tsap", "0632727589", "lviv", "tsapyura1999@gmail.com", "20.04.1999", "23", "m")
print(a.to_dict())
# ==========================================================================================================
# =========================================== 4 ============================================================

class Laptop:
    @abstractclassmethod
    def Screen(self):
        raise NotImplementedError("This method was not implemented")

    @abstractclassmethod
    def Keyboard(self):
        raise NotImplementedError("This method was not implemented")

    @abstractclassmethod
    def Touchpad(self):
        raise NotImplementedError("This method was not implemented")

    @abstractclassmethod
    def WebCam(self):
        raise NotImplementedError("This method was not implemented")

    @abstractclassmethod
    def Ports(self):
        raise NotImplementedError("This method was not implemented")
    @abstractclassmethod
    def Dynamics(self):
        raise NotImplementedError("This method was not implemented")

class HPLaptop(Laptop):
    def __init__(self):
        self.modelOfScreen = ''
        self.backlight = ''
        self.enoughBig = ''
        self.megapixelsOfWebCam = ''
        self.emountOfPorts = ''
        self.enoughLoud = ''

    def Screen(self):
        self.modelOfScreen = input("Please enter how many inches is your screen:")
        return self.modelOfScreen

    def Keyboard(self):
        self.backlight = input("Please enter with or without backlight:")
        return self.backlight

    def Touchpad(self):
        self.enoughBig = input("Please enter is big enough:")
        return self.enoughBig

    def WebCam(self):
        self.megapixelsOfWebCam = input("Please enter how many megapixels your webcam has:")
        return self.megapixelsOfWebCam

    def Ports(self):
        self.emountOfPorts = input("Please enter how many ports are there:")
        return self.emountOfPorts

    def Dynamics(self):
        self.enoughLoud = input("Please enter the speakers are loud enough:")
        return self.enoughLoud

    def info_about_LapTop(self):
        self.Screen()
        self.Keyboard()
        self.Touchpad()
        self.WebCam()
        self.Ports()
        self.Dynamics()
        print(f'Model of laptop screen -> {self.modelOfScreen}, Backlight -> {self.backlight},'
              f' Is enouht big touchpad -> {self.enoughBig}, WebCam -> {self.megapixelsOfWebCam},'
              f' Emount of ports -> {self.emountOfPorts}, Speakers -> {self.enoughLoud}')

comp = HPLaptop()
comp.info_about_LapTop()
# ==========================================================================================================
