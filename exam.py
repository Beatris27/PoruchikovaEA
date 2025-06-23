#  Задача 1. Переменные и типы данных
# 1\. Создайте переменную `number` со значением 42.
number = 42
# 2\. Преобразуйте её в строку и сохраните в переменную `number_str`.
number_str = str(number)
# 3\. Создайте переменную `text` со значением "The answer is: ".
text = "The answer is: "
# 4\. Объедините строку `text` и строку `number_str` и сохраните результат в переменную `result`.
result = text + number_str
# 5\. Выведите на экран:
print(result)
# - значение и тип данных `number`,
print(number, type(number))
# - значение и тип данных `number_str`,
print(number_str, type(number_str))
# - значение и тип данных `text`,
print(text, type(text))
# - значение и тип данных `result`
print(result, type(result))

# Задача 2. Строки
# Даны две переменные:
name = "Лена"
age = 31
# Используя f-строку, выведите на экран сообщение: "Меня зовут ваше имя, мне ваш возраст лет."
print(f"Меня зовут {name}, мне {age} лет.")

# Задача 3. Списки
# Дан список:
my_list = [1, 2, 3]
# Создайте копию этого списка, измените первый элемент копии на 10 и выведите оба списка.
new_list = my_list.copy()
new_list[0] = 10
print(my_list)
print(new_list)

# Задача 4. Условные операторы
# Напишите программу, которая принимает число от пользователя и проверяет:
# - Если число больше 0, выведите "Положительное".
# - Если число равно 0, выведите "Ноль".
# - Если число меньше 0, выведите "Отрицательное".
number = int(input())
if number > 0:
    print("Положительное")
elif number == 0:
    print("Ноль")
else:
    print("Отрицательное")

# Задача 5. Словари
#
# Дан словарь:

person = {

      "name": {

          "first_name": "Иван",

          "last_name": "Иванов"

},

   "address": {

       "city": "Москва",

      "country": "Россия"

    }

}

# Обновите значение ключа "city" на "Санкт-Петербург" и добавьте новый ключ "postal_code" со значением "333777" в словарь "address".
person["address"]["city"] = "Санкт-Петербург"
person["address"]["postal_code"] = "333777"
# Выведите значение через print.
print(person)
# Затем удалите ключ "city" из вложенного словаря "address" и снова выведите значение через print.
del person["address"]["city"]
print(person)

# Задача 6. Циклы
# Напишите цикл while, который выводит числа от 1 до 20, но пропускает числа, которые делятся на 4
# (используйте continue)
number = 1
while number <= 20:
    if number % 4 == 0:
        number +=1
        continue
    print(number)
    number += 1

# Задача 7. Файлы
# Создайте файл с именем "fruits.txt" и запишите в него названия фруктов:
# "яблоко", "банан", "апельсин" (каждое с новой строки).
# Затем откройте этот файл, прочитайте все строки и выведите на экран только те строки, которые начинаются с буквы "а".

with open("fruits.txt", "w", encoding="utf-8") as file:
    file.write("яблоко\nбанан\nапельсин")
with open("fruits.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Убираем пробельные символы в начале/конце
        cleaned_line = line.strip()
        # Проверяем первую букву (учитываем кириллицу)
        if cleaned_line.startswith('а'):
            print(cleaned_line)

# Задача 8. Функции
# Напишите функцию greet_user, которая приветствует пользователя в зависимости от его роли и имени.
# Функция должна принимать два параметра:
# user_role (обязательный) — строка, указывающая роль пользователя (например, "Администратор", "Гость", "Модератор").
# user_name (необязательный) — строка с именем пользователя. По умолчанию должно быть None.
# Логика работы функции:
# - Если имя пользователя передано (user_name не None и не пустая строка), функция должна вывести: "Привет, {user_name}! Ваша роль: {user_role}."
# - Если имя не передано (user_name равно None или пустая строка), функция должна вывести: "Привет, Гость! Ваша роль: {user_role}."
def greet_user(user_role, user_name=None):
    if user_name is not None and user_name.strip() != "":
        print(f"Привет, {user_name}! Ваша роль: {user_role}.")
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")

# Задание 9. ООП ч.1
# Создайте класс `Student`, который будет представлять студента.
# У класса должны быть атрибуты `name`  и `age`, которые задаются при создании объекта через конструктор `__init__`.
# Создай объект класса `Student` с вашим именем и вашим возрастом.
# Выведи на экран имя и возраст студента.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_student = Student(name="Lena", age=31)
print(f"Имя: {my_student.name}, возраст: {my_student.age}")

# Задача 10. ООП ч.2
# Создайте базовый класс Animal с атрибутами:
# name (кличка животного)
# species (вид животного, например "собака", "кошка")
# И методами:
# eat()
# sleep()
# Затем создайте дочерний класс Dog, который:
# Наследует все от класса Animal
# Имеет дополнительный метод bark() (лаять)
# Задание:
# - Создайте объект my_dog класса Dog с любым именем
# - Вызовите все три метода: eat(), sleep(), bark() и выведите результаты
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def eat(self):
        print(f"{self.name}({self.species}) ест.")

    def sleep(self):
        print(f"{self.name}({self.species}) спит.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} ({self.species}) лает: Гав-гав!")

my_dog = Dog(name="Бобик", species="собака")

my_dog.eat()
my_dog.sleep()
my_dog.bark()