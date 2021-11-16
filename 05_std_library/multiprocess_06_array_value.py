# multiprocess_06_array_value.py

from multiprocessing import Process, Array, Value
import time

def append_num(arr, summary, idx, num):
    # arr.append(num)
    arr[idx] = num
    summary.value += num

if __name__ == '__main__':
    # arr = []
    arr = Array('i', [1,2,3])
    summary = Value('i', 10)
    # append_num(arr, 1)
    # append_num(arr, 2)
    p1 = Process(target=append_num, args=(arr, summary, 0, 1))
    p2 = Process(target=append_num, args=(arr, summary, 1, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    time.sleep(2)
    print(arr[:])
    print(summary.value)
