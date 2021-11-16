#1 
import os
os.environ['env'] = 'dev'

#2 
print(os.getenv('env'))

#3
print(os.getcwd())

#4
import sys
if len(sys.argv) > 1:
    arg_1 = sys.argv[1]
    if arg_1 == 'start':
        print('処理を実行します')
    elif arg_1 == 'stop':
        print('処理を終了します')

#5
import csv
with open('input.csv', mode='r', encoding='utf8') as fh:
    csv_reader = csv.DictReader(fh) # {'ClassA': [61,23,54,65]}
    class_grade_dict = {}
    for row in csv_reader:
        class_name = row.get('クラス名')
        if class_name not in class_grade_dict:
            class_grade_dict[class_name] = []
        class_grade_dict[class_name].append(int(row.get('成績')))

# print(class_grade_dict)

class_grades = []
for name, grades in class_grade_dict.items():
    class_grades.append(
        {
            name: {
                'MAX': max(grades),
                'AVG': sum(grades) // len(grades),
                'MIN': min(grades)
            }
        }
    )
print(class_grades)

#6
import json
with open('output.json', mode='w') as fh:
    json.dump(class_grades, fh)