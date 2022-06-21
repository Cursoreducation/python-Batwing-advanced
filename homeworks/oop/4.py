from abc import abstractmethod, ABC


class Laptop:

    @abstractmethod
    def get_screen(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def get_keyboard(self):
        raise NotImplementedError('This method is not realized')

    @abstractmethod
    def get_touchpad(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_webcam(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_ports(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_dynamics(self):
        raise NotImplementedError('This method was not implemented')


class HPLaptop(Laptop, ABC):
    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

    def get_screen(self):
        print(f'This laptop has {self.screen} screen size')

    def get_keyboard(self):
        print(f'Keyboard language - {self.keyboard}')

    def get_touchpad(self):
        print(f'It {self.touchpad} touchpad')

    def get_webcam(self):
        print(f'Laptop {self.webcam} webcam')

    def get_ports(self):
        print(f'Also {self.ports} ports')

    def get_dynamics(self):
        print(f'And {self.dynamics} dynamics')


laptop = HPLaptop(18, "ukranian", "has", "has", 4, 2)
laptop.get_screen()
laptop.get_keyboard()
laptop.get_touchpad()
laptop.get_webcam()
laptop.get_ports()
laptop.get_dynamics()
