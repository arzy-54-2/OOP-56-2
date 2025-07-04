

class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def introduce(self):
        return print(f"привет меня зовут {self.name}")

    # def action(self, ):


asuna = Hero("Asuna", 10, 100)

# Объект|экземпляр  класса
# kirito = Hero("Kirito", 100, 1000)
#
# kirito.introduce()
# asuna.introduce()
# print(kirito.name, kirito.lvl)
# print(asuna.name, asuna.lvl)





print(type(asuna))
# print(type(some_text))


