# Лекция 4, задание 9.  На сковородку одновременно можно положить k котлет.
# Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
# За какое наименьшее время удастся поджарить с обеих сторон n котлет?

def cooking_time(n, k, m):
    all_the_cutlets = n // k
    a_full_frying_pan = n % k
    total_time = all_the_cutlets * 2 * m
    if a_full_frying_pan > 0:
        total_time += 2 * m
    return total_time

n = 10
k = 3
m = 5
result = cooking_time(n, k, m)
print(f'Наименьшее время для обжаривания {n} котлет: {result} минут.')