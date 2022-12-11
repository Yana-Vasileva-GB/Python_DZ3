# # HomeWork 3. Task 2.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# 4 -> [2, 5, 8, 10] -> 20, 40
# 5 -> [2, 2, 4, 8, 8] -> 16, 16, 4

import random
print('Найдем произведение пар чисел списка.')
number = int(input('Введите требуемое количество элементов списка - '))
list = [random.randint(0, 10) for i in range(0, number)]
if number < 0:
    print('Введите положительное значение.')
else:
    print(list)


def mult_numbers():

    list_mult = []

    for i in range(len(list)//2):
        list_mult.append(list[i] * list[len(list) - i - 1])

    if len(list) % 2:
        list_mult.append(list[len(list) // 2])

    print(list_mult)


mult_numbers()