# try except

try:
    b = [10,20,30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('Exception: ', e, type(e))
else:
    print('Else処理')
finally:
    print('Finally処理')

print('処理が完了しました。')