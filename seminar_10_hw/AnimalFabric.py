"""
ДЗ_1

Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
from Animals import Dog, Bird, Fish


class AnimalFabric:
    def creat_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_creater(animal_type)
        return new_animal(*args, **kwargs)

    @staticmethod
    def _get_creater(animal_type: str):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.creat_animal("dog", "Кром", 45, 10, "Курцхаар")
    animal_from_fabric1 = fabric.creat_animal("bird", "Иннокентий", 1, 3, "Попугай", "Поговорим?)")

    print(animal_from_fabric)
    print(animal_from_fabric1)
    print(fabric.creat_animal('Fish', "Угорь", 3, 3, "Морской"))
