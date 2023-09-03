# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions

import fractions

f1 = fractions.Fraction(1, 2)
print(f1)
f2 = fractions.Fraction(2, 3)
print(f2)
print(f'Сумма дробей = {f1+f2}\nПроизведение дробей = {f1 * f2}')

# решение через функцию

def process_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    # сумма дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

frac1_str = "3/4"
frac2_str = "2/3"

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей {frac1_str} и {frac2_str} = {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {frac1_str} и {frac2_str} = {prod_frac[0]}/{prod_frac[1]}")

