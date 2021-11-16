# multiprocess_01_oneprocess.py

import os
import time
import multiprocessing

list_a = []
def process_function(name):
    print('sub process {}. process_id = {}'.format(name, os.getpid()))
    time.sleep(2)
    list_a.append(name)
    print('Sub list', id(list_a))
    print('sub process end')

if __name__ == '__main__':
    # print(multiprocessing.cpu_count())
    sub = multiprocessing.Process(target=process_function, args=('Test',))
    sub.start()
    print('Main Process. process_id={}'.format(os.getpid()))
    # time.sleep(3)
    sub.join()
    print('Main Process End')
    print('Main list', id(list_a))