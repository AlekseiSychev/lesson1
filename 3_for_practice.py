'''Практика: Цикл
Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1.
'''

int_list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for int_list in range(10):
    int_list += 1
    print(int_list)

'''Практика: Цикл
Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.
'''

enter_string = input('Введите строку ')

for word in enter_string:
    print(word)