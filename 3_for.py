"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

  score_different_clases =  [
    
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5б', 'scores': [5,4,3,2,1]},
    {'school_class': '6в', 'scores': [1,2,3,4,5]},
    {'school_class': '7г', 'scores': [2,3,4,2,2]},
    {'school_class': '8д', 'scores': [3,5,5,5,2]}
    
    ]

  sum_scores_all_class = 0

  for dict_scores in score_different_clases:
      sum_dict_scores = sum(dict_scores['scores'])
      sum_scores_all_class += sum_dict_scores
      name_class = dict_scores['school_class']

      avg_sum_class = sum_dict_scores / len(dict_scores['scores'])
      print(f'Средний бал класса {name_class} = {avg_sum_class} ')
      

  avg_sum_school = sum_scores_all_class / len(score_different_clases)
  print(f'Средний бал по всей школе {avg_sum_school} ')

if __name__ == "__main__":
    main()
