# try except
# else: エラーがない場合に実行
# finally: エラーのあるなしに関わらず、実行

try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4] # Index Error
    a = 10 / 0 # ここでエラー
    print(f'aの値: {a}')
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    print(e, type(e))
    print(f'0で割らないでください: {e}')
except IndexError as e:
    print('Index Error発生')
except Exception as e:
    print('その他の例外')
    print('Exception: ', e, type(e))
else: # 例外がない場合に実行
    print('Else の処理が実行されました')
finally: # 例外の実行あるなしに関わらず実行
    print('Finallyの処理が実行されました。')

print('処理が完了しました。')

# ネットワークで、外部データを取得
# インターネットに接続できない→例外→通知
# 画像ファイルを指定してAIで顔認識をする→画像ファイルが存在しない→例外→通知