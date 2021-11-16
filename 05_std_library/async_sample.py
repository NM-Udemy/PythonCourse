# async_sample.py
# 非同期処理
import time
import asyncio

# 素数を判定
def is_prime(x):
    return not any(x%i==0 for i in range(2, x//2))

# 未満で最大の素数
async def highest_prime(x):
    print('{}未満の数値で最も多きな素数'.format(x))
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('{}未満の数値で最も大きな素数は{}'.format(x,y))
            return y
        # time.sleep(0.02)
        await asyncio.sleep(0.02)
    return None

async def main():
    t0 = time.time()
    await asyncio.wait([
        highest_prime(10000),
        highest_prime(1000),
        highest_prime(100)
    ])
    t1 = time.time()
    print('経過時間: {} ms'.format(1000 * (t1 - t0)))

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())