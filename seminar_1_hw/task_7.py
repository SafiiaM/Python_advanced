# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

while True:
    num = input('Введите число: ')
    if num.isdigit(): # проверка на число
        num = int(num)
        if 0 < num < 1000: # проверка на трехзначность
            if 0 < num < 10: # проверка на цифру
                result = f'{num} - {num * num}' # возвращаем квадрат цифры
            elif 9 < num < 100: # проверка на двузначность
              result = f'{num} - {(num // 10) * (num % 10)}' # возвращаем произведение чисел
            else:
              result = f'{num} - {(num % 10 * 100)  +(num // 10 % 10 * 10)  +(num // 100)}' # зеркальное отображение
        else:
          result = 'Error!'
    else:
      result = 'Error!'
    print(result)
    if result != 'Error!':
        break


