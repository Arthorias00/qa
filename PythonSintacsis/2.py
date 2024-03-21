# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
print('-----\\-----\\-----\\-----\\-----\\-----')
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
print('----------------------------------------')
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
momo = 0
for x in list_1:
    if type(x) is int:
        momo = momo + x
print(momo)
print('----------------------------------------')
# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list_2 = ['cat', 'dog', 'horse', 'cow']
tuple_my = tuple(list_2)
print(type(tuple_my))
print('----------------------------------------')
# 3.4. Напишите программу, которая определяет, какая семья больше. 
#       1) Программа имеет два input() - например, family_1, family_2. 
#       2) Членов семьи нужно перечислить через запятую. 
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input("Первая семья: ")
# family_2 = input("Вторая семья: ")
# print("f1 > f2") if family_1 > family_2 else (print("f1 < f2") if family_2 > family_1 else print("f1 = f2"))
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме. 
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
film = {'title' : 'zagolovoc', 'director' : 'director', 'year' : 'god', 'budget' : 'budget', 'main_actor' : 'glavni actor', 'slogan' : 'diviz'}
for key, value in film.items():
    print(f"{key} : {value}")
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 
spisoc = [1, 2, 3, 4, 5, 3, 2, 1]
spisoc_bez_povtorenii = list(set(spisoc))
print(spisoc_bez_povtorenii)
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга 
set10 = {100, 'b'}
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
def returnMatches(a, b):
    return list(set(a) & set(b))
set3 = (set1 - set2) | (set2 - set1)
print(set3)
print(returnMatches(set1, set2))
def podmnog(a, b):
    if a.issubset(b):
        print(f'a - подмножество b: {a}')
    elif b.issubset(a):
        print(f'b - подмножество a: {b}')
    else:
        print('Подмножеств нет')

podmnog(set1, set10)