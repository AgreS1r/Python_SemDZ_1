# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите число: "))
summ = 0
while n != 0:
    summ += (n % 10)
    n = n // 10

print(summ)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Введите сколько всего было сделано журавликов: "))

x = s / 6
PetOrSer = x
Kat = 2 * (x+x)

print(f"Петя сделал {int (x)} журавликов, Серёжа сделал {int (x)} журавликов, Катя сделала {int (Kat)} журавликов")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket_number = input("Введите номер билета: ")

if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Неверный формат номера билета")
else:
    digits = [int(digit) for digit in ticket_number]
    first_half_sum = sum(digits[:3])
    second_half_sum = sum(digits[3:])
    if first_half_sum == second_half_sum:
        print("Билет счастливый!")
    else:
        print("Билет несчастливый")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

i = int(input("Введите количество долек в шоколадке по вертикали: "))
j = int(input("Введите количество долек в шоколадке по горизонтали: "))
k = int(input("Введите количество долек, которые нужно отломить: "))

if k > i * j:
    print("Отломить нужно слишком много долек")
else:
    can_break = (k % i == 0) or (k % j == 0)
    if can_break:
        print("Можно отломить нужное количество долек")
    else:
        print("Нельзя отломить нужное количество долек")
