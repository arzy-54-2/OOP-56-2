# # class Test:
# #     def __init__(self, name):
# #         self.name= name
# #
# #
# #     def __str__(self):
# #         return f"My method!! {self.name}"
# #
# # test = Test("Test")
# #
# # print(test)
#
#
# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     #     +
#     def __add__(self, other):
#
#         print(self.y)
#         print(other.x)
#
#         return self.y + other.x
#
#     #  ==
#     def __eq__(self, other):
#         return "Some texts"
#
#     def __setitem__(self, index, value):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         pass
#
#     #  del
#     def __del__(self):
#         pass
#
#     #  <
#     def __lt__(self, other):
#         pass
#
#     #     >
#     def __gt__(self, other):
#         pass
#
#
#
# # list1 = [1,2,3,4]
# # list1[1] = 123
#
#
# # obj1 = Vector(13, 14)
# # obj2 = Vector(15, 16)
# #
# # obj3 = obj1 == obj2
# #
# # print(obj3)
#
# class Person:
#     db_conn = "sql:user@password:3452"
#
#
#
#     def __init__(self, name):
#         self.name = name
#
#
#
#     def method(self):
#         return "ok"
#
#     @staticmethod
#     def method1(a , b):
#         return a + b
#
#     @classmethod
#     def method2(cls):
#         return cls.db_conn
#
#
#     @property
#     def method3(self):
#         return "Atribut"
#
# person1 = Person("test")
#
# print(person1.method3)
#
#


class Greeter:

    def __init__(self, name):
        self.name = name


    def __call__(self, *args, **kwargs):
        print(f"Привет {self.name}")

# g = Greeter("Ardager")
#
# g()


class MyClass:

    def __init__(self):
        print("init!!")



    def __new__(cls, *args, **kwargs):
        print("new!!!")
        instance = super().__new__(cls)
        return instance

# obj = MyClass()

class FileOpener:

    def __enter__(self):
        print("open file")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close file")

with FileOpener() as f:
    print("Читаем файл!!")