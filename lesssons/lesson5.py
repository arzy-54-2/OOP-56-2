# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

def simple_decorator(func):
    def wrapper():
        print("перед вызовом функции")
        func()
        print("после вызова функции")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello!!")


# say_hello()


def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет {name}")
        func(name)
    return wrapper


@greeting_decorator
def greeting(name):
    print(f"Как дела {name} ?")


# greeting("Арзыбек")


def repeat_decorator(n):

    def decorator(func):

        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


@repeat_decorator(5)
def hello():
    print("привет!!")

# hello()

def class_decorator(cls):

    class NewClass(cls):
        def new_method(self):
            return print('новый метод!!')

    return NewClass


@class_decorator
class MyClass:
    def old_method(self):
        return print("старый метод")

# obj = MyClass()
#
# obj.old_method()

# import lesson1

# lesson1.Hero()

# from lesson1 import Hero
#
# Hero()


# O (n)

def find_element(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1


# print(find_element([1,2,3,4,5,6,7,8,9], 9))


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9]
target = 10
print(binary_search(arr, target))