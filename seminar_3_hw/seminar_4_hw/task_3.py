# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def check(x):
    if x % 50 == 0:
        return True
    else:
        return False


def add(amount, n, count=0):
    if (check(n)):
        if count == 3:
            count = 0
            total = (amount + n) * 1.03
            print(total)
            return total, count
        else:
            count += 1
            total = amount + n
            print(total)
            return total, count
    else:
        print("Ошибка, введенная сумма должна быть кратна 50")
        return amount, count


def calc_commission(n):
    if n * 0.015 < 30:
        return 30
    elif n * 0.015 > 600:
        return 600
    else:
        return n * 0.015


def take_off(amount, n, count=0):
    if (check(n) and amount > n):
        if count == 3:
            count = 0
            total = ((amount - n) - calc_commission(n)) * 1.03
            if total < 0:
                print("Error, total < 0")
                return amount, count
            print(total)
            return total, count
        else:
            count += 1
            total = (amount - n) - calc_commission(n)
            if total < 0:
                print("Error, total < 0")
                return amount, count
            print(total)
            return total, count
    else:
        print("Ошибка, сумма для снятия должна быть кратна 50, "
              "либо сумма для снятия больше суммы остатка на счете")
        return amount, count


amount = 0
count = 0
main_flag = True
while main_flag:
    s = int(input("Введите действие: "
                  "1 - внести средства; "
                  "2 - снять средства; "
                  "3 - выйти из системы: ")
            )
    if s == 1:
        n = int(input("Введите сумму для внесения, кратную 50: "))
        amount, count = add(amount, n, count)
    elif s == 2:
        n = int(input("Введите сумму для снятия, кратную 50: "))
        amount, count = take_off(amount, n, count)
    else:
        break