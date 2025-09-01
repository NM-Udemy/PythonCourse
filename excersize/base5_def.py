import time

def time_measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"実行時間: {execution_time}")
        return result
    return wrapper

def filter_and_transform(data, condition_func, transform_func):
    return [
        transform_func(item)
        for item in data if
        condition_func(item)
    ]

@time_measure
def process_math_students(students):
    # ['田中さん: 85点']
    math_condition = lambda student: student['subject'] == 'math' and student['score'] >= 80
    transform_to_string = lambda student: f"{student['name']}さん: {student['score']}点"
    
    return filter_and_transform(students, math_condition, transform_to_string)

students = [
    {'name': '田中', 'score': 85, 'subject': 'math'},
    {'name': '佐藤', 'score': 92, 'subject': 'english'},
    {'name': '鈴木', 'score': 78, 'subject': 'math'},
    {'name': '高橋', 'score': 95, 'subject': 'science'},
    {'name': '渡辺', 'score': 88, 'subject': 'english'},
]

math_results = process_math_students(students)
print(f"数学80点以上: {math_results}")
