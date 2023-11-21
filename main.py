from abc import abstractmethod, ABCMeta
import math
class Color:
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self):
        return self.value

class Figure(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> float:
        pass
class Circle(Figure):
    def __init__(self, radius: float, color: Color):
        self._name = "Круг"
        self._radius = radius
        self._color = color

    def get_area(self) -> float:
        return self._radius * math.pi

    def __repr__(self):
        return "{}: радиус: {}, цвет: {}".format(self._name, self._radius, self._color)


class Rectangle(Figure):
    def __init__(self, width: float, height: float, color: Color):
        self._name = "Прямоугольник"
        self.width = width
        self.height = height
        self.color = color

    def get_area(self) -> float:
        return self.height * self.width

    def __repr__(self):
        return "{}: ширина: {}, высота: {}, цвет: {}".format(self._name, self.width, self.height, self.color)

class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
        self._name = "Квадрат"

    def __repr__(self):
        return "{}: сторона: {}, цвет: {}".format(self._name, self.width, self.color)

def main():
    print(Rectangle(15, 10, Color("синий")))
    print(Circle(15, Color("зеленый")))
    print(Square(15, Color("красный")))

if __name__ == "__main__":
    main()