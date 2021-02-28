"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def main():
  
  def check_str(Line1, Line2):
    
      if isinstance(Line1, str) and isinstance(Line2, str):

          if Line1 == Line2:
            return '1'
            
          else:
              if len(Line1) == len(Line2):
                return '2'

              else:
                  if Line2 == 'learn':
                    return '3'

                  else:
                    return 'Строка'

      else:               
          return '0'

  print(check_str(123, 123))
  print(check_str(30.5, 30.5))
  print(check_str(True, False))
  print(check_str(None, None))
  print(check_str('первая', 123))
  print(check_str('первая', 30.5))
  print(check_str('первая', True))
  print(check_str('первая', None))
  print(check_str('одинаковая', 'одинаковая'))
  print(check_str('длина 1', 'длина 2'))
  print(check_str('первая', 'learn'))
  print(check_str('строка', 'тоже строка'))

if __name__ == "__main__":
    main()
