# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = 123
# a = 100

print("Введите 3х значное число:")
a = int(input())
b = (a // 10) // 10
c = a % 10
d = (a // 10) % 10


# print(a, b, c, d)

print('Сумма чисел равна:', b + c + d)