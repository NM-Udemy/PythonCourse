from contextlib import contextmanager
import time

@contextmanager
def timer(name='処理'):
    print(f'{name}を開始...')
    start = time.time()
    try:
        yield 'timer'
    finally:
        end = time.time()
        print(f'{name}が完了: {end - start:.3f}秒')

with timer('データベース処理') as d:
    print(d)
    time.sleep(1) # 1秒処理を待つ
    print('重い処理を実行')

print('ファイル終了')