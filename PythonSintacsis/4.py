# 4.1. Напишите функцию $sqar, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
# def sqar(a):
#     z = a * a
#     p = a * 4
#     d = a * (2 ** (0.5))
#     return(f'perimetr = {p}, \n ploshad = {z},\n diagonal = {d} ')
# print(sqar(23))
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение. Например:
# name: Jhon
# last_name:Smith
# age: 35
# position: web devoloper
# class Addem:
#     otvet = "\n-------------------\nSpisoc name/value:\n-------------------\n"
#     peremen = ''
#     def __init__(self, lol):
#         self.lol = lol
#     def almat(self, **kwargs):
#         for name, value in kwargs.items():
#             self.peremen = (f'{name} : {value} \n')
#             self.otvet = self.otvet + self.peremen
#         return(self.otvet)

# testys = Addem('445')
# print(testys.lol)
# print(testys.almat(name='Jhon', last_name='Smith', age=35, position='web devoloper'))
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# my_list2 = lambda x: [value for value in x if value > 0]
# print(my_list2(my_list))
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# mylist = [20, -3, 15, 2, -1, -21]
# result = lambda x: reduce(lambda a, b: a * b, x)
# print(result(mylist))
# 4.5. Декоратор который вычитывает сколько выполнялась функция
# import time
# class mamy():
#     def __init__(self, a):
#         self.a = a
#     def lolololo (func):
#         def wrapper():
#            start_time = time.time()
#            func()
#            end_time = time.time()
#            print(f"Функция {func.__name__} выполнялась {end_time - start_time:.2f} секунд")
#         return wrapper
   
#     @lolololo
#     def funcyyyyyys():
#         print('its work')
#         time.sleep(5)
# ggg = mamy
# ggg.funcyyyyyys()   
# 4.6. Создайте файл my_calcl.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.
# import mycycl
# mycycl.art2('lol')
