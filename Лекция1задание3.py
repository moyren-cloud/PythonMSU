#Лекция1, задание 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))
n = str(n)
nn = n + n
nnn = n + n + n
print(f'{'Выражение: '} {n} + {nn} + {nnn}')
print('Результат: ', int(n) + int(nn) + int(nnn))