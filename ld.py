#List
number = [3, 5, 7, 9, 10.5]
print(number)
print(len(number))

number.append('Python')
print(number)

print(number[0])
print(number[-1])
print(number[1:5])

del number[-1]
print(number)

#Dict
weather = {"city": "Москва", "temperature": "20"}
print(weather['city'])

weather['temperature'] = int(weather['temperature']) - 5
print (weather)

# print(weather['country']) выдается ошибка KeyError: 'country'
print(weather.get('country', 'Ключа country не существует'))

print(weather.get('country', 'Россия'))

weather ['date'] = "27.05.2019"
print(weather)

print(len(weather))
