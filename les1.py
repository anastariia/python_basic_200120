# 1
i = input("Введите значение:")
print(i)

j = 3
print(j)

# 2
sec = int(input("Введите время в секундах:"))
hh = sec // 3600
mm = sec // 60
ss = sec % 60
print(hh, ":", mm, ":", ss)

# 3
n = int(input("Введите одну цифру:"))
nn = n + n * 10
nnn = nn + n * 100
print(n + nn + nnn)

# 4
i = int(input("Введите целое положительное число:"))
j_max = 0
while i > 0:
    j = i % 10
    i = i // 10
    if j > j_max:
        j_max = j
print("Самое большое число в списке:", j_max)

# 5
proseeds = float(input("Ведите выручку:"))
costs = float(input("Введите издержки:"))
if proseeds > costs:
    print("Прибыль: ", proseeds - costs)
    print("Рентабельность: ", (proseeds - costs) / proseeds)
    i = int(input("Введите количество сотрудников:"))
    if i > 0:
        print("Прибыль в расчёте на одного сотрудника: ", (proseeds - costs) / i)
elif proseeds < costs:
    print("Убыток: ", costs - proseeds)
else:
    print("Прибыли нет, но и убытков нет")

# 6
a = int(input("Километров в первый день:"))
b = int(input("Километров в последний день:"))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print(day)
# print("на ", day, "день спортсмен достиг результата — не менее ", b, " км.")
