## Домашнее задание
# Я начал проходить курс по Python в автоматизации и десятая лекция у меня была ООП часть 2,
# в данную лекцию входили такие разделы как:
# - Наследование
# Мне нужно закрепить данную тему и все разделы в ней. Задачи должны быть максимально простые,
# чтобы я закреплял синтаксис и логику, сложные задачи не давай. Выдавай мне в случайном порядке
# по одной задаче из списка разделов данной темы, без решения.
# Когда подсказываешь, не нужно приводить правильные примеры решения задачи, пока я этого не попрошу,
# до тех пор пиши какие доработки мне нужно сделать, чтобы получить правильное решение.
# Задачи выдай по запросу, когда я это напишу и нумеруй задачи.
from pydoc import classify_class_attrs


# Базовый класс + переопределение метода
# Создай базовый класс Animal с методом make_sound(), который печатает "Some generic sound". Затем создай подкласс Dog,
# который переопределяет этот метод, чтобы он печатал "Woof!".

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

my_Dog = Dog()
my_Dog.make_sound()



# Наследование атрибутов
# Создай класс Vehicle с атрибутом wheels = 4. Создай подкласс Motorcycle,
# который наследует Vehicle и изменяет wheels на 2.

class Vehicle:
    wheels = 4


class Motorcycle(Vehicle):
    wheels = 2

car = Vehicle()
print(car.wheels)  # Должно вывести: 4

moto = Motorcycle()
print(moto.wheels)  # Должно вывести: 2

# Добавление нового атрибута в подкласс
# Создай класс Person с атрибутами name и age. Создай подкласс Student,
# который добавляет новый атрибут student_id и метод display_id(), печатающий этот ID.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id

    def display_id(self):
        print(f"Студент номер {self.student_id}, Имя {self.name} Возраст {self.age}")


student = Student(1, "Lena", 30)
student.display_id()

# Расширение метода родителя
# Создай класс Bird с методом fly(), который печатает "Flying!".
# Создай подкласс Penguin, который переопределяет fly() на "Can't fly!".

class Bird:
    def fly(self):
        print("Flying!")

class Penguin(Bird):
    def fly(self):
        print("Can't fly!")

garry = Penguin()
garry.fly()

# Использование super()
# Создай класс Employee с методом work(), печатающим "Working hard".
# Создай подкласс Manager, который использует super() в своем методе work(), чтобы добавить " and delegating tasks" к выводу родителя.

class Employee:
    def work(self):
        print("Working hard",  end='')

class Manager(Employee):
    def work(self):
        super().work()
        print(" and delegating tasks")

valera = Manager()
valera.work()

# Множественное наследование (простой вариант)
# Создай два базовых класса: Walkable (с методом walk()) и Swimmable (с методом swim()).
# Создай подкласс Duck, который наследует оба класса и вызывает их методы.

class Walkable:
    def walk(self):
        print("Прогулка")

class Swimmable:
    def swim(self):
        print("Плывем")

class Duck(Walkable, Swimmable):
    pass

scrodge = Duck()
scrodge.walk()
scrodge.swim()



# Переопределение __init__
# Создай класс Device с атрибутом power_source = "electricity".
# Создай подкласс Smartphone, который в __init__ добавляет атрибут battery_capacity.

class Device:
    power_source = "electricity"

class Smartphone(Device):
    def __init__(self, battery_capacity):
        super().__init__()
        self.battery_capacity = battery_capacity


phone = Smartphone(5000)
print(phone.power_source)
print(phone.battery_capacity)

# Проверка типа наследования
# Создай класс Shape с методом area() (возвращает 0). Создай подкласс Square,
# который принимает side в конструкторе и переопределяет area() (рассчитывает площадь).

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side

kvadrate = Square(4)
print(kvadrate.area())

# Статический метод в иерархии
# Создай класс MathOperations со статическим методом add(a, b). Создай подкласс AdvancedMath,
# который добавляет статический метод multiply(a, b).

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

class AdvancedMath(MathOperations):
    @staticmethod
    def multiply(a, b):
        return a + b

print(MathOperations.add(2, 3))        # 5
print(AdvancedMath.add(2, 3))           # 5 (наследуется)
print(AdvancedMath.multiply(2, 3))

# Класс как атрибут
# Создай класс Engine (с методом start()). Создай класс Car, который содержит атрибут engine как экземпляр Engine.
# В Car добавь метод start_car(), вызывающий engine.start().

class Engine:
    def start():
        pass

class Car:
    def __init__(self):
        # Создай атрибут engine как экземпляр Engine
        pass

    def start_car(self):
        # Вызови метод start() у engine
        pass

my_car = Car()
my_car.start_car()
