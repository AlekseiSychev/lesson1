# Практика: Числа 1
a = 2
b = 0.5
print(a + b)

# Практика: Строки 1
name = 'Алексей' 
hello = 'Привет'
output = '{}, {}!'.format(hello , name)
print(output)

# Практика: Строки 2
short_name = 'Алексей'
print(f'Привет, {short_name}!')

# Практика: Числа 2
v = int(input ('Введите число от 1 до 10: '))
print(v + 10)

# Практика: Строки 3
name = input('Введите ваше имя: ').capitalize()
print(f'Привет, {name}! Как дела?')

# Практика: Приведение типов
a_float = float('1')
print(a_float)

a_int = int(float('2.5')) # a_int = int('2.5') Выдает ошибку: ValueError: invalid literal for int() with base 10: '2.5'
print(a_int)

a_bool = bool(1)
print(a_bool)

a_bool1 = bool('')
print(a_bool1)
            
a = bool(0)
print(a)