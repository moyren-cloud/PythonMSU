# Лекция 4, задание 8. Даны два целых числа A и В. Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания в противном случае.

def print_numbers_in_range(A, B):
    if A < B:
        for number in range(A, B + 1):
            print(number)
    else:
        for number in range(A, B - 1, -1):
            print(number)

A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))
print_numbers_in_range(A, B)
