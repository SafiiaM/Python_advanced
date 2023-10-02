"""
Задание 2

Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. У класса должно быть два
метода, возвращающие периметр и площадь. Если при создании экземпляра передаётся только одна сторона, считаем что у нас
квадрат.
"""


class Rectangle:
    def __init__(self, length: int, width: int = None):
        self.length = length
        self.width = width if width is not None else length

    def square(self) -> int:
        return self.width * self.length

    def perimeter(self) -> int:
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    rect1 = Rectangle(5, 8)
    rect2 = Rectangle(5)

    print(f"{rect1.square()=}, {rect1.perimeter() =} ")
    print(f"{rect2.square()=}, {rect2.perimeter() =} ")
