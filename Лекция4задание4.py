# Лекция 4, задание 4. Улитка ползет по вертикальному шесту высотой h метров,
# поднимаясь за день на a метров, а за ночь спускаясь на b метров.
# На какой день улитка доползет до вершины шеста?

h = float(input('Высота шеста: '))
a = float(input('За день улитка поднялась на такое количество метров: '))
b = float(input('За ночь улитка спустилась на такое количество метров: '))
day = 1
current_result = 0
while current_result < h:
    day += 1
    current_result += a
    if current_result >= h:
        print(day)
    current_result -= b
print((f'{'Улитка достигнет вершины шеста на'} {day}{'-й день:'}'))
