# Надо разобраться с классами и подклассами и ооп
# сегодня учил гит
class Person:
  
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)
     
    def __del__(self):
        print("Удален человек с именем", self.name)
  
tom = Person("Tom")
class lol:
    def __init__(self, name, age):
        self._name = name    # имя человека
        self.age = age 
lol2 = lol('Art', 22)
print(lol2._name('Arthur'))
print(lol._name())
