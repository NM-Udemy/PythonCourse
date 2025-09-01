import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}の実行時間: {end - start:.4f}秒")
        return result
    return wrapper

# 2. 学生データの処理クラス
class StudentProcessor:
    def __init__(self, students):
        self.students = students
    
    @measure_time
    def filter_and_transform(self, condition_func, transform_func):
        """高階関数：条件関数と変換関数を受け取って処理"""
        return [transform_func(student) for student in self.students if condition_func(student)]
    
    @measure_time
    def advanced_analysis(self):
        """複数の機能を組み合わせた分析"""
        # lambda式とリスト内包表記を組み合わせて使用
        high_scorers = [s for s in self.students if s['score'] >= 80]
        
        # 高階関数map()とlambdaを組み合わせ
        score_grades = list(map(lambda s: {**s, 'grade': 'A' if s['score'] >= 90 else 'B'}, high_scorers))
        
        # filter()とlambdaでさらに絞り込み
        a_grade_students = list(filter(lambda s: s['grade'] == 'A', score_grades))
        
        return a_grade_students

# 演習問題実行部分
if __name__ == "__main__":
    # サンプルデータ
    students = [
        {'name': '田中', 'score': 85, 'subject': 'math'},
        {'name': '佐藤', 'score': 92, 'subject': 'english'},
        {'name': '鈴木', 'score': 78, 'subject': 'math'},
        {'name': '高橋', 'score': 95, 'subject': 'science'},
        {'name': '渡辺', 'score': 88, 'subject': 'english'}
    ]
    
    processor = StudentProcessor(students)
    
    # 問題1: lambda式と高階関数を使って数学の学生で80点以上を抽出・変換
    math_high_scorers = processor.filter_and_transform(
        lambda s: s['subject'] == 'math' and s['score'] >= 80,
        lambda s: f"{s['name']}さん: {s['score']}点"
    )
    print("数学80点以上:", math_high_scorers)
    
    # 問題2: 総合分析実行
    a_students = processor.advanced_analysis()
    print("A評価学生:", a_students)