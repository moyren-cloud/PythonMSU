# Лекция 6, задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

filename = 'ex4.txt'

translations = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(filename, 'r', encoding='utf-8') as file:
    with open('translated_numbers.txt', 'w', encoding='utf-8') as output_file:
        for line in file:
            parts = line.strip().split()
            number_in_english = parts[0]
            dash = parts[1]
            number = parts[2]
            russian_word = translations.get(number_in_english, number_in_english)
            output_file.write(f'{russian_word} — {number}\n')

print("Перевод завершен. Результат записан в файл 'translated_numbers.txt'.")
