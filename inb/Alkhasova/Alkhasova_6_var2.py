# задача №6 v2
# Создайте игру,
# в которой компьютер загадывает название одного из семи холмов, на которых по легенде была построена Москва

print("Программа случайным оброзом загадывает название одного из четырех животных, встреченных колобком в лесу, а игрок дожен его угадать. ")

import random as r

x = ['Заяц', 'Волк', 'Медведь', 'Лиса']

n = input("Назовите одного из 4 животных: ")
if n == (r.choice(x)):
    print ("Молодец ты угадал")
else:
    print("Вы не угадали!!!")
    print("Правильный ответ:", (r.choice(x)))

end = input("\nНажмите Enter для выхода")