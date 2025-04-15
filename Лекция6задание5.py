# Лекция 6, задание 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from fileinput import filename

numbers = [4, 55, 6, 70, 8]
filename = 'new_numbers.txt'

with open(filename, 'w', encoding='utf-8') as file:
    file.write(' '.join([str(number) for number in numbers]))
total_sum = 0
with open(filename, 'r', encoding='utf-8') as file:
    for el in file:
        parts = el.split()
        total_sum += sum(int(part) for part in parts)
print("Сумма чисел: ", total_sum)
