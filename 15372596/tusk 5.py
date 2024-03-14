# https://inf-ege.sdamgia.ru/problem?id=59683
def algoritm(n):
    # 1.Строится двоичная запись числа N.
    binary = bin(n)
    binary = binary[2:]
    # 2.Далее эта запись обрабатывается по следующему правилу:
    # а)если число N делится на 3, то в этой записи дописываются справа три последние двоичные цифры;

    if n % 3 == 0:
        last_numbers_from_binary = binary + binary[-3:]
    # б)если число N на 3 не делится, то остаток от деления умножается на 3, переводится в двоичную запись и дописывается в конец числа.
    if n % 3 != 0:
        last_numbers_from_binary = bin((n % 3) * 3)
        last_numbers_from_binary = binary + last_numbers_from_binary[2:]
    # 3.Результат переводится в десятичную систему и выводится на экран.

    return int(last_numbers_from_binary, 2)

max = 0
for i in range(10000):
    a = algoritm(i)
    if a < 170 and a > max:
        max = a
print(max)

