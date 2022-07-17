
class Calculator:
    """ A simple calculator App"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        """Add Function"""
        return self.x + self.y

    def subtract(self):
        """Subtract Function"""
        return self.x - self.y

    def multiply(self):
        """Multiply Function"""
        return self.x * self.y

    def divide(self):
        """Divide Function"""
        if self.y == 0:
            raise ValueError('Can not divide by zero!')
        return self.x / self.y
    def test_for_mock(self):
        a = self.multiply(self.x, self.y) + 10
        return a