# threading_04_gil1.py

import concurrent.futures
import time

def loop_number(number):
    count = 0
    for _ in range(number):
        count += 1

number = 10000000
start_time = time.time()
# loop_number(number)
# loop_number(number)
# loop_number(number)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(loop_number, [number, number, number])
end_time = time.time()
print(end_time - start_time)
