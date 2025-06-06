# Домашнее задание
# Я начал проходить курс по Python в автоматизации и третья лекция у меня была списки, в данную лекцию входили такие разделы как:
#
# Создание списка
# Получение элементов списка
# Добавление элементов в список и их замена
# Добавление элементов в конкретное место списка
# Замена элементов в списке
# Удаление элементов из списка и его очистка
# Срезы список
# Слияние списков
# Мне нужно закрепить данную тему и все разделы в ней. Задачи должны быть максимально простые, чтобы я закреплял синтаксис и логику, сложные задачи не давай. Выдавай мне в случайном порядке по одной задаче из списка разделов данной темы, без решения.
#
# Когда подсказываешь, не нужно приводить правильные примеры решения задачи, пока я этого не попрошу, до тех пор пиши какие доработки мне нужно сделать, чтобы получить правильное решение.
#
# Задачи выдай по запросу, когда я это напишу и нумеруй задачи.

# Задача 1 (Раздел: Получение элементов списка):
# Дан список colors = ['red', 'green', 'blue']. Выведи третий элемент списка.

colors = ['red', 'green', 'blue']
print(colors[2])

# Задача 2 (Раздел: Добавление элементов в список):
# Дан список numbers = [10, 20, 30]. Добавь число 40 в конец списка.

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# Задача 3 (Раздел: Срезы списка):
# Дан список letters = ['a', 'b', 'c', 'd', 'e', 'f'].
# Выведи срез списка, содержащий элементы со второго по четвертый (включительно).

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[1:4])

# Задача 4 (Раздел: Замена элементов в списке):
# Дан список fruits = ['apple', 'banana', 'cherry', 'date'].
# Замени второй элемент списка на 'kiwi' и выведи обновлённый список.

fruits = ['apple', 'banana', 'cherry', 'date']
fruits[1] = 'kiwi'
print(fruits)

# Задача 5 (Раздел: Удаление элементов из списка):
# Дан список languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby'].
# Удали из списка элемент 'C++' и выведи обновлённый список.

languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
languages.remove('C++')
print(languages)

# Задача 6 (Раздел: Слияние списков):
# Даны два списка:
# python
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# Объедини их в один список двумя разными способами и выведи результат каждого.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
copy = list1.copy()
result = list1 + list2
copy.extend(list2)

# Задача 7 (Раздел: Добавление элементов в конкретное место списка):
# Дан список:
# python
# colors = ['red', 'blue', 'green']
# Вставь строку 'yellow' между 'red' и 'blue' (на позицию с индексом 1),
# затем выведи обновлённый список.

colors = ['red', 'blue', 'green']
colors.insert(1, "yellow")
print(colors)

# Задача 8 (Раздел: Очистка списка):
# Дан список:
# numbers = [10, 20, 30, 40, 50]

numbers = [10, 20, 30, 40, 50]
numbers.clear()
print(numbers)

numbers = [10, 20, 30, 40, 50]
numbers = []
print(numbers)

# Задача 9 (Раздел: Получение элементов списка + срезы):
# Дан список:
# animals = ['cat', 'dog', 'fox', 'bear', 'rabbit', 'deer']
# Выведи последний элемент списка (используя отрицательный индекс)
# Сделай срез, чтобы получить подсписок ['fox', 'bear', 'rabbit']
# Выведи каждый второй элемент списка (шаг 2), начиная с первого

animals = ['cat', 'dog', 'fox', 'bear', 'rabbit', 'deer']
print(animals[-1])
print(animals[2:5])
print(animals[::2])

# Задача 10 (Раздел: Комбинированная — добавление + замена + удаление):
# Дан список:
# inventory = ['sword', 'shield', 'potion', 'scroll', 'key']
# Добавь 'apple' после 'potion' (на позицию с индексом 3)
# Замени 'scroll' на 'map'
# Удали 'shield' любым способом
# Выведи итоговый список

inventory = ['sword', 'shield', 'potion', 'scroll', 'key']
inventory.insert(3, 'apple') # Правильно: добавляем 'apple' ПОСЛЕ 'potion' (индекс 3)
inventory[4] = 'map' # Индекс изменился после вставки!
inventory.remove("shield")
print(inventory)

# Задача 11 (Раздел: Комбинированная работа со списками):
# Дан список:
# books = ['Гарри Поттер', 'Властелин Колец', 'Хоббит', '1984']
# Добавь книгу 'Метро 2033' на вторую позицию (индекс 1)
# Замени 'Хоббит' на 'Игра престолов'
# Удали последнюю книгу любым способом
# Выведи:
# Итоговый список
# Количество оставшихся книг (используй len())

books = ['Гарри Поттер', 'Властелин Колец', 'Хоббит', '1984']
books.insert(1, 'Метро 2033')
books[books.index('Хоббит')] = 'Игра престолов'
books.pop()
print(books)
print(f"Количество книг: {len(books)}")

# Задача 12 (Раздел: Генерация списков + работа со строками):
# Дан список слов:
# words = ["Яблоко", "Банан", "Гранат", "Ананас", "Манго"]
# Выбери только фрукты короче 6 букв
# Добавь выбранные фрукты в новый список
# Выведи:
# Исходный список
# Новый список
# Число фруктов в новом списке

words = ["Яблоко", "Банан", "Гранат", "Ананас", "Манго"]
print(words)
short_fruits = []
for fruit in words:
    if len(fruit) < 6:
        short_fruits.append(fruit.upper())

print("Подходящие фрукты:", short_fruits)
print("Найдено", len(short_fruits), "фрукта")

