# Лекция 6, задание 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
from idlelib.iomenu import encoding

filename = 'salary.txt'

salary_under_20k = []

with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        salary = parts[1]
        try:
            salary = int(salary)
            if salary < 20000:
                salary_under_20k.append(name)
        except ValueError:
            print(f"Ошибка преобразования зарплаты для {name}: {salary}")

print('Сотрудники с зарплатой меньше 20000: ', salary_under_20k)
