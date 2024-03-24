# Вадание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран false, в противном случае Тгие.
# mag = int(input('scolco hp'))
# if mag <= 0:
#     print('false')
# else:
#     print("True")

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если
# да, выведите на экран текст “Четное”, а иначе - “Нечетное”
# mag2 = int(input("yavlaetsa li chetnim"))
# print("ne chetnoe") if mag2 %2 else print('chetnoe')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми
# считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются
# столетиями (500, 600). Однако, если год делится без остатка на 400, он также
# считается високосным (1200, 2000)
# god = int(input("proverca visocosny god = "))
# if (god%4 == 0 and god%100 != 0 or god%400 == 0):
#     print("vesocosni god")
# else:
#     print("god ne visocosny")

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз,
# построчно. Текст и количество повторений нужно ввести с помощью input()
# def texx(a, b):
#     x = 0
#     while x < a:
#         print(f'{b}')
#         x+=1
# text = str(input('text:'))
# col = int(input('kolichestvo povtorov - '))
# texx(col, text)

# Задание 2.5.
# Напишите программу калькулятор, которая принимает 2 значения и арифметическое действие и в конце выводит их в виде
# Param1 operator param2 = result
# sign = input('Знак операции: ')
# a = int(input('Число 1: '))
# b = int(input('Число 2: '))

# match sign:
#     case '+':
#         print(f'{a} {sign} {b} = {a + b}')
#     case '-':
#         print(f'{a} {sign} {b} = {a - b}')
#     case '/':
#         if b != 0:
#             print(f'{a} {sign} {b} = {round(a / b, 2)}')
#         else:
#             print(f'na 0 delit nelza {a} {sign} {b} = ERROR')
#     case '*':
#         print(f'{a} {sign} {b} = {a * b}')
#     case _:
#         print('Неверный знак операции')