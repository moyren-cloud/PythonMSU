#Лекция 3, задание 4. Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    def power_with_operator(x, y):
        return x ** y
    result_with_operator = power_with_operator(x, y)
    return result_with_operator

x = 5
y = -2
result = my_func(x, y)
print(f"Результат с использованием оператора **: {result}")

# Решение №2 - не смогла сделать
