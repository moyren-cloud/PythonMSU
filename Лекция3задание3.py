#3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a > b:
        first_largest = a
        second_largest = b
    else:
        first_largest = b
        second_largest = a
    if c > first_largest:
        second_largest = first_largest
        first_largest = c
    elif c > second_largest:
        second_largest = c

    return first_largest + second_largest

result = my_func(4,20, 30)
print(f'Сумма наибольших двух аргументов: {result}')
