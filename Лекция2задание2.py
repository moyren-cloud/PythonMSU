#Лекция 2, задание 2.	Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = input('Введите элементы списка, разделив их пробелом: ')
el = list.split()
print('Ваш список до обмена соседних элементов: ', el)
for i in range(0, len(el) - 1, 2):
    el[i], el[i+1] = el[i+1], el[i]
print('Список после обмена соседних элементов: ', el)
