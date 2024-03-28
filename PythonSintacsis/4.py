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
class Addem:
    otvet = "\n-------------------\nSpisoc name/value:\n-------------------\n"
    peremen = ''
    def __init__(self, lol):
        self.lol = lol
    def almat(self, **kwargs):
        for name, value in kwargs.items():
            self.peremen = (f'{name} : {value} \n')
            self.otvet = self.otvet + self.peremen
        return(self.otvet)

testys = Addem('445')
print(testys.lol)
print(testys.almat(name='Jhon', last_name='Smith', age=35, position='web devoloper'))
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# my_list2 = lambda my_list, my_list2: [i for i in my_list if i > 0 my_list2.append(i)]
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# 4.5. Декоратор который вычитывает сколько выполнялась функция

# 4.6. Создайте файл my_calcl.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.