# Разработайте программное обеспечение для ведения журнала событий. Вам необходим класс, который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.
# Создайте класс MyStr, который наследуется от встроенного класса str. Этот класс будет представлять строки с информацией о событиях.
# Класс MyStr должен иметь следующие атрибуты:
# value (str): Строковое значение с описанием события.
# author (str): Имя автора, создавшего запись.
# time (float): Время создания записи в формате '%Y-%m-%d %H:%M'.
# Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author. Метод также автоматически фиксирует время создания записи.
# Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr с информацией о событии, авторе и времени создания.
# Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr для отладки.
# Пример использования.
# На входе:
# event = MyStr("Завершилось тестирование", "John")
# print(event)
# На выходе:
# Завершилось тестирование (Автор: John, Время создания: [время в секундах])



import time

class MyStr(str):

    def __new__(cls, value: str, author: str ):

        instance = super(MyStr, cls).__new__(cls, value )
        instance.author = author
        instance.time = time.strftime('%Y-%m-%d %H:%M')
        return instance


    def __str__(self):
     return  f'{super().__str__()} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f'MyStr("{self}", "{self.author}")'


# Пример использования
event = MyStr("Завершилось тестирование", "John")
print(event)

"""
Разработайте программу для хранения и управления текстовыми и числовыми записями.
Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:
Класс Archive должен иметь следующие атрибуты:
archive_text (list): Список архивированных текстовых записей.
archive_number (list): Список архивированных числовых записей.
text (str): Текущая текстовая запись, которую нужно добавить в архив.
number (int или float): Текущая числовая запись, которую нужно добавить в архив.
Класс Archive должен реализовать шаблон Singleton, чтобы гарантировать, что существует только один экземпляр архива.
Класс Archive должен иметь метод __init__(self, text: str, number: int | float), который принимает текстовую и числовую запись и сохраняет их как текущие записи для добавления в архив.
Класс Archive должен реализовать методы
__str__(self) и __repr__(self), чтобы можно было получить строковое представление текущих записей и архива.
Пример
На входе:
archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)

На выходе:
Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]

"""

class Archive:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls, text: str, number: int | float):
        # Проверяем, существует ли уже экземпляр, и возвращаем его, если да
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        # Добавляем текущие записи в архив
        cls._instance.archive_text.append(text)
        cls._instance.archive_number.append(number)
        return cls._instance

    def __init__(self, text: str, number: int | float):
        self.text = text
        self.number = number

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"


# Пример использования
archive1 = Archive("Запись 1", 42)
print(archive1)

archive2 = Archive("Запись 2", 3.14)
print(archive2)

#Ожидаемый ответ:

# ['First Text', 'Second Text']
# [1, 2]
# ['First Text', 'Second Text']
# [1, 2]

# Text is First Text and number is 1. Also [] and []
# Text is Second Text and number is 2. Also ['First Text'] and [1]
# Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]
# Text is Third Text and number is 3. Also ['First Text', 'Second Text'] and [1, 2]


Text is First Text and number is 1. Also ['First Text'] and [1]
Text is Second Text and number is 2. Also ['First Text', 'Second Text'] and [1, 2]
Text is Third Text and number is 3. Also ['First Text', 'Second Text', 'Third Text'] and [1, 2, 3]
Text is Third Text and number is 3. Also ['First Text', 'Second Text', 'Third Text'] and [1, 2, 3]
['First Text', 'Second Text', 'Third Text']
[1, 2, 3]
['First Text', 'Second Text', 'Third Text']
[1, 2, 3]


"""
Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
Класс Rectangle должен иметь следующие атрибуты и методы:
Атрибуты:
width (int): ширина прямоугольника.
height (int): высота прямоугольника.
Методы:
perimeter(): метод для вычисления периметра прямоугольника. Возвращает периметр как целое число.
area(): метод для вычисления площади
прямоугольника. Возвращает площадь как целое число. __add__(other): метод, позволяющий складывать два прямоугольника. Возвращает новый прямоугольник с шириной и высотой, равными сумме соответствующих атрибутов исходных прямоугольников.
__sub__(other): метод, позволяющий вычитать один прямоугольник из другого. Возвращает новый прямоугольник с шириной и высотой, равными разности соответствующих атрибутов исходных прямоугольников.
__lt__(other): метод, определяющий, является ли текущий прямоугольник меньше по площади, чем другой прямоугольник. Возвращает True, если площадь текущего прямоугольника меньше площади другого, и False в противном случае.
__eq__(other): метод, определяющий, равны ли два прямоугольника по площади. Возвращает True, если площади равны, и False в противном случае.
__le__(other): метод, определяющий, меньше или равен текущий прямоугольник по площади, чем другой прямоугольник. Возвращает True, если площадь текущего прямоугольника меньше или равна площади другого, и False в противном случае.
__str__(): метод для получения строкового представления прямоугольника. Возвращает строку с информацией о ширине и высоте прямоугольника.
__repr__(): метод для получения строкового представления прямоугольника, которое может быть использовано для создания нового объекта.
Пример использования:
На входе:
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")  
print(f"Площадь rect2: {rect2.area()}")    
print(f"rect1 < rect2: {rect1 < rect2}")        
print(f"rect1 == rect2: {rect1 == rect2}")   
print(f"rect1 <= rect2: {rect1 <= rect2}")     

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}") 
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")          
На выходе:
Периметр rect1: 30
Площадь rect2: 21
rect1 < rect2: False
rect1 == rect2: False
rect1 <= rect2: False
Периметр rect3: 50.0
Ширина rect4: 2

"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        else:
            raise ValueError("Can only add two Rectangle objects.")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(abs(self.width - other.width), abs(self.height - other.height))
        else:
            raise ValueError("Can only subtract two Rectangle objects.")

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise ValueError("Can only compare two Rectangle objects.")

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise ValueError("Can only compare two Rectangle objects.")

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        else:
            raise ValueError("Can only compare two Rectangle objects.")

    def __str__(self):
        return f"Rectangle (Width: {self.width}, Height: {self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


# Пример использования
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")


"""
Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:
Инициализация матрицы. Конструктор класса должен принимать количество строк rows и количество столбцов cols и создавать матрицу с нулевыми значениями.
Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.
Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными размерами (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).
Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.
Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы, где элементы строки разделены пробелами, а строки сами разделены символами новой строки.
Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__, который возвращает строку, которую можно использовать для создания нового объекта класса Matrix.

"""


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"

        return result.strip()

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"


# Пример использования
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

matrix3 = matrix1 + matrix2
print("matrix3 (Addition):")
print(matrix3)

matrix4 = matrix1 * matrix2
print("\nmatrix4 (Multiplication):")
print(matrix4)

matrix5 = Matrix(2, 2)
matrix5.data = [[1, 2], [3, 4]]

print("\nmatrix1 == matrix5:", matrix1 == matrix5)