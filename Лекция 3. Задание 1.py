#Лекция 3, задание 1.	Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_division():
    try:
        arg_1 = int(input('Введите первое число: '))
        arg_2 = int(input('Введите второе число: '))
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'
print(my_division())
