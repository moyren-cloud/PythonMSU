#Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

a = float(input('Результат первого дня: '))
b = float(input('Ожидаемый результат: '))
day = 1
current_result = a
while current_result < b:
    current_result *= 1.1
    day += 1
print(f'{'Спортсмен достигнет результат на'} {day}{'-й день:'}')
