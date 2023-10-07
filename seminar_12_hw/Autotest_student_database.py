"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
__init__(self, name, subjects_file): конструктор класса, принимающий ФИО студента и имя файла с данными о предметах и оценках.
add_subject(self, subject, grade, test_score): метод для добавления информации о предмете, оценке и результате теста.
get_average_grade(self): метод, возвращающий средний балл студента по всем предметам.
get_subjects(self): метод, возвращающий список всех предметов, по которым есть информация у студента.
Реализовать функцию get_average_grades(students), которая принимает список студентов и выводит информацию о средних баллах для каждого студента.
Реализовать функцию get_subject_average(students, subject), которая принимает список студентов и название предмета, и выводит информацию о среднем балле по этому предмету для каждого студента.
Реализовать функцию get_top_student(students, subject), которая принимает список студентов и название предмета, и выводит информацию о студенте с наивысшим средним баллом по этому предмету.
Пример
На входе:

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История

"""

import csv

# Дескриптор для проверки ФИО
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.replace(" ", "").isalpha() or not value.istitle():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы.")

# Класс для хранения оценок и результатов тестов по предметам
class SubjectInfo:
    def __init__(self):
        self.grades = []# Список оценок
        self.test_scores = []# Список результатов тестов

    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.grades.append(grade)

    def add_test_score(self, test_score):
        if test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.test_scores.append(test_score)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def get_average_test_score(self):
        return sum(self.test_scores) / len(self.test_scores) if self.test_scores else 0

# Класс Студент
class Student:

    def __init__(self, name, subjects_file):
        self._name = name
        self._subjects = self.load_subjects_from_csv(subjects_file)  # Список предметов из CSV файла
        self.subject_info = {subject: SubjectInfo() for subject in self._subjects}# Информация о предметах

    def load_subjects_from_csv(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            subjects = next(reader)# Считываем предметы из первой строки CSV файла
        return subjects

    def add_grade(self, subject, grade):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден в списке допустимых предметов.")
        self.subject_info[subject].add_grade(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден в списке допустимых предметов.")
        self.subject_info[subject].add_test_score(test_score)

    def get_average_grade(self):
        total_grades = sum(info.get_average_grade() for info in self.subject_info.values())
        return total_grades / len(self._subjects) if self._subjects else 0

    def get_subjects(self):
        return ", ".join(self._subjects) if self._subjects else ""

    def get_average_test_score(self, subject):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден в списке допустимых предметов.")
        total_test_scores = sum(info.get_average_test_score() for info in self.subject_info.values())
        return total_test_scores / len(self._subjects) if self._subjects else 0

    def __str__(self):
        return f"Студент: {self._name}\nПредметы: {self.get_subjects()}"

# Функция для получения среднего балла студента по предметам
def get_average_grades(students):
      for student in students:
        print(f"Средний балл студента {student._name}: {student.get_average_grade()}")

# Функция для получения среднего балла студентов по определенному предмету
def get_subject_average(students, subject):
    for student in students:
        if subject in student._subjects:
            print(
                f"Средний балл по предмету '{subject}' для студента {student._name}: {student.subject_info[subject].get_average_grade()}")

# Функция для определения лучшего студента по среднему баллу по предмету
def get_top_student(students, subject):
    top_student = None
    top_grade = 0

    for student in students:
        if subject in student._subjects:
            average_grade = student.subject_info[subject].get_average_grade()
            if average_grade > top_grade:
                top_student = student
                top_grade = average_grade

    if top_student:
        print(f"Лучший студент по предмету '{subject}': {top_student._name} (средний балл {top_grade})")
    else:
        print(f"Нет данных о студентах по предмету '{subject}'")


# Пример использования

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)



