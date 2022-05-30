from abc import abstractmethod, ABC


class LaptopInterface(ABC):
    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HP_Laptop(LaptopInterface):
    def __init__(self, screen_size, keyboard_brand, touchpad_type, webcam_type, ports_type, dynamics_volume):
        self.screen_size = screen_size
        self.keyboard_brand = keyboard_brand
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.ports_type = ports_type
        self.dynamics_volume = dynamics_volume

    def screen(self):
        print(f"The size of the screen is {self.screen_size}")

    def keyboard(self):
        print(f"Keyboard brand is {self.keyboard_brand}")

    def touchpad(self):
        print(f"Touchpad type is {self.touchpad_type} ")

    def webcam(self):
        print(f"Webcam type is {self.webcam_type}")

    def ports(self):
        print(f"Ports type are {self.ports_type}")

    def dynamics(self):
        print(f"Dynamics volume: {self.dynamics_volume}")


Laptop_1 = HP_Laptop("5686x4556", "toshiba", "laser", "monochromatic", "usb 5.1", "450 dcb")
Laptop_1.ports()
Laptop_1.webcam()
