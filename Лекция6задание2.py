# Лекция 6, задание 2.	Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = 'my_new_file.txt'
with open(file, 'r', encoding='utf-8') as my_new_file:
    lines = my_new_file.readlines()
print('Количество строк в файле: ', len(lines))
for ind, line in enumerate(lines, start = 0):
    word_count = len(line.strip().split())
    print('Количество слов: ', word_count)
