# Задание 2.1
my_list = [-451, 2, 99.99, 'One', True, None, any]
def my_type(el):
    for el in range(len(my_list)):
# Вывод названия каждого типа на экран
        print(type(my_list[el]))
    return
my_type(my_list)

# Задание 2.2
s_stop = input('Введите слово, которым вы завершите формирование списка. Например, "end": ')
s_input = 'Введите следующее значение списка, или завершите список словом "' + s_stop + '": '
my_list = []
x = ''
# Формирование списка в цикле, пока не будет написано слово = s_stop
while True:
    x = input(s_input)
    if x == s_stop: 
        break
    my_list.append(x)

i = 0
# Подмена значений
for elem in range(int(len(my_list)/2)):
        my_list[i], my_list[i + 1] = my_list [i + 1], my_list[i]
        i += 2
print(my_list) 

# Возможен другой вариант решения: пользователь заранее должен посчитать кол-во 
# элементов списка, что часто очень неудобно. 
# Но в таком случае можно было бы написать код по-другому,
# спросив сначала кол-во элементов, и пройдясь циклом по списку столько раз.



# Задание 2.3
s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
s_month = int(input("Введите номер месяца: "))
if s_month ==1 or s_month == 12 or s_month == 2:
    print("list:", s_list[0])
    print("dict:", s_dict.get(1))
elif s_month == 3 or s_month == 4 or s_month ==5:
    print("list:", s_list[1])
    print("dict:", s_dict.get(2))
elif s_month == 6 or s_month == 7 or s_month == 8:
    print("list:", s_list[2])
    print("dict:", s_dict.get(3))
elif s_month == 9 or s_month == 10 or s_month == 11:
    print("list:", s_list[3])
    print("dict:", s_dict.get(4))
else:
    print("А как бы вы назвали новый", s_month, "месяц и его сезон?") 

