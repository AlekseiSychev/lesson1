"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как проходит обучение?": "Медленно", "Что сейчас изучаешь?": "While"}

def ask_user(answers_dict):

  while True:

      user_say = input("Введите вопрос ")

      for question in questions_and_answers.keys():
          if user_say == question:
              print(questions_and_answers[f'{question}'])
          else:
              user_say

if __name__ == "__main__":
    ask_user(questions_and_answers)
