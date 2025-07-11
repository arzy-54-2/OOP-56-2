# Инкапсуляция
import random

class BankAccount:
    # Атрибут класса
    def_pass = "admin"

    def get_user(self):
        return print(f"{self.user}")


    def __generate_defoult_pass(self):
        self.__password = self.__def_pass

    def reset_pass(self):
        self.__generate_defoult_pass()
        return print("pass reset !!")

    def __init__(self, user, balance, password):
        # Атрибуты экземпляра класса
        self.user = user
        self._balance = balance # Защищенный атрибут
        self.__password = password # Приватный атрибут


john = BankAccount("John", 1000, 123321)

# print(dir(john))
#
# john.reset_pass()

# Абстракция

from abc import ABC, abstractmethod


# Абстрактный класс
class Animal(ABC):

    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def __init__(self, nik):
        self.nik = nik

    def make_sound(self):
        return print(f"{self.nik} Gaf Gaf")

    def step(self):
        return print(f"step")

sharik = Dog("Sharik")

sharik.make_sound()

