# Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
# часы, минуты и секунды для каждого из моментов времени.
# Известно, что второй момент времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.

def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print('Введите первый момент времени: ')
hours1 = int(input('Часы: '))
minutes1 = int(input('Минуты: '))
seconds1 = int(input('Секунды: '))

print('Введите второй момент времени: ')
hours2 = int(input('Часы: '))
minutes2 = int(input('Минуты: '))
seconds2 = int(input('Секунды: '))

first_time_in_seconds = time_to_seconds(hours1, minutes1, seconds1)
second_time_in_seconds = time_to_seconds(hours2, minutes2, seconds2)

difference_in_seconds = second_time_in_seconds - first_time_in_seconds

print('Количество секунд между двумя моментами времени: ', difference_in_seconds)
