#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input('Введите целое положительное число: '))
max_digit = 0
while n > 0:
    current_digit = n % 10
    if current_digit > max_digit:
        max_digit = current_digit
    n //= 10
print('Самая большая цифра в вашем числе: ', max_digit)
