"""
Задание 5

Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен
создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не
допускайте отрицательных значений."""


class Rectangle:
    """ We are finalizing the rectangle class from the last seminar. Add the ability to add and subtract. """
    def __init__(self, a: int, b: int = None):
        """
        initialize a and b
        :param a:   -- a number
        :param b:   -- b number
        """
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        """
        calculate the perimeter
        :return:    -- perimeter
        """
        return 2 * (self.a + self.b)

    def area(self):
        """
        calculate the area rectangle
        :return:    -- area
        """
        return self.a * self.b

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)


def run_rectangle():
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5, 10)
    print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    print(f'{rect_2.perimeter()= } {rect_2.area()= }')
    res_sum = rect_1 + rect_2
    print(res_sum.a, res_sum.b)
    res_sub = rect_1 - rect_2
    print(res_sub.a, res_sub.b)
    help(Rectangle)


if __name__ == '__main__':
    run_rectangle()
