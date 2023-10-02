"""
Задание 5

Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. У каждого класса должны быть как общие
свойства, например имя, так и специфичные для класса. Для каждого класса создайте метод, выводящий информацию
специфичную для данного класса.

Задание 6

Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное. Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animals:

    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Bird(Animals):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Летать"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type} {self.move()} {self.say()}"


class Dog(Animals):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type
        self.commands = []

    def move(self):
        return "Охотиться"

    def say(self):
        return "Лай"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type} {self.move()} {self.say()}"


class Fish(Animals):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Плавать"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type} {self.move()}"


if __name__ == '__main__':
    dog = Dog("Кром", 45, 10, "Курцхаар")
    bird = Bird("Иннокентий", 1, 3, "Попугай", )
    fish = Fish("Угорь", 3, 3, "Морской")

    print(dog)
    print(bird)
    print(fish)

####
# class Animals:
#
#     def __init__(self, name: str, weight: int, age: int):
#         self.name = name
#         self.weight = weight
#         self.age = age
#
#     def move(self):
#         pass
#
#     def say(self):
#         pass
#
#     def __str__(self):
#         return f"{self.name} {self.weight} {self.age}"
#
#
# class Bird(Animals):
#     def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
#         super().__init__(name, weight, age)
#         self.bird_type = bird_type
#         self._sound = sound
#
#     def move(self):
#         return "Летать"
#
#     def say(self):
#         return self._sound
#
#     def __str__(self):
#         return f"{super().__str__()} {self.bird_type} {self.move()} {self.say()}"
#
#
# class Dog(Animals):
#     def __init__(self, name: str, weight: int, age: int, dog_type: str):
#         super().__init__(name, weight, age)
#         self.dog_type = dog_type
#         self.commands = []
#
#     def move(self):
#         return "Охотиться"
#
#     def say(self):
#         return "Лай"
#
#     def __str__(self):
#         return f"{super().__str__()} {self.dog_type} {self.move()} {self.say()}"
#
#
# class Fish(Animals):
#     def __init__(self, name: str, weight: int, age: int, fish_type: str):
#         super().__init__(name, weight, age)
#         self.fish_type = fish_type
#
#     def move(self):
#         return "Плавать"
#
#     def say(self):
#         return ""
#
#     def __str__(self):
#         return f"{super().__str__()} {self.fish_type} {self.move()}"
#
#
# if __name__ == '__main__':
#     dog = Dog("Кром", 45, 10, "Курцхаар")
#     bird = Bird("Иннокентий", 1, 3, "Попугай", "Поговорим?)")
#     fish = Fish("Угорь", 3, 3, "Морской")
#
#     print(dog)
#     print(bird)
#     print(fish)
