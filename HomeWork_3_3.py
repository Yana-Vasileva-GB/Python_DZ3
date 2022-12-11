# # HomeWork 3. Task 3.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк
# 11 -> 1011
# 88 -> 1011000

# ----------БЕЗ ИСПОЛЬЗОВАНИЯ СТРОК--------
print('Преобразуем десятичное число в двоичное.')

number = int(input('Введите десятичное число - '))

number_bin = []
while number > 0:
    number_bin.append(number % 2)
    number = number // 2
number_bin.reverse()
print(*number_bin, sep = '')



# # ----------С ИСПОЛЬЗОВАНИЕМ СТРОК--------
# print('Преобразуем десятичное число в двоичное.')

# number = int(input('Введите десятичное число - '))
# number_bin = ''
# while number > 0:
#     number_bin = str(number % 2) + number_bin
#     number = number // 2
# print(number_bin)
