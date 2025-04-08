#Лекция 3, задание 2.	Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birth_year, city, email, phone):
    info = (
        f'Имя: {name}, '
        f'Фамилия: {surname}, '
        f'Год рождения: {birth_year}, '
        f'Город: {city}, '
        f'Email: {email}, '
        f'Телефон: {phone}'
    )
    return info

print(user_info(
    name = 'Антон"',
    surname = 'Городецкий',
    birth_year = 1968,
    city = 'Москва',
    email = 'anton.gorodetskyi@mail.ru',
    phone = '+7 (999) 111-11-11'
))