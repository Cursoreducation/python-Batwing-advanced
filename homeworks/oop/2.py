class Person:
    def __init__(self):
        right_hand = Arm('empty')
        left_hand = Arm('phone')
        self.right_hand = right_hand.type
        self.left_hand = left_hand.type

    def information(self):
        print(f'I have {self.right_hand} right hand and in my left hand I have {self.left_hand}.')


class Arm:
    def __init__(self, type):
        self.type = type


person = Person()
person.information()


# 2b
class CellPhone:
    def __init__(self, screen):
        self.screen = screen

    def info(self):
        print(f'My phone has {self.screen} screen.')


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


phone_screen = Screen('OLED')
phone = CellPhone(phone_screen.screen_type)
phone.info()
