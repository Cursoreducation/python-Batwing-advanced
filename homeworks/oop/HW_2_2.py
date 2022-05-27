#  2.a.
class Person:
    def __init__(self):
        arm_one = Arm('Left arm')
        arm_two = Arm('Right arm')
        self.muscles = [arm_one.muscles, arm_two.muscles]


class Arm:
    def __init__(self, muscles):
        self.muscles = muscles


person = Person()
print(person.muscles)


#  2.b.
class Cellphone:
    def __init__(self, pixels):
        self.pixels = pixels

    def get_pixels(self):
        print(f"Amount of pixels of this phone is {self.pixels}")


class Screen:
    def __init__(self, pixels_number):
        self.pixels_number = pixels_number


screen_1 = Screen("23")
screen_2 = Screen("256")
Oppo = Cellphone(screen_1.pixels_number)
Reno = Cellphone(screen_2.pixels_number)
Oppo.get_pixels()
Reno.get_pixels()
