from FunctionsToMethods import run
from AnimalFabric import AnimalFabric
from Animals import Dog, Bird, Fish
from Circle import Circle
from Rectangle import Rectangle
from Employee import Employee
from Human import Human

if __name__ == '__main__':
    circle = Circle(3)
    print(f'{circle.circumference()= }, {circle.square()= }\n')
    rect1 = Rectangle(5, 8)
    rect2 = Rectangle(5)
    print(f"{rect1.square()=}, {rect1.perimeter() =} ")
    print(f"{rect2.square()=}, {rect2.perimeter() =} \n")
    emp_1 = Employee('Инженер', 'Алексей', 'Дубровин', 48, 'мужской')
    print(f'{emp_1}\n')
    h_1 = Human('Бронислав', 'Дубровин', 17, 'мужской')
    h_2 = Human('Тамара', 'Мамедова', 78, 'женский')
    print(h_1)
    print(h_2)
    h_1.birthday()
    h_2.birthday()
    print(h_1)
    print(f'{h_2}\n')
    dog = Dog("Кром", 45, 10, "Курцхаар")
    bird = Bird("Иннокентий", 1, 3, "Попугай", "Поговорим?)")
    fish = Fish("Угорь", 3, 3, "Морской")
    print(dog)
    print(bird)
    print(f'{fish}\n')
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Рэкс", 40, 5, "Такса")
    animal_from_fabric1 = fabric.make_animal("bird", "Гоша", 1, 3, "Попугай", "Чирик")
    print(animal_from_fabric)
    print(animal_from_fabric1)
    print(fabric.make_animal('Fish', "Карп", 10, 5, "Речной"))
    print()
    run()
