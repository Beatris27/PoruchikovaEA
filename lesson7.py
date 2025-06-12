# file = open("data.txt", "r", encoding="utf-8")
#print(file.readlines())
# for line in file.readlines():
#     print(line)
# file = open("data.txt", "w", encoding="utf-8")
# file.write("Новая запись ")
from contextlib import closing

# Домашнее задание
# Я начал проходить курс по Python в автоматизации и седьмая лекция у меня была файлы,
# в данную лекцию входили такие разделы как:
# Работа с файлами
# Контекстный менеджер with
# Мне нужно закрепить данную тему и все разделы в ней.
# Задачи должны быть максимально простые, чтобы я закреплял синтаксис и логику,
# сложные задачи не давай. Выдавай мне в случайном порядке по одной задаче из списка
# разделов данной темы, без решения.
# Когда подсказываешь, не нужно приводить правильные примеры решения задачи,
# пока я этого не попрошу, до тех пор пиши какие доработки мне нужно сделать,
# чтобы получить правильное решение.
# Задачи выдай по запросу, когда я это напишу и нумеруй задачи.

# Прочитать первую строку из файла data.txt и вывести её на экран.

with open("data.txt", "r", encoding="utf-8") as file:
    print(file.readline())


# Используя with, записать строку "Hello, Python!" в новый файл greeting.txt.

with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")

# Добавить строку "New data" в конец файла greeting.txt (без перезаписи).

with open("greeting.txt", "a", encoding="utf-8") as file:
    file.write("\nNew data")

# Прочитать весь текст из файла data.txt и вывести его.

with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Используя with, скопировать содержимое файла data.txt в файл greeting.txt.

with open("data.txt", "r", encoding="UTF-8") as file1, open("greeting.txt", "w", encoding="utf-8") as file2:
    file2.write(file1.read())

# Прочитать файл data.txt построчно и вывести каждую строку на экран.

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="") # Добавить end="" чтобы убрать лишний перенос

# Используя with, добавить строку "Appended line" в конец файла greeting.txt.

with open("greeting.txt", "a", encoding="utf-8") as file:
    file.write("\nAppended line")

# Прочитать первые 5 символов из файла greeting.txt и вывести их.

with open("greeting.txt", "r", encoding="utf-8") as file:
    print(file.read(5))

# Перезаписать файл greeting.txt новым текстом: "Updated content".

with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Updated content")

# Используя with, прочитать файл greeting.txt и вывести его содержимое.

with open("greeting.txt", "r", encoding="utf-8") as file:
    print(file.read())