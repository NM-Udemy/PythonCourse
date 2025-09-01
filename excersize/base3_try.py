class ScoreInvalidError(Exception):
    pass

grades = {
    'math': [85, 92, 78, 90, 88],
    'english': [-100, 76, 95, 82, 91],
    'science': [91, 87, 84, 89, 93],
}

print('=== 成績管理システム ===')

try:
    subject = input('科目を入力して(math, english, science): ')
    student_num = int(input('学生番号を入力して(1-5): '))
    score = grades[subject][student_num-1]
    if score < 0 or score > 100:
        raise ScoreInvalidError('Scoreの値が正しくありません')
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f'評価: {grade}')
    
except KeyError as e:
    print('エラー: 指定した科目はありません')
except ValueError as e:
    print('エラー:　入力が正しくありません。')
except IndexError as e:
    print('エラー: 学生番号が範囲外です')
except ScoreInvalidError as e:
    print('エラー: スコアの値が正しくありません')
except Exception as e:
    print('エラー: 予期せぬ例外が発生しました')
else:
    print('成績情報が正常に処理されました')
finally:
    print('処理が終了しました。')
