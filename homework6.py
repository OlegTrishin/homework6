my_dict = {"Arnold": 1990, "Carl": 1991, "Felix": 1992, "Harry": 1993} # Создали словарь
print("Dict:", my_dict)                             # Вывели на экран словарь my_dict
print("Existing value:", my_dict["Arnold"])         # Вывели на экран одно значение по существующему ключу
print("Not existing value:", my_dict.get("Victor")) # Вывели на экран значение по отсутствующиму в словаре ключу
my_dict["John"] = 1994                              # Добабляем две пары того же формата в словарь my_dict
my_dict["Kevin"] = 1995
a = my_dict.pop("Carl")                     # Удаляем одну из пар в словаре по существующему ключу из словаря my_dict
print("Deleted value:", a)                  # и выведим значение из этой пары на экран
print("Modified dictionary:",my_dict)       # Выводим на экран словарь my_dict
print(" ")                                      # Пустая строка
my_set = {33, "Test", 12.5, 33, 12.5, "Test"}       # Создаём множество
print("Set:", my_set)                               # Выводим на экран множество my_set
my_set.update([11, "Ok"])               # Добавляем 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.discard(33)                      # Удаляем один элемент из множества my_set
print("Modified set:", my_set)          # Выводим на экран измененное множество my_set
