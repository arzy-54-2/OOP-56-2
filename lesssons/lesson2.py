#Наследование



# # Родительский|Супер класс
# class Hero:
#
#     def __init__(self, name, lvl, age, hp):
#         self.name = name
#         self.lvl = lvl
#         self.age = age
#         self.hp = hp
#



#     def action(self):
#         return print(f"Base action")
#
# #
#
# # Дочерний класс
# class MageHero(Hero):
#
#
#     def __init__(self, name, lvl, hp, age, mp):
#         super().__init__(name, lvl, age, hp)
#         self.mp = mp
#
#     def rest(self):
#         return print(f"я отдыхаю")
#
#
#     # def action(self):
#     #     return print(f"==============")
#
# hero = MageHero("Hero1", 100, 26, 1000, 100)
#
# hero.action()




class Animal:
    def action(self):
        return print(f"Animal")

class Fly(Animal):
    def action(self):
        super().action()
        # return print(f"Fly")

class Swim(Animal):
    def action(self):
        super().action()
        # return print(f"Swim")


class Duck(Swim,Fly):
    pass

donald_duck = Duck()
donald_duck.action()

# print(Duck.mro())
# donald_duck.action()
# donald_duck.action()
