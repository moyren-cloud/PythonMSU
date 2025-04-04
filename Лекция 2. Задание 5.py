#Лекция 2, задание 5. Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [8, 7, 6, 5, 4, 3, 2]
new_evaluation = int(input('Поставьте свою оценку книге от 1 до 10: '))
while True:
    for el in range(len(rating)):
        if rating[el] == new_evaluation:
            rating.insert(el + 1, new_evaluation)
            break
        elif rating[0] < new_evaluation:
            rating.insert(0, new_evaluation)
        elif rating[-1] > new_evaluation:
            rating.append(new_evaluation)
        elif rating[el] > new_evaluation and rating[el + 1] < new_evaluation:
            rating.insert(el + 1, new_evaluation)
    print('Новый рейтинг: ', rating)
    break




